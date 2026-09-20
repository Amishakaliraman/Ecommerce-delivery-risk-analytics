# Architecture overview

This project follows a layered design for trustworthy e-commerce delivery risk analytics.

## Layered flow

1. Raw Olist CSV files are stored under `data/raw/`.
2. Ingestion jobs in `src/ingestion/` standardize file loading and staging.
3. dbt models transform the staged data into trusted marts for analytics.
4. Airflow schedules and monitors pipeline execution.
5. Notebooks support exploratory analysis and ML experiments.
6. The Streamlit app exposes a user-facing risk dashboard.

## Data contracts

- Keep raw file schemas immutable for source-of-truth comparisons.
- Validate essential columns before writing to the warehouse.
- Use semantic names in final marts to avoid repeated business logic.

## Recommended outputs

- order risk score
- delivery delay risk segment
- seller risk profile
- geography and fulfillment risk views
