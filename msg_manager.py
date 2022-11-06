import mubert
import translator
from langdetect import detect


async def get_reply(msg):
    """ Получаем ответ на msg """
    return mubert.generate_track_by_prompt(msg)


async def message_processing(text):
    if detect(text) != 'en':  # Если запрос не на английском, то переводим на английский
        msg = translator.translate(text)
    else:  # Иначе оставляем как есть
        msg = text
    return msg