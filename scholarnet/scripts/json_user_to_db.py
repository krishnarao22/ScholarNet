import mysql.connector
import sys
import json
import spacy
from collections import Counter
from rake_nltk import Rake

def extract_keywords(raw_txt):
    # nlp = spacy.load("en_core_web_sm")
    # processed = nlp(raw_txt)

    # keywords = [token.text for token in processed if token.pos_ in ['NOUN', 'PROPN']]

    # # Calculate frequency distribution of keywords
    # freq_dist = Counter(keywords)

    # # Get the 5 most common keywords
    # top_keywords = freq_dist.most_common(5)

    rake = Rake()
    rake.extract_keywords_from_text(raw_txt)
    return rake.get_ranked_phrases()

    # print(top_keywords)

def main(json_path):
    db = mysql.connector.connect(host="localhost", user="root", password="", database="vial")
    if db.is_connected():
        print("SUCCESSFULLY CONNECTED TO VIAL DATABASE")
    json_data = None
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    # print(json_data)
    keywords = ','.join(extract_keywords(json_data["Resume raw text"])[-30:])

    print(keywords)

    query = "INSERT INTO students (first_name, last_name, school_year, year_of_birth, email, resume_keys) VALUES (%s, %s, %s, %s, %s, %s)"
    in_vals = (json_data["First name"], json_data["Last name"], json_data["Year in school"], json_data["Birth year"], json_data["Email"], keywords)

    cursor = db.cursor()
    
    cursor.execute(query, in_vals)

    db.commit()

    print("SUCCESSFULLY INSERTED STUDENT INTO TABLE")

    print("CLOSING CONNECTION TO VIAL DATABASE...")

    cursor.close()
    db.close()

    

if __name__ == "__main__":
    json_path = None
    try:
        json_path = sys.argv[1]
    except:
        "NEED JSON FILE PATH AS ARGUMENT"
    main(json_path)
    