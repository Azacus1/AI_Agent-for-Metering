import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
# Ensure punkt is downloaded

# Download NLTK data


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(filtered_tokens)


if __name__=="__main__":
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    text = "This is a sample text. It contains some words."
    preprocessed_text = preprocess_text(text)
    print(preprocessed_text)
