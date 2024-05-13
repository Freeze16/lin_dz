import nltk
# from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')


def main():
    nltk.download('punkt')
    with open('2.txt', 'r') as file:
        txt = file.read()

    tokens = word_tokenize(txt)
    # tokenization = [word for word in tokens if word not in stopwords.words('english')]
    return tokens


if __name__ == '__main__':
    print(main())
