import numpy as np
import math
population = [5,10,15,220,25,300,35,40,45]
print("Original population:", population)
pop_mean = sum(population) / len(population)
print("Mean of population:", pop_mean)
sq_pop_deviation = [(i-pop_mean)**2 for i in population]
print("Squared deviations from mean:", sq_pop_deviation)
pop_variance = sum(sq_pop_deviation) / len(population)
print('Variance of population: {}'.format(round(pop_variance, 2)))
sample = np.arange(5,25,5)
print("Sample:", sample)
samp_mean = sum(sample) / len(sample)
print("Mean of sample:", samp_mean)
sq_s_deviation = [(i - samp_mean) ** 2 for i in sample]
#print("Squared deviations from mean:", sq_s_deviation)      
s_variance = sum(sq_s_deviation) / (len(sample) - 1)
print('Variance of sample: {}'.format(round(s_variance, 2)))   
print(pop_variance) 
std_dev = math.sqrt(pop_variance)
print('Standard Deviation of population: {}'.format(round(std_dev, 2)))
print(pop_mean)