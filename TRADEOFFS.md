# TRADEOFFS.md

# Overview

This prototype was built within a limited assignment timeline, so several features were intentionally simplified or left out in order to focus on the core ingestion and review workflow.

The goal was to prioritize:
- realistic ingestion architecture
- normalization
- traceability
- analyst review workflow

instead of trying to build a fully production-ready ESG platform.

---

# 1. No Direct ERP or API Integrations

I chose CSV uploads instead of building live integrations with:
- SAP
- utility providers
- Concur/Navan APIs

While direct integrations would be more realistic in production, they would also require:
- authentication flows
- API credentials
- middleware setup
- connector maintenance

For this prototype, CSV ingestion was enough to demonstrate:
- schema normalization
- source tracking
- ingestion workflows

---

# 2. No OCR or PDF Parsing

Utility bills are often received as PDFs, but I intentionally avoided OCR and document parsing.

Instead, utility ingestion assumes CSV exports from utility portals.

OCR pipelines would introduce:
- image preprocessing
- parsing accuracy issues
- significantly more complexity

I decided to focus on the ingestion pipeline itself rather than document extraction.

---

# 3. No Emission Factor Calculations

The system currently stores normalized activity data but does not calculate actual carbon emissions.

For example:
- fuel usage is normalized
- electricity usage is normalized
- travel activity is normalized

but emission factors are not applied yet.

I intentionally left this out because the assignment seemed more focused on:
- ingestion
- normalization
- auditability
- review workflow

rather than emissions accounting logic.

---

# 4. Simplified Suspicious Detection

Suspicious record detection currently checks:
- negative values
- unknown units

A real production system would likely include:
- statistical anomaly detection
- historical comparisons
- threshold monitoring
- ML-based validation

I kept the rules intentionally lightweight to keep the workflow understandable.

---

# 5. No Duplicate Detection

The current prototype allows repeated uploads of the same CSV.

Production systems would likely require:
- checksum validation
- duplicate row detection
- batch deduplication

I chose not to implement this because it was less important than the core ingestion workflow.

---

# 6. No Authentication or Role Management

The application currently does not implement:
- login flows
- RBAC
- tenant-specific access controls

These features are important in production but would require additional backend complexity.

The focus of the assignment appeared to be ingestion architecture rather than user management.

---

# 7. Synchronous Processing

Uploads are processed synchronously during API requests.

For large enterprise uploads, production systems would likely use:
- background workers
- queues
- asynchronous ingestion pipelines

I kept processing synchronous to simplify debugging and keep the architecture easier to follow.

---

# 8. Minimal Frontend Design

The frontend focuses mainly on:
- usability
- visibility of suspicious rows
- analyst actions
- dashboard metrics

I intentionally avoided building a heavily designed UI because I wanted to spend more time on:
- ingestion pipelines
- backend architecture
- normalization logic
- review workflow

---

# Final Note

The prototype is intentionally scoped as a realistic MVP rather than a production-ready ESG platform.

The focus was on demonstrating:
- ingestion thinking
- normalization strategy
- auditability
- analyst review flow
- multi-source data handling