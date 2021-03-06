import numpy as np
import matplotlib.pyplot as plt

# example data with peaks:
# x = np.linspace(-1,3,1000)
# data = -0.1*np.cos(12*x)+ np.exp(-(1-x)**2)
# #data = [-1,4,29,6,7,8,9,4,5,34,7,5,69,5,6,5,6,5,65]

# #     ___ detection of local minimums and maximums ___

# a = np.diff(np.sign(np.diff(data))).nonzero()[0] + 1               # local min & max
# b = (np.diff(np.sign(np.diff(data))) > 0).nonzero()[0] + 1         # local min
# c = (np.diff(np.sign(np.diff(data))) < 0).nonzero()[0] + 1         # local max
# # +1 due to the fact that diff reduces the original index number

# # plot
# plt.figure(figsize=(12, 5))
# plt.plot(x, data, color='grey')
# plt.plot(x[b], data[b], "o", label="min", color='r')
# plt.plot(x[c], data[c], "o", label="max", color='b')
# plt.show()

data = [38,19,58,29,88,44,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1]
x=38
minn=[]
maxx=[]

for i in range(len(data)):
    i+=2
    minn = data(i)


for j in range(len(data)):
    maxx = data(j)
    j+=2

plt.figure(figsize=(12, 5))
plt.plot(x, data, color='grey')
plt.plot(x[_min], data[_min], "o", label="min", color='r')
plt.plot(x[_max], data[_max], "o", label="max", color='b')
plt.show()