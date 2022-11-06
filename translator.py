from googletrans import Translator

translator = Translator()


def translate(text):
    result = translator.translate(text=text, dest='en')
    return result.text
