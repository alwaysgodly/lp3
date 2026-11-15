"""
B5 - Customer Segmentation using K-Means and Hierarchical Clustering
Dataset expected: sales_data_sample.csv
Uses numeric columns, standardizes them, plots the K-Means elbow curve,
then runs K-Means and Agglomerative (hierarchical) clustering.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

FILE = "sales_data_sample.csv"
if not os.path.exists(FILE):
    raise FileNotFoundError("Place sales_data_sample.csv in the same folder as this script.")

df = pd.read_csv(FILE, encoding="latin1")
print("Dataset shape:", df.shape)
print(df.head())

# Select numeric columns; exclude constant columns and likely identifiers.
numeric = df.select_dtypes(include=np.number).copy()
numeric = numeric.drop(
    columns=[c for c in numeric.columns
             if c.lower() in ["ordernumber", "orderlinenumber", "customerid"]],
    errors="ignore"
)
numeric = numeric.loc[:, numeric.nunique(dropna=True) > 1]

if numeric.shape[1] < 2:
    raise ValueError("Need at least two useful numeric columns for clustering.")

X = SimpleImputer(strategy="median").fit_transform(numeric)
X_scaled = StandardScaler().fit_transform(X)

# Elbow method: compute within-cluster sum of squares (inertia).
max_k = min(10, len(X_scaled) - 1)
if max_k < 2:
    raise ValueError("Dataset needs at least 3 rows.")

inertias = []
for k in range(1, max_k + 1):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.plot(range(1, max_k + 1), inertias, marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia / WCSS")
plt.title("Elbow Method")
plt.xticks(range(1, max_k + 1))
plt.grid(True)
plt.tight_layout()
plt.show()

k = min(3, max_k)
print(f"\nUsing k = {k}. Change k after inspecting the elbow plot if needed.")

kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)
df["KMeans_Cluster"] = kmeans_labels

hierarchical = AgglomerativeClustering(n_clusters=k, linkage="ward")
hierarchical_labels = hierarchical.fit_predict(X_scaled)
df["Hierarchical_Cluster"] = hierarchical_labels

print("\nK-Means cluster sizes:\n", df["KMeans_Cluster"].value_counts().sort_index())
print("\nHierarchical cluster sizes:\n",
      df["Hierarchical_Cluster"].value_counts().sort_index())

if len(set(kmeans_labels)) > 1:
    print("K-Means Silhouette Score:",
          round(silhouette_score(X_scaled, kmeans_labels), 4))
if len(set(hierarchical_labels)) > 1:
    print("Hierarchical Silhouette Score:",
          round(silhouette_score(X_scaled, hierarchical_labels), 4))

# Save rows with assigned cluster labels.
output = "customer_segments_output.csv"
df.to_csv(output, index=False)
print(f"\nCluster assignments saved to {output}")
