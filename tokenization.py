import nltk
line_to_tokenization = "Natural language processing is the basic for understanding and manipulating any language ."
after_tokenization = nltk.word_tokenize(line_to_tokenization)
print('Before tokenization:', line_to_tokenization)
print('After tokenization:', after_tokenization)