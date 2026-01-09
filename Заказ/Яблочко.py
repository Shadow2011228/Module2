import telebot
from telebot.types import Message, ReplyKeyboardRemove as clear
import random


bot = telebot.TeleBot("8334595002:AAGeLcNNeyseq_ff-EBF8ynvHQJFvKYk6uQ")

reg=("Приветствую тебя юный археолог\n"
     "Твоя задача заключается в том чтобы раскопать побольше промокодов\n"
     "Если ты будешь хорошо раскапывать территорию, то тебе может попасться супер промокод")

#     'Название':'путь к картинке',
res = {
    'Древний меч': 'pictures/img.png',
    "Флейта":"pictures/флейта.jpg",
    "Лира":"pictures/лира.jpeg",
    "Кифара":"pictures/Кифара.jpg",
    "Арфа":"pictures/Арфа.jpg",
    "Гусли":"pictures/Гусли.jpg",
    "Бубен":"pictures/Бубен.jpeg",
    "Барабан":"pictures/Барабан.jpg",
    "Волынка":"pictures/Волынка.jpeg",
    "Свирель":"pictures/Свирель.jpg",
    "Варган": "pictures/Варган.jpg",
    "Кугиклы": "pictures/Кугикли.jpg",
    "Свистулька": "pictures/Свистулька.jpeg",
    "Рожок": "pictures/Рожок.jpeg",
    "Погремушка ": "pictures/Погремушка.jpeg",
    "Трещотка": "pictures/Трещотка.jpg",
    "Рубель": "pictures/Рубель.jpg",
    "Колокол": "pictures/Колокол.jpeg",
    "Карникс": "pictures/Карникс.jpeg",
    "Киннор": "pictures/Киннор.jpeg",
    "Канун": "pictures/Канун.jpeg",
    "Жалейка": "pictures/Жалейка.jpeg",
    "Калюка": "pictures/Калюка.jpeg",
    "Неандертальская флейта": "pictures/Неандертальская флейта.jpeg",
    "Гудок": "pictures/Гудок.jpeg"
}

@bot.message_handler(['start'])  # Обработчик команды /start
def start(msg: Message):
    kb = telebot.types.ReplyKeyboardMarkup(False, False)
    kb.row('Копать')
    bot.send_message(msg.chat.id, reg, reply_markup=kb)
    bot.register_next_step_handler(msg, bot_handler)
def bot_handler(msg: Message):
    key = random.choice(list(res))

    if msg.text == "Копать":
        chance = random.randint(0, 100)
        if chance < 6:
            bot.send_message(msg.chat.id, 'Вы нашли промокод: Super_Promo2023')
        else:
            bot.send_photo(msg.chat.id, open(res[key], 'rb'), f"Вы нашли древний инструмент: {key}")
        bot.register_next_step_handler(msg, bot_handler)

bot.infinity_polling()