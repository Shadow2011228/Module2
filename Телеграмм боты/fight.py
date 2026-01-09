import db
import telebot
import random


bot = telebot.TeleBot("8407714627:AAGvWG9HcDCuKN18LWPbkghqWQ3poH3fwCA") #

powers = {
    'Вода 🌊':[120,15],
    'Земля':[100,25],
    'Воздух':[100,25],
    'Аватар':[200,50]
}

def sleeping(msg, hp):
    player = db.users.read("userid", msg.chat.id)
    player[3] += int(hp)
    db.users.write(player)
    print("Игрок поспал.")

class Enemy:
    def __init__(self):
        profs = {
            "Огненный элементаль 🪬": (30, 5),
            "Огненный проказник 🤪": (35, 8),
            "Стена Огня 🔥": (40, 15),
            "Ученик Огня 🧑‍🎓": (80, 20),
            "Студент Огня 👨‍🎓": (100, 25),
            "Заклинатель Огня 🧙": (120, 30),
            "Маг Огня 🧙‍♂️": (135, 35),
            "ОГНЕННЫЙ СМЕРЧ 🔥🌪️": (200, 80),
        }

        self.name = random.choice(list(profs)) # self.name - это атрибут класса Enemy
        self.hp, self.dmg = profs[self.name]

    def attack(self, msg, player):  # - это создание метода attack для класса Enemy
        player = db.users.read("userid", msg.chat.id)
        player[3] -= self.dmg
        db.users.write(player)

        bot.send_message(msg.chat.id, f"{self.name} ударил тебя на {self.dmg} урона!")

        if player[3] <= 0:
            player[3] = 0
            bot.send_message(msg.chat.id, f"{self.name} победил тебя!")
            db.users.write(player)
            return True
        else:
            bot.send_message(msg.chat.id, f"Теперь у тебя {round(player[3], 2)}❤️")
            return False
