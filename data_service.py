import numpy as np

data = np.loadtxt("data_files/sensors.csv", delimiter=",")

print(data)
print(data.shape)
print(data.ndim)

sectors = data.reshape(12, 10, 14, 10).transpose(0, 2, 1, 3)

print(sectors.shape)
print(sectors.ndim)
print(sectors[0][0])
