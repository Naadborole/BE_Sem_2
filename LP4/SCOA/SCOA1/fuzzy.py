class FuzzySet:
    def __init__(self, A: dict = None, func = None, U: dict = None):
        self.S = dict()
        if A is None and func is None:
            self.S = dict()
        elif func is None:
            self.S = A
        else:
            for i in sorted(U.keys()):
                t = func(U[i])
                assert t>=0 and t<=1, "The values must be between 0 and 1"
                self.S[i] = t

    def __str__(self) -> str:
        ans = "{"
        for i in sorted(self.S.keys()):
            ans+= f'({i}, {self.S[i]}) '
        ans+='}'
        return ans

    def __len__(self):
        return len(self.S)

    def add(self, key, val):
        assert val >=0 and val<=1, 'The value should be between 0 and 1'
        self.S[key] = val

    def keys(self):
        return set(self.S.keys())

    def Union(self, B):
        ans = FuzzySet()
        temp = self.keys().union(B.keys())
        for i in temp:
            ans.add(i, max(self.S.get(i, 0), B.S.get(i, 0)))
        return ans

    def Intersection(self, B):
        ans = FuzzySet()
        temp = self.keys().intersection(B.keys())
        for i in temp:
            ans.add(i, min(self.S.get(i, 0), B.S.get(i, 0)))
        return ans

    def Complement(self):
        ans = FuzzySet()
        for i in self.S.keys():
            ans.add(i, round(1-self.S[i], 3))
        return ans

    def Difference(self, B):
        return self.Intersection(B.Complement())


if __name__ == "__main__":

    A = FuzzySet({'A': 0.2, 'B': 0.7, 'C': 0.1})
    B = FuzzySet({'A': 0.3, 'B': 0.2, 'C': 0.7, 'D': 0.4})

    print()
    print('--------------------Union-----------------------')
    print(f'A : {str(A)}')
    print(f'B : {str(B)}')
    print(f'Union: {str(A.Union(B))}')
    print('------------------------------------------------')
    print()

    print()
    print('--------------------Intersection-----------------------')
    print(f'A : {str(A)}')
    print(f'B : {str(B)}')
    print(f'Intersection: {str(A.Intersection(B))}')
    print('------------------------------------------------')
    print()

    print()
    print('--------------------Complement-----------------------')
    print(f'A : {str(A)}')
    print(f'Complement: {str(A.Complement())}')
    print('-----------------------------------------------------')
    print()

    print()
    print('--------------------Difference-----------------------')
    print(f'A : {str(A)}')
    print(f'B : {str(B)}')
    print(f'A - B: {str(A.Difference(B))}')
    print(f'B - A: {str(B.Difference(A))}')
    print('-----------------------------------------------------')
    print()

    print("------------Using Member Function---------------------")
    U = {'A':22,'B':67,'C':89,'D':56,'E':94}
    print(f'Universal Set: {str(U)}')
    def memberfunc(x):
        return x/100
    Uset = FuzzySet(func = memberfunc, U = U)
    print(Uset)
    print("-------------------------------------------------------")
    
