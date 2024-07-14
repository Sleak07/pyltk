from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""
stop words refer to the words that don't  contain a meaning
and meant to be removed.
"""

example = "Indulge in the flavors of traditional cuisine with this easy One Pot Chicken Pulao recipe, designed for a quick and delightful experience using a pressure cooker. This dish captures the essence of Indian spices and tender chicken, making it a perfect meal for any occasion."

stopwords = set(stopwords.words("english"))

words = word_tokenize(example)
filtered_sentence = []
for w in words:
    if w not in stopwords:
        filtered_sentence.append(w)

print(filtered_sentence)

=================================================================

