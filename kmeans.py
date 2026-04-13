import numpy as np

def kmeans(data, k, max_iters=100):
    n = len(data)

    # Step 1: randomly choose k centroids
    centroids = data[np.random.choice(n, k, replace=False)]

    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]

        # Step 2: assign points to nearest centroid
        for point in data:
            distances = [np.linalg.norm(point - c) for c in centroids]
            idx = np.argmin(distances)
            clusters[idx].append(point)

        # Step 3: compute new centroids
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroids.append(np.mean(cluster, axis=0))
            else:
                new_centroids.append(centroids[len(new_centroids)])

        new_centroids = np.array(new_centroids)

        # Step 4: check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, clusters


# Example usage
data = np.array([
    [1, 2], [2, 3], [3, 4],
    [8, 8], [9, 9], [10, 10]
])

k = 2

centroids, clusters = kmeans(data, k)

print("Centroids:")
print(centroids)

print("\nClusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")