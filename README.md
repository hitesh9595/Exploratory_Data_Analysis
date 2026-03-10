# Exploratory_Data_Analysis

Netflix Content Analysis & Visualization
 
# Project Overview
An extensive data visualization and analysis project exploring Netflix's content library. This project transforms raw Netflix data into meaningful insights through various visualization techniques, showcasing content distribution across countries, genres, ratings, and release years.

# Key Features
•	Multi-Country Analysis: Focuses on 14 major content-producing countries
•	Genre Classification: Maps complex genre combinations into 20+ major categories
•	4 Interactive Visualizations: Scatter plots, histograms, pie charts, and bar charts
•	High-Quality Exports: All visualizations saved at 300 DPI for professional use
•	Data Cleaning Pipeline: Handles missing values and standardizes formats

# Visualizations Created
1️.Countries and Genres Distribution
Type: Scatter Plot
Purpose: Shows relationship between countries and content genres
Insights: Identifies which genres are popular in specific countries
Color Theme: Deep red (#6D0000) for premium feel

<img width="605" height="451" alt="image" src="https://github.com/user-attachments/assets/d34944df-b973-414e-9f06-c4b58d1b3160" />

2️.Netflix Content by Release Year
Type: Histogram
Purpose: Displays distribution of content over time
Insights: Reveals Netflix's content production/ acquisition trends
Color Theme: Vibrant pink (#FF00EA) for visual impact
 
<img width="606" height="452" alt="image" src="https://github.com/user-attachments/assets/f62070cd-dd72-47d2-9ddb-c0303f605108" />

3️.Movies vs. TV Shows Distribution
Type: Pie Chart
Purpose: Shows the ratio of Movies to TV Shows
Insights: Understands Netflix's content strategy balance
Color Theme: Pink (#FF00D4) and Blue (#002AFF) contrast

 <img width="464" height="450" alt="image" src="https://github.com/user-attachments/assets/f43e6e91-b0bc-44b0-a549-632eea894521" />

4️. Content Rating Distribution
Type: Bar Chart
Purpose: Analyzes content by maturity ratings
Insights: Helps understand target audience segments
Color Theme: Purple (#AE00FFC7) for sophistication

 <img width="606" height="451" alt="image" src="https://github.com/user-attachments/assets/a8876747-e576-4ca6-944a-0fff644cb949" />

# Technologies Used
Category	Tools/Libraries
Data Processing	Pandas, NumPy
Visualization	Matplotlib
Machine Learning	scikit-learn (KNNImputer)
Data Sources	Custom mapping dictionaries
Export Format	PNG (300 DPI)

# Data Processing Pipeline
Country Standardization
python
#Splits multi-country entries and filters for top 14 countries
important_countries = ["United States", "India", "United Kingdom", ...]
dt = dt.explode("country")
dt = dt[dt["country"].isin(important_countries)]
Genre Classification
Maps 200+ complex genre combinations into 20 major categories

Examples:

"International TV Shows, TV Dramas, TV Sci-Fi & Fantasy" → "Fantasy & Sci-Fi"
"Horror Movies, International Movies, Thrillers" → "Horror"
"Dramas, Independent Movies, Romantic Movies" → "Drama"
Missing Value Handling
Rating: Filled with mode (most common rating)
Countries: Filtered to include only major markets
Genres: Standardized through mapping dictionaries

# Key Insights Generated
•	Geographic Insights
Analysis of content distribution across 14 major countries
Identification of country-specific genre preferences

# Temporal Trends
Content production trends over decades
Netflix's expansion timeline visualization

# Content Type Analysis
Movie vs. TV Show ratio
Platform's content strategy evolution

# Audience Targeting
Content rating distribution (PG-13, R, TV-MA, etc.)
Family-friendly vs. mature content balance

# Visualization Specifications
Chart Type	Dimensions	Color Scheme	Key Elements
Scatter Plot	800x600	Dark red (#6D0000)	Grid lines, legend, rotated labels
Histogram	800x600	Bright pink (#FF00EA)	10 bins, black edges
Pie Chart	800x600	Pink & Blue (#FF00D4, #002AFF)	Percentage labels
Bar Chart	800x600	Purple (#AE00FFC7)	Width 0.5, rotated x-labels

# Skills Demonstrated
Data Visualization: Creating publication-quality charts with Matplotlib
Data Cleaning: Handling missing values, standardizing formats
Genre Classification: Building custom mapping dictionaries
Color Theory: Selecting professional color schemes
Export Optimization: High-resolution exports for presentations
Code Organization: Modular structure with separate data file

# Future Enhancements
Add interactive visualizations with Plotly
Include time-series analysis of content addition
Create dashboard with multiple views
Add statistical analysis of ratings by country
Implement machine learning for genre prediction
Add word clouds for titles and descriptions

# Data Sources
Primary Dataset: Netflix Movies and TV Shows dataset
Country Mapping: Custom dictionary for country name standardization
Genre Mapping: Hand-crafted mapping of 200+ genre combinations

# License
This project is licensed under the MIT License - see the LICENSE file for details.

Note: This project was developed as part of my data analysis portfolio to demonstrate data visualization skills essential for data science and analytics roles.
