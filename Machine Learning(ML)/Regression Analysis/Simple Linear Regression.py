from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the Diabetes dataset
diabetes = load_diabetes()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes.data[:, 2],
diabetes.target, test_size=0.2, random_state=0)

# Reshape the input data
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

# Create a linear regression object
lr_model = LinearRegression()

# Fit the model on the training data
lr_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = lr_model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Calculate the coefficient of determination
r2 = r2_score(y_test, y_pred)

print('Mean Squared Error:', mse)
print('Coefficient of Determination:', r2)

# Plot the training data
plt.figure(figsize=(7.5, 3.5))
plt.scatter(X_train, y_train, color='gray')

# Plot the regression line
plt.plot(X_train, lr_model.predict(X_train), color='red', linewidth=2)

# Add axis labels
plt.xlabel('Mean Blood Pressure')
plt.ylabel('Disease Progression')

# Show the plot
plt.show()