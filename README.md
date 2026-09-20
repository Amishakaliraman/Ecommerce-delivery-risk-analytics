# E-commerce Delivery Risk Analytics

This repository contains a production-style analytics project for Olist e-commerce delivery risk analysis, built in phases across ingestion, warehouse modeling, orchestration, ML, and productization.

## Project goals

- Ingest and normalize raw Olist datasets
- Build trusted analytics models in dbt
- Orchestrate the pipeline with Airflow
- Explore delivery risk drivers with notebooks
- Train and validate predictive models for risk scoring
- Surface results in a Streamlit app

## Repository structure

- `data/raw/` stores the 9 original Olist CSV files. These are treated as source-of-truth inputs and should never be edited.
- `src/` contains ingestion scripts and shared project utilities.
- `dbt/` contains transformation models for warehouse logic and curated marts.
- `airflow/dags/` contains orchestration DAGs for the pipeline.
- `notebooks/` is reserved for EDA, NLP, and ML experimentation.
- `app/` hosts the Streamlit application.
- `docs/` contains architecture notes and generated docs.

## Local setup

1. Create a virtual environment:
   python -m venv .venv
2. Activate the environment:
   - Windows PowerShell: .\.venv\Scripts\Activate.ps1
   - Windows Command Prompt: .\.venv\Scripts\activate.bat
3. Install dependencies:
   pip install -r requirements.txt
4. Copy the example environment file and fill in real values:
   copy .env.example .env
5. Place the 9 Olist CSV files inside `data/raw/`.

## Environment variables

The project expects the following keys in `.env`:

- `SNOWFLAKE_ACCOUNT`
- `SNOWFLAKE_USER`
- `SNOWFLAKE_PASSWORD`
- `SNOWFLAKE_ROLE`
- `SNOWFLAKE_WAREHOUSE`
- `SNOWFLAKE_DATABASE`
- `SNOWFLAKE_SCHEMA`
- `SNOWFLAKE_SCHEMA_RAW`

## Phase plan

- Phase 1: Ingestion and raw warehouse loads
- Phase 2: Data quality validation and schema checks
- Phase 3: dbt transformations and semantic modeling
- Phase 4: Feature engineering for risk analysis
- Phase 5: Airflow orchestration
- Phase 6: Exploratory data analysis
- Phase 7: NLP and behavior signals
- Phase 8: ML modeling and validation
- Phase 9: Deployment and monitoring
- Phase 10: Streamlit dashboard

## Notes

- Keep raw data immutable and version-controlled only through explicit ingestion jobs.
- Prefer dbt for transformations and curated data products.
- Store credentials in `.env`, never in source control.
