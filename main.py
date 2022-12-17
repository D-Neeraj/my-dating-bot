from service.data_cleaning import DataCleaning

conversation = DataCleaning.getInstance()

lower_text_conversation = conversation.text_to_lower("Hey, how are you buddy, I am came from working to give you gifts")

filtered_words = conversation.remove_stop_words(lower_text_conversation)

lemmatized_words = conversation.lemmatization(filtered_words)

print(lemmatized_words)


