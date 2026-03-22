# Find Mean, Median, Mode, Standard deviation, Variance

import math 


#------------------------------Subsidary Functions------------------------------
def sum_frequency(frequency:list):
    Sum_frequency = 0

    for i in range(len(frequency) - 1):
        Sum_frequency += frequency[i]

    return Sum_frequency

def class_size(Class:list):

    try:
        Class_size = Class[0][1] - Class[0][0]    
    except IndexError:
        print(r"Restart the function and give a value for 'Class' parameter (give a 2D array or list)")
        Class_size = 0
    
    return Class_size

def class_midpoint(Class:list):
    Class_midpoint = []

    for i in range(len(Class) - 1):
        Class_midpoint.append(math.ceil((Class[i][0] + Class[i][1])/2))

    return Class_midpoint

def assumed_mean(Class:list):
    Class_midpoint = class_midpoint(Class)

    Assumed_mean = Class_midpoint[math.floor(len(Class_midpoint)/2)]
    return Assumed_mean

def step_deviation(Class:list):
    Step_Deviation = []
    Class_midpoint = class_midpoint(Class)
    Assumed_mean = assumed_mean(Class)
    Class_size = class_size(Class)

    for i in range(len(Class) - 1):
        Step_Deviation.append((Class_midpoint[i] - Assumed_mean) / Class_size)

    return Step_Deviation

def sum_frequency_step_deviation(Class:list, frequency:list):
    Step_Deviation = step_deviation(Class)
    Sum_frequency_stepDeviation = 0

    for i in range(len(frequency) - 1):
        Sum_frequency_stepDeviation += frequency[i] * Step_Deviation[i]

    return Sum_frequency_stepDeviation

def cumulative_frequency(frequency:list):
    Cumulative_frequency = [frequency[0]]

    for x in range(len(frequency) - 1):
        Cumulative_frequency.append(Cumulative_frequency[x] + frequency[x + 1])

    return Cumulative_frequency

def median_class(Class:list):
    Median_class = Class[math.floor(len(Class) / 2)]
    return Median_class

def median_cumulative_frequency(frequency:list):
    Cumulative_frequency = cumulative_frequency(frequency)

    Median_cumulative_frequency = Cumulative_frequency[(math.floor(len(Cumulative_frequency) / 2)) - 1]
    return Median_cumulative_frequency

def median_class_frequency(frequency:list):
    Median_class_frequency = frequency[math.floor(len(frequency) / 2)]
    return Median_class_frequency

def median_class_lower_limit(Class:list):
    Median_class = median_class(Class)

    Median_class_lower_limit = min(Median_class)
    return Median_class_lower_limit

def modal_class(Class:list, frequency:list):
    Modal_class = Class[frequency.index(max(frequency))]
    return Modal_class

def frequency_preceeding_modal_class(frequency:list):
    try:
        Frequency_preceeding_modal_class = frequency[(frequency.index(max(frequency))) - 1]
    except IndexError:
        Frequency_preceeding_modal_class = 0

    return Frequency_preceeding_modal_class

def modal_class_frequency(frequency:list):
    Modal_class_frequency = frequency[frequency.index(max(frequency))]
    return Modal_class_frequency

def frequency_succeeding_modal_class(frequency:list):
    try:
        Frequency_succeeding_modal_class = frequency[(frequency.index(max(frequency))) + 1]
    except IndexError:
        Frequency_succeeding_modal_class = 0

    return Frequency_succeeding_modal_class 

def modal_class_lower_limit(Class:list, frequency:list):
    Modal_class = modal_class(Class, frequency)

    Lower_limit_modal_class = min(Modal_class)
    return Lower_limit_modal_class

def sum_frequency_step_devaition_squared(Class:list, frequency:list):
    Class_midpoint = class_midpoint(Class)
    Step_deviation = step_deviation(Class)
    Sum_frequency_step_deviation_squared = 0

    for i in range(len(Class_midpoint) - 1):
        Sum_frequency_step_deviation_squared += frequency[i] * (Step_deviation[i] ** 2)

    return Sum_frequency_step_deviation_squared



#------------------------------Main Functions------------------------------

#--------Mean--------
def mean(Class:list, frequency:list):

    Mean = 0
    Class_size = class_size(Class)
    Assumed_mean = assumed_mean(Class)
    Sum_frequency = sum_frequency(frequency) 
    sum_frequency_stepDeviation = sum_frequency_step_deviation(Class, frequency)

    #Mean Formula
    Mean = Assumed_mean + (sum_frequency_stepDeviation / Sum_frequency) * Class_size

    return Mean


#--------Median--------
def median(Class:list, frequency:list):

    Median = 0
    Class_size = class_size(Class)
    Sum_frequency = sum_frequency(frequency)
    Median_frequency = median_class_frequency(frequency)
    lowerLimit_MedianClass = median_class_lower_limit(Class)
    Median_cumulativeFrequency = median_cumulative_frequency(frequency)

    # Median Formula
    Median = lowerLimit_MedianClass + (((Sum_frequency / 2) - Median_cumulativeFrequency) / Median_frequency) * Class_size

    return Median

#--------Mode--------
def mode(Class:list, frequency:list):
      
    Mode = 0
    Class_size = class_size(Class)
    Frequency_Modal_class = modal_class_frequency(frequency)
    lowerLimit_modealClass = modal_class_lower_limit(Class, frequency)
    Frequency_preceeding_Modal_class = frequency_preceeding_modal_class(frequency)    
    Frequency_succeeding_Modal_class = frequency_succeeding_modal_class(frequency)   
    
    #Mode Formula
    Mode = lowerLimit_modealClass + ((Frequency_Modal_class - Frequency_preceeding_Modal_class) / ((2 * (Frequency_Modal_class)) - Frequency_preceeding_Modal_class - Frequency_succeeding_Modal_class)) * Class_size

    return Mode


#--------Standard Deviation--------    
def standard_deviation(Class:list, frequency:list):
    
    Standard_deviation = 0
    Class_size = class_size(Class)
    Sum_frequency = sum_frequency(frequency)
    sum_frequency_stepDeviation = sum_frequency_step_deviation(Class, frequency)
    Sum_frequency_step_devaition_squared = sum_frequency_step_devaition_squared(Class, frequency)
    
    #Standard Deviation Formula
    Standard_deviation = (Class_size / Sum_frequency) * math.sqrt((Sum_frequency * Sum_frequency_step_devaition_squared) - ((sum_frequency_stepDeviation) ** 2))

    return Standard_deviation


#--------Variance--------
def variance(Class:list, frequency:list):

    Variance = 0
    sd = standard_deviation(Class, frequency)

    Variance = sd ** 2
    return Variance


#---------Main()---------
Classes = [[0, 10], [10, 20], [20, 30]]
frequencies = [10, 15, 20]

Mean = mean(Classes, frequencies)
Median = median(Classes, frequencies)
Mode = mode(Classes, frequencies)
Standard_Deviation = standard_deviation(Classes, frequencies)
Variance = variance(Classes, frequencies)


print("Mean =", Mean)
print("Median =", Median)
print("Mode =", Mode)
print("Standard Deviation =", Standard_Deviation)
print("Variance =", Variance)

