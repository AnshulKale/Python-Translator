#Coded by AnshulKale
#https://github.com/AnshulKale/Python-Translator/

import translators

#Inputing Text to be translated into a file
with open(r'path file\filename.txt', mode='w') as myfile:

    #can edit
    print("Enter the text you want to translate (press Enter twice to finish): ")

    translateEdit = ''
    while True:
        line = input()
        if line:
            translateEdit += line + '\n'
        else:
            break
    myfile.write(translateEdit)

#Inputing the language user wants to translate to
#can edit
translateTolang = input("Enter the language you want the text to be translated to by including only first two letters of the language: ")


#Collecting the text given by user for translation
with open(r'path file\filename.txt', mode='r') as myfile:
    tobeTranslated = myfile.read()

#Translating
print(translators.translate_text(tobeTranslated, 'google', 'en', translateTolang))
translatedText = translators.translate_text(tobeTranslated, 'google', 'en', translateTolang)

#can edit
fileEdit = f'\n**********************************************************************************\n\nTranslated Text:\n{translatedText}'

#Writing to a text file using the content of fileEdit
with open(r'path file\filename.txt', mode='a',encoding='utf-8') as myfile:
    myfile.write(fileEdit)
