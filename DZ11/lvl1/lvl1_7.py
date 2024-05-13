import nltk
from nltk.corpus import stopwords

from lvl1_6 import delete_punctuation


def delete_stop_words() -> list[str]:
    nltk.download('stopwords')
    return [word for word in delete_punctuation() if word not in stopwords.words('russian')]


if __name__ == '__main__':
    print(delete_stop_words())
