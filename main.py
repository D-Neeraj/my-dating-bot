from service.data_cleaning import DataCleaning

gender = input("Please select your gender - (Male | M, Female F): ")
your_nick_name = input("Please enter your nick name: ")
print(f"Diamond Jackson: Hello {your_nick_name}!!!, welcome to our heaven...")
data_clean = DataCleaning.getInstance()
while True:
    message = input(f"{your_nick_name}: ")
    cleaned_message = data_clean.clean_message(message)
    print(f"Diamond Jackson: {cleaned_message}")


