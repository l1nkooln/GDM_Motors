import telebot
from telebot import time, types
from datetime import datetime, timedelta
from time import sleep
from datetime import datetime

current_datetime = datetime.now()

clickIdTimes = {}

def checkClick(chat_id, timer_dict, timeout):
    if chat_id not in timer_dict or timer_dict[chat_id] < datetime.now() - timedelta(seconds=timeout):
        timer_dict[chat_id] = datetime.now()
        return True
    return False

print(checkClick(10, clickIdTimes, timeout=1))
print(checkClick(10, clickIdTimes, timeout=1))
sleep(2)
print(checkClick(10, clickIdTimes, timeout=1))
print(checkClick(10, clickIdTimes, timeout=1))

def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter

token = '6585154727:AAG33-rokgu3Hbjlqzd6zn3imnEqOXcBNTo' 
bot = telebot.TeleBot(token)
admin_id = [1132004570, 715627118]  

@bot.message_handler(commands=['start'])
def button(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Залишити заявку')
    bt2 = types.KeyboardButton("Зв'язатися з менеджером")
    bt3 = types.KeyboardButton('Про компанію')
    bt4 = types.KeyboardButton('Наші соц.мережі')
    bt5 = types.KeyboardButton('Звʼязатись з нами')
    markup.add(bt1, bt2, bt3, bt4, bt5)
   
    bot.send_message(chat_id, f'Вітаю, {message.from_user.first_name}! Будь ласка, оберіть потрібне Вам меню.',
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Залишити заявку':
            a = telebot.types.ReplyKeyboardRemove()
            if not checkClick(chat_id, clickIdTimes, 2*60):
                bot.send_message(chat_id, "📌Ви вже залишили заявку\n Спробуйте через пару хвилин")
                return
            msg = bot.send_message(chat_id, "📃 Будь ласка, залиште Ваше ПІБ для того, щоб менеджер міг Вас ідентифікувати.")
            bot.register_next_step_handler(msg,regist_1)
        elif message.text == "Зв'язатися з менеджером":
            msg = bot.send_message(chat_id, "Як до вас звертатися?")
            bot.register_next_step_handler(msg ,call_1)
        elif message.text == 'Про компанію':
                bot.send_message(message.chat.id, "Ми почали свою діяльність у 2018 році та стали популярним вибором серед тих, хто шукає високоякісний автомобіль за доступною ціною. Купуючи авто зі США, наші клієнти економлять до 40% від вартості подібних авто в Україні. Ми гарантуємо якість кожного автомобіля, оскільки він проходить перевірку на технічний стан перед тим, як його відправити до України. Американський авторинок завжди був відомий своїм широким асортиментом вибору автомобілей по доступній ціні. Ми з гордістю пропонуємо нашим клієнтам ці автомобілі, які стануть надійними та стильними спутниками на дорогах України.")
        elif message.text == 'Наші соц.мережі':
                telegram = 'Наш телеграм:\n---------\n(https://t.me/greendrivemotors)\n---------'
                insta = 'Наш інстраграм:\n---------\n(https://www.instagram.com/green.drive.motors?igsh=a3FwNmt3b3J4d2M1&utm_source=qr)\n---------'
                tiktok = 'Наш тік ток:\n---------\n(https://www.tiktok.com/@greendrivemotors?_t=8j4xO7NzujO&_r=1)\n---------'
                site = 'Наш сайт:\n---------\n(https://gdmcars.fun/)\n---------'
                bot.send_message(message.chat.id, f'{telegram}\n{insta}\n{tiktok}\n{site}')
        elif message.text == 'Звʼязатись з нами':
                bot.send_message(message.chat.id, "+380675898538 - Cергій\n+380639644361 - Арсен\n+380965898856 - Святослав\n+380983974349 - Василь")
        
def regist_1(message):
    global user_pib
    global username
    user_pib = message.text
    username = message.from_user.username
    markupp = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Надати номер', request_contact=True)
    markupp.add(bt1)
    msg3 = bot.send_message(message.chat.id, "📞 Надайте Ваш контактний номер телефону)", reply_markup=markupp)
    bot.register_next_step_handler(msg3, regist_2)
def regist_2(message):
    global user_phone
    global user_pib
    global kyzov


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Залишити заявку')
    bt2 = types.KeyboardButton("Зв'язатися з менеджером")
    bt3 = types.KeyboardButton('Про компанію')
    bt4 = types.KeyboardButton('Наші соц.мережі')
    bt5 = types.KeyboardButton('Звʼязатись з нами')
    markup.add(bt1, bt2, bt3, bt4, bt5)
    if message.text == str(message.text):
        user_phone = message.text
    elif message.contact.phone_number == message.contact.phone_number:
        user_phone = message.contact.phone_number
    # user_phone = message.text, message.contact.phone_number
    
    msg2 = bot.send_message(message.chat.id, "🚗 Будь ласка, введіть назву марки автомобіля, який Вас цікавить. (Audi, Renault...)", reply_markup= markup)
    bot.register_next_step_handler(msg2, regist_3)
def regist_3(message):
    global user_phone
    global user_pib
    global kyzov
    global model
    kyzov = message.text
    msg4 = bot.send_message(message.chat.id, "Будь ласка, уточніть модель заданої Вами марки, яка Вас цікавить.")
    bot.register_next_step_handler(msg4, regist_4)
def regist_4(message):
    global user_phone
    global user_pib
    global kyzov
    global model
    global msg5
    model = message.text
    msg5 = bot.send_message(message.chat.id, "🕧 Будь ласка, введіть рік моделі, яка Вас цікавить.")
    bot.register_next_step_handler(msg5, regist_5)
def regist_5(message):
    global user_phone
    global user_pib
    global kyzov
    global model
    global price
    global year
    global msg5
    
    year = message.text
    if int(year) < 1980 or int(year) > current_datetime.year: 
        bot.send_message(message.chat.id, 'Не вірний рік авто. Перевірь і спробуй ще раз')
        return bot.send_message(message.chat.id, "Не вірний рік авто. Перевірь і спробуй ще раз")

    msg6 = bot.send_message(message.chat.id, "💰 Введіть Ваш бюджет, на який Ви розраховуєте. (У доларах США)")
    bot.register_next_step_handler(msg6, regist_6)
def regist_6(message):
    global user_phone
    global user_pib
    global kyzov
    global model
    global price
    global year
    global username
    price = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Залишити заявку')
    bt2 = types.KeyboardButton("Зв'язатися з менеджером")
    bt3 = types.KeyboardButton('Про компанію')
    bt4 = types.KeyboardButton('Наші соц.мережі')
    bt5 = types.KeyboardButton('Звʼязатись з нами')
    markup.add(bt1, bt2, bt3, bt4, bt5)
    
    if username == None:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        username = 'не визначено'
        bot.send_message(message.chat.id,"Дякуємо за вашу заявку, наш менеджер з вами зв'яжеться", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(len(admin_id)):
            bot.send_message(admin_id[i], f"📍Нова заявка: \n Нік юзера: {username} \n ПІБ: {user_pib}\n Номер телефону: {user_phone} \n Марка т/з: {kyzov} \n Модель: {model} \n Рік: {year} \n Бажана ціна: {price}")
    
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,"Дякуємо за вашу заявку, наш менеджер з вами зв'яжеться", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(len(admin_id)):
            bot.send_message(admin_id[i], f"📍Нова заявка: \n Нік юзера: @{username} \n ПІБ: {user_pib}\n Номер телефону: {user_phone} \n Марка т/з: {kyzov} \n Модель: {model} \n Рік: {year} \n Бажана ціна: {price}")

def call_1(message):
    global user_pib
    global username
    user_pib = message.text
    username = message.from_user.username
    markupp = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Надати номер', request_contact=True)
    markupp.add(bt1)
    msg3 = bot.send_message(message.chat.id, "📞 Надайте Ваш контактний номер телефону)", reply_markup=markupp)
    bot.register_next_step_handler(msg3, call_2)
def call_2(message):
    global user_phone
    global user_pib
    global username
    global admins_id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Залишити заявку')
    bt2 = types.KeyboardButton("Зв'язатися з менеджером")
    bt3 = types.KeyboardButton('Про компанію')
    bt4 = types.KeyboardButton('Наші соц.мережі')
    bt5 = types.KeyboardButton('Звʼязатись з нами')
    markup.add(bt1, bt2, bt3, bt4, bt5)
    if message.text == str(message.text):
        user_phone = message.text
    elif message.contact.phone_number == message.contact.phone_number:
        user_phone = message.contact.phone_number
    


    if username == None:
        username = 'не визначено'
        bot.send_message(message.chat.id,"Дякуємо за вашу заявку, наш менеджер незабаром з вами зв'яжеться", reply_markup=markup)
        for i in range(len(admin_id)):
            bot.send_message(admin_id[i], f"📍Нова заявка: \n Нік юзера: {username} \n ПІБ: {user_pib}\n Номер телефону: {user_phone}")

    else:
        bot.send_message(message.chat.id,"Дякуємо за ваше звернення, наш менеджер незабаром з вами зв'яжеться", reply_markup=markup)
        for i in range(len(admin_id)):
            bot.send_message(admin_id[i], f"📍Нова заявка: \n Нік юзера: @{username} \n ПІБ: {user_pib}\n Номер телефону: {user_phone}")

    
    

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)