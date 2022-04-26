from fuzzy import FuzzySet
from prettytable import PrettyTable

class FuzzyRelation:
    def __init__(self, A: FuzzySet = None, B: FuzzySet = None):
        if A is None:
            self.mat = list()
            self.row = list()
            self.col = list()
        else:
            ta = sorted(A.S.keys())
            tb = sorted(B.S.keys())       
            self.row = sorted(A.S.keys())
            self.col = sorted(B.S.keys())
            self.mat = list()
            for i in ta:
                tl = list()
                for j in tb:
                    tl.append(min(A.S.get(i,1), B.S.get(j,1)))
                self.mat.append(tl)
        
    def __str__(self):
        x = PrettyTable()
        x.field_names = [""] + self.col
        for i in range(len(self.row)):
            tl = list()
            tl.append(self.row[i])
            for j in range(len(self.col)):
                tl.append(self.mat[i][j])
            x.add_row(tl)
        return x.get_string()

    def MaxMin(self, R2):
        assert len(self.col) == len(R2.row), "Invalid dimensions"
        Rans = FuzzyRelation()
        Rans.row = self.row.copy()
        Rans.col = R2.col.copy()
        Rans.mat = [[0]*len(Rans.col) for i in range(len(Rans.row))]
        for i in range(len(Rans.row)):
            for j in range(len(Rans.col)):
                temp = 0
                for m in range(len(self.col)): #ith row from R1 and jth column from R2 
                    temp = max(temp, min(self.mat[i][m], R2.mat[m][i]))
                Rans.mat[i][j] = temp
        return Rans                

if __name__ == "__main__":

    A = FuzzySet({'A': 0.9, 'B': 0.7, 'C': 0.1})
    B = FuzzySet({'D': 0.3, 'E': 0.2, 'F': 0.7, 'G': 0.4})
    C = FuzzySet({'W': 0.3, 'X': 0.2, 'Y': 0.7, 'Z': 0.4})
    R1 = FuzzyRelation(A,B) # Fuzzy relation between A and B
    R2 = FuzzyRelation(B,C) # Fuzzy relation between B and C
    print(R1)
    print()
    print(R2)
    print()
    print(R1.MaxMin(R2))
