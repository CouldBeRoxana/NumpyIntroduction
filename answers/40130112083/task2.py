import numpy as np

a = np.array([3,6,5,1,9])
b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
c = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]] , [[13,14,15,16], [17,18,19,20], [21,22,23,24]]])


print(f'''1 :
{a[3]}
{b[2][3]}''')

# 2
print(f'''2 :
{b[::2, ::3]}''')

# 3
for i in c :
    print(f'''3 :
{i}''')