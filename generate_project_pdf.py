#!/usr/bin/env python3
"""
Generate a professional PDF document showcasing the DeltaClimate project.
This document serves as a portfolio piece demonstrating the work completed on this climate data visualization and AI-powered analytics platform.
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from datetime import datetime
import os


def generate_deltaclimate_pdf():
    """Generate a comprehensive PDF document showcasing the DeltaClimate project."""
    
    # Create PDF file
    pdf_filename = "DeltaClimate_Project_Portfolio.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Container for the 'flowable' objects
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=14
    )
    
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['BodyText'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=6,
        leading=13
    )
    
    # Title Page
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("DeltaClimate", title_style))
    story.append(Paragraph("AI-Powered Climate Data Analytics Platform", 
                          ParagraphStyle('subtitle', parent=styles['Normal'], 
                                       fontSize=16, alignment=TA_CENTER, 
                                       textColor=colors.HexColor('#4b5563'))))
    story.append(Spacer(1, 0.5*inch))
    
    story.append(Paragraph("Project Portfolio Document", 
                          ParagraphStyle('subtitle2', parent=styles['Normal'], 
                                       fontSize=14, alignment=TA_CENTER, 
                                       textColor=colors.HexColor('#6b7280'))))
    story.append(Spacer(1, 0.3*inch))
    
    # Author info
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y')}", 
                          ParagraphStyle('date', parent=styles['Normal'], 
                                       fontSize=12, alignment=TA_CENTER, 
                                       textColor=colors.HexColor('#9ca3af'))))
    
    story.append(PageBreak())
    
    # Executive Summary
    story.append(Paragraph("Executive Summary", heading1_style))
    story.append(Paragraph(
        "DeltaClimate is an innovative web application that revolutionizes how users interact with climate change data. "
        "Built with a custom PyReact framework, this platform combines advanced AI capabilities with intuitive data "
        "visualization to make complex climate information accessible to everyone. The project demonstrates expertise "
        "in full-stack development, AI integration, data processing, and modern web technologies.",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Project Overview
    story.append(Paragraph("Project Overview", heading1_style))
    story.append(Paragraph(
        "DeltaClimate is a comprehensive climate data analytics platform that empowers users to explore, understand, "
        "and analyze climate change data through an interactive web interface. The application leverages Google's "
        "Gemini AI to generate detailed narratives about climate impacts, while providing real-time data visualization "
        "of CO2 emissions trends spanning from 1960 to 2018.",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Key Features
    story.append(Paragraph("Key Features & Capabilities", heading1_style))
    
    features = [
        ("Interactive Data Visualization", 
         "Dynamic charts and graphs powered by ApexCharts that display CO2 emissions trends over time with country-specific filtering"),
        
        ("AI-Powered Climate Stories", 
         "Integration with Google Gemini AI to generate comprehensive, formatted narratives about climate change impacts for specific countries and timelines"),
        
        ("Intelligent Q&A System", 
         "Natural language question-answering system that provides context-aware responses about climate data using AI"),
        
        ("Country-Specific Analysis", 
         "Detailed exploration of climate data and impacts for different countries with interactive map visualizations"),
        
        ("Modern Responsive UI", 
         "Professional dark-themed interface built with DaisyUI and Tailwind CSS for optimal user experience"),
        
        ("Real-time Data Processing", 
         "Access to comprehensive datasets including CO2 emissions from 1960-2018 and supply chain GHG emission factors")
    ]
    
    for feature_title, feature_desc in features:
        story.append(Paragraph(f"<b>{feature_title}:</b> {feature_desc}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Technology Stack
    story.append(Paragraph("Technology Stack", heading1_style))
    story.append(Paragraph(
        "The project demonstrates proficiency across multiple modern technologies and frameworks:",
        body_style
    ))
    
    tech_data = [
        ['Category', 'Technologies'],
        ['Framework', 'PyReact (Custom Python-based framework)'],
        ['Backend', 'FastAPI, Uvicorn, Python 3.7+'],
        ['AI/ML', 'Google Generative AI (Gemini 1.5 Flash)'],
        ['Frontend', 'DaisyUI, Tailwind CSS, ApexCharts'],
        ['Data Processing', 'Python CSV processing, Pandas-style operations'],
        ['Development', 'Hot reloading, watchdog file monitoring']
    ]
    
    tech_table = Table(tech_data, colWidths=[1.5*inch, 4*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(tech_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(PageBreak())
    
    # Architecture & Design
    story.append(Paragraph("Architecture & Design", heading1_style))
    
    story.append(Paragraph("PyReact Framework", heading2_style))
    story.append(Paragraph(
        "At the core of DeltaClimate is PyReact, a custom-built Python web framework that combines the best of "
        "server-side rendering with client-side interactivity. This framework was designed specifically to handle "
        "the unique requirements of data-intensive applications with real-time updates.",
        body_style
    ))
    
    pyreact_features = [
        "Component-based architecture for modular, reusable UI elements",
        "Server-side rendering for optimal initial load performance",
        "Client-side routing for seamless navigation without page reloads",
        "Automatic state management across components",
        "Built-in event handling system",
        "Hot module reloading during development for rapid iteration"
    ]
    
    for feature in pyreact_features:
        story.append(Paragraph(f"• {feature}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Application Structure", heading2_style))
    story.append(Paragraph(
        "The application follows a clean, modular architecture that separates concerns and promotes maintainability:",
        body_style
    ))
    
    structure = [
        "<b>app.py</b> - Main application entry point with route definitions and request handlers",
        "<b>pyreact.py</b> - Core framework implementation with component system and routing logic",
        "<b>gemini.py</b> - Google Gemini AI integration for generating climate narratives",
        "<b>ask.py</b> - Question-answering module for interactive climate data queries",
        "<b>datalists.py</b> - Data management utilities and CSV processing functions",
        "<b>components/</b> - Reusable UI components (navbar, graphs, maps, chat panels)"
    ]
    
    for item in structure:
        story.append(Paragraph(f"• {item}", bullet_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # API Endpoints
    story.append(Paragraph("API Endpoints", heading1_style))
    
    api_data = [
        ['Method', 'Endpoint', 'Description'],
        ['GET', '/', 'Home page with pre-loaded climate data and visualizations'],
        ['POST', '/gemini', 'Generate detailed climate change stories for specific countries and timelines'],
        ['POST', '/ask', 'Ask questions about climate data and receive AI-powered answers']
    ]
    
    api_table = Table(api_data, colWidths=[0.8*inch, 1.2*inch, 3.5*inch])
    api_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(api_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(PageBreak())
    
    # Data Sources
    story.append(Paragraph("Data Sources & Processing", heading1_style))
    story.append(Paragraph(
        "The application utilizes comprehensive datasets to provide accurate, data-driven insights:",
        body_style
    ))
    
    data_sources = [
        "<b>CO2 Emissions Dataset (1960-2018):</b> Historical CO2 emissions data spanning nearly 60 years across all countries",
        "<b>Supply Chain GHG Emission Factors:</b> Comprehensive greenhouse gas emission factors using NAICS classification",
        "<b>Pre-computed Response Data:</b> Optimized JSON structures for fast initial page loads"
    ]
    
    for source in data_sources:
        story.append(Paragraph(f"• {source}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # AI Integration
    story.append(Paragraph("AI Integration & Intelligence", heading1_style))
    story.append(Paragraph(
        "DeltaClimate leverages Google's Gemini 1.5 Flash model to provide intelligent, context-aware insights. "
        "The AI integration includes:",
        body_style
    ))
    
    ai_features = [
        "Narrative generation with structured HTML output for professional presentation",
        "Context-aware responses based on uploaded CSV datasets",
        "Timeline-specific analysis with proper historical context",
        "Solution-oriented storytelling that includes actionable climate mitigation strategies",
        "Custom prompt engineering for consistent, high-quality outputs",
        "JSON response formatting for seamless frontend integration"
    ]
    
    for feature in ai_features:
        story.append(Paragraph(f"• {feature}", bullet_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Technical Achievements
    story.append(Paragraph("Technical Achievements", heading1_style))
    
    achievements = [
        ("Custom Framework Development", 
         "Built PyReact, a full-featured Python web framework from scratch with component-based architecture"),
        
        ("AI Model Integration", 
         "Successfully integrated Google Gemini AI with custom prompt engineering and file upload capabilities"),
        
        ("Real-time Data Visualization", 
         "Implemented dynamic, interactive charts using ApexCharts with server-side data processing"),
        
        ("Responsive Design", 
         "Created a modern, responsive UI using utility-first CSS with DaisyUI and Tailwind CSS"),
        
        ("API Design", 
         "Developed a clean, RESTful API structure using FastAPI with async/await patterns"),
        
        ("Data Processing Pipeline", 
         "Built efficient CSV data processing and transformation pipelines for large datasets")
    ]
    
    for achievement_title, achievement_desc in achievements:
        story.append(Paragraph(f"<b>{achievement_title}:</b> {achievement_desc}", bullet_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    story.append(PageBreak())
    
    # User Experience
    story.append(Paragraph("User Experience & Interface", heading1_style))
    story.append(Paragraph(
        "The application prioritizes user experience with an intuitive, visually appealing interface:",
        body_style
    ))
    
    ux_features = [
        "Dark theme optimized for extended viewing sessions",
        "Responsive layout that works seamlessly across devices",
        "Interactive charts with hover effects and data tooltips",
        "Clear navigation with a persistent navbar component",
        "AI-generated content with proper formatting and structure",
        "Loading states and error handling for smooth user interactions"
    ]
    
    for feature in ux_features:
        story.append(Paragraph(f"• {feature}", bullet_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Use Cases
    story.append(Paragraph("Use Cases & Applications", heading1_style))
    
    use_cases = [
        "<b>Educational Research:</b> Students and researchers can explore historical climate data and generate comprehensive reports",
        "<b>Policy Development:</b> Policymakers can analyze country-specific climate trends to inform environmental policies",
        "<b>Business Analytics:</b> Companies can assess supply chain emission factors for sustainability reporting",
        "<b>Public Awareness:</b> General public can access easy-to-understand climate information and AI-generated insights",
        "<b>Environmental Planning:</b> Organizations can use timeline-specific data for long-term environmental planning"
    ]
    
    for use_case in use_cases:
        story.append(Paragraph(f"• {use_case}", bullet_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Development Process
    story.append(Paragraph("Development Process & Methodology", heading1_style))
    story.append(Paragraph(
        "The project was developed following modern software engineering practices:",
        body_style
    ))
    
    dev_process = [
        "Modular code organization with clear separation of concerns",
        "Environment-based configuration using .env files",
        "Hot reload development mode for rapid iteration",
        "Comprehensive error handling and logging",
        "RESTful API design principles",
        "Component-based UI architecture for reusability"
    ]
    
    for process in dev_process:
        story.append(Paragraph(f"• {process}", bullet_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    story.append(PageBreak())
    
    # Future Enhancements
    story.append(Paragraph("Future Enhancements & Roadmap", heading1_style))
    story.append(Paragraph(
        "Potential future improvements to expand the platform's capabilities:",
        body_style
    ))
    
    future = [
        "Real-time data updates from live climate monitoring APIs",
        "User authentication and personalized dashboards",
        "Export functionality for reports and visualizations",
        "Advanced machine learning models for climate prediction",
        "Collaborative features for sharing insights and reports",
        "Mobile application using the same backend API",
        "Multi-language support for global accessibility",
        "Integration with additional climate databases and APIs"
    ]
    
    for item in future:
        story.append(Paragraph(f"• {item}", bullet_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Conclusion
    story.append(Paragraph("Conclusion", heading1_style))
    story.append(Paragraph(
        "DeltaClimate represents a significant achievement in combining modern web technologies, artificial intelligence, "
        "and data visualization to address one of the most pressing issues of our time: climate change. The project "
        "demonstrates strong technical capabilities across full-stack development, from building a custom web framework "
        "to integrating advanced AI models and processing large datasets.",
        body_style
    ))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "By making complex climate data accessible and understandable through AI-generated narratives and interactive "
        "visualizations, DeltaClimate serves as both a powerful analytical tool and an educational platform. The modular "
        "architecture and clean code structure ensure the application can be easily extended and maintained as climate "
        "data and analysis techniques continue to evolve.",
        body_style
    ))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "This project showcases the ability to design and implement sophisticated web applications that combine multiple "
        "advanced technologies into a cohesive, user-friendly platform that delivers real value to its users.",
        body_style
    ))
    
    story.append(Spacer(1, 0.5*inch))
    
    # Footer
    story.append(Paragraph("───────────────────────────────────────────", 
                          ParagraphStyle('divider', parent=styles['Normal'], 
                                       fontSize=12, alignment=TA_CENTER, 
                                       textColor=colors.HexColor('#9ca3af'))))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("DeltaClimate - Making Climate Data Accessible to Everyone", 
                          ParagraphStyle('footer', parent=styles['Normal'], 
                                       fontSize=10, alignment=TA_CENTER, 
                                       textColor=colors.HexColor('#6b7280'))))
    story.append(Paragraph("https://github.com/mianjunaid1223/DeltaClimate", 
                          ParagraphStyle('footer', parent=styles['Normal'], 
                                       fontSize=10, alignment=TA_CENTER, 
                                       textColor=colors.HexColor('#2563eb'))))
    
    # Build PDF
    doc.build(story)
    print(f"\n✅ PDF generated successfully: {pdf_filename}")
    return pdf_filename


if __name__ == "__main__":
    generate_deltaclimate_pdf()
