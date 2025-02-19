# in ra tat ca cac chu trong file.txt
# for line in open("file.txt"):
#     for word in line.split():
#         print(word)

# def calculate_total(exp):
#     total = 0
#     for item in exp:
#         total += item
#     return total

# import calendar
# if __name__ == '__main__':
#     cal1 = calendar.month(2025,2)
#     cal2 = calendar.month(2025,4)
#     print(cal1,cal2)

# import re

# pattern = r"hello"
# text = "hello world"

# # match = re.match(pattern, text)
# # if match:
# #     print("Khớp!")
# # else:
# #     print("Không khớp!")

# match = re.search(pattern, text)
# if match:
#     print("Tìm thấy:", match.group())

#sdt = r"\(\d{3}\)-(\d{3})-(\d{4})|\d{10}"
#email = [a-zA-z0-9_.+-]*@[a-zA-Z]*\.[a-zA-Z]*
# text = "Ngay 17/02/2025, ..."
# pattern = r"(\d{2})/(\d{2})/(\d{4})"
# match = re.search(pattern,text)
# if match:
#     print(match.group(1), "/" ,match.group(2),"/",match.group(3))

# tach tu 
# from nltk.tokenize import word_tokenize
# text = "Natural Language Processing is amazing"
# tokens = word_tokenize(text)
# print(tokens)

# from nltk.corpus import stopwords
# stop_words = set(stopwords.words('english'))
# tokens = ["This", "is", "an", "example", "of", "stopwords", "removal"]
# filtered_tokens = []
# for word in tokens:
#     if word.lower() not in stop_words:
#         filtered_tokens.append(word)
# print(filtered_tokens)

# from nltk.stem import PorterStemmer,LancasterStemmer
# stemmer = PorterStemmer()
# lanStemmer = LancasterStemmer()
# words = ["running", "flies", "easily", "studies"]
# stems1 = [stemmer.stem(word) for word in words]
# stems2 = [lanStemmer.stem(word) for word in words]
# print(stems1)
# print(stems2)
import re

text = "Xin chào?!... Hôm nay là ngày 17/02/2025."
clean_text = re.sub(r"[^\w\s]", "", text)
print(clean_text)
