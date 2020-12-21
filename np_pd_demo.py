# numpy and pandas demo

import numpy as np

# ------numpy-----
a = np.array([1,2,3,4,5])
b = np.array([[1,2],[3,4]])

print(a)
print(b)
#
print(b.shape)
#
print(b[1,1])
#
print(np.eye(4))

c = np.random.rand(6)
print(c)

np.sqrt(a)
np.exp(a)
np.log(a)
np.std(a)

print(np.std(b))

d = [0,1,2,3,4,5,6,7]
print(d[1:3])
print(d[-3:-1])

print(b[::])
print(b[:1])
print(b[1:])

# ------pandas-------

import pandas as pd

#1. load data
ratings = pd.read_csv('resources/u.rating', sep='\t', header=0)
print(ratings)

#2. rename
print(ratings.columns)
ratings.rename(columns={ratings.columns[0]:'id'})
print(ratings.head())

#3. map
ratings['timestamp'] = ratings['timestamp'].map(lambda x : x/1000)
print(ratings)

pd.to_datetime()

# [function(x) for x in list_of_x]

# -----matlibplot----
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabelx1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
#
plt.show()('time (s)')
plt.ylabel('Undamped')
#
plt.show()

