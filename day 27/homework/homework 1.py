my_word = "bread"
user_word = input("Enter a word: ")
if user_word.strip().casefold() == my_word.casefold():
    print("Our words are similar :)")
else:
    print("We have different words :(")




