import math
import numpy as np

class KMeans:
    def __init__(self, k):
        self.k = k
    
    def EuclideanDistance(self, p1 , p2):
        return math.sqrt((p1[0]-p2[0])**2  + (p1[1]-p2[1])**2) 

    def fit(self, points, centroids):
        prev_clusters = None
        idx = 0
        Clusters = [set() for _ in range(self.k)]
        while prev_clusters != Clusters:
            prev_clusters = Clusters
            for p in points:
                for i in range(1, self.k):
                    if self.EuclideanDistance(p, centroids[i]) < self.EuclideanDistance(p, centroids[idx]):
                        idx = i
                Clusters[idx].add(p)
            for i in range(self.k):
                centroids[i] = np.mean(list(Clusters[i]), axis = 0)
        return Clusters, centroids

points = [
          (0.1, 0.6),
          (0.15, 0.71),
          (0.08,0.9),
          (0.16, 0.85),
          (0.2,0.3),
          (0.25,0.5),
          (0.24,0.1),
          (0.3,0.2)
]

model = KMeans(2)
clusters, centroids = model.fit(points, centroids = [(0.1, 0.6),(0.3,0.2)])