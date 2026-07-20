import numpy as np
v1 = np.array([3,4])
v2 = np.array([6,8])
# using the euclidean distace formula to calculate the duistance between two vectors 
distance = np.linalg.norm(v1-v2)
print("the distance between the two vectors is = ",distance)