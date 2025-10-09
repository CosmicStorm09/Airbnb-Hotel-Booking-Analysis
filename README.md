Airbnb Hotel Booking Analysis
Project Overview

This repository contains a simple Python-based analysis of Airbnb listings to extract key pricing insights, perform market segmentation by room type and neighborhood, and generate actionable recommendations. The project was completed as part of the VOIS AICTE DIY internship, October 2025.
Repository Structure

text
airbnb-analysis/  
│  
├── data/  
│   └── airbnb_listings.csv      # Airbnb CSV dataset  
│  
├── code/  
│   └── simple_airbnb_basic_full.py  # Python analysis script  
│  
├── output/  
│   ├── simple_airbnb_results.csv    # Generated CSV results  
│   ├── chart_room_type.png          # Bar chart: average price by room type  
│   ├── chart_borough.png            # Bar chart: average price by borough  
│   ├── chart_availability.png       # Chart: availability distribution  
│   ├── prompt_basic.png             # Screenshot: basic mode terminal run  
│   └── prompt_full.png              # Screenshot: full mode terminal run  
│  
├── ppt/  
│   └── Airbnb_Hotel_Analysis.pptx   # Final project presentation  
│  
└── README.md                        # This file  

How to Run the Analysis

    Clone the repository

bash
git clone https://github.com/YourUsername/airbnb-analysis.git
cd airbnb-analysis

Install dependencies

bash
pip install pandas openpyxl

Run the script

    bash
    python code/simple_airbnb_basic_full.py

        When prompted, enter the path to data/airbnb_listings.csv.

        Choose basic or full mode for analysis.

    View outputs

        Results saved to output/simple_airbnb_results.csv.

        Charts and terminal screenshots located in output/.

Screenshots & Visuals

    Basic mode: average, min, max prices (output/prompt_basic.png)

    Full mode: includes room type and neighborhood breakdown (output/prompt_full.png)

    Charts:

        Room type averages (output/chart_room_type.png)

        Borough averages (output/chart_borough.png)

        Availability distribution (output/chart_availability.png)

Presentation

See ppt/Airbnb_Hotel_Analysis.pptx for slides covering objectives, methodology, findings, and recommendations.
Future Work

    Extend analysis with machine learning price prediction

    Build an interactive dashboard (Streamlit or Dash)

    Automate data updates and reporting
