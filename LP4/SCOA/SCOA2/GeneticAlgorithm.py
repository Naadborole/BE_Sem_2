from typing import Callable
import random
import copy

class Individual:
    def __init__(self, val, fitness, xu, xl, n=None):
        self.val = val
        self.fitness = fitness
        if n is None:
            n = 8
        else:
            self.numberOfBits = n
        self.bitstring = self.getBitStringFromVal(xu, xl)

    def getBitStringFromVal(self, xu, xl):
        """Real number to binary representation 
        xu = upper limit 
        xl = lower limit
        """
        # x = int(xl + ((xu - xl)/(2**self.numberOfBits - 1))*self.val)
        t = '{0:b}'.format(self.val)
        return '0'*(self.numberOfBits - len(t)) + t


class GeneticAlgorithmBinary:
    def __init__(self, ipop: list, lowlim: float, uplim: float, maxgen: int, fitness: Callable, ts: int, pc: float, pm: float, numberOfBits: int = None):
        """Initialize GA algorithm with parameters and cost function/fitness function
           ipop: list of Intial population
           lowlim: lower limit of population
           uplim: upper limit of population
           maxgen: Maximum generations/iterations
           fitness: Cost/Fitness function 
           ts: Tournamnet Size
        """
        assert ts <= len(
            ipop), "The tournamnet size cannot exceed population size"
        self.initialPopulation = ipop
        self.pop = list()
        self.fitness = fitness
        self.uplim = uplim
        self.lowlim = lowlim
        self.maxgen = maxgen
        self.popsize = len(ipop)
        self.pm = pm
        self.ts = ts
        self.pc = pc
        if numberOfBits is None:
            self.numberOfbits = 8
        else:
            self.numberOfbits = numberOfBits
        for i in self.initialPopulation:
            t = Individual(i, self.fitness(i), self.uplim,
                           self.lowlim, self.numberOfbits)
            self.pop.append(t)

    def TournamentSelection(self):
        tl = random.sample(self.pop, self.ts)
        min = tl[0]
        for i in tl:
            if i.fitness > min.fitness:
                min = i
        return min

    def Crossover(self, p1: Individual, p2: Individual):
        r = random.random()
        if r <= self.pc:
            k = random.randint(1, self.numberOfbits-1)
            bt1 = p1.bitstring[:k] + p2.bitstring[k:]
            bt2 = p2.bitstring[:k] + p1.bitstring[k:]
            bt1val = int(bt1, 2)
            c1 = Individual(bt1val, self.fitness(bt1val),
                            self.uplim, self.lowlim, self.numberOfbits)
            bt2val = int(bt2, 2)
            c2 = Individual(bt2val, self.fitness(bt2val),
                            self.uplim, self.lowlim, self.numberOfbits)
            return c1, c2
        return p1,p2

    def BitFlipMutation(self, p1: Individual):
        r = random.random()
        if r <= self.pm:
            btc1 = list(p1.bitstring)
            k = random.randint(0, self.numberOfbits-1)
            btc1[k] = str(1 - int(btc1[k]))
            btc1 = "".join(btc1)
            btc1val = int(btc1, 2)
            c1 = Individual(btc1val, self.fitness(btc1val), self.uplim, self.lowlim, self.numberOfbits)
            return c1
        return p1

    def fit(self):
        print("----------------Start----------------")
        print()
        print("Initial Population, it's binary representation and fitness")
        for t in self.pop:
            print(f'{t.val}: {t.bitstring}: {t.fitness}')
        print()
        for mg in range(self.maxgen):
            print(f'--------------------Generation {mg+1}--------------------')
            tpop = []
            while len(tpop) < len(self.pop):
                t1 = self.TournamentSelection()
                t2 = self.TournamentSelection()
                t1,t2 = self.Crossover(t1, t2)
                t1 = self.BitFlipMutation(t1)
                t2 = self.BitFlipMutation(t2)
                tpop.append(t1)
                tpop.append(t2)
            self.pop = copy.deepcopy(tpop)
            for t in self.pop:
                print(f'{t.val}: {t.bitstring}: {t.fitness}')
            print()

if __name__ == "__main__":
    def square(x):
        return x**2
    tp = [19,18,17,16,15,14,13,12,11,10]
    # tp = [1,4,6,8,9,10,13,16,19,20]
    ga = GeneticAlgorithmBinary(tp, 0,31,20,square,5,0.8,0.2,5)
    ga.fit()
