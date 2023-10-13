import PyPDF2
# import spacy

def parseResume(file):
    # reject the resume if it is not a pdf file
    if file.filename[-3:] != 'pdf':
        return "Please upload a pdf file!"
    

    pdfReader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in pdfReader.pages:
        text += page.extractText()

    doc = nlp(text)

    # Extract keywords
    keywords = []
    for token in doc:
        if not token.is_stop and not token.is_punct and not token.is_space:
            keywords.append(token.text)

    return keywords


    # get the keywords from the text using spacy
    # nlp = spacy.load("en_core_web_sm")
    # text = ""
    # for page in pdfReader.pages:
    #     text += page.extractText()
    # doc = nlp(text)
    # keywords = []
    # for token in doc:
    #     if token.pos_ == 'NOUN':
    #         keywords.append(token.text)
    # return keywords

def hello():
    print("Hello World!")
