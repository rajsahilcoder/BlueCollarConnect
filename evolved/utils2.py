import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)


def load_data():
    ratings = pd.read_csv("ratings.csv")
    cooks = pd.read_csv("cook.csv")
    return ratings, cooks


def data_processing(ratings, cooks):
    n_ratings = len(ratings)
    n_cooks = len(ratings["cookId"].unique())
    n_users = len(ratings["userId"].unique())
    print(f"Number of ratings: {n_ratings}")
    print(f"Number of unique cookId's: {n_cooks}")
    print(f"Number of unique users: {n_users}")
    print(f"Average ratings per user: {round(n_ratings/n_users, 2)}")
    print(f"Average ratings per cook: {round(n_ratings/n_cooks, 2)}")
    mean_rating = ratings.groupby("cookId")[["rating"]].mean()
    return mean_rating


def create_matrix(df):
    N = len(df["userId"].unique())
    M = len(df["cookId"].unique())

    user_mapper = dict(zip(np.unique(df["userId"]), list(range(N))))
    cook_mapper = dict(zip(np.unique(df["cookId"]), list(range(M))))

    user_inv_mapper = dict(zip(list(range(N)), np.unique(df["userId"])))
    cook_inv_mapper = dict(zip(list(range(M)), np.unique(df["cookId"])))

    user_index = [user_mapper[i] for i in df["userId"]]
    cook_index = [cook_mapper[i] for i in df["cookId"]]

    X = csr_matrix((df["rating"], (cook_index, user_index)), shape=(M, N))
    return X, user_mapper, cook_mapper, user_inv_mapper, cook_inv_mapper


def find_similar_cooks(
    cook_id, cook_mapper, cook_inv_mapper, X, k, metric="cosine", show_distance=False
):
    neighbour_ids = []

    cook_ind = cook_mapper[cook_id]
    cook_vec = X[cook_ind]
    k += 1
    kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
    kNN.fit(X)
    cook_vec = cook_vec.reshape(1, -1)
    neighbour = kNN.kneighbors(cook_vec, return_distance=show_distance)
    for i in range(0, k):
        n = neighbour.item(i)
        neighbour_ids.append(cook_inv_mapper[n])
    neighbour_ids.pop(0)
    return neighbour_ids


def main2(cook_id):
    ratings, cooks = load_data()
    mean_rating = data_processing(ratings, cooks)
    X, user_mapper, cook_mapper, user_inv_mapper, cook_inv_mapper = create_matrix(
        ratings
    )
    cook_Names = dict(zip(cooks["cookId"], cooks["Name"]))
    cook_specialty = dict(zip(cooks["cookId"], cooks["Specialty"]))
    cook_city = dict(zip(cooks["cookId"], cooks["City"]))
    cook_area = dict(zip(cooks["cookId"], cooks["Area"]))
    cook_pincode = dict(zip(cooks["cookId"], cooks["Pincode"]))
    cook_distict = dict(zip(cooks["cookId"], cooks["District"]))
    cook_state = dict(zip(cooks["cookId"], cooks["State"]))
    similar_ids = find_similar_cooks(cook_id, cook_mapper, cook_inv_mapper, X, k=10)
    rval = []
    for i in similar_ids:
        val = []
        val += (
            cook_Names[i].capitalize(),
            str(int(mean_rating.loc[mean_rating.index == i]["rating"])),
            cook_specialty[i],
            cook_area[i],
            cook_city[i],
            cook_distict[i],
            cook_state[i],
            str(cook_pincode[i]),
        )
        rval.append(val)
    return rval
