import numpy as np
from scipy.stats import norm

def calculate_mean(data):
    mean = np.mean(data)
    return mean

def calculate_standard_deviation(data):
    standard_deviation = np.std(data, ddof=1)
    return standard_deviation

def calculate_confidence_interval(data, confidence_level):
    confidence_interval = norm.interval(confidence_level, data)
    return confidence_interval
