import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.stem import WordNetLemmatizer
url = "https://edition.cnn.com/politics/live-news/trump-administration-russia-ukraine-02-17-25/index.html"
res = requests.get(url)
html_content = res.text

soup = BeautifulSoup(html_content, 'html.parser') # Sử dụng BeautifulSoup để phân tích cú pháp HTML
article_divs = soup.find_all('div', class_='live-story-post__wrapper')
article_text = ""

for article_div in article_divs:
    paragraphs = article_div.find_all('p')
    article_text += ' '.join([para.get_text() for para in paragraphs]) + "\n"

# Bắt đầu áp dụng các bước tiền xử lý trong văn bản NLP
def preprocess_nlp_with_Stemming(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]","",text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer1 = LancasterStemmer() # Sử dung LancasterStemmer
    tokens = [stemmer1.stem(word) for word in tokens]
    return ' '.join(tokens) 

def preprocess_nlp_with_Lemmatization(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]","",text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer() # Sử dung WordNetLemmatizer
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# run ctrinh
process_text_with_Stemming = preprocess_nlp_with_Stemming(article_text)
process_text_with_Lemmatization = preprocess_nlp_with_Lemmatization(article_text)

with open("file_after_process_with_stemming.txt","w", encoding="utf-8") as file:
    file.write(process_text_with_Stemming)
    file.close()
    
with open("file_after_process_with_Lemmatization.txt","w", encoding="utf-8") as file:
    file.write(process_text_with_Lemmatization)
    file.close()