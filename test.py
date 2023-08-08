import pandas as pd
from geopy.geocoders import Nominatim
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import cdist

# Load the data
# cook_df = pd.read_csv("cook.csv")
# ratings_df = pd.read_csv("ratings.csv")
# df = pd.merge(cook_df, ratings_df, on="cookId")
df = pd.read_csv("data.csv")
label_encoder = LabelEncoder()
df["Specialty"] = label_encoder.fit_transform(df["Specialty"])


def recommend_cooks(address, specialty):
    if address == None:
        print("Address is none")
        return ["None", "None", "None", "None"]
    geolocator = Nominatim(user_agent="cook_locator")
    user_location = geolocator.geocode(address + ", India")
    if user_location != None:
        user_lat = user_location.latitude
        user_long = user_location.longitude
        # label_encoder = LabelEncoder()
        encoded_location = label_encoder.transform([specialty])[0]
        print(
            str(df[df["Specialty"] == encoded_location]) + " ||" + str(encoded_location)
        )
        specialty_data = df[df["Specialty"] == encoded_location]
        specialty_data["Distance"] = (
            cdist(
                [[user_lat, user_long]],
                specialty_data[["Latitude", "Longitude"]],
                metric="euclidean",
            )[0]
            * 111
        )
        recommended_cooks = specialty_data.sort_values(
            by=["Distance", "rating"], ascending=[True, False]
        )
        return recommended_cooks[["Name", "Location", "Distance", "rating"]]
    else:
        print("Geolocation is none")
        return [["None", "None", "None", "None"]]


address = "Kankarbagh, Patna, Bihar"
specialty = "South Indian"


# def main(address, specialty):
#     recommended_cooks = recommend_cooks(address, specialty)
#     return recommended_cooks.head(10).to_dict(orient="records")


recommended_cooks = recommend_cooks(address, specialty)
# print(recommended_cooks)
# print(type(recommended_cooks))
