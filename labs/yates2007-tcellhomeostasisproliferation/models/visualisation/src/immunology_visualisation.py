# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Dedicated visualisation model for immunology labs."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import AcceptedSignalProfile, BioSignal, SignalSpec


SUMMARY_SCHEMA = {
    "duration_simulated": "float",
    "observable_count": "int",
    "largest_change_observable": "str",
    "largest_change_magnitude": "float",
    "peak_observable": "str",
    "peak_value": "float",
}


def _value(signal: Any) -> Any:
    if hasattr(signal, "value"):
        signal = signal.value
    if isinstance(signal, dict) and set(signal) == {"payload"}:
        return signal["payload"]
    return signal


def _as_mapping(value: Any) -> dict[str, Any]:
    value = _value(value)
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _number(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


class ImmunologyVisualisationModel(BioModule):
    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        answer_focus: str,
        context: str,
        sources: list[dict[str, Any]],
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = lab_title
        self.question = question
        self.answer_focus = answer_focus
        self.context = context
        self.sources = list(sources)
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._history: dict[str, list[dict[str, float]]] = {}
        self._labels: dict[str, dict[str, str]] = {}
        self._summaries: dict[str, dict[str, Any]] = {}

    def inputs(self) -> dict[str, SignalSpec]:
        specs: dict[str, SignalSpec] = {}
        for source in self.sources:
            alias = str(source["alias"])
            specs[f"{alias}_state"] = SignalSpec.record(schema={"payload": "json"}, description="Core model state record.")
            specs[f"{alias}_summary"] = SignalSpec.record(
                schema=SUMMARY_SCHEMA,
                accepted_profiles=(
                    AcceptedSignalProfile(signal_type="record", schema=SUMMARY_SCHEMA),
                    AcceptedSignalProfile(signal_type="record", schema={"payload": "json"}),
                ),
                description="Core model summary record.",
            )
            specs[f"{alias}_species_labels"] = SignalSpec.record(schema={"payload": "json"}, description="Core model display label map.")
        return specs

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self._history = {str(source["alias"]): [] for source in self.sources}
        self._labels = {str(source["alias"]): {} for source in self.sources}
        self._summaries = {str(source["alias"]): {} for source in self.sources}

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        for source in self.sources:
            alias = str(source["alias"])
            state = _as_mapping(self._inputs.get(f"{alias}_state"))
            if state:
                point = {"t": float(end)}
                for key, raw in state.items():
                    number = _number(raw)
                    if number is not None:
                        point[str(key)] = number
                if len(point) > 1:
                    self._history.setdefault(alias, []).append(point)
            summary = _as_mapping(self._inputs.get(f"{alias}_summary"))
            if summary:
                self._summaries[alias] = summary
            labels = _as_mapping(self._inputs.get(f"{alias}_species_labels"))
            if labels:
                self._labels[alias] = {str(k): str(v) for k, v in labels.items()}

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def _selected_observables(self, source: Mapping[str, Any], alias: str) -> list[tuple[str, str]]:
        configured = source.get("observables") or []
        labels = self._labels.get(alias, {})
        pairs: list[tuple[str, str]] = []
        for item in configured:
            if isinstance(item, Mapping):
                obs = str(item.get("id") or "")
                label = str(item.get("label") or labels.get(obs) or obs)
                if obs:
                    pairs.append((obs, label))
        if pairs:
            return pairs[:6]
        history = self._history.get(alias, [])
        if history:
            keys = [key for key in history[-1] if key != "t"]
            return [(key, labels.get(key, key)) for key in keys[:6]]
        return []

    def _answer(self, alias: str) -> tuple[str, str, str]:
        history = self._history.get(alias, [])
        summary = self._summaries.get(alias, {})
        if not history:
            return (
                "No numeric state values were emitted for the current run.",
                "The core module did not provide renderable numeric state data.",
                "No dominant numeric module could be resolved.",
            )
        first = history[0]
        last = history[-1]
        changes = {
            key: abs(float(last.get(key, 0.0)) - float(first.get(key, 0.0)))
            for key in last
            if key != "t"
        }
        if not changes:
            return (
                "The model emitted a steady or non-numeric state over this short run.",
                "State records were present but no numeric excursions were measurable.",
                "Steady-state evidence",
            )
        top = max(changes, key=changes.get)
        labels = self._labels.get(alias, {})
        label = labels.get(top, top)
        magnitude = changes[top]
        caveat = str(summary.get("caveat") or "Interpretation is limited to the bundled source model and conservative display labels.")
        return (
            f"{label} showed the largest measured excursion in this run.",
            f"Largest absolute change was {magnitude:.6g} in `{top}` across {len(history)} sampled point(s).",
            caveat,
        )

    def visualize(self) -> Optional[list[dict[str, Any]]]:
        visuals: list[dict[str, Any]] = []
        for source in self.sources:
            alias = str(source["alias"])
            title = str(source.get("title") or self.lab_title)
            answer, evidence, caveat = self._answer(alias)
            visuals.append(
                {
                    "render": "table",
                    "description": "Direct scientific answer for this immunology lab run.",
                    "data": {
                        "title": f"{self.lab_title} - run interpretation",
                        "columns": ["Prompt", "Answer"],
                        "rows": [
                            ["Scientific question", self.question],
                            ["Observed answer", answer],
                            ["Evidence", evidence],
                            ["Dominant module", self.answer_focus],
                            ["Caveat", caveat],
                        ],
                    },
                }
            )

            pairs = self._selected_observables(source, alias)
            history = self._history.get(alias, [])
            series = []
            for obs, label in pairs:
                points = [[float(row["t"]), float(row[obs])] for row in history if obs in row]
                if points:
                    series.append({"name": label, "points": points})
            if series:
                visuals.append(
                    {
                        "render": "timeseries",
                        "description": f"{title} selected immunology observables over model time.",
                        "data": {
                            "title": str(source.get("visual_scope") or "Selected immunology observables"),
                            "x_label": "Model time",
                            "y_label": "Native source value",
                            "series": series,
                        },
                    }
                )

            if history:
                first = history[0]
                last = history[-1]
                labels = self._labels.get(alias, {})
                items = []
                for key in last:
                    if key == "t" or key not in first:
                        continue
                    items.append({"label": labels.get(key, key), "value": abs(float(last[key]) - float(first[key]))})
                items = sorted(items, key=lambda item: item["value"], reverse=True)[:8]
                if items:
                    visuals.append(
                        {
                            "render": "bar",
                            "description": "Largest within-run state excursions.",
                            "data": {"title": "Largest state excursions", "items": items},
                        }
                    )
        return visuals or None
