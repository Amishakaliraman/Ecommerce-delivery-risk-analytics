# 🛒 Olist E-Commerce Data Engineering & Analytics

An end-to-end **Data Engineering and Analytics project** built using the Brazilian Olist E-Commerce dataset.

The project takes raw e-commerce data through ingestion, cleaning, validation, transformation, data modeling, orchestration, and exploratory data analysis using **Python, SQL, Snowflake, Snowpark, Pandas, and Matplotlib**.

---

## 📌 Project Overview

The main goal of this project is to build a scalable data pipeline that transforms raw Olist e-commerce data into clean, validated, business-ready analytical data.

The project covers:

- Data ingestion
- Data cleaning and transformation
- Data quality validation
- Snowflake data warehouse modeling
- Fact and dimension tables
- Customer RFM analysis
- Stored procedures
- Snowflake Tasks
- Pipeline orchestration
- Exploratory Data Analysis (EDA)
- Business-focused insights

---

## 🏗️ Project Architecture

```text
                    OLIST DATA
                        │
                        ▼
              ┌──────────────────┐
              │   PHASE 1        │
              │ Data Ingestion   │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   PHASE 2        │
              │ Data Cleaning &  │
              │ Transformation   │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   PHASE 3        │
              │ Data Quality &   │
              │   Validation     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   PHASE 4        │
              │ Data Modeling    │
              │ RAW → STAGING →  │
              │ MARTS            │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   PHASE 5        │
              │ Orchestration    │
              │ Procedures +    │
              │ Snowflake Tasks  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   PHASE 6        │
              │ EDA & Business   │
              │    Analysis      │
              └──────────────────┘
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and analysis |
| SQL | Data transformation and validation |
| Snowflake | Cloud data warehouse |
| Snowpark Python | Python processing inside Snowflake |
| Snowflake Notebooks | Exploratory Data Analysis |
| Matplotlib | Data visualization |
| Git | Version control |
| GitHub | Project repository |

---

# 📂 Dataset

The project uses the **Brazilian Olist E-Commerce Dataset**.

The dataset contains information about:

- Orders
- Order items
- Payments
- Customers
- Sellers
- Products
- Geolocation
- Customer reviews

---

# 🚀 Phase 1 — Data Ingestion

## Objective

Load the raw Olist datasets into Snowflake without major transformations.

The raw data is stored in:

```text
OLIST_DB.RAW
```

### Main RAW tables

```text
ORDERS
ORDER_ITEMS
ORDER_PAYMENTS
CUSTOMERS
SELLERS
PRODUCT
GEOLOCATION
ORDER_REVIEWS
```

The RAW layer preserves the source data and acts as the starting point of the pipeline.

---

# 🧹 Phase 2 — Data Cleaning & Transformation

## Objective

Clean and standardize the raw datasets before using them for analytics.

The cleaned data is stored in:

```text
OLIST_DB.STAGING
```

### Main STAGING tables

```text
ORDERS
ORDER_ITEMS
ORDER_PAYMENTS
CUSTOMERS
SELLERS
PRODUCTS
GEOLOCATION
ORDER_REVIEWS
```

### Transformations performed

- Removed records with missing critical IDs
- Standardized customer city names
- Standardized state values
- Handled missing product categories
- Renamed columns for analytical clarity
- Prepared timestamp fields
- Aggregated geolocation data
- Created clean datasets for downstream modeling

### Example

Customer cities are standardized using:

```sql
INITCAP(CUSTOMER_CITY)
```

States are standardized using:

```sql
UPPER(CUSTOMER_STATE)
```

Missing product categories are handled using:

```sql
COALESCE(PRODUCT_CATEGORY_NAME, 'unknown')
```

---

# 🔍 Phase 3 — Data Quality & Validation

## Objective

Validate the data before using it for business analysis.

The project includes checks for:

### 1. Null Values

Checks important fields such as:

```text
ORDER_ID
CUSTOMER_ID
PRODUCT_ID
SELLER_ID
```

### 2. Record Count Validation

Compares data between:

```text
RAW
 ↓
STAGING
```

to identify unexpected data loss.

### 3. Duplicate Records

Checks for duplicate IDs in analytical tables.

### 4. Referential Integrity

Checks relationships such as:

```text
Order → Customer
Order Item → Product
Order Item → Seller
```

### 5. Invalid Values

Checks for issues such as:

```text
Negative order values
Negative monetary values
Invalid RFM values
```

The objective is to ensure that the analytical tables contain reliable data.

---

# 🏛️ Phase 4 — Data Modeling

## Snowflake Layered Architecture

The project follows a layered warehouse architecture:

```text
RAW
 ↓
STAGING
 ↓
MARTS
```

### RAW

Contains source data with minimal transformation.

### STAGING

Contains cleaned and standardized data.

### MARTS

Contains business-ready analytical tables.

---

# 📊 MARTS Layer

The MARTS layer contains analytical tables used for reporting and analysis.

Main tables include:

```text
FCT_ORDERS
FCT_ORDER_ITEMS
CUSTOMER_RFM
DIM_CUSTOMERS
DIM_PRODUCTS
DIM_SELLERS
```

---

## Fact Tables

### FCT_ORDERS

Used for order-level analysis.

Contains information related to:

- Orders
- Customers
- Order status
- Purchase timestamps
- Delivery timestamps
- Estimated delivery
- Late delivery indicator

---

### FCT_ORDER_ITEMS

Used for product and seller-level analysis.

Contains:

- Order ID
- Order item ID
- Product ID
- Seller ID
- Price
- Freight value
- Shipping information

---

# Dimension Tables

### DIM_CUSTOMERS

Contains customer-level information used for analytics.

### DIM_PRODUCTS

Contains product information including:

- Product category
- Weight
- Length
- Height
- Width

### DIM_SELLERS

Contains seller information including:

- Seller location
- Seller city
- Seller state

---

# 👥 Customer RFM Analysis

The project creates a:

```text
CUSTOMER_RFM
```

analytical table.

RFM stands for:

### Recency

How recently a customer purchased.

### Frequency

How frequently a customer purchased.

### Monetary

How much a customer spent.

RFM analysis helps understand customer purchasing behavior and identify different customer segments.

---

# ⚙️ Phase 5 — Transformation & Orchestration

## Objective

Automate the transformation pipeline using **Snowflake Stored Procedures and Tasks**.

The pipeline follows:

```text
RAW
 ↓
SP_REFRESH_STAGING
 ↓
STAGING
 ↓
SP_REFRESH_MARTS
 ↓
MARTS
```

---

## Stored Procedures

### SP_REFRESH_STAGING

Refreshes the STAGING tables from the RAW layer.

### SP_REFRESH_MARTS

Refreshes the MARTS analytical tables from the STAGING layer.

---

## Snowflake Tasks

The project uses Snowflake Tasks to automate execution.

```text
REFRESH_STAGING_TASK
          │
          ▼
REFRESH_MARTS_TASK
```

The MARTS task depends on the completion of the STAGING task.

This creates an automated pipeline where:

1. STAGING is refreshed.
2. After STAGING completes, MARTS is refreshed.

---

# 📈 Phase 6 — Exploratory Data Analysis

EDA is performed using a **Snowflake Notebook**.

### Technologies used

```text
Snowflake
   +
Snowpark Python
   +
Pandas
   +
Matplotlib
```

The notebook combines SQL processing with Python-based analysis and visualization.

---

# 📊 EDA Question 1 — Where Are Late Deliveries Worst?

## Objective

Calculate the overall late delivery rate and identify states with higher late-delivery rates.

### Tables used

```text
MARTS.FCT_ORDERS
STAGING.CUSTOMERS
```

The tables are joined using:

```text
CUSTOMER_ID
```

The analysis calculates:

```text
Late Delivery Rate =
Late Orders / Total Orders × 100
```

The result is visualized using a bar chart showing the top states by late-delivery rate.

### Business Question

> Which customer states experience higher delivery delays?

---

# 💰 EDA Question 2 — How Concentrated Is Revenue?

## Objective

Understand how revenue is distributed among customers based on their spending.

The analysis uses:

```text
MARTS.CUSTOMER_RFM
```

Customers are divided into four monetary groups:

```text
Q1 → Low Spending
Q2 → Lower-Middle Spending
Q3 → Higher-Middle Spending
Q4 → High Spending
```

The total monetary value of each group is calculated to understand revenue concentration.

### Business Question

> How much revenue is generated by high-spending customers?

---

# 📅 EDA Question 3 — Is There Seasonality in Order Volume?

## Objective

Identify monthly patterns in order volume.

The analysis uses:

```text
STAGING.ORDERS
```

The process is:

```text
Purchase Timestamp
        ↓
Extract Month
        ↓
Group by Month
        ↓
Count Orders
        ↓
Line Chart
```

### Business Question

> Are there months with higher or lower order volumes?

---

# 🏪 EDA Question 4 — Which Sellers Have Higher Late Rates?

## Objective

Analyze seller-level delivery performance.

Tables used:

```text
MARTS.FCT_ORDER_ITEMS
MARTS.FCT_ORDERS
```

The tables are joined using:

```text
ORDER_ID
```

Seller-level late delivery rates are calculated.

Only sellers with at least **20 orders** are included to avoid results based on very small sample sizes.

### Output

```text
SELLER_ID
TOTAL_ORDERS
LATE_RATE_PCT
```

### Business Question

> Which sellers have relatively high late-delivery rates?

---

# 🐍 Snowpark + Pandas Approach

The project does not load every Snowflake table into Pandas.

Two important tables are loaded directly:

```python
orders_df = session.table("MARTS.FCT_ORDERS").to_pandas()

rfm_df = session.table("MARTS.CUSTOMER_RFM").to_pandas()
```

For larger joins and aggregations, SQL is executed inside Snowflake.

The general approach is:

```text
Large Snowflake Data
        ↓
SQL filtering / joining / aggregation
        ↓
Small summarized result
        ↓
Pandas
        ↓
Visualization
```

This keeps large-data processing inside Snowflake and uses Pandas mainly for analysis and visualization.

---

# 📊 Business Analysis Areas

| Business Area | Analysis |
|---|---|
| Orders | Order volume and trends |
| Delivery | Late delivery performance |
| Customers | RFM analysis |
| Revenue | Customer spending concentration |
| Sellers | Seller delivery performance |
| Products | Product and category analysis |
| Geography | Customer and seller locations |
| Reviews | Customer feedback data |

---

# 📁 Project Structure

```text
olist-ecommerce-data-engineering/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingest.py
│   ├── transform.py
│   └── validation.py
│
├── sql/
│   ├── schema.sql
│   ├── staging.sql
│   ├── marts.sql
│   ├── data_quality.sql
│   └── tasks.sql
│
├── notebooks/
│   └── phase6_eda.ipynb
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# 🧪 Data Quality Checks

The project validates:

- Null values
- Duplicate records
- Referential integrity
- Orphan records
- Negative values
- Record-count differences
- Invalid analytical values

These checks help ensure that data is reliable before it reaches the analytical layer.

---

# 🎯 Key Learning Outcomes

This project demonstrates practical experience with:

- End-to-end ETL pipelines
- Snowflake data warehousing
- RAW / STAGING / MARTS architecture
- SQL transformations
- Data cleaning
- Data validation
- Fact and dimension modeling
- RFM analysis
- Snowflake Stored Procedures
- Snowflake Tasks
- Task dependencies
- Snowpark Python
- Pandas
- Exploratory Data Analysis
- Data visualization
- Business-oriented analytics

---

# 🔮 Future Enhancements

Planned or potential extensions include:

- NLP analysis of customer reviews
- Sentiment analysis
- Customer segmentation
- Seller performance scoring
- Power BI dashboard
- Automated data quality monitoring
- Pipeline failure notifications
- Advanced business analytics

---

# 📌 Project Status

### Completed

- [x] Phase 1 — Data Ingestion
- [x] Phase 2 — Data Cleaning & Transformation
- [x] Phase 3 — Data Quality & Validation
- [x] Phase 4 — Data Modeling
- [x] Phase 5 — Transformation & Orchestration
- [x] Phase 6 — Exploratory Data Analysis

### Upcoming

- [ ] Phase 7 — NLP / Sentiment Analysis
- [ ] Advanced Analytics
- [ ] BI Dashboard
- [ ] Final Documentation

---

# 👩‍💻 Project Summary

This project demonstrates an end-to-end **E-Commerce Data Engineering and Analytics workflow** using Snowflake and Python.

The pipeline transforms raw Olist data into clean, validated, business-ready analytical datasets and uses them to investigate customer behavior, delivery performance, seller performance, revenue concentration, and order trends.

```text
RAW DATA
   ↓
DATA CLEANING
   ↓
DATA VALIDATION
   ↓
DATA MODELING
   ↓
ORCHESTRATION
   ↓
EDA
   ↓
BUSINESS INSIGHTS
```

---

## ⭐ Skills Demonstrated

**Python | SQL | Snowflake | Snowpark | Pandas | Matplotlib | ETL | Data Cleaning | Data Quality | Data Modeling | RFM Analysis | Data Engineering | Exploratory Data Analysis | Git | GitHub**
