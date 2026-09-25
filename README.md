# Delta Climate: Climate Intelligence Dashboard

A data visualization and climate intelligence platform built with the PyReact Python framework, FastAPI, and Google Gemini AI. Delta Climate combines historical global greenhouse gas records with contextual generative AI to translate complex emissions datasets into interactive visual trends and readable analytical narratives.

---

## System Architecture

```
+-----------------------+      +---------------------------+      +-------------------------+
|   Client Web Browser  | <--> |   PyReact / FastAPI App   | <--> | Google Gemini AI Model  |
| (ApexCharts, Tailwind)|      |   (Uvicorn ASGI Server)   |      | (gemini-1.5-flash)      |
+-----------------------+      +---------------------------+      +-------------------------+
                                             |
                                             v
                               +---------------------------+
                               |   Climate Data Sources    |
                               | - CO2 Emissions 1960-2018 |
                               | - Supply Chain GHG Factors|
                               | - pre-response.json Cache |
                               +---------------------------+
```

---

## Core Capabilities

1. Time-Series Emissions Analytics:
   Visualizes multidecadal CO2 emissions trajectories from 1960 through 2018 across global territories using responsive ApexCharts components.

2. AI-Driven Environmental Narratives:
   Dispatches country and temporal parameters to Google Gemini to synthesize historical policy changes, industrial shifts, and emissions drivers into structured analytical reports.

3. Interactive Data Query Interface:
   Enables users to submit ad-hoc analytical queries regarding emissions patterns, receiving synthesized answers grounded in historical records and supply chain data.

4. Supply Chain GHG Profiling:
   Integrates NAICS-classified supply chain emission factors (2021 USD equivalent) to evaluate industry-level greenhouse gas contributions.

5. Portfolio & Report Generation:
   Includes an integrated PDF engine (`generate_project_pdf.py`) that compiles architectural summaries, technical achievements, and visualizations into downloadable documents.

---

## Technical Stack

- Web Framework: PyReact (Python component layout and reactive state engine)
- ASGI Server: FastAPI and Uvicorn
- AI Engine: Google Generative AI Python SDK (Gemini 1.5 Flash)
- Data Visualization: ApexCharts
- Interface Styling: Tailwind CSS and DaisyUI
- Data Processing: Python (Pandas, CSV parsing routines)
- Document Generation: ReportLab / PDF export utilities

---

## Dataset Reference

Delta Climate integrates the following primary data sources:

1. `CO2_Emissions_1960-2018.csv`:
   Annual carbon dioxide emissions aggregated across sovereign nations from 1960 to 2018, measured in metric tons per capita and gross national output.

2. `SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv`:
   Granular emissions intensity metrics across commercial industries categorized by North American Industry Classification System (NAICS) codes.

3. `pre-response.json`:
   Pre-cached baseline query responses to accelerate initial dashboard loads without redundant AI API calls.

---

## API Documentation

### 1. Primary Dashboard View
- Method: `GET`
- Endpoint: `/`
- Description: Delivers the main PyReact single-page dashboard with pre-loaded charts and search panels.

### 2. Generate Regional Climate Narrative
- Method: `POST`
- Endpoint: `/gemini`
- Request Format: JSON
  ```json
  {
    "country": "Germany",
    "timeline": "1990-2018"
  }
  ```
- Response: Formatted narrative examining historical emission trends and major contributing sectors.

### 3. Query Climate Data
- Method: `POST`
- Endpoint: `/ask`
- Request Format: JSON
  ```json
  {
    "question": "Which industrial sectors accounted for the largest emissions growth after 2000?"
  }
  ```
- Response: Synthesized explanation referencing dataset records.

### 4. Download Technical Portfolio
- Method: `GET`
- Endpoint: `/portfolio-pdf`
- Response: Direct binary stream of `DeltaClimate_Project_Portfolio.pdf`.

---

## Installation & Local Execution

### Prerequisites
- Python 3.8 or newer
- Google Gemini API key

### Setup Steps

1. Clone repository:
   ```bash
   git clone https://github.com/mianjunaid1223/DeltaClimate.git
   cd DeltaClimate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirenments.txt
   ```

3. Set up environment variables in `.env`:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:3000` in your browser.

6. To generate the project portfolio PDF directly from command line:
   ```bash
   python generate_project_pdf.py
   ```

---

## Project Structure

```
DeltaClimate/
|-- app.py                     # Main application entry point and routing
|-- pyreact.py                 # Core PyReact component engine
|-- gemini.py                  # Google Gemini API integration and prompts
|-- ask.py                     # Q&A query handler
|-- datalists.py               # Data parsing and lookup utilities
|-- generate_project_pdf.py    # Automated PDF documentation generator
|-- index.html                 # HTML shell template
|-- components/                # Modular PyReact UI components
|   |-- navbar.py              # Navigation bar
|   |-- story.py               # AI story presentation view
|   |-- chatp.py               # Interactive chat panel
|   |-- graph.py               # ApexCharts visual wrapper
|   |-- map.py                 # Geographical data view
|-- static/                    # CSS stylesheets and client scripts
|-- pre-response.json          # Cached sample responses
```
