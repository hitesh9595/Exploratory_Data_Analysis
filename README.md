# Netflix Content Analysis & Visualization
 
## Project Overview
An extensive data visualization and analysis project exploring Netflix's content library. This project transforms raw Netflix data into meaningful insights through various visualization techniques, showcasing content distribution across countries, genres, ratings, and release years.

## Key Features
•	Multi-Country Analysis: Focuses on 14 major content-producing countries
•	Genre Classification: Maps complex genre combinations into 20+ major categories
•	4 Interactive Visualizations: Scatter plots, histograms, pie charts, and bar charts
•	High-Quality Exports: All visualizations saved at 300 DPI for professional use
•	Data Cleaning Pipeline: Handles missing values and standardizes formats

## Visualizations Created
1️.Countries and Genres Distribution
Type: Scatter Plot
Purpose: Shows relationship between countries and content genres
Insights: Identifies which genres are popular in specific countries
Color Theme: Deep red (##6D0000) for premium feel

<img width="2519" height="1881" alt="CountriesAndGenresHighQuality" src="https://github.com/user-attachments/assets/e5c849c1-753a-4bfb-8aab-3720a2495e18" />

2️.Netflix Content by Release Year
Type: Histogram
Purpose: Displays distribution of content over time
Insights: Reveals Netflix's content production/ acquisition trends
Color Theme: Vibrant pink (##FF00EA) for visual impact
 
<img width="2523" height="1879" alt="DistributionofNetflixContentbyReleaseYear" src="https://github.com/user-attachments/assets/7966b365-85dc-40c1-bfad-d58dfd967fa3" />

3️.Movies vs. TV Shows Distribution
Type: Pie Chart
Purpose: Shows the ratio of Movies to TV Shows
Insights: Understands Netflix's content strategy balance
Color Theme: Pink (##FF00D4) and Blue (##002AFF) contrast

<img width="1928" height="1875" alt="PercentageDistributionofNetflixMoviesandTVShows" src="https://github.com/user-attachments/assets/b2938ced-37f7-49aa-b039-6a8144ef8808" />

4️. Content Rating Distribution
Type: Bar Chart
Purpose: Analyzes content by maturity ratings
Insights: Helps understand target audience segments
Color Theme: Purple (##AE00FFC7) for sophistication

<img width="2523" height="1878" alt="DistributionofNetflixTitlesbyContentRating" src="https://github.com/user-attachments/assets/78efe704-ea8f-4cfe-b95f-e9981f1f5a34" />

## Technologies Used
Category	Tools/Libraries
Data Processing	Pandas, NumPy
Visualization	Matplotlib
Machine Learning	scikit-learn (KNNImputer)
Data Sources	Custom mapping dictionaries
Export Format	PNG (300 DPI)

## Data Processing Pipeline
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

## Key Insights Generated
•	Geographic Insights
Analysis of content distribution across 14 major countries
Identification of country-specific genre preferences

## Temporal Trends
Content production trends over decades
Netflix's expansion timeline visualization

## Content Type Analysis
Movie vs. TV Show ratio
Platform's content strategy evolution

## Audience Targeting
Content rating distribution (PG-13, R, TV-MA, etc.)
Family-friendly vs. mature content balance

## Visualization Specifications
Chart Type	Dimensions	Color Scheme	Key Elements
<table border="1" cellpadding="10" cellspacing="0">
    <thead>
        <tr>
            <th>Chart Type</th>
            <th>Size</th>
            <th>Color</th>
            <th>Settings</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Scatter Plot</td>
            <td>800x600</td>
            <td>#6D0000 (Dark Red)</td>
            <td>Grid lines, legend, rotated labels</td>
        </tr>
        <tr>
            <td>Histogram</td>
            <td>800x600</td>
            <td>#FF00EA (Bright Pink)</td>
            <td>10 bins, black edges</td>
        </tr>
        <tr>
            <td>Pie Chart</td>
            <td>800x600</td>
            <td>#FF00D4, #002AFF (Pink & Blue)</td>
            <td>Percentage labels</td>
        </tr>
        <tr>
            <td>Bar Chart</td>
            <td>800x600</td>
            <td>#AE00FFC7 (Purple)</td>
            <td>Width 0.5, rotated x-labels</td>
        </tr>
    </tbody>
</table>

## Skills Demonstrated
Data Visualization: Creating publication-quality charts with Matplotlib
Data Cleaning: Handling missing values, standardizing formats
Genre Classification: Building custom mapping dictionaries
Color Theory: Selecting professional color schemes
Export Optimization: High-resolution exports for presentations
Code Organization: Modular structure with separate data file

## Future Enhancements
Add interactive visualizations with Plotly
Include time-series analysis of content addition
Create dashboard with multiple views
Add statistical analysis of ratings by country
Implement machine learning for genre prediction
Add word clouds for titles and descriptions

## Data Sources
Primary Dataset: Netflix Movies and TV Shows dataset
Country Mapping: Custom dictionary for country name standardization
Genre Mapping: Hand-crafted mapping of 200+ genre combinations

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Note: This project was developed as part of my data analysis portfolio to demonstrate data visualization skills essential for data science and analytics roles.
