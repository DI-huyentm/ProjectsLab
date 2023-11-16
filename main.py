import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Assuming your dataset is in a CSV file named 'data.csv'
data = pd.read_csv('./dataset/creditcard.csv')

# Assuming 'Class' is the column you want to predict
target = 'Class'
features = [col for col in data.columns if col != target]

# Set value for vector X and output label y
X = data[features]
y = data[target]

# Split the data into training and testing sets
test_rate = 0.2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_rate, random_state=42)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}% with test rate = {test_rate}") 


