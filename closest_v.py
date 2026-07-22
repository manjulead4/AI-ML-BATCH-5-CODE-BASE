import numpy as np

vectors = np.array([[1,2],[3,4],[6,8],[10,10]]) 
target = np.array([5,5])

distances = np.linalg.norm(vectors-target,axis=1)

# finding the closest vector to target vector                                               
closest_index = np.argmin(distances)
print("the closest vector to the target vector is = ", vectors[closest_index])


