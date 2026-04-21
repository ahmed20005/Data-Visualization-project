# Global Education Statistics Dashboard

## Data Visualization Final Project - Plotly Dash Application

### Project Overview

This interactive dashboard analyzes global education statistics across countries worldwide. It provides comprehensive visualizations of education indicators including literacy rates, school enrollment, government spending on education, student-teacher ratios, and their relationships with economic factors.

### Dataset Description

**Source**: World Education Data (Kaggle)
- **Countries**: 66 countries across all continents
- **Time Period**: 2015-2019 (5 years)
- **Total Records**: 330 observations
- **Key Metrics**:
  - Literacy rates (overall, male, female)
  - GDP per capita
  - Government spending on education (% of GDP)
  - Student-teacher ratio
  - School life expectancy
  - Enrollment rates (primary, secondary, tertiary)
  - Additional socioeconomic indicators

### Features & Visualizations

The dashboard includes all required chart types from the course curriculum:

#### Week 1: Comparison Charts
- **Column Chart**: Literacy Rate by Country
- **Bar Chart**: GDP per Capita by Region

#### Week 2: Advanced Comparison Charts
- **Stacked Column Chart**: Enrollment Rates by Education Level (Vertical)
- **Stacked Bar Chart**: Enrollment Rates by Education Level (Horizontal)
- **Clustered Column Chart**: Male vs Female Literacy Rates (Vertical)
- **Clustered Bar Chart**: Male vs Female Literacy Rates (Horizontal)

#### Week 3: Relationship Charts
- **Scatter Chart**: GDP vs Literacy Rate relationship

#### Week 4: Relationship Charts
- **Bubble Chart**: Education Spending vs Enrollment (with bubble size representing secondary enrollment)

#### Week 5: Distribution Charts
- **Histogram**: Distribution of Literacy Rates

#### Week 6: Distribution Charts
- **Box Chart**: GDP Distribution by Continent

#### Week 7: Distribution Charts
- **Violin Chart**: Student-Teacher Ratio Distribution by Continent

#### Week 8: Time-Series Charts
- **Line Chart**: Literacy Rate Trend Over Years

#### Week 9: Time-Series Charts
- **Area Chart**: Education Spending as % of GDP Over Time

### Interactive Elements

The dashboard includes **4 interactive controls**:

1. **Region Dropdown**: Filter data by geographic region
2. **Year Dropdown**: Select specific year or view all years
3. **Country Multi-select Dropdown**: Choose specific countries to compare
4. **Literacy Rate Slider**: Set minimum literacy rate threshold
5. **Chart Type Radio Buttons**: Toggle between bar and column chart orientations

### Team Members

- [Add team member names and roles here]

### Installation & Setup

#### Prerequisites
- Python 3.8 or higher
- pip package manager

#### Required Packages
```bash
pip install plotly dash pandas numpy
```

#### Running the Dashboard

1. Navigate to the project directory:
```bash
cd /workspace
```

2. Run the Dash application:
```bash
python app.py
```

3. Open your web browser and go to:
```
http://127.0.0.1:8050/
```

### File Structure

```
/workspace/
├── app.py                          # Main Dash application
├── cleaned_education_data.csv      # Processed dataset
├── Global_Education.csv            # Original dataset
├── data_preprocessing.ipynb        # Jupyter notebook for data cleaning
└── README.md                       # This documentation file
```

### Data Preprocessing Steps

The `data_preprocessing.ipynb` notebook documents all data cleaning and transformation steps:

1. **Data Loading**: Import raw education data
2. **Missing Value Handling**: Imputation strategies for incomplete data
3. **Data Transformation**: Column renaming, type conversion
4. **Feature Engineering**: Creating continent groupings, derived metrics
5. **Data Validation**: Checking for duplicates, outliers, and data quality
6. **Export**: Saving cleaned dataset for dashboard use

### Usage Instructions

1. **Filtering Data**: Use the dropdown menus and slider to filter the displayed data
2. **Exploring Charts**: Each chart shows different aspects of education statistics
3. **Hover Information**: Hover over chart elements to see detailed values
4. **Interactive Legends**: Click on legend items to show/hide data series

### Key Insights

The dashboard helps answer questions such as:
- How do literacy rates vary across different regions?
- What is the relationship between GDP and education outcomes?
- How has education spending changed over time?
- Are there gender disparities in literacy rates?
- Which regions have the best/worst student-teacher ratios?

### Technical Details

- **Framework**: Plotly Dash
- **Visualization Library**: Plotly Express & Plotly Graph Objects
- **Data Processing**: Pandas, NumPy
- **Responsive Design**: Mobile-friendly layout
- **Callbacks**: Real-time updates based on user interactions

### Academic Integrity

This project was created as part of the Data Visualization course final project. All code was written by the team members with understanding of each component. External resources and documentation were consulted but all implementations are original.

### License

This project is created for educational purposes.

### Contact

For questions about this project, please contact the team members.

---

**Course**: Data Visualization  
**Project**: Final Dashboard Project  
**Date**: 2024
