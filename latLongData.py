import pandas as pd
from geopy.geocoders import Nominatim
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import cdist

cook_df = pd.read_csv("cook.csv")
ratings_df = pd.read_csv("ratings.csv")
df = pd.merge(cook_df, ratings_df, on="cookId")

# label_encoder = LabelEncoder()

# df["Specialty"] = label_encoder.fit_transform(df["Specialty"])
df["Location"] = df["City"] + ", " + df["State"] + ", India"
unique_locations = df["Location"].unique()

geolocator = Nominatim(user_agent="cook_locator")

location_dict = {}
for location in unique_locations:
    try:
        geolocation = geolocator.geocode(location)
        if geolocation != None:
            location_dict[location] = (geolocation.latitude, geolocation.longitude)
        else:
            location
        print(
            location
            + " : "
            + str(geolocation.latitude)
            + " : "
            + str(geolocation.longitude)
        )
    except:
        location_dict[location] = (None, None)
        print(location + " ||" + "None, None")

df["Latitude"] = df["Location"].map(lambda x: location_dict[x][0])
df["Longitude"] = df["Location"].map(lambda x: location_dict[x][1])

df.to_csv("data.csv", index=False)
