import SingleLayerPerceptron

# Parameter1 = Input1, Parameter2 = input2, Parameter3 = AND/OR
result = SingleLayerPerceptron.startNN(0, 0, "AND")

# Print Ergebnis
print("Input1", result[0])
print("Input2", result[1])
print("Output", result[2])
