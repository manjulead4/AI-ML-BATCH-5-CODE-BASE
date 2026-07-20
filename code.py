import numpy as np
# nuympy is used for math numerical computing 
from statistics import mean, median,mode, variance, stdev
from sklearn.preprocessing import StandardScaler

scores = [45,50,55,60,65,70,75,80,85,90]

print(mean(scores))
print(median(scores))
print(mode(scores))
print(variance(scores))
print(stdev(scores))