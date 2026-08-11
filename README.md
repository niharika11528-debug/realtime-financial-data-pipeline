# Real-Time Financial Market Data Streaming Pipeline (Python & CI/CD)

An event-driven, production-grade real-time streaming architecture engineered to simulate continuous market trading activity, execute stream filtering and transformation routines, perform automated financial anomaly detection, and append clean transactional metrics directly into an analytical data store layout.

## 🏗️ Event-Driven Streaming Architecture Design
```text
[Live Finnhub API Source / Financial Feeds]
                 │
                 ▼ (Continuous Ingestion via Python Core)
[Stage 1: stream_market.py] ───(Generates Micro-Batch Blocks)───> [/tmp/streaming_buffer/ (Bronze Zone)]
                 │
                 ▼ (Event-Driven Transformation Filter: max(ctime))
[Stage 2: process_stream.py] ──(Calculates Valuations & Anomalies)─> [Analytical Data Warehouse (Gold Zone)]
                 │
                 ▼ (Push Quality Control Gate)
[GitHub Actions CI/CD Run] ────(Automated Server Compilation)─────> [Production Verified Release Build]
```

## 💡 Engineering Highlights & Core Patterns Demonstrated
* **Micro-Batch Buffering Engine:** Simulates real-time market activity by capturing ticks into structured columnar partitions (`Parquet`) to preserve high-velocity system processing capabilities.
* **Stream Feature Engineering & Filtering:** Evaluates transactional data in real time to derive execution valuations and flags extreme high-value volume shifts (`total_order_value > $50,000`) instantly for downstream algorithms.
* **Data State Consolidation & Appending:** Gracefully detects historical state shapes inside storage folders, dynamically running memory combinations via Pandas vectors to append live micro-records into clean time-series files without duplication.
* **Continuous Integration CI/CD Gates:** Leverages automated configuration suites via GitHub Actions to ensure modular codebases compile and check successfully across cloud systems before builds execute live.

## 🛠️ Data Technology Stack
* **Processing & Streaming Language:** Python Core Programming Interface
* **Transformations & Data Structures:** Pandas Core Engine, Numpy Matrix Foundations
* **Storage Performance Formats:** Compressed Parquet (PyArrow Columnar Serialization Engines)
* **Automated Quality Pipelines:** GitHub Actions Server Workflows (Ubuntu Linux Core Runners)

## 📁 Repository Directory Layout
* `streaming_src/extract/` — Interactive core script establishing ingestion ticks and micro-batch stream file generation blocks.
* `streaming_src/transform/` — Event-driven computation script managing parsing, valuation generation, and asset state consolidations.
* `.github/workflows/` — Continuous Integration pipeline rules defining server testing suites.
* `requirements.txt` — Explicit framework packages pinning precise operational version control.

---
*Developed completely via mobile terminal infrastructure interfaces to demonstrate versatile engineering, system flexibility, and version-control competencies.*
