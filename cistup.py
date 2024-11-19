import numpy as np
def calculate_probabilities(parameters, data, utilities):
    # Initialize the list to store probabilities for each alternative
    probabilities = []

    for utility in utilities:
        # Calculate utility for each alternative based on the provided functions
        V = utility(data, parameters)
        
        # Calculate exponentials of utilities
        exp_V = [np.exp(v) for v in V]
        
        # Calculate the denominator for probabilities
        denominator = sum([np.exp(u) for u in utility(data, parameters)] for utility in utilities)
        
        # Calculate probabilities for each alternative and append to the list
        prob = [ev / denominator for ev in exp_V]
        probabilities.append(prob)

    return probabilities

# Sample data dictionary
data = {
    'X1': [2, 3, 5, 7, 1, 8, 4, 5, 6, 7],
    'X2': [1, 5, 3, 8, 2, 7, 5, 9, 4, 2],
    'Sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Parameters dictionary
parameters = {
    'beta_01': 0.1,
    'beta_1': 0.5,
    'beta_2': 0.5,
    'beta_02': 1,
    'beta_03': 0
}

# Utility functions for each alternative
def utility_func_1(data, parameters):
    return [parameters['beta_01'] + parameters['beta_1'] * x1 + parameters['beta_2'] * x2 for x1, x2 in zip(data['X1'], data['X2'])]

def utility_func_2(data, parameters):
    return [parameters['beta_02'] + parameters['beta_1'] * x1 + parameters['beta_2'] * x2 for x1, x2 in zip(data['X1'], data['X2'])]

def utility_func_3(data, parameters):
    return [parameters['beta_03'] + parameters['beta_1'] * s + parameters['beta_2'] * s for s in data['Sero']]

utilities = [utility_func_1, utility_func_2, utility_func_3]

# Calculate probabilities for each alternative
probabilities = calculate_probabilities(parameters, data, utilities)

# Print or use the probabilities as needed
for i, probs in enumerate(probabilities, start=1):
    print(f'P{i} = {probs}')
