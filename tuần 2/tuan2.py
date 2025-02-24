import nltk
import matplotlib.pyplot as plt
from nltk.util import ngrams
from collections import Counter, defaultdict
import random

# Dữ liệu mẫu (có thể thay bằng tập dữ liệu lớn hơn)
corpus = """Hôm nay trời đẹp. Hôm nay tôi đi học. Hôm nay tôi ăn sáng. Ngày mai tôi đi làm."""

# Tiền xử lý dữ liệu
def preprocess(text):
    text = text.lower()  # Chuyển thành chữ thường
    tokens = nltk.word_tokenize(text)  # Tách từ
    return tokens

tokens = preprocess(corpus)

# Xây dựng mô hình n-gram
n = 2  # Dùng mô hình bigram
ngrams_list = list(ngrams(tokens, n))

# Xây dựng bảng tần suất
model = defaultdict(Counter)
for w1, w2 in ngrams_list:
    model[w1][w2] += 1

# Vẽ biểu đồ tần suất
def plot_frequency(model):
    words = []
    frequencies = []
    
    for word, counter in model.items():
        for next_word, freq in counter.items():
            words.append(f"{word} {next_word}")
            frequencies.append(freq)
    
    plt.figure(figsize=(10, 5))
    plt.barh(words, frequencies, color='skyblue')
    plt.xlabel("Tần suất")
    plt.ylabel("Bigram")
    plt.title("Biểu đồ tần suất bigram")
    plt.show()

plot_frequency(model)

def predict_next_word(word):
    if word in model:
        return model[word].most_common(1)[0][0]  # Chọn từ có tần suất cao nhất
    else:
        return random.choice(tokens)  # Nếu không có từ tiếp theo, chọn ngẫu nhiên

# Dự đoán từ tiếp theo
test_word = "hôm"
predicted_word = predict_next_word(test_word)
print(f"Từ tiếp theo của '{test_word}' là '{predicted_word}'")