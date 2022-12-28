#This is my personal attempt to understand Numpy module at a deeper level 

#%%
#The logic behind Numpy ndarrays: simple multiplication

a = [1,2,3]
b = [4,5,6]
c = []

for i in range(len(a)):
    c.append(a[i] * b[i])

print(c)


#%%
#Initial import + arange and reshape functions

import numpy as np

a = np.arange(15).reshape(3,5)

print(f"a: {a}",'\n')
print(f"a.shape: {a.shape}",'\n')
print(f"a.size: {a.size}",'\n')
print(f"a.ndim: {a.ndim}",'\n')
print(f"a.dtype: {a.dtype}",'\n')
print(f"type(a): {type(a)}",'\n')

#%%
#Arange with sequencing and data type

b = np.arange(1,5,2, dtype= complex)

print(f"b: {b}",'\n')
print(f"b.shbpe: {b.shape}",'\n')
print(f"b.size: {b.size}",'\n')
print(f"b.ndim: {b.ndim}",'\n')
print(f"b.dtype: {b.dtype}",'\n')
print(f"type(b): {type(b)}",'\n')

# %%
#Broadcasting and zeros/ones

c = np.zeros((2,2), dtype= 'int16')

print(f"c: {c}",'\n')

d = np.ones((2,2), dtype= 'int16')

print(f"d: {d}",'\n')

e = c + d

print(f"e: {e}",'\n')

f = (e + 1) ** 2

print(f"f: {f}",'\n')

g = f @ e

print(f"g: {g}",'\n')

# %%
#Linespace (different to arange)

h = np.linspace(1,3,2, dtype= complex)

print(f"h: {h}",'\n')
# %%
