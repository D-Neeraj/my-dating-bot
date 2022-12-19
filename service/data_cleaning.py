import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


class DataCleaning:
    __conversation__ = None

    @staticmethod
    def getInstance():
        """
        If the class variable __conversation__ is None, then create a new instance of the class and assign it to the class
        variable __conversation__
        :return: The instance of the class.
        """
        if DataCleaning.__conversation__ is None:
            DataCleaning()
        return DataCleaning.__conversation__

    def __init__(self):
        """
        If the class has not been instantiated, instantiate it.
        If it has been instantiated, raise an exception
        """
        if DataCleaning.__conversation__ is not None:
            raise Exception("This class is singleton class")
        else:
            DataCleaning.__conversation__ = self

    '''
        1. Remove Stop words 
        2. To Lower
        3. Lemma
    '''

    def text_to_lower(self, chat_msg):
        """
        It takes a string, converts it to lowercase, and returns it

        :param chat_msg: The message that the user has sent
        :return: The chat_msg is being returned in lower case.
        """
        return chat_msg.lower()

    def remove_stop_words(self, chat_msg):
        """
        It takes a string of words, splits it into a list of words, removes the stop words, and returns a list of words

        :param chat_msg: The message that the user has sent
        :return: A list of words that are not stop words.
        """
        chat_msg = re.sub(r'[^\w]', ' ', chat_msg)
        chat_msg = nltk.word_tokenize(chat_msg)
        stop_words = stopwords.words('english')
        return [word for word in chat_msg if word not in stop_words]

    def lemmatization(self, chat_msg):
        """
        It takes a string of words, tokenizes it, tags the parts of speech, and then lemmatizes the words based on their
        parts of speech

        :param chat_msg: The chat message that we want to lemmatize
        :return: A string of the lemmatized words.
        """
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word, pos='v') for word in chat_msg]

    def clean_message(self, chat_message):

        lower_text_conversation = self.text_to_lower(chat_message)

        filtered_words = self.remove_stop_words(lower_text_conversation)

        return ' '.join(self.lemmatization(filtered_words))


# Intent - Order, Dating
# Entity - Purchase - buy, get, order, Products - sex toys, condom, lingeria
# Sexy_chat - love, date, sex, fuck | Romance - kiss, smooch

# I want to buy a sex toys
# Response -
