import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import string

def preprocess_and_load_training_data():
    df = pd.read_csv('training_data.csv')

    df['text'] = df['text'].apply(preprocess_text)

    label_encoder = LabelEncoder()
    df['label'] = label_encoder.fit_transform(df['label'])

    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

    return X_train, y_train

def preprocess_text(text):
    text = text.lower()
    
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    stop_words = set(stopwords.words('english')).union(ENGLISH_STOP_WORDS)
    text = ' '.join([word for word in text.split() if word not in stop_words])

    return text
