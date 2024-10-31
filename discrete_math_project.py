import numpy as np
import networkx as nx
from IPython.display import display
from PIL import Image
from networkx.drawing.nx_agraph import to_agraph

def print_matrix(Matrix,n):
    print("\nМатрица смежности:\n")
    for i in range(n):
        for j in range(n):
            print(Matrix[i][j], end = " ")
        print()
def enter_matrix(Matrix,n):
    print("\nВведите матрицу смежности:\n")
    for i in range(n):        
        for j in range(n):
            temp = int(input())
            if temp!=0 and temp!=1:
                Matrix[i][j] = 1
            else:
                Matrix[i][j] = temp
            

print("Выберите, что Вы хотите сделать:\n")
flag = int(input("1-сгенерировать матрицу смежности\n2-задать матрицу смежности\n3-использовать заготовленную матрицу смежности\n"))
if flag == 1:
    n = int(input("Введите число вершин графа:"))
    Matrix = np.random.randint(2, size=(n, n))
    print_matrix(Matrix,n)
if flag == 2:
    n = int(input("Введите число вершин графа:"))
    Matrix = np.random.randint(1, size=(n,n))
    enter_matrix(Matrix,n)
    print_matrix(Matrix,n)
if flag!=1 and flag!=2:
    n = 6
    Matrix=[[0,0,1,0,0,0], 
            [1,1,1,0,1,0], 
            [0,1,0,0,0,1], 
            [0,0,1,1,0,1], 
            [0,0,0,1,0,1], 
            [1,0,0,0,1,0]] 
    print_matrix(Matrix,n)

Nodes = list(map(chr, range(65, 65+n)))
Edges = list()

G = nx.DiGraph(directed = True)
for i in range(0,n):
    G.add_node(Nodes[i])

for i in range(n):
    for j in range(n):
        if Matrix[i][j] == True:
            G.add_edge(Nodes[i],Nodes[j])

for i in range(n):
    for j in range(n):
        if Matrix[i][j] == True:
            Edges.append(Nodes[i] + Nodes[j])
        
A = to_agraph(G)
A.layout('circo')
A.draw('test.png')
print("\nГраф:\n")
path="test.png"
display(Image.open(path))

def func(Matrix,n, Nodes):
    Matrix_ = ['0'] * n
    for i in range(n):
        Matrix_[i] = ['0'] * n
        for j in range(n):
            Matrix_[i][j] = ['0'] * 5000

    for i in range(n):
        for j in range(n):
            if Matrix[i][j] != 0:
                Matrix_[i][j][0] = Nodes[i] + Nodes[j]

    Matrix_1 = ['0'] * n
    for i in range(n):
        Matrix_1[i] = ['0'] * n
        for j in range(n):
            Matrix_1[i][j] = ['0'] * 5000
    
    for i in range(n):
        for j in range(n):
            if Matrix_[i][j][0] != '0':
                Matrix_1[i][j][0] = Nodes[j]

    print("Петли:")
    for i in range(n):
        if Matrix_[i][i][0] != '0':
            print(Matrix_[i][i][0])
            print()

    for s in range(2,n+1):
        Matrix_next = ['0'] * n
        for i in range(n):
            Matrix_next[i] = ['0'] * n
            for j in range(n):
                Matrix_next[i][j] = ['0'] * 5000
                    
        for i in range(n):
            for j in range(n):
                l=0
                while Matrix_[i][j][l] != '0':
                    for k in range(n):
                        if Matrix_1[j][k][0] != '0':
                            if Matrix_next[i][k][l] == '0':
                                Matrix_next[i][k][l] = Matrix_[i][j][l] + Matrix_1[j][k][0]
                            else:
                                m = 0
                                while Matrix_next[i][k][m] != '0':
                                    m+=1
                                    if m == 5000:
                                        print("Хватит!")
                                        return
                                Matrix_next[i][k][m] = Matrix_[i][j][l] + Matrix_1[j][k][0]
                                if i!=k and (len(Matrix_next[i][k][m]) - 1 >= len(set(Matrix_next[i][k][m]))):
                                    Matrix_next[i][k][m] = '0'   
                    l+=1                                                            
        print("Контуры длины", s)
        for i in range(n):
            l = 0
            while Matrix_next[i][i][l] != '0':
                if len(Matrix_next[i][i][l]) - 1 == len(set(Matrix_next[i][i][l])):
                    print(Matrix_next[i][i][l])
                    Matrix_next[i][i][l] = '0'
                l+=1
        Matrix_ = Matrix_next
        print()
        
func(Matrix,n, Nodes)