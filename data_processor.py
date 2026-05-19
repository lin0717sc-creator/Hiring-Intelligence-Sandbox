"""JD text cleaning and feature extraction for strategic human-capital screening."""

from __future__ import annotations

import json
import re
import string
from typing import Final, TypedDict

# Singapore big-tech Solutions Architect — raw JD fixture (test input)
SAMPLE_JD_RAW: Final[str] = """
Solutions Architect (Singapore)

We are hiring a Senior Solutions Architect to partner with enterprise customers
across ASEAN. You will design cloud-native architectures on AWS and GCP, leverage
Generative AI and LLM platforms, and guide Kubernetes-based container workloads.

Must-have:
- 8+ years in solution architecture, distributed systems, and microservices
- Proven scalability, high availability, and resilience patterns at regional scale
- Hands-on with Terraform, Docker, and API-led integration

Business & stakeholder alignment:
- Lead pre-sales solution workshops and executive stakeholder reviews
- Translate commercial objectives into technical roadmaps with consulting rigor
- Collaborate with product, sales, and customer success on outcome-based delivery
""".strip()

_CLOUD_NATIVE_TERMS: Final[tuple[str, ...]] = (
    "aws",
    "gcp",
    "azure",
    "generative ai",
    "llm",
    "kubernetes",
    "k8s",
    "docker",
    "terraform",
    "serverless",
    "cloud native",
    "cloud-native",
    "container",
)

_DISTRIBUTED_SYSTEMS_TERMS: Final[tuple[str, ...]] = (
    "architecture",
    "scalability",
    "high availability",
    "distributed systems",
    "distributed system",
    "microservices",
    "resilience",
    "regional scale",
)

_BUSINESS_ALIGNMENT_TERMS: Final[tuple[str, ...]] = (
    "solution",
    "consulting",
    "stakeholder",
    "commercial",
    "pre-sales",
    "executive",
    "outcome-based",
)


class FeatureSignal(TypedDict):
    present: bool
    frequency: int


class ExtractedFeatures(TypedDict):
    cloud_native_skills: FeatureSignal
    distributed_systems: FeatureSignal
    business_alignment: FeatureSignal


def clean_text(text: str) -> str:
    """Normalize JD text: lowercase, strip punctuation, collapse whitespace."""
    lowered = text.lower()
    no_punct = lowered.translate(str.maketrans("", "", string.punctuation))
    collapsed = re.sub(r"\s+", " ", no_punct).strip()
    return collapsed


def _count_term_hits(cleaned_text: str, terms: tuple[str, ...]) -> int:
    return sum(cleaned_text.count(term) for term in terms)


def extract_features(cleaned_text: str) -> ExtractedFeatures:
    """Extract hiring-model signals from cleaned JD text."""
    cloud_hits = _count_term_hits(cleaned_text, _CLOUD_NATIVE_TERMS)
    distributed_hits = _count_term_hits(cleaned_text, _DISTRIBUTED_SYSTEMS_TERMS)
    business_hits = _count_term_hits(cleaned_text, _BUSINESS_ALIGNMENT_TERMS)

    return {
        "cloud_native_skills": {
            "present": cloud_hits > 0,
            "frequency": cloud_hits,
        },
        "distributed_systems": {
            "present": distributed_hits > 0,
            "frequency": distributed_hits,
        },
        "business_alignment": {
            "present": business_hits > 0,
            "frequency": business_hits,
        },
    }


def calculate_strategic_score(
    features: dict[str, FeatureSignal],
    weights: dict[str, float],
) -> float:
    """Weighted sum of feature frequencies → Strategic Match Score."""
    return sum(
        features[dimension]["frequency"] * weight
        for dimension, weight in weights.items()
    )


def _print_success_score(score: float) -> None:
    bold_green = "\033[1;92m"
    reset = "\033[0m"
    print(
        f"\n{bold_green}[SUCCESS] Candidate Strategic Match Score: {score:.2f}{reset}"
    )


def main() -> None:
    WEIGHTS: dict[str, float] = {
        "cloud_native_skills": 0.4,
        "distributed_systems": 0.3,
        "business_alignment": 0.3,
    }

    cleaned = clean_text(SAMPLE_JD_RAW)
    features = extract_features(cleaned)
    print(json.dumps(features, indent=2, ensure_ascii=False))

    strategic_score = calculate_strategic_score(features, WEIGHTS)
    _print_success_score(strategic_score)


if __name__ == "__main__":
    main()
