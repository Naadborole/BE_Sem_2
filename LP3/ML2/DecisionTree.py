import pandas as pd
df = pd.read_csv(
    "https://raw.githubusercontent.com/Naadborole/Datasets/main/DecisionTreeData.csv")
df = df[:-1]
df = df.drop(columns= ['ID'])
dfY = df[-1:]
class Node:
    def __init__(self, attr, definite, output = None):
        self.attr = attr
        self.definite = definite
        self.output_Map = dict()
        if definite:
            self.out = output
    
    def output(self, input):
        if self.definite:
            return self.out
        else:
            return self.output_Map[input[self.attr]].output(input)
        
    def __str__(self) -> str:
        return f'COl: {self.attr} DEFI: {self.definite}'

class GiniIndex:
    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.cols = list(data.columns)
        self.cols.remove(target)

    def gini_Whole(self):
        tdf = list(df[self.target].value_counts())
        s = sum(tdf)
        ans = 1
        for i in tdf:
            ans = ans - (i/s)**2
        return ans

    def gini_index(self, col):
        ans = 0
        values = self.data[col].unique()
        val_cnt = list(self.data[col].value_counts())
        indi_gini = list()
        for i in values:
            tdf = list(df[df[col] == i][self.target].value_counts())
            s = sum(tdf)
            gin_val = 1
            for m in tdf:
                gin_val = gin_val - (m/s)**2
            indi_gini.append(gin_val)
        for i in range(len(indi_gini)):
            ans = ans + indi_gini[i]*(val_cnt[i]/sum(val_cnt))
        return ans

    def Calculate_Gini(self):
        self.gini_map = dict()
        for i in self.cols:
            self.gini_map[i] = self.gini_index(i)
        self.cols.sort( key = lambda x : self.gini_map[x])
        return self.cols[0]
    
class DecisionTree:
    def __init__(self, data, target):
        self.root =self.BuildTree(data, target)
        self.data = data
        self.target = target

    def BuildTree(self, data, target):
        t = GiniIndex(data, target)
        col = t.Calculate_Gini()
        unq = list(data[col].unique())
        temp = None
        if len(unq) == 1:
            defi = True
            out = data[target].value_counts().idxmax()
            temp = Node(col, defi, out)
        elif len(data.columns) == 2:
            defi = True 
            ot = data[target].value_counts().idxmax()
            temp = Node(col, defi, ot)
        else:
            defi = False
            temp =Node(col, defi, None)
            for i in data[col].unique():
                tdf = data[data[col] == i]
                tdf = tdf.drop(columns=[col])
                temp.output_Map[i] = self.BuildTree(tdf, target)
        return temp                

    def predict(self, input):
        ans = list()
        for index, row in input.iterrows():
            ans.append(self.root.output(row))
        return ans



dtree = DecisionTree(df, "Buys")
print(dtree.predict(dfY))
