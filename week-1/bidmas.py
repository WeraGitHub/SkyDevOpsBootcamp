# Alex and Weronika

# assign integer values to variables a - e
a = 10
b = 5
c = 2
d = 1
e = 8

# create an empty list to store our results in
results_list = []
calculation_result = a + b - c * d / e
results_list.append(calculation_result)

calculation_result = (a + b) - c * d / e
results_list.append(calculation_result)

calculation_result = a + (b - c) * d / e
results_list.append(calculation_result)

calculation_result = a + b - (c * d) / e
results_list.append(calculation_result)

calculation_result = (a + b - c) * d / e
results_list.append(calculation_result)

calculation_result = (a + b - c * d) / e
results_list.append(calculation_result)

calculation_result = a + (b - c * d) / e
results_list.append(calculation_result)

print(results_list)
