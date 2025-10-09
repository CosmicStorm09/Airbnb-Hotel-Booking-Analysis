# Airbnb Hotel Booking Analysis

Welcome to the **Airbnb Hotel Booking Analysis** project! This repository contains everything needed to reproduce the analysis, view visuals, and review the presentation.

## 📂 Repository Structure  
```
├── data/
│   └── airbnb.csv         # Raw Airbnb dataset (CSV)
│
├── code/
│   └── airbnb.py          # Python script with “basic” and “full” modes
│
├── output/
│   ├── Price Distribution_Figure_1.webp                       # CSV of analysis results
│   ├── Average Price per Room Type_Figure_2.webp              # Bar chart: avg price by room type
│   ├── Average Price per Neighbourhood group_Figure_3.webp    # Bar chart: avg price by borough
│   ├── chart_availability.png                                 # Chart: availability distribution
│   ├── Basic Analysis.png                                     # Screenshot: basic mode run
│   └── Full Analysis.png                                      # Screenshot: full mode run
│
├── ppt/
│   └── airbnb.pptx  # Final presentation
│
└── README.md                       # This file
```

***

## 🚀 Quick Start

1. **Clone this repository**  
   ```bash
   git clone https://github.com/YourUsername/airbnb-analysis.git
   cd airbnb-analysis
   ```

2. **Install dependencies**  
   ```bash
   pip install pandas openpyxl
   ```

3. **Run the analysis**  
   ```bash
   python code/airbnb.py
   ```
   - Enter the path to `data/airbnb.csv` when prompted  
   - Choose **basic** or **full** mode for results  

4. **View outputs**  
   - Results CSV: `output/simple_airbnb_results.csv`  
   - Visual charts in `output/`  
   - Terminal screenshots in `output/`

***

## 🎯 Project Components

### 1. Python Code (`code/simple_airbnb_basic_full.py`)  
- **load_data()**: Reads Excel/CSV or loads sample data  
- **basic_analysis()**: Computes average, min, max price  
- **full_analysis()**: Adds breakdown by room type & neighborhood  
- **main()**: Ties it together with user prompts  

### 2. Data (`data/airbnb_listings.csv`)  
- ~102,599 Airbnb listings  
- Key columns: `price`, `room type`, `neighbourhood group`  

### 3. Outputs (`output/`)  
- **Average Price per Room Type_Figure_2.webp**: Average price by room type  
- **Average Price per Neighbourhood group_Figure_3.webp**: Average price by borough  
- **Price Distribution_Figure_1.webp**: Availability distribution chart  
- **Basic Analysis.png**: Screenshot of basic mode  
- **Full Analysis.png**: Screenshot of full mode  

### 4. Presentation (`ppt/Airbnb_Hotel_Analysis.pptx`)  
Contains slides on:
- Objective & scope  
- Data overview  
- Methodology  
- Key findings  
- Charts & visuals  
- Recommendations  
- Code & GitHub link  

***

## 🔗 GitHub Repository

Visit the live repo here:  
https://github.com/YourUsername/airbnb-analysis

Clone and explore all code, data, outputs, and the PPT.

***

## 🌟 Next Steps

- Extend with a machine learning price prediction model  
- Deploy a web dashboard for interactive exploration  
- Automate data updates and notifications  

***

**Thank you for reviewing!** Feel free to raise an issue or pull request if you have suggestions.
