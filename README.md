# Breathe ESG Ingestion Dashboard

I built this project as a prototype ESG ingestion and analyst review system using Django REST Framework and React.

The goal was to simulate how sustainability teams collect messy operational data from different enterprise systems, normalize it into a common structure, and allow analysts to review records before audit sign-off.

The assignment focused more on ingestion thinking and data modeling than advanced UI design, so I spent most of the time on backend architecture, normalization, and workflow handling.

---

# What the System Does

The application can ingest ESG-related activity data from three different sources:

- SAP-style fuel/procurement exports
- Utility electricity exports
- Corporate travel exports

After ingestion, the system:
- stores raw uploaded rows
- normalizes records into a common format
- classifies ESG scopes
- flags suspicious rows
- allows analyst approval/rejection

---

# Sources Supported

## 1. SAP Fuel / Procurement Data

Example:

```csv
fuel_type,quantity,unit
Diesel,500,L
Petrol,300,L
HSD,-100,L
Coal,50,KG

## 2. Utility Electricity Data

Example:

```csv
meter_id,kwh_used,unit
M101,450,kwh
M102,1200,kwh
M103,-50,kwh