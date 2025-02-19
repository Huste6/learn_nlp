import nltk
import spacy
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Tải dữ liệu cần thiết
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('punkt', force=True)

# Tải mô hình tiếng Anh của spaCy
nlp = spacy.load("en_core_web_sm")

# Văn bản mẫu
text = "Natural Language Processing (NLP) is a sub-field of AI that focuses on human-computer interaction using natural language."

# 1️⃣ Chuyển về chữ thường
text = text.lower()

# 2️⃣ Loại bỏ dấu câu
text = text.translate(str.maketrans("", "", string.punctuation))

# 3️⃣ Tokenization
tokens = word_tokenize(text)

# 4️⃣ Loại bỏ từ dừng
stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word not in stop_words]

# 5️⃣ Stemming (rút gọn từ gốc)
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# 6️⃣ Lemmatization (chuyển về dạng nguyên thể)
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# 🔥 Hiển thị kết quả
print("Original Text:", text)
print("\nTokenized Words:", tokens)
print("\nAfter Removing Stopwords:", filtered_tokens)
print("\nAfter Stemming:", stemmed_tokens)
print("\nAfter Lemmatization:", lemmatized_tokens)
