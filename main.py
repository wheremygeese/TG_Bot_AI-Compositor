import config
import audio_msg
from msg_manager import get_reply, message_processing

import logging

from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
user_data = {}




@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Вас приветствует бот композитор!\nНапишите, что бы вы хотели услышать")


@dp.message_handler(content_types=types.message.ContentTypes.TEXT)
async def msg_text(message: types.Message):
    """
    Пришлет аудио в ответ на текстовый запрос
    """
    msg = await message_processing(message.text)
    await message.answer(f'Пробую создать музыку по запросу "{message.text}".')
    await message.answer_audio(await get_reply(msg))
    await message.answer(f'Создал музыку по вашему запросу "{message.text}". \n Хотите чтобы я создал что нибудь еще?')


@dp.message_handler(content_types=types.message.ContentTypes.VOICE)
async def msg_audio(message: types.Voice):
    # Обращаемся к audio_msg чтобы получить текст из аудио и получаем ответ
    reply = await get_reply(await audio_msg.text_from_voice(message))
    msg = await message_processing(reply)
    await message.answer(f'Пробую создать музыку по запросу "{reply}".')
    await message.answer_audio(await get_reply(msg))
    await message.answer(f'Создал музыку по вашему запросу {reply} \n Хотите чтобы я создал что нибудь еще?')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
