# matrix of vectors in dataset 
import numpy as np
A = np.array([[3,4],[1,2],[5,12]])
b = np.array([[1,2],[3,4],[5,6]])
# i nned to caluulate the Magnitude of each vector 
magnitudes_A= np.linalg.norm(A, axis=1)
magnitudes_B= np.linalg.norm(b, axis=1)
print("magnitudes of each vector in the dataset A is = ",magnitudes_A)
print("magnitudes of each vector in the dataset B is = ",magnitudes_B)