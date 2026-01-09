import telebot
from telebot.types import Message, ReplyKeyboardRemove as clear, InlineKeyboardButton as IB, CallbackQuery
import db
import time
import fight
import random

bot = telebot.TeleBot("8407714627:AAGvWG9HcDCuKN18LWPbkghqWQ3poH3fwCA") #

reg1 = ('Приветствую тебя воин!\n' 
        'Ты встал на путь аватара и ты должен его пройти.\n' 
        'У тебя на пути будет много опасностей, но я знаю, что ты справишься!\n'
        'Удачи\n'
        'Напиши свое имя, чтобы племя Нави знало как тебя называть:')

reg3=('Хорошо\n'
      'Теперь выбери себе стихию')

def check_sleep(msg: Message):
    sleep_over = db.sleep.read('userid', msg.chat.id)[1]
    current_time = time.time()
    sleep_count = sleep_over - current_time
    if sleep_count > 0:
        kb = telebot.types.ReplyKeyboardMarkup(True, True)  # создали пустую клавиатуру
        kb.row("Да")  # Добавили кнопки
        kb.row("Нет")
        bot.send_message(msg.chat.id, f'Вы все еще спите, осталось {sleep_count//60} минут\n'
                                      f'Хотите проснуться?',reply_markup=kb)
        bot.register_next_step_handler(msg, wakeup, sleep_count)
        return False

    return True

def wakeup(msg: Message, sleep_count):
    player = db.users.read("userid", msg.chat.id)
    if msg.text.lower() == 'да':
        player[3] -= sleep_count//60*2
        bot.send_message(msg.chat.id, f'Вы проснулись, ваше здоровье {player[3]} ')
        db.users.write(player)
        db.sleep.write([msg.chat.id, 1])
        start(msg)
    else:
        bot.send_message(msg.chat.id, f'Вы продолжили спать\n'
                                      f'Спать осталось: {sleep_count//60} минут.')

temp = {}
@bot.message_handler(['menu'])
def menu(msg: Message):
    text = 'Что будем делать?\n'\
          '/square - площадь\n'\
          '/home - лагерь\n'\
          '/stats - статистика\n'
    if db.defend.read('userid', msg.chat.id)[1] >= 10:
        text += '/defend - защита города'
    if check_sleep(msg):

        bot.send_message(msg.chat.id, text, reply_markup=clear())


@bot.message_handler(['start'])  # Обработчик команды /start
def start(msg: Message):
    temp[msg.chat.id] = {}
    temp[msg.chat.id]['score'] = 0

    if db.is_new_player(msg):
        temp[msg.chat.id]['name'] = ''
        bot.send_message(msg.chat.id, reg1) # Отправляет сообщение от имени бота в указанный чат
        bot.register_next_step_handler(msg, start1) # Ждет пока появится сообщения, после вызывает прикрепленную функцию
    else:
        if check_sleep(msg):
            menu(msg)
            player = db.users.read("userid", msg.chat.id)
            temp[msg.chat.id]['name'] = player[1]


def start1(msg: Message):
    if  temp[msg.chat.id]['name']:
        temp[msg.chat.id]['name'] = msg.text

    kb = telebot.types.ReplyKeyboardMarkup(True, True) # создали пустую клавиатуру
    kb.row('Огонь','Вода 🌊') # Добавили кнопки
    kb.row('Земля','Воздух')

    bot.send_message(msg.chat.id, reg3, reply_markup=kb) # Прикрепили клавиатуру к сообщению
    bot.register_next_step_handler(msg, reg_2)  # Ждет пока появится сообщения, после вызывает прикрепленную функцию

def reg_2(msg: Message):
    if msg.text.lower() == "огонь":
        reg4 = ('Ты захотел выбрать стихию огня\n'
                'Но тебе еще рано ее изучать\n'
                'Потому что это самая сильная стихия\n'
                'Выбери чо-то другое')
        bot.send_message(msg.chat.id, reg4)
        start1(msg)
        return

    # Сохраняем стихию
    temp[msg.chat.id]["power"] = msg.text
    hp, dmg = fight.powers[msg.text]
    db.users.write([
        msg.chat.id, temp[msg.chat.id]["name"],
        msg.text, hp, dmg, 1, 0
    ])
    db.heals.write([
        msg.chat.id, {}
    ])
    db.sleep.write([
        msg.chat.id, 0
    ])
    db.defend.write([
        msg.chat.id, 0
    ])
    print("Игрок добавлен в БД")
    bot.send_message(msg.chat.id, 'Тебя приняли а племя\n'
                                  'Но ты должен усердно учиться и доказать свое право быть в племени\n'
                                  'Ты должен хорошо учить их обычаи и правила\n'
                                  'Это может быть не легко\n'
                                  'Но ты справишься', reply_markup=clear()) # Удалили кнопки

    time.sleep(2)
    menu(msg)

@bot.message_handler(['square'])
def square(msg: Message):
    if check_sleep(msg):

        kb = telebot.types.ReplyKeyboardMarkup(True, True)  # создали пустую клавиатуру
        kb.row('Тренироваться')
        kb.row('Проверить силы')
        bot.send_message(msg.chat.id, 'Ты на площади тренировок', reply_markup=kb)
        bot.register_next_step_handler(msg, square_handler)  # Ждет пока появится сообщения, после вызывает прикрепле

def square_handler(msg: Message):
    if msg.text == "Тренироваться":
        workout(msg)
    if msg.text == 'Проверить силы':
        exam(msg)

@bot.message_handler(['home'])
def home(msg: Message):
    if check_sleep(msg):
        kb = telebot.types.ReplyKeyboardMarkup(True, True)  # создали пустую клавиатуру
        kb.row('Поесть')
        kb.row('Поспать')
        bot.send_message(msg.chat.id, 'Ты дома', reply_markup=kb)
        bot.register_next_step_handler(msg, home_handler)  # Ждет пока появится сообщения, после вызывает прикрепле

def home_handler(msg: Message):
    if msg.text == "Поспать":
        sleep(msg)
    if msg.text == "Поесть":
        eat(msg)

@bot.message_handler(['stats'])
def stats(msg: Message):
    if check_sleep(msg):
        user_list = db.users.read('userid', msg.chat.id) # Берем из таблицы запись
        print(user_list) # Выводим в консоль словарь
        bot.send_message(msg.chat.id,  f'Твоя статистика:\n'
                                       f'❤️{user_list[3]}\n'
                                       f'⚔️{user_list[4]}\n'
                                       f'')
@bot.message_handler(['add_heal'])
def add_heal(msg: Message):
    _, food = db.heals.read("userid", msg.chat.id)
    print(food)

    eatenemy = {'Бешпармак':50, 'Крылышки KFC':15, 'Кола Добрый':10, 'Choco Pie':5, 'Банан':20}

    # food["Хлеб"] = [5, 15]
    # food["Айва"] = [5, 50]

    key=random.choice(list(eatenemy))
    count=random.randint(1,3)
    food[key] = [count, eatenemy[key]]
    db.heals.write([msg.chat.id, food])
    bot.send_message(msg.chat.id, f"Вам с врага выпала еда: {key} в кол-ве {count} шт.")

def eat(msg: Message):
    kb = telebot.types.InlineKeyboardMarkup()
    _, food = db.heals.read("userid", msg.chat.id)
    for key in food:
        kb.row(IB(f"{key} {food[key][1]}❤️ -- {food[key][0]} шт.",
                 callback_data=f"food_{key}_{food[key][1]}"))
    # bot.send_message(msg.chat.id, "Что будешь есть?", reply_markup=kb)
    if food == {}:
        bot.send_message(msg.chat.id, "Еды нет")
    else:
        bot.send_message(msg.chat.id, "Что будешь есть?", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def callback(call: CallbackQuery):
    print(call.data)
    if call.data.startswith("food_"):
       a = call.data.split("_")
       eating(call.message, a[1], a[2])

       # Придётся ещё раз создать клавиатуру
       kb = telebot.types.InlineKeyboardMarkup()
       _, food = db.heals.read("userid", call.message.chat.id)
       for key in food:
           kb.row(IB(f"{key} {food[key][1]}❤️ — {food[key][0]} шт.",
                     callback_data=f"food_{key}_{food[key][1]}"))

       bot.edit_message_reply_markup(call.message.chat.id,
                                     call.message.message_id,
                                     reply_markup=kb
                                     )

    if call.data.startswith("sleep_"):
        a = call.data.split("_")
        bot.delete_message(call.message.chat.id, call.message.message_id)
        t = int(a[1]) // 2
        bot.send_message(call.message.chat.id, f"Ты лег отдыхать на {t} минут")
        seconds = 0.3 * 60
        fight.sleeping(call.message, a[1])
        sleep_over = time.time() + seconds
        db.sleep.write([call.message.chat.id, sleep_over])
        time.sleep(seconds)
        if db.sleep.read('userid', call.message.chat.id)[1] == 1:
            return
        bot.send_message(call.message.chat.id, f"Вы проснулись!")
        menu(call.message)
    if call.data.startswith("menu"):
        bot.delete_message(call.message.chat.id, call.message.id)
        menu(call.message)
    if call.data == "workout":
        player = db.users.read("userid", call.message.chat.id)
        player[4] += player[5] / 10
        player[4] = round(player[4], 1)
        print(player[4])
        db.users.write(player)
        bot.answer_callback_query(call.id, "Ты тренируешься и твоя сила увеличивается! \n"
                                           f"Теперь ты наносишь {player[4]}⚔️", True)

def eating(msg, ft, hp):
    _, food = db.heals.read("userid", msg.chat.id)
    player = db.users.read("userid", msg.chat.id)
    # Отнимаем хлеб
    if food[ft][0] == 1:
        del food[ft]
    else:
        food[ft][0] -= 1

    db.heals.write([msg.chat.id, food])

    # Добавляем ХП
    player[3] += int(hp)
    db.users.write(player)
    print("Игрок поел.")

def sleep(msg: Message):
    player = db.users.read("userid", msg.chat.id)
    low = int(fight.powers[player[2]][0] * player[5]) // 2 - player[3]
    high = int(fight.powers[player[2]][0] * player[5]) - player[3]
    kb = telebot.types.InlineKeyboardMarkup()
    if player[3] < fight.powers[player[2]][0]:
        if low > 0:
            kb.row(IB(f"Вздремнуть — +{low}❤️", callback_data=f"sleep_{low}"))
        if high > 0:
            kb.row(IB(f"Поспать — +{high}❤️", callback_data=f"sleep_{high}"))
    else:
        kb.row(IB(f"Спать не хочется", callback_data="menu"))
    bot.send_message(msg.chat.id, "Выбери, сколько будешь отдыхать:", reply_markup=kb)

def workout(msg: Message):
    kb = telebot.types.InlineKeyboardMarkup()
    kb.row(IB("Тренироваться", callback_data="workout"))
    kb.row(IB("Назад", callback_data="menu"))
    bot.send_message(msg.chat.id, "Жми, чтобы тренироваться!", reply_markup=kb)


def exam(msg: Message):
    bot.send_message(msg.chat.id, f"Приготовься к испытанию, {temp[msg.chat.id]['name']}!", reply_markup=clear())
    time.sleep(2)
    start_exam(msg)

def start_exam(msg: Message):
    random.choice((block, attack))(msg)
    # attack(msg)
    # block(msg)
def block(msg: Message):
    # Создаём список сторон и перемешиваем его
    sides = ["Слева", "Справа", "Сверху", "Снизу"]
    random.shuffle(sides) # Перемешивает список

    # Создаём клавиатуру
    kb = telebot.types.ReplyKeyboardMarkup(True, False)
    kb.row(sides[0], sides[3])
    kb.row(sides[1], sides[2])

    # Выбираем сторону удара и отправляем сообщение
    right = random.choice(sides)
    bot.send_message(msg.chat.id, f"Защищайся! Удар {right}!", reply_markup=kb)
    temp[msg.chat.id]["block_start"] = time.time()
    bot.register_next_step_handler(msg, block_handler, right)

def block_handler(msg: Message, side: str):
    final = time.time()
    player = db.users.read("userid", msg.chat.id)
    if final - temp[msg.chat.id]["block_start"] > player.dmg / 10 or side != msg.text:
        bot.send_message(msg.chat.id, "Твоя реакция слишком медлительна! Ты не готов!")
        temp[msg.chat.id]['score'] = 0
        time.sleep(3)
        menu(msg)
        return
    temp[msg.chat.id]['score'] += 1
    bot.send_message(msg.chat.id, f"Ты справился, продолжаем! очки: {temp[msg.chat.id]['score']}")

    if temp[msg.chat.id]['score'] >= 10:
        bot.send_message(msg.chat.id, f"Ты победил!")
        db.defend.write([
            msg.chat.id, temp[msg.chat.id]['score']
        ])
        menu(msg)
        return
    block(msg)

def attack(msg: Message):
    # Создаём список сторон и перемешиваем его
    sides1 = ["Слева", "Справа", "Сверху", "Снизу"]

    right = random.choice(sides1)
    kb = telebot.types.ReplyKeyboardMarkup(True, False)
    kb.row(sides1[0], sides1[3])
    kb.row(sides1[1], sides1[2])
    bot.send_message(msg.chat.id, "Выбери сторону атаки! Воин!", reply_markup=kb)
    temp[msg.chat.id]["attack_start"] = time.time()
    bot.register_next_step_handler(msg, attack_handler, right)

def attack_handler(msg: Message, side: str):
    final = time.time()
    player = db.users.read("userid", msg.chat.id)

    if side == msg.text or final - temp[msg.chat.id]["attack_start"] > player.dmg / 10:
        if final - temp[msg.chat.id]["attack_start"] > player.dmg / 10:
            bot.send_message(msg.chat.id, "Мастер отбил атаку")
        if side == msg.text:
            bot.send_message(msg.chat.id, "Твоя реакция слишком медлительна! Ты не готов!")

        temp[msg.chat.id]['score'] = 0
        time.sleep(3)
        menu(msg)
        return

    temp[msg.chat.id]['score'] += 1
    bot.send_message(msg.chat.id, f"Ты справился, продолжаем! очки: {temp[msg.chat.id]['score']}")

    if temp[msg.chat.id]['score'] >= 10:
        bot.send_message(msg.chat.id, f"Ты победил!")
        db.defend.write([
            msg.chat.id, temp[msg.chat.id]['score']
        ])
        menu(msg)
        return
    attack(msg)

@bot.message_handler(['defend'])
def defend(msg: Message):
    if check_sleep(msg):
        bot.send_message(msg.chat.id, 'Разведчики прибыли.\n'
                                            'Они доложили новость, что на нас идут враги и их очень много.\n'
                                            'Ты должен защищать свое племя.\n'
                                            'Это будет тяжело, но ты справишься\n')

        temp[msg.chat.id]['defend'] = 0
        new_enemy(msg)

def enemy_desc(enemy):
   return f"На тебя нападает {enemy.name}!\n" \
          f"У него {enemy.hp}❤️ и {enemy.dmg}⚔️\n\n" \
          f"Что будешь делать?"

def new_enemy(msg: Message, enemy = None):
    if enemy is None:
        enemy = fight.Enemy()
    kb = telebot.types.ReplyKeyboardMarkup(True, True)
    kb.row("Напасть", "Отойти в сторону")
    kb.row("Сбежать в город")
    kb.row("Поесть")
    bot.send_message(msg.chat.id, enemy_desc(enemy), reply_markup=kb)
    bot.register_next_step_handler(msg, fight_choice, enemy)

def fight_choice(msg: Message, enemy):
    if msg.text == "Напасть":
        fight_handler(msg, enemy)
    elif msg.text == "Сбежать в город":
        bot.send_message(msg.chat.id, "Повезёт в другой раз")
        xp_check(msg)
        menu(msg)
    elif msg.text == "Отойти в сторону":  # Всё равно что «Отойти в сторону»
        bot.send_message(msg.chat.id, "Ты увернулся и отошёл в сторону!")
        new_enemy(msg)
    else:
        eat(msg)
        time.sleep(5)
        new_enemy(msg, enemy)

def fight_handler(msg: Message, enemy):
    player = db.users.read("userid", msg.chat.id)
    loser = player_attack(msg, enemy)
    if loser:
        # Игрок не убил врага
        loser = enemy.attack(msg, player)
        if loser:
            # Игрок проиграл
            bot.send_message(msg.chat.id, "Ты получил сильное ранение! "
                                     "Твои братья оттащили тебя в деревню.")
            temp[msg.chat.id]["defend"] = 0
            menu(msg)
            return
        else:
            # Игрок бьёт заново
            fight_handler(msg, enemy)
    else:
        # Игрок убил врага
        temp[msg.chat.id]["defend"] += enemy.dmg // 2
        new_enemy(msg)

def player_attack(msg: Message, enemy: fight):
    player = db.users.read("userid", msg.chat.id)
    enemy.hp -= player[4]
    bot.send_message(msg.chat.id, f"Ты ударил врага на {player[4]} урона!")

    time.sleep(0.5)

    if enemy.hp <= 0:
        # Игрок победил
        bot.send_message(msg.chat.id, f"Ты победил врага {enemy.name}")
        time.sleep(0.5)
        add_heal(msg)
        return False
    else:
        # Теперь бьёт враг
        bot.send_message(msg.chat.id, f"Теперь у него {round(enemy.hp, 2)}❤️")
        time.sleep(0.5)
        return True

def xp_check(msg: Message):
    player = db.users.read("userid", msg.chat.id)
    player[6] += temp[msg.chat.id]["defend"]
    if player[6] >= 1:
        player[5] += 1
        player[6] = 0
        player[4] += 5
        fight.powers[player[2]][0] += 50
        bot.send_message(msg.chat.id, f'Вы подняли свой уровень теперь у ваc он такой:{player[5]}\n'
                                            f'Здоровье на: 50❤️\n'
                                            f'Урон на: 5')
    db.users.write(player)

bot.infinity_polling()