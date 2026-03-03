# Airbnb Hotel Booking Analysis

Welcome to the **Airbnb Hotel Booking Analysis** project! This repository contains everything needed to reproduce the analysis, view visuals, and review the presentation.

##  Repository Structure  
```
├── data/
│   └── airbnb.xlsx        # Raw Airbnb dataset (XLSX/CSV)
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
└── README.md               # This file
```

***

##  Quick Start

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
   - Enter the path to `data/airbnb.xlsx` when prompted  
   - Choose **basic** or **full** mode for results  

4. **View outputs**  
   - Results CSV: `output/airbnb_results.csv`  
   - Visual charts in `output/`  
   - Terminal screenshots in `output/`

***

##  Project Components

### Python Code (`code/airbnb.py`)  
- **load_data()**: Reads CSV or loads sample data  
- **basic_analysis()**: Computes average, min, max price  
- **full_analysis()**: Adds breakdown by room type & neighborhood  
- **main()**: Ties it together with user prompts  

### Data (`data/airbnb.csv`)  
- ~102,599 Airbnb listings  
- Key columns: `price`, `room type`, `neighbourhood group`  

### Outputs (`output/`)  
- **Average Price per Room Type_Figure_2.webp**: Average price by room type  
- **Average Price per Neighbourhood group_Figure_3.webp**: Average price by borough  
- **Price Distribution_Figure_1.webp**: Availability distribution chart  
- **Basic Analysis.png**: Screenshot of basic mode  
- **Full Analysis.png**: Screenshot of full mode  


***

##  Next Steps

- Extend with a machine learning price prediction model  
- Deploy a web dashboard for interactive exploration  
- Automate data updates and notifications  

***

**Thank you for reviewing!** Feel free to raise an issue or pull request if you have suggestions.
