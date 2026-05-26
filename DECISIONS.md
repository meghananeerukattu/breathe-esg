# DECISIONS.md

# Overview

This project involved a lot of open-ended decisions around ingestion formats, normalization, and workflow design. Since the assignment only provided high-level requirements, I focused on building a realistic prototype that demonstrates how enterprise ESG ingestion systems could work without overengineering the solution.

---

# Why I Chose CSV Uploads

I used CSV uploads for all three sources instead of building direct integrations.

The main reason is that CSV exports are still very common in enterprise workflows. Sustainability teams often receive:
- SAP exports as spreadsheets
- utility data from portals
- travel reports from Concur/Navan exports

Building actual ERP connectors or OAuth integrations would have taken a lot of time and would not add much value to the core assignment goals.

The assignment seemed more focused on:
- normalization
- source traceability
- review workflows
- data modeling

So I prioritized those areas.

---

# SAP Ingestion Choice

I decided to handle SAP-style flat file exports instead of trying to simulate full SAP integrations like IDocs or OData services.

Real SAP integrations are large projects on their own and usually involve:
- middleware
- authentication
- connector configuration
- ERP access

For this prototype, I wanted to focus more on the messy structure of ERP exports:
- inconsistent units
- different column naming
- normalization problems

The SAP ingestion pipeline currently assumes CSV exports containing fuel/procurement activity.

---

# Utility Data Decision

For utility ingestion, I chose CSV exports from utility portals instead of PDF parsing.

A lot of facilities teams already download monthly electricity usage reports as spreadsheets, so this felt realistic enough for the assignment scope.

I intentionally skipped:
- OCR
- tariff calculations
- PDF parsing
- billing logic

because those would increase complexity significantly without improving the core ingestion architecture.

---

# Travel Data Decision

For travel data, I modeled exported trip activity rows instead of integrating with real travel APIs.

The travel upload currently supports:
- flights
- taxis
- hotel stays

I mainly wanted to demonstrate:
- Scope 3 classification
- normalization
- analyst review

I did not implement:
- airport distance calculations
- emission factor calculations
- multi-leg trips

because the focus of the prototype was ingestion workflow rather than carbon calculation accuracy.

---

# Why I Separated Raw and Normalized Records

One decision I considered important was separating raw uploaded rows from normalized ESG records.

I wanted uploaded data to always remain traceable back to:
- original upload
- original row
- source system

This makes debugging and audit review much easier.

The raw rows are stored exactly as uploaded, while normalized records contain cleaned and standardized values used by analysts.

---

# Suspicious Record Handling

I added simple suspicious record checks during ingestion.

Currently records are flagged if:
- quantities are negative
- units are unknown

This is obviously simplified compared to a real anomaly detection system, but it demonstrates how analysts can be alerted to potentially invalid data before approval.

Suspicious rows are highlighted in the dashboard for easier review.

---

# Analyst Review Workflow

The assignment specifically mentioned analyst approval before audit sign-off, so I added:
- PENDING
- APPROVED
- REJECTED

statuses to records.

I kept the workflow intentionally lightweight but still realistic enough to demonstrate human review before finalized reporting.

---

# Frontend Decisions

I kept the frontend relatively simple and focused more on usability than design complexity.

The dashboard supports:
- uploads
- record review
- suspicious row highlighting
- approval actions
- dashboard statistics

I avoided spending too much time on animations or advanced UI libraries because I felt the assignment prioritized backend architecture and ingestion realism more heavily.

---

# Database Decision

I used SQLite during development because it simplified setup and allowed faster iteration.

For a production system, PostgreSQL would be a better choice due to:
- scalability
- concurrency
- better query performance

---

# Processing Approach

Uploads are currently processed synchronously during API requests.

This keeps the prototype straightforward and easier to understand.

In a production system I would likely move ingestion into asynchronous background workers using something like:
- Celery
- Redis queues
- event-driven processing

especially for large enterprise uploads.

---

# Overall Tradeoff

Throughout the assignment I tried to prioritize:
- clean data modeling
- realistic ingestion flows
- auditability
- review workflow clarity

over implementing too many partially-finished features.