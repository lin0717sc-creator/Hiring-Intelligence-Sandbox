# Project: AI-Driven Strategic Talent Acquisition & ROI Prediction Model

**Hiring Intelligence Sandbox** — a production-grade feature-weighting engine that converts unstructured job descriptions and candidate signals into quantified **Strategic Match Scores**. The system operationalizes **data-driven decision-making** for Singapore’s tier-one technology employers, elevating **Revenue per Employee (RPE)** by aligning headcount to revenue-critical capability vectors while systematically compressing **Attrition Risk** through objective, repeatable screening logic.

---

## Business Pain Point & First Principles

Singapore’s premium technology labor market exhibits a structural paradox: enterprises compete aggressively for **Solutions Architects** and advanced analytics leaders, yet hiring pipelines remain dominated by subjective résumé review, unstructured interviews, and implicit bias—yielding mis-hires whose cost compounds through onboarding drag, failed delivery milestones, and premature separation.

From first principles, **human capital is a balance-sheet asset** whose marginal return must be measured against revenue contribution, not pedigree alone. When screening lacks quantified feature extraction:

| Failure Mode | Economic Consequence |
|--------------|----------------------|
| Over-indexing on brand or tenure proxies | Elevated **RPE** dilution from under-performing FTEs |
| Under-weighting cloud-native and platform leverage | Missed attach rates on AWS/GCP/GenAI revenue motions |
| Neglecting stakeholder & commercial alignment | Solutions roles that cannot convert architecture into closed ARR |
| Opaque, non-auditable selection | Higher **Attrition Risk** among “brilliant but misfit” profiles |

This model reframes talent acquisition as a **capital allocation problem**: ingest JD and candidate text, normalize signals, apply a transparent weighting matrix, and emit a deterministic **Strategic Match Score**—a leading indicator of role–market fit before offer stage. By encoding capability dimensions as measurable frequencies rather than intuition, the engine **reduces variance in hiring outcomes**, narrows the tail risk of early-tenure exits, and channels finite recruiting bandwidth toward candidates whose skill composition maps to Singapore big-tech’s highest-leverage mandates: **cloud-native platform delivery**, **distributed systems resilience**, and **commercial solution leadership**.

---

## Mathematical Scoring Matrix

Let \( T \) denote raw JD or candidate narrative text. The pipeline applies a normalization operator \( \mathcal{C}(\cdot) \) (lowercasing, punctuation stripping, whitespace collapse) to produce cleaned text \( t = \mathcal{C}(T) \).

For each strategic dimension \( d \in \mathcal{D} \), define a controlled lexicon \( \Lambda_d \) and extract **term-hit frequency**:

\[
f_d(t) = \sum_{\lambda \in \Lambda_d} \text{count}(\lambda, t)
\]

where \( \text{count}(\lambda, t) \) is the occurrence count of phrase \( \lambda \) in \( t \).

The dimension set is:

\[
\mathcal{D} = \{ \text{cloud\_native\_skills},\ \text{distributed\_systems},\ \text{business\_alignment} \}
\]

**Lexicon anchors (non-exhaustive):**

| Dimension \( d \) | Representative terms in \( \Lambda_d \) |
|-------------------|----------------------------------------|
| `cloud_native_skills` | aws, gcp, generative ai, kubernetes, terraform, docker, serverless, cloud-native |
| `distributed_systems` | architecture, scalability, high availability, microservices, resilience |
| `business_alignment` | solution, consulting, stakeholder, commercial, pre-sales, executive |

The **Strategic Match Score** \( S \) is a convex-weighted linear functional over feature frequencies, reflecting Singapore platform economics where cloud-native leverage commands the highest marginal RPE impact:

\[
S(t) = \sum_{d \in \mathcal{D}} w_d \cdot f_d(t)
\]

**Weight vector** (unit-sum, cloud-native priority):

\[
\mathbf{w} = \begin{pmatrix} w_{\text{cloud}} \\ w_{\text{dist}} \\ w_{\text{biz}} \end{pmatrix} = \begin{pmatrix} 0.4 \\ 0.3 \\ 0.3 \end{pmatrix}, \quad \sum_d w_d = 1.0
\]

Equivalently:

\[
S = 0.4 \cdot f_{\text{cloud\_native\_skills}} + 0.3 \cdot f_{\text{distributed\_systems}} + 0.3 \cdot f_{\text{business\_alignment}}
\]

Each dimension also exposes a boolean presence flag \( \mathbb{1}[f_d > 0] \) for hard-gate workflows (e.g., mandatory cloud footprint for Solutions Architect mandates).

**Reference calibration (embedded Singapore Solutions Architect JD fixture):**

| Dimension | \( f_d \) | Weighted contribution |
|-----------|-----------|------------------------|
| `cloud_native_skills` | 8 | \( 8 \times 0.4 = 3.20 \) |
| `distributed_systems` | 9 | \( 9 \times 0.3 = 2.70 \) |
| `business_alignment` | 9 | \( 9 \times 0.3 = 2.70 \) |
| **Strategic Match Score** | — | **\( S = 8.60 \)** |

Scores are **monotonic in signal density**: richer alignment with revenue-critical lexicons increases \( S \), enabling rank-ordering of candidates and role variants on a single interpretable scale—supporting portfolio-level workforce planning and attrition-sensitive redeployment decisions.

---

## System Architecture & Execution

### Pipeline Overview

```
┌─────────────────┐     ┌──────────────┐     ┌───────────────────┐     ┌─────────────────────────┐
│  Raw JD / CV    │────▶│  clean_text  │────▶│ extract_features  │────▶│ calculate_strategic_  │
│  Text Ingest    │     │  Normalize   │     │  f_d, present_d   │     │ score (weighted S)    │
└─────────────────┘     └──────────────┘     └───────────────────┘     └─────────────────────────┘
```

| Module | Function | Responsibility |
|--------|----------|----------------|
| `clean_text(text: str) -> str` | Normalization | Bias-resistant, deterministic text standardization |
| `extract_features(cleaned_text: str) -> dict` | Signal extraction | Frequency + presence per dimension \( d \in \mathcal{D} \) |
| `calculate_strategic_score(features, weights) -> float` | Scoring | Applies \( \mathbf{w} \) to produce \( S \) |
| `main()` | Orchestration | Ingest fixture JD → emit JSON features → print \( S \) |

**Runtime:** Python 3.5+ with strict type annotations (`TypedDict`, `Final`, annotated return types).

### Physical Ignition

From the repository root:

```bash
python data_processor.py
```

**Expected console output (deterministic):**

1. Structured feature payload:

```json
{
  "cloud_native_skills": { "present": true, "frequency": 8 },
  "distributed_systems": { "present": true, "frequency": 9 },
  "business_alignment": { "present": true, "frequency": 9 }
}
```

2. Terminal score line:

```text
[SUCCESS] Candidate Strategic Match Score: 8.60
```

### Strategic Deployment Thesis

| Capability | Business Outcome |
|------------|------------------|
| Auditable lexicon-based features | Defensible hiring decisions; reduced legal and DEI variance |
| Transparent weights \( \mathbf{w} \) | Tunable to business unit RPE targets (e.g., elevate GenAI weight in FY26) |
| Repeatable \( S \) across JD/CV pairs | Throughput scaling for high-volume Singapore tech recruiting |
| Early mismatch detection | Lower **Attrition Risk** by flagging low-\( S \) profiles pre-offer |

The engine is the foundational layer of a broader **Human Capital ROI stack**: batch-score applicant pipelines, back-test weights against historical performer cohorts, and feed scores into downstream attrition and productivity models—closing the loop between **talent intake** and **shareholder-grade workforce productivity**.

---

*Hiring Intelligence Sandbox — Data-driven talent capital, quantified.*
