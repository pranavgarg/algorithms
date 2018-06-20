import os,sys
sys.path.append(os.path.dirname(os.getcwd())+"/src")
from problem_200 import Graph
a = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
row = len(a)
col = len(a[0])
g = Graph(row, col, a)
print g.countIslands() == 1

