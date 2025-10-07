# Delta Climate

Delta Climate is a PyReact-based web application that allows users to access complex climate change information in an easy and interactive manner. Built using the PyReact framework, this application provides comprehensive climate data analysis, visualizations, and AI-powered insights.

## About

Delta Climate leverages the power of PyReact framework to deliver an intuitive interface for exploring climate change data. Users can visualize CO2 emissions trends, explore country-specific climate information, and get AI-generated stories and insights about climate change impacts across different timelines.

## Features

- **Interactive Climate Data Visualization**: Dynamic charts and graphs showing CO2 emissions trends over time using ApexCharts
- **AI-Powered Climate Stories**: Generate detailed, formatted narratives about climate change for specific countries and time periods using Google Gemini AI
- **Country-Specific Analysis**: Explore climate data and impacts for different countries with interactive maps
- **Question & Answer System**: Ask specific questions about climate data and get AI-powered answers
- **Responsive Dark Theme UI**: Modern, user-friendly interface built with DaisyUI and Tailwind CSS
- **Real-time Data Processing**: Access to comprehensive CO2 emissions data from 1960-2018 and supply chain GHG emission factors
- **Project Portfolio PDF**: Generate a comprehensive PDF document showcasing the project's features, architecture, and technical accomplishments

## Technology Stack

- **Framework**: PyReact (custom Python-based web framework)
- **Backend**: FastAPI, Uvicorn
- **AI Integration**: Google Generative AI (Gemini)
- **Frontend**: DaisyUI, Tailwind CSS, ApexCharts
- **Data Processing**: Python with CSV datasets

## Installation

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/mianjunaid1223/DeltaClimate.git
cd DeltaClimate
```

2. Install the required dependencies:
```bash
pip install -r requirenments.txt
```

3. Set up your environment variables:
Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

4. Ensure you have the required data files:
- `CO2_Emissions_1960-2018.csv`
- `SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv`
- `pre-response.json`

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:3000
```

3. Interact with the application:
   - View pre-loaded climate data visualizations on the home page
   - Select countries and time periods to generate detailed climate stories
   - Ask specific questions about climate data using the interactive panel
   - Explore CO2 emissions trends through interactive graphs

### Generate Project Portfolio PDF

To generate a PDF document showcasing the project:

**Option 1: Run the generation script directly**
```bash
python generate_project_pdf.py
```

**Option 2: Access via the web interface**
```
http://127.0.0.1:3000/portfolio-pdf
```

This will generate and download a comprehensive PDF document (`DeltaClimate_Project_Portfolio.pdf`) containing:
- Executive summary
- Project overview and features
- Technology stack and architecture details
- API documentation
- Technical achievements and design decisions

## Project Structure

```
DeltaClimate/
│
├── app.py                          # Main application entry point
├── pyreact.py                      # PyReact framework core
├── index.html                      # HTML template
├── gemini.py                       # Google Gemini AI integration
├── ask.py                          # Question answering module
├── datalists.py                    # Data management utilities
├── components/                     # UI components
│   ├── navbar.py                   # Navigation bar component
│   ├── story.py                    # Climate story display component
│   ├── chatp.py                    # Chat panel component
│   ├── graph.py                    # Data visualization component
│   └── map.py                      # Map visualization component
├── static/                         # Static assets (CSS, JS)
├── .env                            # Environment variables (create this)
├── pre-response.json               # Pre-loaded response data
├── CO2_Emissions_1960-2018.csv    # Historical CO2 emissions data
└── SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv
```

## API Endpoints

- `GET /` - Home page with pre-loaded climate data and visualizations
- `POST /gemini` - Generate climate change stories for specific countries and timelines
- `POST /ask` - Ask questions about climate data and get AI-powered answers
- `GET /portfolio-pdf` - Download the DeltaClimate project portfolio PDF document

## About PyReact Framework

This application is built using PyReact, a custom Python-based web framework that combines server-side rendering with client-side interactivity. PyReact provides:

- Component-based architecture
- Server-side rendering
- Client-side routing
- Automatic state management
- Event handling
- Hot reloading in development mode

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms specified in the LICENSE file.

## Acknowledgments

- Climate data sourced from global CO2 emissions databases
- AI capabilities powered by Google Gemini
- UI components styled with DaisyUI and Tailwind CSS
- Built with the PyReact framework
