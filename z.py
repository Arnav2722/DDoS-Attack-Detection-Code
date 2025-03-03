import matplotlib.pyplot as plt

# Update accuracy values with correct data
accuracy_data = {
    "Decision Tree": 94.19,
    "Logistic Regression": 75.22,
    "SVM": 92.0,
    "Random Forest": 99.42,
}

# Plot the updated accuracy graph
plt.figure(figsize=(8, 5))
plt.bar(
    accuracy_data.keys(),
    accuracy_data.values(),
    color=["blue", "green", "red", "purple"],
)
plt.xlabel("Machine Learning Models")
plt.ylabel("Accuracy (%)")
plt.title("Model Accuracy Comparison of DDoS Attack Detection")
plt.ylim(0, 100)

# Show the updated graph
plt.show()
