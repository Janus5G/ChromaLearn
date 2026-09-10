from dataclasses import dataclass, field

MODALITIES = ("text", "visual", "audio", "activity")

MODALITY_LABELS = {
    "text": "tekst",
    "visual": "visuel",
    "audio": "lyd",
    "activity": "aktivitet",
}

MODALITY_INSTRUCTIONS = {
    "text": "Explain concisely in text, using short steps and one focused question.",
    "visual": "Use a visual representation in plain text: a compact table, labelled structure, timeline, flow, coordinate sketch, or ASCII diagram when useful. Do not claim to have generated an image.",
    "audio": "Write for listening: short sentences, clear pauses, minimal symbols, and speakable wording. The local UI may read this aloud with text-to-speech.",
    "activity": "Give a safe, concrete learner activity using ordinary classroom/home materials or an embodied action. The activity must make the learner produce or observe evidence, not just watch passively.",
}

@dataclass
class AdaptiveProfile:
    # Scores are evidence-weighted and kept per subject/topic. This is not a fixed 'learning style'.
    subject: str
    topic: str = "general"
    evidence: dict = field(default_factory=dict)

    def __post_init__(self):
        for m in MODALITIES:
            self.evidence.setdefault(m, {"attempts": 0, "points": 0})

    def record(self, modality: str, score: int):
        if modality not in MODALITIES:
            raise ValueError("Unknown modality")
        score = int(score)
        if score not in (0, 1, 2):
            raise ValueError("Score must be 0, 1 or 2")
        row = self.evidence[modality]
        row["attempts"] += 1
        row["points"] += score

    def mean(self, modality: str):
        row = self.evidence[modality]
        return None if not row["attempts"] else row["points"] / (2 * row["attempts"])

    def ranking(self):
        # Untested methods are deliberately not ranked as bad; exploration remains possible.
        tested = []
        untested = []
        for m in MODALITIES:
            avg = self.mean(m)
            if avg is None:
                untested.append(m)
            else:
                tested.append((avg, self.evidence[m]["attempts"], m))
        tested.sort(key=lambda x: (x[0], x[1]), reverse=True)
        return [m for _, _, m in tested] + untested

    def recommendation(self):
        ranked = self.ranking()
        best = ranked[0] if ranked else "text"
        tested = [m for m in MODALITIES if self.mean(m) is not None]
        if len(tested) < 2:
            return {"modality": best, "reason": "Der er endnu kun lidt målt læringsevidens; systemet varierer metoderne for at lære mere."}
        avg = self.mean(best)
        return {"modality": best, "reason": f"Denne metode har foreløbig den højeste målte transfer-score i dette fag/emne ({avg:.0%})."}

    def public_summary(self):
        out = {}
        for m in MODALITIES:
            row = self.evidence[m]
            out[m] = {"attempts": row["attempts"], "score": self.mean(m)}
        return out
