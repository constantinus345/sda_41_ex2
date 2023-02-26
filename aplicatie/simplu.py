from translate_api import translate_text

#Ask for user input 
text = input("Enter text to translate: ")

raspuns_functiei = translate_text('en', text)
raspunsul_final = f"""Textul tradus este: {raspuns_functiei['translatedText']} 
\n --din limba {raspuns_functiei['detectedSourceLanguage']}
"""

print(raspunsul_final)