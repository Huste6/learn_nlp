import re
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# Tiền xử lý văn bản: chuẩn hóa và tách từ
# - Chuyển tất cả chữ thành chữ thường
# - Loại bỏ các ký tự không phải chữ cái
# - Tách câu thành danh sách từ
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # Chỉ giữ lại chữ cái và khoảng trắng
    return text.split()

# Mô hình n-gram đơn giản (Bigram)
class BigramModel:
    def __init__(self, corpus):
        # Sử dụng defaultdict để lưu tần suất xuất hiện của từng cặp từ (bigram)
        self.bigram_counts = defaultdict(Counter)
        self.unigram_counts = Counter()
        self.vocab = set()
        self._train(corpus)

    def _train(self, corpus):
        # Xử lý văn bản và cập nhật từ vựng
        words = preprocess_text(corpus)
        self.vocab.update(words)
        
        # Duyệt qua từng cặp từ liên tiếp để xây dựng thống kê
        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]
            
            # Cập nhật số lần xuất hiện của từng bigram và unigram
            self.bigram_counts[first_word][second_word] += 1
            self.unigram_counts[first_word] += 1
    
    def predict_next_word(self, word):
        """Dự đoán từ tiếp theo có xác suất cao nhất dựa trên một từ."""
        if word not in self.bigram_counts:
            return "Không có dữ liệu cho từ này"
        
        # Tính xác suất của mỗi từ tiếp theo dựa trên tần suất xuất hiện của chúng
        word_probs = {
            next_word: count / self.unigram_counts[word]
            for next_word, count in self.bigram_counts[word].items()
        }
        
        # Chọn từ có xác suất cao nhất
        return max(word_probs, key=word_probs.get)
    
    def plot_word_distribution(self, word):
        """Vẽ biểu đồ phân phối xác suất của các từ tiếp theo."""
        if word not in self.bigram_counts:
            print(f"Không có dữ liệu cho từ '{word}'.")
            return
        
        # Tính xác suất của từng từ tiếp theo
        word_probs = {
            next_word: count / self.unigram_counts[word]
            for next_word, count in self.bigram_counts[word].items()
        }
        
        # Tách danh sách từ và xác suất tương ứng
        words, probs = zip(*word_probs.items())
        
        # Vẽ biểu đồ
        plt.figure(figsize=(10, 5))
        plt.bar(words, probs, color='lightcoral')
        plt.xlabel("Từ dự đoán")
        plt.ylabel("Xác suất")
        plt.title(f"Phân phối xác suất của từ tiếp theo sau '{word}'")
        plt.xticks(rotation=45)
        plt.show()

# Đọc dữ liệu từ file văn bản
# - Mở file ở chế độ đọc với encoding UTF-8 để tránh lỗi ký tự
with open("C:\\Users\\Admin\\OneDrive\\문서\\hoc python\\tuần 2\\test.txt", "r", encoding="utf-8") as file:
    text_corpus = file.read()

# Khởi tạo và huấn luyện mô hình
model = BigramModel(text_corpus)

# Nhập từ đầu vào từ người dùng
test_word = input("Nhập từ đầu tiên: ")

# Dự đoán từ tiếp theo
predicted_word = model.predict_next_word(test_word)
print(f"Từ tiếp theo dự đoán sau '{test_word}' là: {predicted_word}")

# Hiển thị phân phối xác suất
model.plot_word_distribution(test_word)
