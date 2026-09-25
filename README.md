# DeltaClimate: Environmental Data Analytics Platform

[![Year Built](https://img.shields.io/badge/Year%20Built-2024-blue.svg)](#)


Full-stack climate data exploration and greenhouse gas economic modeling platform built with PyReact, FastAPI, Gemini 1.5 Flash, and ReportLab.

```
+-----------------------------------------------------------------------------------------+
|                                    Client Viewport                                      |
|                                                                                         |
|   +---------------------------------------------------------------------------------+   |
|   | PyReact Reactive UI Engine (State Models, Event Listeners, Dynamic DOM Mounts)  |   |
|   | Geospatial emission maps, chronological emissions 1960-2018, economic models    |   |
|   +----------------------------------------|----------------------------------------+   |
+--------------------------------------------|--------------------------------------------+
                                             |
                                             v
+-----------------------------------------------------------------------------------------+
|                                FastAPI Application Core                                 |
|                                                                                         |
|   +-----------------------------------+   +-----------------------------------------+   |
|   | Temporal Emissions Engine         |   | Supply Chain GHG Modeler                |   |
|   | CO2_Emissions_1960-2018.csv       |   | SupplyChainGHGEmissionFactors (NAICS)   |   |
|   | Global historical timeseries      |   | Carbon intensity per USD capital flow   |   |
|   +-----------------+-----------------+   +--------------------+--------------------+   |
|                     |                                          |                        |
|                     +---------------------+--------------------+                        |
|                                           |                                             |
|                                           v                                             |
|   +---------------------------------------------------------------------------------+   |
|   | AI Synthesis & Document Generation                                              |   |
|   | - Google Gemini 1.5 Flash: Automated policy narratives and sector decarbonization|   |
|   | - ReportLab PDF Engine: Executive climate portfolio compilation (app.py)        |   |
|   +---------------------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------------------+
```

## System Architecture

DeltaClimate is an open-source environmental data intelligence application combining historical carbon emission records with modern industrial supply-chain factor models. The frontend utilizes the PyReact framework to deliver reactive components in Python that transpile to client-side DOM trees.

### Analytical Pipelines

1. Historical Emissions Timeseries: Ingests CO2_Emissions_1960-2018.csv spanning global records across five decades. Generates trend projections, baseline shifts, and country-level comparisons.

2. NAICS Supply-Chain GHG Economic Engine: Uses SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv to calculate emission intensity ratios per dollar spent across industrial classification codes.

3. AI Climate Policy Synthesis: The gemini.py module interfaces with Gemini 1.5 Flash to convert raw numerical timeseries data into structured executive briefs and mitigation strategies.

4. Automated Report Generation: The generate_project_pdf.py script compiles live statistical evaluations into printable PDF documents through ReportLab.

## Technical Specifications

| Parameter | Specification |
|---|---|
| Year Built | 2024 |
| Frontend Framework | PyReact (Python-based component model) |
| Backend Server | FastAPI with ASGI Uvicorn workers |
| Datasets | Global CO2 (1960-2018), US EPA Supply Chain GHG Factors v1.2 |
| AI Foundation | Google Gemini 1.5 Flash via google-generativeai |
| Report Compiler | ReportLab canvas graphics and flowables |

## API Endpoints

| Route | Method | Description |
|---|---|---|
| /api/emissions/timeseries | GET | Retrieves chronological emissions records for selected country |
| /api/naics/factor | GET | Queries greenhouse gas factor by NAICS industry code |
| /api/analyze | POST | Dispatches timeseries data to Gemini 1.5 Flash for policy narrative |
| /api/export-pdf | GET | Generates downloadable ReportLab summary document |

## Local Installation

```bash
git clone https://github.com/mianjunaid1223/DeltaClimate.git
cd DeltaClimate
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install fastapi uvicorn google-generativeai pandas reportlab
python app.py
```
