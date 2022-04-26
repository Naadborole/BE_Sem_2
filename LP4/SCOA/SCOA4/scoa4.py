import numpy as np

class NeuralNet:
  def __init__(self, input_nodes):
    self.n = input_nodes
    self.w = np.zeros((self.n))
    self.b = 0

  def __train(self, x, y):
    self.w += np.array(x) * y
    self.b += y

  def fit(self, X, y):
    assert len(X[0]) == self.n, "Invalid input shape."
    for i in range(len(X)):
      self.__train(X[i], y[i])

  def predict(self, X):
    return np.sum(self.w * X, axis = 1) + self.b

#OR GATE

or_model = NeuralNet(2)

X = [
     [-1, -1],
     [-1, 1],
     [1, -1],
     [1, 1]
]
y = [-1, 1, 1, 1]

or_model.fit(X, y)

or_model.w
or_model.b

print(or_model.predict(X))

#AND GATE

and_model = NeuralNet(2)

X = [
     [-1, -1],
     [-1, 1],
     [1, -1],
     [1, 1]
]
y = [-1, -1, -1, 1]

and_model.fit(X, y)

and_model.w
and_model.b

print(and_model.predict(X))

#NOT GATE

not_model = NeuralNet(1)

X = [
     [-1],
     [1]
]
y = [1, -1]

not_model.fit(X, y)

not_model.w, not_model.b

print(not_model.predict(X))

#NOR GATE

nor_model = NeuralNet(2)

X = [
     [-1, -1],
     [-1, 1],
     [1, -1],
     [1, 1]
]
y = [1, -1, -1, -1]

nor_model.fit(X, y)

nor_model.w, nor_model.b

print(nor_model.predict(X))

#NAND GATE

nand_model = NeuralNet(2)

X = [
     [-1, -1],
     [-1, 1],
     [1, -1],
     [1, 1]
]
y = [1, 1, 1, -1]

nand_model.fit(X, y)

nand_model.w, nand_model.b

print(nand_model.predict(X))
