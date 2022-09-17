import os # для работы с системными переменными
import telebot # для работы с Телеграммом
import logging # для логирования отладочной информации
from config import *
from flask import Flask, request # из библиотеки flask импортируем модуль flask (для настройки вертекса) и requests (для обработки запросов)
#---------------------------------------------------------------------------------------------------------------------
# доимпортировал со своего кода
from telebot import types # достаём типы для создания кнопок
from keyboa import Keyboa # для создания встроенных клавиатур любой сложности для ботов, разработанных на базе pyTelegramBotAPI
#---------------------------------------------------------------------------------------------------------------------
# из файла config.py импортируем
bot = telebot.TeleBot(BOT_TOKEN) # создаём переменную бот, в качестве аргумента в конструктор передаём токен нашего телебота
server = Flask(__name__) # создаём переменную server - это екземпляр класс Flask, в конструктор передаём имя текущего модуля
logger = telebot.logger # создаём переменную logger и
logger.setLevel(logging.DEBUG) # устанавливаем уровень логирования на ДЕБАГ (для отладочных сообщений с Heroku...)
# реализовываем направление входящих сообщений с сервера (Github) нашему телеграм-боту
@server.route(f"/{BOT_TOKEN}", methods=["PORT"]) # через декоратор и
def redirect_message(): # функцию redirect_message
    json_string = request.get_data().decode("utf-8") # получаем данные от сервера в utf-8 формате
    update = telebot.types.Update.de_json(json_string) # и применим их к боту
    bot.process_new_updates([update]) # с помощью вызова метода process_new_updates
    return "!", 200
#---------------------------------------------------------------------------------------------------------------------
# Сам код бота: #Создаём кнопки:
def create_keyboard():
    keyboard=types.InlineKeyboardMarkup()
    # keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    python_btn=types.InlineKeyboardButton(text='Python',callback_data='1')
    operators_btn=types.InlineKeyboardButton(text='Operators',callback_data='2')
    data_types_btn = types.InlineKeyboardButton(text='Data types', callback_data='3')
    functions_btn = types.InlineKeyboardButton(text='Functions', callback_data='4')
    oop_btn = types.InlineKeyboardButton(text='OOP', callback_data='5')
    database_btn=types.InlineKeyboardButton(text='Database',callback_data='6')
    modules_btn = types.InlineKeyboardButton(text='Modules', callback_data='777')
    git_btn=types.InlineKeyboardButton(text='Git',callback_data='7')
    django_btn=types.InlineKeyboardButton(text='Django',callback_data='8')
    flask_btn=types.InlineKeyboardButton(text='Flask',callback_data='9')
    site_btn=types.InlineKeyboardButton(text='More information', url='https://it-overone.skillspace.ru/school')
    send_bot_btn=types.InlineKeyboardButton(text='Send Bot to', switch_inline_query="Telegram")
    keyboard.add(python_btn)
    keyboard.add(operators_btn)
    keyboard.add(data_types_btn)
    keyboard.add(functions_btn)
    keyboard.add(oop_btn)
    keyboard.add(database_btn)
    keyboard.add(modules_btn)
    keyboard.add(git_btn)
    keyboard.row(django_btn, flask_btn) # добавление кнопок в один ряд
    keyboard.add(site_btn) # URL-кнопка перенаправляет пользователя по ссылке, с соответствующим предупреждением.
    keyboard.add(send_bot_btn) # Switch-кнопка перенаправления пользователя в какой-либо чат с активацией (встроенного) inline-режима общения с ботом
    return keyboard
def create_telebotReplyKeyboard():
    telebotReplyKeyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    request_contact_replybtn = types.KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
    request_location_replybtn = types.KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
    ads_replybtn = types.KeyboardButton("http://marketstat.ru/partner/ab2")
    start_replybtn = types.KeyboardButton("/start")
    dltkb_replybtn = types.KeyboardButton("/delete_keybord")
    telebotReplyKeyboard.add(request_contact_replybtn,request_location_replybtn)
    telebotReplyKeyboard.add(start_replybtn, dltkb_replybtn)
    telebotReplyKeyboard.add(ads_replybtn)
    return telebotReplyKeyboard
def create_closekeyboard():
    closekeyboard=types.InlineKeyboardMarkup()
    close_btn = types.InlineKeyboardButton(text='close', callback_data='10')
    closekeyboard.add(close_btn)
    return closekeyboard
def create_backkeyboard():
    backkeyboard=types.InlineKeyboardMarkup()
    back_btn = types.InlineKeyboardButton(text='back', callback_data='24')
    backkeyboard.add(back_btn)
    return backkeyboard

@bot.message_handler(commands=['start']) # чтобы функция сработала, при команде /start
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(message.chat.id, u'\U00002139'u'\U0001F49C'u'\U0001F40D', reply_markup=keyboard) # смайлики и клава
@bot.message_handler(commands=['delete_keybord']) # происходит удаление клавиатуры c появлением сообщениея
def process_rm_command(message: types.Message):
    bot.send_message(message.chat.id,"Убираем шаблоны сообщений", reply_markup=types.ReplyKeyboardRemove()),

# добавляем к кнопкам действия. # Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    telebotReplyKeyboard = create_telebotReplyKeyboard()
    closekeyboard=create_closekeyboard()
    # backkeyboard=create_backkeyboard()
    # operators_btn = create_operators_btn()
    # linear_operators_btn = create_linear_operators_btn()
    # conditional_operators_btn= create_conditional_operators_btn()
    # data_types_btn = create_data_types_btn()
    # numbers_btn = create_numbers_btn()
    # oop_btn = create_oop_btn()
    # bd_btn = create_bd_btn()
    # bd2_btn = create_bd2_btn()
    # bd3_btn = create_bd3_btn()
    # modules_btn = create_modules_btn()
    if call.message:       # Если произошло нажати
        if call.data=="1": # и оно соответствует 1, то получили нажатие кнопки 'Python'
            pythons_btn = ["Простой","Легкий в освоении","Свободный и открытый","Язык высокого уровня","Портируемый","Интерпретируемый","Объектно-ориентированный","Расширяемый","Встраиваемый","Обширные библиотеки","back"]
            kb_pythons_btn = Keyboa(items=pythons_btn)
            bot.send_message(call.message.chat.id, text='''<u><b>Python</b></u> – это простой в освоении и мощный язык программирования. Он предоставляет эффективные высокоуровневые структуры данных, а также простой, но эффективный подход к объектно-ориентированному программированию. Его элегантный синтаксис и динамическая типизация наряду с тем, что он является интерпретируемым, делают его идеальным языком для написания сценариев и быстрой разработки приложений в различных областях и на большинстве платформ.
    <b>История названия</b>:
    Гвидо Ван Россум, создатель языка Python, назвал его так в честь телешоу на BBC под названием  <a href="https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus">«Летающий цирк Монти Пайтона»</a>, а вовсе не потому,что он любит змей, <i><tg-spoiler>убивающих животных обвиванием своего длинного тела вокруг них и задавливанием.</tg-spoiler></i>
        <b>Особенности Python</b>: 
<a href="tg://user?id=1578151550">\U0001F642</a>''', reply_markup=kb_pythons_btn(), parse_mode='HTML')
        elif call.data == 'Простой': # 'Простой' or "&pythons_btn=Простой$" or '10'
            bot.send_message(call.message.chat.id, text='''Python – простой и минималистичный язык. Чтение хорошей программы на Python очень напоминает чтение английского текста, хотя и достаточно строгого! Такая псевдо-кодовая природа Python является одной из его самых сильных сторон. Она позволяет вам сосредоточиться на решении задачи, а не на самом языке.''',
                             reply_markup=telebotReplyKeyboard)
        elif call.data == 'Легкий в освоении':
            bot.send_message(call.message.chat.id, text='''Как вы увидите, на Python чрезвычайно легко начать программировать. Python обладает исключительно простым синтаксисом, как уже отмечалось выше.''',
                             reply_markup=closekeyboard)
        elif call.data == 'Свободный и открытый':
            bot.send_message(call.message.chat.id, text='''Python – это пример свободного и открытого программного обеспечения – FLOSS (Free/Libré and Open Source Software). Проще говоря, вы имеете право свободно распространять копии этого программного обеспечения, читать его исходные тексты, вносить изменения, а также использовать его части в своих программах. В основе свободного ПО лежит идея сообщества, которое делится своими знаниями. Это одна из причин, по которым Python так хорош: он был создан и постоянно улучшается сообществом, котороепросто хочет сделать его лучше.''',
                             reply_markup=closekeyboard)
        elif call.data == 'Язык высокого уровня':
            bot.send_message(call.message.chat.id, text='''При написании программы на Python вам никогда не придётся отвлекаться на такие низкоуровневые детали, как управление памятью, используемой вашей программой, и т.п.''',
                             reply_markup=closekeyboard)
        elif call.data == 'Портируемый':
            bot.send_message(call.message.chat.id, text='''Благодаря своей открытой природе, Python был портирован на много платформ (т.е. изменён таким образом, чтобы работать на них). Все ваши программы смогут запускаться на любой из этих платформ без каких-либо изменений, если только вы избегали использования системно-зависимых функций.
    Python можно использовать в GNU/Linux, Windows, FreeBSD, Macintosh, Solaris, OS/2, Amiga, AROS, AS/400, BeOS, OS/390, z/OS, Palm OS, QNX, VMS, Psion, Acorn RISC OS, VxWorks,PlayStation, Sharp Zaurus, Windows CE и даже на PocketPC!
    Вы можете даже использовать такую платформу, как Kivy для создания игр для iOS (iPhone, iPad) и Android.''',
                             reply_markup=closekeyboard)
        elif call.data == 'Интерпретируемый':
            bot.send_message(call.message.chat.id, text='''Программа, написанная на компилируемом языке программирования, как например, C или C++, преобразуется из исходного языка (т.е. C или C++) в язык, понятный компьютеру (бинарный код, т.е. нули и единицы) при помощи компилятора с применением разнообразных флагов и параметров. Когда вы запускаете такую программу, компоновщик/загрузчик копирует программу с диска в оперативную память и запускает её.
    Python же, напротив, не требует компиляции в бинарный код. Программа просто выполняется из исходного текста. Python сам преобразует этот исходный текст в некоторую промежуточную форму, называемую байт-кодом, а затем переводит его на машинный язык и запускает. Всё это заметно облегчает использование Python, поскольку нет необходимости заботиться о компиляции программы, подключении и загрузке нужных библиотек и т.д. Вместе с тем, это делает программы на Python намного более переносимыми, так как достаточно их просто скопировать на другой компьютер, и они работают!''',
                             reply_markup=closekeyboard)
        elif call.data == 'Объектно-ориентированный':
            bot.send_message(call.message.chat.id, text='''Python поддерживает как процедурно-ориентированное, так и объектноориентированное программирование. В процедурно-ориентированных языках программы строятся на основе процедур или функций, которые представляют собой просто-напросто многократно используемые фрагменты программы. В объектноориентированных языках программирования программы строятся на основе объектов, объединяющих в себе данные и функционал. Python предоставляет простые, но мощные средства для ООП, особенно в сравнении с такими большими языками программирования, как C++ или Java.''',
                             reply_markup=closekeyboard)
        elif call.data == 'Расширяемый':
            bot.send_message(call.message.chat.id, text='''Если вам нужно, чтобы некоторая критическая часть программы работала очень быстроили вы вынуждены скрыть часть алгоритма, вы можете написать эту часть программына C или C++, а затем вызывать её из программы на Python.''',
                             reply_markup=closekeyboard)
        elif call.data == 'Встраиваемый':
            bot.send_message(call.message.chat.id, text='''Python можно встраивать в программы на C/C++, чтобы предоставлять возможности написания сценариев их пользователям.''',
                             reply_markup=closekeyboard)
        elif call.data == 'Обширные библиотеки':
            bot.send_message(call.message.chat.id, text='''<a href="https://docs.python.org/3/library/">Стандартная библиотека Python</a> просто огромна. Она может помочь в решении самых разнообразных задач, связанных с использованием регулярных выражений, генерированием документации, проверкой блоков кода, распараллеливанием процессов, базами данных, веб-браузерами, CGI, FTP, электронной почтой, XML, XML-RPC, HTML, WAV файлами, криптографией, GUI (графическим интерфейсом пользователя) и другими системно- зависимыми вещами. Помните, что всё это доступно абсолютно везде, где установлен Python. В этом заключается философия Python «Всё включено». Кроме стандартной библиотеки, существует множество других высококачественных библиотек.''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == 'back':
            bot.delete_message(call.message.chat.id, call.message.message_id)

#---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__": # конструкция гарантирующая, что сервер запустится только при непосредственном...main скрипта)
    bot.remove_webhook() # устанваливаем и обнавляем webhook для нашего бота (удаляем текущий и устанавливаем новый)
    bot.set_webhook(url=APP_URL) # устанваливаем url нашего приложения
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) # запускаем сервер с помощью метода run,
    # передав в него аргументы: host с нулями (это позволит сделать сервер публичным, а не локальным)
    # и port: воспользуемся модулем os и возьмём переменную PORT и значение
