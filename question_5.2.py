import pandas as pd
import numpy as np


n = 2
L = 64
a = [0,139,1451,977,1072,457]
k = 1
c = ['blankspace','R','B', 'G','W','Y']
b = np.zeros((101,101))
for i in range(1,L+1):
    for j in range(1,L+1):
        if (i+j)&1:
            b[i][j]=k
            a[k]-=1
            if a[k]==0:
                k+=1
for i in range(1,L+1):
    for j in range(1,L+1):
        if b[i][j]==0:
            b[i][j]=k
            a[k]-=1
            if a[k]==0:
                k+=1
p=0
for i in range(1,L+1):
    for j in range(1,L+1):
        if b[i][j]==b[i-1][j]:
            p+=1
        if b[i][j]==b[i][j-1]:
            p+=1
x_numpy = []
for i in range(1,L+1):
    t = []
    for j in range(1,L+1):
        t.append(c[int(b[i][j])])
        print(c[int(b[i][j])], end=' ')
    x_numpy.append(t)
    print()
x_numpy = np.array(x_numpy)
pd.DataFrame(x_numpy).to_csv('output_question_5.2.txt', index=False, header=None)