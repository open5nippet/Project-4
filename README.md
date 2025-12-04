# Weather Data Visualizer - Mini Project

**Course:** Programming for Problem Solving using Python  
**Assignment Title:** Data Analysis and Visualization with Real-World Weather Data  
**Type:** Individual Mini Project  
**Name:** Ayush Kumar
**Roll No:** 2501420003
**Programme:** BTech CSE (DS)

## 📋 Project Overview

This project implements a complete weather data analysis and visualization system that covers data acquisition, cleaning, statistical analysis, visualization, and reporting. It addresses the real-world problem of climate awareness and sustainability by providing actionable insights from weather data.

## 🎯 Learning Objectives

By completing this project, you will:
- ✓ Load and clean real-world CSV datasets with Pandas
- ✓ Compute statistics using NumPy and group-by operations
- ✓ Create informative plots using Matplotlib
- ✓ Apply storytelling techniques to present insights
- ✓ Automate analysis and export summaries in Python

## 📁 Project Structure

```
Project-4/
├── main.py                          # Main project script
├── weather_data.csv                 # Sample weather dataset
├── README.md                        # This file
└── output/                          # Output directory (created on first run)
    ├── 01_temperature_trends.png
    ├── 02_monthly_rainfall.png
    ├── 03_humidity_vs_temperature.png
    ├── weather_analysis_combined.png
    ├── cleaned_weather_data.csv
    ├── aggregated_data_M.csv
    └── WEATHER_ANALYSIS_REPORT.md
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Required Libraries

Install the required packages using:

```bash
pip install pandas numpy matplotlib
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### 1. **Prepare Your Data**

Option A: Use the provided sample data
- The `weather_data.csv` file is already included with the project

Option B: Use your own data
- Download weather data from:
  - [Kaggle Datasets](https://www.kaggle.com/)
  - [IMD (India Meteorological Department)](https://mausam.imd.gov.in/)
  - [Weather.com Historical Data](https://weather.com/)
  - [NOAA Climate Data](https://www.ncei.noaa.gov/)

- CSV file must contain columns like: `Date`, `Temperature`, `Rainfall`, `Humidity`, `Pressure`
- Place the CSV file in the project directory
- Update the `csv_file` variable in `main.py` if using a different filename

### 2. **Run the Analysis**

```bash
python main.py
```

The script will:
1. Load and inspect the weather data
2. Clean and process the data
3. Compute statistical metrics
4. Generate visualizations
5. Perform grouping and aggregation
6. Export results and generate a report

## 📊 Project Tasks

### **Task 1: Data Acquisition and Loading**
- ✓ Load CSV file into Pandas DataFrame
- ✓ Inspect data structure with `head()`, `info()`, `describe()`
- ✓ Display missing values summary

### **Task 2: Data Cleaning and Processing**
- ✓ Handle missing values (mean imputation for numeric, drop for dates)
- ✓ Convert date columns to datetime format
- ✓ Filter and validate relevant columns

### **Task 3: Statistical Analysis with NumPy**
- ✓ Compute daily, monthly, and yearly statistics
- ✓ Calculate mean, median, std dev, min, max, percentiles
- ✓ Generate comprehensive statistical summaries

### **Task 4: Visualization with Matplotlib**
- ✓ **Line Chart:** Daily temperature trends
- ✓ **Bar Chart:** Monthly rainfall totals
- ✓ **Scatter Plot:** Humidity vs. Temperature correlation
- ✓ **Combined Figure:** Multiple plots in single view

### **Task 5: Grouping and Aggregation**
- ✓ Group data by month/season using `groupby()`
- ✓ Use `resample()` for time-series aggregation
- ✓ Calculate aggregate statistics (mean, sum, min, max)

### **Task 6: Export and Reporting**
- ✓ Export cleaned data to CSV
- ✓ Save all plots as PNG images
- ✓ Generate comprehensive Markdown report

## 📈 Output Files

After running the script, the following files will be created in the `output/` directory:

### Visualizations
- **01_temperature_trends.png** - Daily temperature line chart
- **02_monthly_rainfall.png** - Monthly rainfall bar chart
- **03_humidity_vs_temperature.png** - Humidity-temperature scatter plot
- **weather_analysis_combined.png** - Combined multi-panel visualization

### Data Files
- **cleaned_weather_data.csv** - Processed dataset ready for further analysis
- **aggregated_data_M.csv** - Monthly aggregated statistics

### Report
- **WEATHER_ANALYSIS_REPORT.md** - Comprehensive analysis report with:
  - Executive summary
  - Dataset overview
  - Statistical findings
  - Key insights
  - Sustainability recommendations
  - Methodology
  - Conclusions

## 💻 Code Architecture

### Main Class: `WeatherDataVisualizer`

```python
class WeatherDataVisualizer:
    """Main class for weather data analysis and visualization"""
    
    def load_and_inspect_data()          # Task 1
    def clean_and_process_data()         # Task 2
    def compute_statistics()              # Task 3
    def create_visualizations()           # Task 4
    def group_and_aggregate()             # Task 5
    def export_cleaned_data()             # Task 6
    def generate_report()                 # Task 6
```

### Key Methods

| Method | Purpose | Task |
|--------|---------|------|
| `load_and_inspect_data()` | Load CSV and display structure | 1 |
| `clean_and_process_data()` | Handle missing values, convert dates | 2 |
| `compute_statistics()` | Calculate NumPy-based statistics | 3 |
| `create_visualizations()` | Generate Matplotlib plots | 4 |
| `group_and_aggregate()` | Time-series grouping and aggregation | 5 |
| `export_cleaned_data()` | Save processed data to CSV | 6 |
| `generate_report()` | Create Markdown analysis report | 6 |

## 📊 Sample Data Structure

The provided `weather_data.csv` contains:

| Date | Temperature | Rainfall | Humidity | Pressure |
|------|-------------|----------|----------|----------|
| 2024-01-01 | 15.2 | 0.0 | 62 | 1013.5 |
| 2024-01-02 | 16.1 | 0.5 | 65 | 1012.8 |
| ... | ... | ... | ... | ... |

**Columns:**
- **Date:** Date in YYYY-MM-DD format
- **Temperature:** Daily mean temperature in °C
- **Rainfall:** Daily precipitation in mm
- **Humidity:** Relative humidity as percentage (0-100)
- **Pressure:** Atmospheric pressure in hPa

## 📈 Sample Output

### Console Output
```
======================================================================
WEATHER DATA VISUALIZER - MINI PROJECT
======================================================================

======================================================================
TASK 1: DATA ACQUISITION AND LOADING
======================================================================

✓ Successfully loaded weather_data.csv

Dataset Shape: 365 rows, 5 columns

--- First 5 Rows ---
        Date  Temperature  Rainfall  Humidity  Pressure
0 2024-01-01         15.2       0.0        62     1013.5
...

--- Statistical Summary ---
       Temperature    Rainfall    Humidity    Pressure
count    365.000000  365.000000  365.000000  365.000000
mean      25.234658    2.104110   52.972603 1008.921918
...

[Continues with Tasks 2-6...]

✓ ALL TASKS COMPLETED SUCCESSFULLY!

Output files saved to './output/' directory:
  • weather_analysis_combined.png
  • 01_temperature_trends.png
  • 02_monthly_rainfall.png
  • 03_humidity_vs_temperature.png
  • cleaned_weather_data.csv
  • aggregated_data_M.csv
  • WEATHER_ANALYSIS_REPORT.md
```

## 🔍 Customization Guide

### Change Column Names
Edit the method calls in `main()`:

```python
visualizer.clean_and_process_data(
    date_column='YourDateColumn',
    temp_column='YourTempColumn',
    rainfall_column='YourRainfallColumn',
    humidity_column='YourHumidityColumn'
)
```

### Adjust Visualization Style
Modify the style in `WeatherDataVisualizer.__init__()`:

```python
plt.style.use('seaborn-v0_8-whitegrid')  # Other options: 'ggplot', 'bmh', 'dark_background'
plt.rcParams['figure.figsize'] = (16, 10)  # Change figure size
```

### Change Aggregation Frequency
In `group_and_aggregate()`:

```python
visualizer.group_and_aggregate(group_by='D')  # 'D'=daily, 'M'=monthly, 'Y'=yearly
```

### Modify Report Content
Edit the `generate_report()` method to add custom sections or analysis.

## 🎨 Visualization Examples

### 1. Temperature Trends
- Shows daily temperature variations
- Highlights seasonal patterns and anomalies
- Includes filled area for visual emphasis

### 2. Monthly Rainfall
- Bar chart of accumulated rainfall per month
- Identifies wet and dry seasons
- Useful for water management planning

### 3. Humidity-Temperature Correlation
- Scatter plot with trend line
- Shows inverse correlation in many climates
- Includes polynomial regression line

### 4. Combined Analysis
- 2×2 grid combining all major visualizations
- Comprehensive overview in single image
- Professional presentation format

## 📝 Sample Report Sections

The generated report includes:

1. **Executive Summary** - Overview of analysis
2. **Dataset Overview** - Data dimensions and date range
3. **Statistical Analysis** - Detailed metrics for each variable
4. **Visualizations** - Description of charts
5. **Key Findings** - Important insights
6. **Data Quality Assessment** - Cleaning actions performed
7. **Sustainability Recommendations** - Actionable insights
8. **Methodology** - Tools and techniques used
9. **Conclusion** - Summary and future directions

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pandas'"
**Solution:** Install required packages
```bash
pip install pandas numpy matplotlib
```

### Issue: "File not found" error
**Solution:** Ensure CSV file is in the same directory as `main.py` or provide full path

### Issue: Plots not showing
**Solution:** The script saves plots to files; check the `output/` directory

### Issue: Date conversion error
**Solution:** Ensure date column format is standard (YYYY-MM-DD, MM/DD/YYYY, etc.)

### Issue: Missing column error
**Solution:** Update column names in `main()` to match your CSV file

## 📚 Libraries Used

- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations and statistics
- **Matplotlib** - Data visualization and plotting
- **Pathlib** - Cross-platform file path handling
- **Datetime** - Date/time handling

## 🌍 Real-World Applications

This project demonstrates skills applicable to:
- Environmental monitoring systems
- Climate research and reporting
- Energy management optimization
- Agricultural planning
- Urban sustainability initiatives
- Weather forecasting support
- Insurance risk assessment

## 📖 References & Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy User Guide](https://numpy.org/doc/stable/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/)
- [Kaggle Weather Datasets](https://www.kaggle.com/datasets?search=weather)
- [IMD Open Data](https://mausam.imd.gov.in/)

## ✅ Assessment Criteria

This project addresses the following evaluation criteria:

| Criteria | Coverage |
|----------|----------|
| Data Loading | ✓ CSV loading with Pandas |
| Data Cleaning | ✓ Missing value handling, type conversion |
| Statistical Analysis | ✓ NumPy-based computations |
| Visualization | ✓ Multiple chart types |
| Aggregation | ✓ Groupby and resample operations |
| Export/Reporting | ✓ CSV export and Markdown report |
| Code Quality | ✓ Well-documented, modular design |
| Functionality | ✓ All tasks automated |

## 📄 License & Attribution

This project is provided for educational purposes as part of the Programming for Problem Solving using Python course.

---

**Last Updated:** December 2025
**Version:** 1.0  
**Status:** Complete and Ready for Submission
