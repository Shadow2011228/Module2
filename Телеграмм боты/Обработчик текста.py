import telebot


bot = telebot.TeleBot("8407714627:AAGvWG9HcDCuKN18LWPbkghqWQ3poH3fwCA") # создание бота с помощью токена от botFather

@bot.message_handler(content_types=["text"]) # Событие получения текста
def start(msg: telebot.types.Message): # Функция прикрепленная к событию выше, msg - Сообщение
   print(msg.text) # выводим текст отправленного сообщения



bot.infinity_polling() # Бесконечный повтор кода