from sklearn.cluster import KMeans
import pandas as pd
import subprocess

def cluster(df):
    X = df[['total_amount', 'quantity']]

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    cluster_labels = kmeans.labels_
    cluster_counts = pd.Series(cluster_labels).value_counts()
    cluster_counts.to_csv('k.txt', header=['Number of Records'], sep='\t', index_label='Cluster')
    subprocess.call(["./final.sh"])

