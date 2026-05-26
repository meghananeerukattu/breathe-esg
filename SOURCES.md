# SOURCES.md

# Overview

Before building the ingestion flows, I researched how enterprise sustainability data is commonly exported from operational systems.

The goal was not to perfectly replicate each source system, but to model realistic ingestion patterns and data quality issues that ESG platforms typically face.

---

# 1. SAP Fuel and Procurement Data

## What I Researched

I researched common SAP export approaches including:
- flat file exports
- IDocs
- OData services
- spreadsheet-based ERP exports

I found that many operational teams still work heavily with exported CSV or Excel files, especially during sustainability reporting workflows.

---

## What I Chose

I chose simplified SAP-style CSV exports for the prototype.

Example structure:

```csv
fuel_type,quantity,unit
Diesel,500,L
Petrol,300,L
HSD,-100,L
Coal,50,KG