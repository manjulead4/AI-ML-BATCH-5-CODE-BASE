import numpy as np
v = np.array([3,4]) # right angled traingle 
magnitude = np.linalg.norm(v)
print("magnitude of given vector is ", magnitude)

# i nned to find direction fro these we call it  as unit vector 

direction = v/magnitude

print("the direction of given vector is = ",direction)
