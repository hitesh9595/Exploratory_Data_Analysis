import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer as kn
import data

dt = pd.read_csv(r"C:\DataAnalyst\Learning\DataVisualizationProject\NetFlix.csv")


important_countries = [
    "United States",
    "India",
    "United Kingdom",
    "Canada",
    "France",
    "Spain",
    "Germany",
    "Japan",
    "South Korea",
    "Mexico",
    "Australia",
    "China",
    "Italy",
    "Brazil"
]

# Country
dt.columns = dt.columns.str.strip()
dt["country"] = dt["country"].str.split(",")
dt = dt.explode("country")
dt["country"] = dt["country"].str.strip()
dt = dt[dt["country"].isin(important_countries)]

# Rating
dt["rating"] = dt["rating"].fillna(dt["rating"].mode()[0])

# Genres
dt["genres"] = dt["genres"].replace(data.genre_mapping)
dt["genres"] = dt["genres"].replace(data.Major_genres)

x_scat = dt["country"]
y_scat = dt["genres"]

plt.scatter(x_scat ,y_scat,color = "#6D0000" , marker="o",s=10,label="Country and Genre")
plt.xlabel("Countries",fontsize = 8,color="#5B005E")
plt.ylabel("Genres",fontsize = 8,color = "#5B005E")
plt.xticks(rotation=45,fontsize=6,color = "#88358C")
plt.yticks(fontsize=6,color="#621067")
plt.grid(color="gray",linestyle=":")
plt.legend(fontsize=6)
plt.title("Countries and Genres",fontsize=8,color = "#5B005E")

plt.tight_layout()
plt.savefig("DataVisualizationProject/CountriesAndGenres.png",dpi=300,bbox_inches="tight")
plt.show()

x_hist = dt["release_year"]

plt.hist(x_hist,bins=10,color="#FF00EA",edgecolor="black")
plt.xlabel("Release Years",fontsize=8,color="#C300B6")
plt.ylabel("Movie Counts",fontsize=8,color="#C300B6")
plt.grid(color="gray",linestyle=":")
plt.title("Distribution of Netflix Content by Release Year",fontsize=10,color="#FF00EEB0")

plt.tight_layout()
plt.savefig("DataVisualizationProject/DistributionofNetflixContentbyReleaseYear.png",dpi=300,bbox_inches="tight")
plt.show()

Pieplot = dt["type"].value_counts()
Pieplotval = dt["type"].unique()

plt.pie(Pieplot,labels = Pieplotval,autopct="%1.1f%%",colors=["#FF00D4","#002AFF"])
plt.title("Percentage Distribution of Netflix Movies and TV Shows",fontsize=12,color="#000000")

plt.tight_layout()
plt.savefig("DataVisualizationProject/PercentageDistributionofNetflixMoviesandTVShows.png",dpi=300,bbox_inches="tight")
plt.show()

x_bar = dt["rating"].unique()
y_bar = dt["rating"].value_counts()

plt.bar(x_bar,y_bar,color="#AE00FFC7",label="Netflix Movie Rating",width = 0.5)
plt.xlabel("Content Rating",fontsize = 8,color="#DA00CF")
plt.xticks(color="#000000",fontsize=6,rotation=45)
plt.ylabel("Number of Titles",fontsize = 8,color="#DA00CF")
plt.legend(fontsize=6)
plt.grid(color="gray",linestyle=":")
plt.title("Distribution of Netflix Titles by Content Rating",color="#880086",fontsize=10)

plt.tight_layout()
plt.savefig("DataVisualizationProject/DistributionofNetflixTitlesbyContentRating.png",dpi = 300,bbox_inches = "tight")
plt.show()