# MODEL.md

## Overview

The system is designed to ingest emissions and activity data from multiple enterprise sources, normalize the records into a common structure, and allow analysts to review and approve records before audit sign-off.

The architecture separates raw uploaded data from normalized ESG records to preserve auditability and source traceability.

---

# Core Design Principles

1. Multi-tenancy support
2. Source traceability
3. Audit-friendly ingestion
4. Normalization pipeline
5. Analyst review workflow
6. Scope classification
7. Suspicious activity detection

---

# Data Model

## Tenant

Represents an enterprise customer.

Fields:
- id
- name
- created_at

Purpose:
Supports multi-tenant architecture where multiple companies can use the platform independently.

---

## DataSource

Represents the source system from which data originated.

Supported sources:
- SAP
- Utility
- Travel

Fields:
- tenant
- source_type
- ingestion_method
- created_at

Purpose:
Tracks the origin of uploaded data and preserves source-of-truth metadata.

---

## UploadBatch

Represents a single uploaded file batch.

Fields:
- datasource
- filename
- uploaded_at
- processing_status

Purpose:
Groups records by upload event and provides ingestion traceability.

---

## RawRecord

Stores original uploaded row data before normalization.

Fields:
- upload_batch
- row_number
- raw_data
- validation_errors

Purpose:
Preserves the original uploaded structure exactly as received from source systems.

This is critical for:
- auditability
- debugging
- traceability
- replaying normalization logic later

Raw records are intentionally not modified after ingestion.

---

## NormalizedRecord

Represents cleaned and standardized ESG activity data.

Fields:
- raw_record
- source_type
- category
- scope
- quantity
- normalized_unit
- suspicious_flag
- status
- created_at

Purpose:
Creates a consistent structure across heterogeneous enterprise data sources.

Examples:
- Fuel consumption
- Electricity usage
- Business travel activity

---

# Scope Classification

The system classifies records into ESG scopes:

## Scope 1
Direct emissions:
- fuel consumption
- diesel
- petrol
- coal

## Scope 2
Purchased electricity:
- utility electricity usage

## Scope 3
Indirect business activity:
- flights
- taxis
- hotel stays

---

# Normalization Strategy

Uploaded data often contains inconsistent units and schemas.

Examples:
- litre
- litres
- L
- kg
- kwh
- km

The normalization pipeline standardizes these values into canonical units.

Examples:
- litre → L
- kwh → KWH
- km → KM

Unknown units are flagged as suspicious.

---

# Suspicious Record Detection

The system flags potentially invalid data during ingestion.

Current checks include:
- negative quantities
- unknown units

Examples:
- negative fuel consumption
- negative electricity usage
- negative travel distance

Suspicious rows are highlighted in the analyst dashboard.

---

# Analyst Workflow

Analysts can:
- review normalized records
- approve records
- reject records

Record statuses:
- PENDING
- APPROVED
- REJECTED

This supports audit review workflows before external reporting.

---

# Auditability

The architecture preserves complete traceability:

Raw Upload
→ Upload Batch
→ Raw Record
→ Normalized Record

This ensures every normalized ESG value can be traced back to:
- original uploaded file
- original uploaded row
- upload timestamp
- source system

---

# Design Tradeoffs

The prototype intentionally uses:
- synchronous processing
- CSV uploads
- simplified normalization rules

instead of:
- asynchronous queues
- OCR pipelines
- live ERP integrations

to keep the scope manageable within the assignment timeline.

---

# Future Improvements

Potential production improvements:
- async ingestion queues
- OCR for utility PDFs
- real SAP OData integration
- emission factor calculations
- duplicate detection
- role-based access control
- approval history tracking
- AI-assisted anomaly detection