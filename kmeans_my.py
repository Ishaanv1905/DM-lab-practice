import numpy as np
def kmeans(data,k,max_iters=100):
    n=len(data)
    centroids=data[np.random.choice(n,k,replace=False)]
    for _ in range(max_iters):
        clusters=[[] for _ in range(k)]
        for point in data:
            distances=[np.linalg.norm(point-c) for c in centroids]
            idx=np.argmin(distances)
            clusters[idx].append(point)
        
        new_centroids=[]
        for cluster in clusters:
            if cluster:
                new_centroids.append(np.mean(cluster,axis=0))
            else:
                new_centroids.append(centroids[len(new_centroids)])
                
        new_centroids=np.array(new_centroids)
        if np.all(centroids==new_centroids):
            break
        centroids=new_centroids
    return centroids,clusters

data=np.array([
    [1, 2], [2, 3], [3, 4],
    [8, 8], [9, 9], [10, 10]
])
k=2
centroids,clusters=kmeans(data,k)
print("Centroids: \n",centroids)

print("\nClusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster{i+1}:{cluster}")
        