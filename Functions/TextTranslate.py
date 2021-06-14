from translate import Translator

First_language  =  input("Enter the language :")
Second_language = input("which language do you want to translate in:")
trans = input("what do you want to translate:")


translator= Translator(from_lang = First_language, to_lang = Second_language )
translation = translator.translate(trans)
print (translation)
