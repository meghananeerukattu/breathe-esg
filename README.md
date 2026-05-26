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
```

---

## 2. Utility Electricity Data

Example:

```csv
meter_id,kwh_used,unit
M101,450,kwh
M102,1200,kwh
M103,-50,kwh
```

Used mainly for:
- Scope 2 electricity activity

---

## 3. Travel Data

Example:

```csv
trip_type,distance,unit
Flight,1200,km
Taxi,30,km
Hotel,2,nights
Flight,-500,km
```

Used mainly for:
- Scope 3 travel activity

---

# Features

## Multi-source ingestion
Supports multiple upload pipelines with different schemas.

## ESG scope classification
Records are categorized into:
- Scope 1
- Scope 2
- Scope 3

## Suspicious row detection
The system currently flags:
- negative quantities
- unknown units

Suspicious rows are highlighted in the dashboard.

## Analyst review workflow
Analysts can:
- review records
- approve records
- reject records

## Dashboard statistics
The dashboard displays:
- total records
- suspicious records
- approved records

---

# Tech Stack

## Backend
- Django
- Django REST Framework
- SQLite

## Frontend
- React
- Axios
---

# Project Structure

```text
breathe-esg/
│
├── backend/
├── frontend/
│
├── sample_sap.csv
├── sample_utility.csv
├── sample_travel.csv
│
├── MODEL.md
├── DECISIONS.md
├── TRADEOFFS.md
├── SOURCES.md
├── README.md
```

---

# Running the Project Locally

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install django djangorestframework pandas django-cors-headers

python manage.py migrate

python manage.py runserver
```

---

## Frontend

```bash
cd frontend

npm install

npm start
```

---

# Main API Endpoints

## Upload APIs

- `/api/upload/sap/`
- `/api/upload/utility/`
- `/api/upload/travel/`

## Dashboard APIs

- `/api/records/`
- `/api/stats/`

## Approval Workflow

- `/api/records/<id>/status/`

---

# Things I Intentionally Kept Simple

To keep the assignment manageable, I intentionally did not implement:
- direct SAP integrations
- OCR/PDF parsing
- emission factor calculations
- async queues
- authentication/role management

I wanted to focus mainly on:
- ingestion architecture
- normalization
- auditability
- analyst workflow

instead of trying to partially build too many features.

---

# Future Improvements

Some production improvements I would add later:
- PostgreSQL
- async ingestion queues
- OCR support for utility bills
- duplicate detection
- emission calculations
- role-based access control
- audit history tracking
- direct ERP integrations