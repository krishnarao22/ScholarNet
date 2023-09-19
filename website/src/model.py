# Training the model (Step 4)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

X_train, y_train = preprocess_and_load_training_data()

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_train_vec)
accuracy = accuracy_score(y_train, y_pred)
print(f"Training Accuracy: {accuracy}")

joblib.dump(model, 'resume_similarity_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
