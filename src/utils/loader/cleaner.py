import re
from typing import List
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import SnowballStemmer, WordNetLemmatizer

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

class TextCleaner:
    @classmethod
    def clean_text(cls, txt: str) -> str:
        """
        Bereinigt den Text durch Entfernen von speziellen Zeichen, HTML-Tags, überflüssigen Leerzeichen und Stopwörtern.
        Führt auch Stemming und Lemmatization durch.

        :param txt: Der zu bereinigende Text.
        :return: Der bereinigte Text.
        """


        # Entfernen von (cid:2) und ähnlichen Mustern
        txt = re.sub(r'\(cid:\d+\)', '', txt)

        # Normalisierung von Leerzeichen (alle Whitespaces in ein einzelnes Leerzeichen umwandeln)
        txt = re.sub(r'\s+', ' ', txt).strip()

        cleaned_text = txt 
        return cleaned_text
