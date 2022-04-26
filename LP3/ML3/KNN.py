import math
from collections import Counter

class KNN:
    def __init__(self, K):
        self.K = K
        self.X = list()
        self.Y = list()
    
    def fit(self, X, y):
        self.X = X
        self.Y = y
    
    def EuclideanDistance(self, X, y):
        return float(math.sqrt((X[0]-y[0])**2 + (X[1]-y[1])**2))

    def __getClass(self, Yn):
        distances = list()
        for i in range(len(self.X)):
            distances.append((self.EuclideanDistance(X[i],Yn), self.Y[i]))
        distances = sorted(distances)[:self.K]
        t = Counter(i[1] for i in distances)
        cl = max(t, key=t.get)
        return cl

    def predict(self, Y):
        if type(Y) == type(list()):
            ans = list()
            for i in Y:
                ans.append(self.__getClass(i))
            return ans
        else:
            return self.__getClass(Y)

knn = KNN(K = 3)
X = [
     (2, 4),
     (4, 6),
     (4, 4),
     (4, 2),
     (6, 4),
     (6 ,2)
]
y = ['Y', 'Y', 'B', 'Y', 'Y', 'B']

knn.fit(X, y)
print(knn.predict([(6,6)]))