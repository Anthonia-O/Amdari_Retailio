Retail Sales Analytics Pipeline (Snowflake + Airbyte + Power BI)
��� Project Overview

This project demonstrates an end-to-end data analytics pipeline built using modern data engineering tools.
Raw retail sales and product data are ingested, cleaned, transformed, and visualised in a professional Power BI dashboard to support business decision-making.

The project focuses on:

Reliable data ingestion

Clean, analytics-ready data modelling

Business-focused visualisation and insights

���️ Architecture Overview
Source Data
   ↓
Airbyte (Ingestion)
   ↓
Snowflake (RAW → CLEAN → ANALYTICS)
   ↓
Power BI (Executive Dashboards)

Key Design Principles

Separation of RAW, CLEAN, and ANALYTICS layers

Idempotent transformations using SQL and stored procedures

BI-friendly views optimised for reporting

Scalable and production-style architecture

��� Repository Structure
.
├── data/
│   └── Raw input datasets (sales & product data)
│
├── encoding.py
│   └── Utility script for handling encoding or preprocessing tasks
│
├── POWERBI_VISUALS/
│   └── Power BI (.pbix) files and dashboard assets
│
├── requirements.txt
│   └── Python dependencies for local scripts
│
├── test.py
│   └── Testing or exploratory scripts
│
├── tempCodeRunnerFile.py
│   └── Temporary file (can be ignored or removed)
│
├── venv/
│   └── Python virtual environment (not required for production)
│
└── README.md

��� Data Pipeline Details
1️⃣ Data Ingestion

Data is ingested into Snowflake using Airbyte

Tables are first landed in the RAW schema without transformation

Schema tracking is enabled to handle future changes safely

2️⃣ Data Transformation

SQL transformations clean and standardise the data

Key transformations include:

Date parsing and formatting

Numeric type casting (Sales, Profit, Quantity, Discount)

Standardised naming conventions

Final output is exposed as a BI-friendly view:

V_POWERBI_CLEAN_DATA

3️⃣ Analytics Layer

Cleaned sales and product data are joined

Business-ready metrics are derived:

Total Sales

Total Profit

Profit Margin

Quantity Sold

Discount impact

��� Power BI Dashboard

The Power BI report is designed for executive and business users and includes:

��� Executive Overview

KPI cards (Sales, Profit, Margin, Quantity)

Sales vs Profit trends over time

Regional performance comparison

��� Product & Category Performance

Profitability by category and sub-category

Top and bottom performing products

Sales vs Profit comparison

��� Discount & Loss Analysis

Discount vs Profit scatter analysis

Profit margin by discount bands

Identification of loss-making discount strategies

All visuals are fully interactive using slicers for:

Date

Region

Segment

Category

���️ Technologies Used

Snowflake – Cloud data warehouse

Airbyte – Data ingestion & orchestration

Power BI – Business intelligence & visualisation

SQL – Data transformation and modelling

Python – Supporting scripts and utilities

��� How to Use This Project

Load raw data into Snowflake (via Airbyte or manual upload)

Run transformation scripts / stored procedures

Connect Power BI to the V_POWERBI_CLEAN_DATA view

Refresh visuals and explore insights

��� Key Learning Outcomes

Designing a modern analytics pipeline

Working with cloud data warehouses

Building executive-level dashboards

Translating raw data into business insights

Applying best practices in data modelling and BI

��� Contact

If you’d like to discuss this project or collaborate:

Author: Anthonia
Focus Areas: Data Engineering • Analytics • Business Intelligence
