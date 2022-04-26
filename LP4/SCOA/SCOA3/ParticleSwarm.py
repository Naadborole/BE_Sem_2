import numpy as np
np.random.seed(40)


def dec_to_bin(x, n):
    b = bin(x).replace('0b', '')
    return '0' * max((n - len(b)), 0) + b


class BitPopulation:
    def __init__(self, length, initial_size, c1, c2, w1, w2):
        self.length = length
        self.size = initial_size
        self.__init_population()
        self.c1 = c1
        self.c2 = c2
        self.w1 = w1
        self.w2 = w2

    def __init_population(self):
        mean = 2 ** (self.length - 2)
        std = mean / 2
        self.min_val = 0
        self.max_val = 2 ** self.length - 1
        population = np.random.normal(mean, std, self.size)
        self.__population = [
            int(max(self.min_val, min(self.max_val, x))) for x in population]
        self.__velocity = np.random.normal(10, 1, self.size)
        self.__pbest = self.__population.copy()
        self.__gbest = np.max(self.__pbest)

    def get_popultation(self):
        # return self.__population.copy()
        return [dec_to_bin(x, self.length) for x in self.__population]

    def display_population(self):
        for x in self.__population:
            print(f'{dec_to_bin(x, self.length)}: {x}')
        print()

    def __fitness(self, x):
        return x * x

    def __update_pbest(self):
        for i in range(self.size):
            if self.__fitness(self.__population[i]) > self.__fitness(self.__pbest[i]):
                self.__pbest[i] = self.__population[i]

    def __update_position(self, w):
        r1 = np.random.rand()
        r2 = np.random.rand()
        for i in range(self.size):
            self.__velocity[i] = self.__velocity[i] * w + self.c1 * r1 * (
                self.__pbest[i] - self.__population[i]) + self.c2 * r2 * (self.__gbest - self.__population[i])
            x = self.__population[i] + self.__velocity[i]
            self.__population[i] = int(max(self.min_val, min(self.max_val, x)))

    def __perform_iteration(self, i):
        w = self.alpha * i + self.w1
        self.__update_pbest()
        self.__gbest = np.max(self.__pbest)
        self.__update_position(w)

    def fit(self, iterations):
        print('INITIAL POPULATION:')
        self.display_population()
        self.alpha = (self.w2 - self.w1) / (iterations - 1)
        for i in range(iterations):
            self.__perform_iteration(i)
            print(f'ITERATION {i+1}: ')
            self.display_population()


population = BitPopulation(8, 8, 2, 2, 0.9, 0.4)
population.fit(5)
