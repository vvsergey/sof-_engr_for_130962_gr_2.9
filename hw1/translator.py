from transformers import pipeline

en_ru_translator = pipeline("translation_en_to_ru", model="Helsinki-NLP/opus-mt-en-ru")
text = "How are you?"
translator = en_ru_translator(text)
print(translator)