# 📘 Assignment: Learn AI in 10 Days

## 🎯 Objective

Learn the foundations of machine learning by building and evaluating a small text-classification program in Python. Over ten days, you will prepare labeled examples, train a model, test its predictions, and explain what you learned about AI systems.

## 📝 Tasks

### 🛠️ Days 1–3: Explore AI and Prepare Data

#### Description

Choose two text categories for a simple classifier, such as `positive` and `negative` messages. Learn how labeled examples help a machine-learning model find patterns, then prepare a small dataset for your project.

#### Requirements

Completed program should:

- Describe the problem the classifier will solve and identify its two categories.
- Provide at least 20 labeled text examples, with at least 10 examples in each category.
- Store the example text and labels in clearly named Python lists or a data file.
- Explain one possible source of bias or error in the examples.

### 🛠️ Days 4–7: Train a Text Classifier

#### Description

Use the provided starter code to turn text into numerical features and train a scikit-learn classifier. Split the examples into training and testing data so the model can be evaluated on text it has not seen before.

#### Requirements

Completed program should:

- Split the dataset into training and testing sets.
- Use a text vectorizer such as `TfidfVectorizer` to create features.
- Train a classification model such as `LogisticRegression`.
- Predict the category of at least three new messages.

### 🛠️ Days 8–10: Evaluate and Explain the Model

#### Description

Measure how well the model performs, investigate a few predictions, and communicate the strengths and limitations of your AI system.

#### Requirements

Completed program should:

- Calculate and display the model's accuracy on the test set.
- Display a classification report or another useful set of evaluation metrics.
- Include two correct predictions and one incorrect or uncertain prediction, if available.
- Write a short reflection explaining what the model learned, where it may fail, and how the training examples could be improved.
