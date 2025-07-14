
# 🛫 Databricks Flights Data Pipeline Project

This is an **end-to-end data engineering project** on Databricks that demonstrates the modern **medallion architecture** — processing raw airline data through Bronze, Silver, and Gold layers using Delta Lake, Auto Loader, DBT, and dynamic notebooks for dimension and fact modeling.

> 🎥 [Watch Demo Video](https://youtu.be/vT7Oeu7WqHg?si=ujHz9mqmH2TD_l3H)  
> 📂 [GitHub Repo](https://github.com/PJ9172/Databricks_FlightsData.git)

---

## 🔍 Project Overview

The main goal of this project is to build a **robust data lakehouse** that ingests, transforms, and serves flight-related datasets such as:

- ✈️ Flights
- 🧑 Customers
- 🧾 Bookings
- 🗺️ Airports

This pipeline follows the **Lakehouse Architecture**:
- Ingest raw data into **Bronze Layer**
- Transform and clean into **Silver Layer**
- Create dimensional and aggregated tables in the **Gold Layer**
- Use **DBT for analytics modeling** and **dynamic notebooks** for building **dimensions and facts**

---

## 🧱 Architecture

```
              ┌────────────┐
              │  Raw Data  │
              └────┬───────┘
                   ▼
            ┌─────────────┐
            │ Bronze Layer│  <- Ingested using Auto Loader
            └────┬────────┘
                 ▼
           ┌─────────────┐
           │ Silver Layer│  <- Cleaned and Joined DataFrames
           └────┬────────┘
                ▼
         ┌──────────────────┐
         │ Gold Layer (DBT) │  <- Fact & Dim Models (SCD Type 1)
         └────┬─────────────┘
              ▼
    ┌────────────────────────────┐
    │ Dynamic Notebooks for Facts│
    │ and Dimensions (SCD Type 1)│
    └────────────────────────────┘
```

---

## 🧠 Key Features

- ✅ **Auto Loader** for schema inference and file ingestion
- ✅ **Dynamic Dimension Builder**: Generates dimension tables with upsert logic
- ✅ **Dynamic Fact Builder**: Builds fact tables from Silver layer dynamically
- ✅ **SCD Type 1** implementation using `MERGE` in Delta Lake
- ✅ **DBT Integration** for analytical modeling and reproducibility

---

## 🗂️ Catalog Structure (Databricks)

```
flight/
├── rawdata/
│   ├── airports/
│   ├── bookings/
│   ├── customers/
│   └── flights/
├── bronze/
│   └── bronzevolume/
├── silver/
│   └── Tables (6)
├── gold/
│   └── Tables (4)
├── dbt_pjagtap/
│   └── my_first_dbt_model/
└── information_schema/
```

> 📸 Catalog Preview:  
![Catalog Screenshot](./Screenshots/catalog.png)

---

## ⚙️ Technologies Used

- **Databricks Community Edition**
- **Delta Lake & Unity Catalog**
- **PySpark & SQL**
- **Auto Loader (Streaming Ingestion)**
- **Dynamic Notebooks (Dimension + Fact Builder)**
- **DBT (Data Build Tool)**

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/PJ9172/Databricks_FlightsData.git
```

2. Import notebooks into Databricks:
   - Use the **workspace UI** to import `.dbc` or individual notebooks.
   - Attach to a cluster and run cells in order.

3. Upload the raw data to `dbfs:/Volumes/flight/rawdata/`.

4. Run the **Bronze ingestion notebook** → **Silver transformations** → **Dynamic dimension/fact builders** → **DBT models**.

---

## 🧪 Dynamic Notebooks Logic

### 🔷 Dimension Builder
- Reads mapping configs to identify dimension tables
- Performs **UPSERT (SCD Type 1)** using `MERGE INTO`
- Automatically handles new & updated records

### 🔶 Fact Builder
- Joins cleaned Silver tables
- Generates fact tables with reference keys
- Supports partitioning & optimized Delta writes

---

## 📊 Sample Outputs (Gold Layer)

> ✨ Examples:
- Top 10 most booked airports
- Flight count by customer region
- Revenue by booking channel
- Frequent fliers with booking history

---

## 🙏 Acknowledgements

- Inspired by [YouTube Tutorial](https://youtu.be/vT7Oeu7WqHg?si=ujHz9mqmH2TD_l3H)
- Built on **Databricks Free Tier**

---

## 📬 Connect with Me

- 🔗 GitHub: [PJ9172](https://github.com/PJ9172)
- 💼 LinkedIn: [Prajwal-Jagtap](www.linkedin.com/in/prajwal-jagtap)

---
