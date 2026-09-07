"""Starter code for the Learn AI in 10 Days assignment."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


messages = [
    "I loved this helpful lesson",
    "This explanation was clear and useful",
    "The project was fun to complete",
    "I am happy with the result",
    "The instructions made sense",
    "This was a frustrating experience",
    "The example did not work",
    "I found the lesson confusing",
    "The program gave an error",
    "I am disappointed with the result",
]

labels = [
    "positive",
    "positive",
    "positive",
    "positive",
    "positive",
    "negative",
    "negative",
    "negative",
    "negative",
    "negative",
]


training_messages, test_messages, training_labels, test_labels = train_test_split(
    messages,
    labels,
    test_size=0.3,
    random_state=42,
    stratify=labels,
)

model = Pipeline(
    [
        ("vectorizer", TfidfVectorizer()),
        ("classifier", LogisticRegression()),
    ]
)

# TODO: Train the model with training_messages and training_labels.
# TODO: Predict labels for test_messages.
# TODO: Print accuracy_score(test_labels, predictions).
# TODO: Print classification_report(test_labels, predictions).

new_messages = [
    "The activity was easy to understand",
    "I could not follow the instructions",
    "The final result made me smile",
]

# TODO: Predict and print the categories for new_messages.
