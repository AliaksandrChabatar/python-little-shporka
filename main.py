import os # для работы с системными переменными (из примера)
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
def create_operators_btn():
    operators_btn=types.InlineKeyboardMarkup()
    linear_operators_btn = types.InlineKeyboardButton(text='Линейные операторы', callback_data='11')
    conditional_operators_btn = types.InlineKeyboardButton(text='Условные операторы', callback_data='12')
    cycle_for_btn = types.InlineKeyboardButton(text='Цикл for', callback_data='13')
    cycle_while_btn = types.InlineKeyboardButton(text='Цикл while', callback_data='14')
    priority_btn = types.InlineKeyboardButton(text='Приоритет операторов в Python', callback_data='15')
    back_btn = types.InlineKeyboardButton(text='back', callback_data='16')
    operators_btn.row(linear_operators_btn, conditional_operators_btn)
    operators_btn.row(cycle_for_btn, cycle_while_btn)
    operators_btn.add(priority_btn)
    operators_btn.add(back_btn)
    return operators_btn
def create_linear_operators_btn():
    linear_operators_btn=types.InlineKeyboardMarkup()
    arithmetic_operators_btn = types.InlineKeyboardButton(text='Арифметические операторы', callback_data='17')
    comparison_operators_btn = types.InlineKeyboardButton(text='Операторы сравнения (реляционные)', callback_data='18')
    assignment_operators_btn = types.InlineKeyboardButton(text='Операторы присваивания', callback_data='19')
    bitwise_operators_btn = types.InlineKeyboardButton(text='Побитовые операторы', callback_data='20')
    logical_operators_btn = types.InlineKeyboardButton(text='Логические (булевые) операторы', callback_data='21')
    membership_operators_btn = types.InlineKeyboardButton(text='Операторы членства (Membership operators)', callback_data='22')
    identity_operators_btn = types.InlineKeyboardButton(text='Операторы тождественности (Identity operators)', callback_data='23')
    lo_back_btn = types.InlineKeyboardButton(text='back', callback_data='16')
    linear_operators_btn.add(arithmetic_operators_btn)
    linear_operators_btn.add(comparison_operators_btn)
    linear_operators_btn.add(assignment_operators_btn)
    linear_operators_btn.add(bitwise_operators_btn)
    linear_operators_btn.add(logical_operators_btn)
    linear_operators_btn.add(membership_operators_btn)
    linear_operators_btn.add(identity_operators_btn)
    linear_operators_btn.add(lo_back_btn)
    return linear_operators_btn
def create_conditional_operators_btn():
    conditional_operators_btn=types.InlineKeyboardMarkup()
    example_btn = types.InlineKeyboardButton(text='Примеры', callback_data='25')
    back_btn = types.InlineKeyboardButton(text='back', callback_data='24')
    conditional_operators_btn.row(example_btn, back_btn)
    return conditional_operators_btn
def create_data_types_btn():
    data_types_btn=types.InlineKeyboardMarkup()
    numbers_btn = types.InlineKeyboardButton(text='Numbers (числа) - НЕизменяемые', callback_data='26')
    bool_btn = types.InlineKeyboardButton(text='Boolean (логический тип данных) bool', callback_data='27')
    bytes_btn = types.InlineKeyboardButton(text='Bytes, bytearray (байты и массивы байтов)', callback_data='28')
    str_btn = types.InlineKeyboardButton(text='''Strings (строки) str - НЕизменяемые, упорядоченные''', callback_data='29')
    list_btn = types.InlineKeyboardButton(text='Lists (списки) list - изменяемые, упорядоченные', callback_data='30')
    dict_btn = types.InlineKeyboardButton(text='Dictionaries (словари) dict - изменяемые, НЕупорядоченные', callback_data='31')
    tupl_btn = types.InlineKeyboardButton(text='Tuples (кортежи) tupl - НЕизменяемые, упорядоченные', callback_data='32')
    set_btn = types.InlineKeyboardButton(text='Sets (множества) set - изменяемые, НЕупорядоченные', callback_data='33')
    file_btn = types.InlineKeyboardButton(text='Файл file', callback_data='34')
    range_btn = types.InlineKeyboardButton(text='range object (a type of iterable)', callback_data='35')
    none_btn = types.InlineKeyboardButton(text='None', callback_data='36')
    work_with_types_btn = types.InlineKeyboardButton(text='Работа с типами', callback_data='43')
    dt_back_btn = types.InlineKeyboardButton(text='back', callback_data='37')
    data_types_btn.add(numbers_btn)
    data_types_btn.add(bool_btn)
    data_types_btn.add(bytes_btn)
    data_types_btn.add(str_btn)
    data_types_btn.add(list_btn)
    data_types_btn.add(dict_btn)
    data_types_btn.add(tupl_btn)
    data_types_btn.add(set_btn)
    data_types_btn.add(file_btn)
    data_types_btn.add(range_btn)
    data_types_btn.add(none_btn)
    data_types_btn.add(work_with_types_btn)
    data_types_btn.add(dt_back_btn)
    return data_types_btn
def create_numbers_btn():
    numbers_btn=types.InlineKeyboardMarkup()
    int_btn = types.InlineKeyboardButton(text='integer (целое число) int', callback_data='38')
    float_btn = types.InlineKeyboardButton(text='float (вещественное - число с плавающей точкой)', callback_data='39')
    complex_btn = types.InlineKeyboardButton(text='complex (комплексное число)', callback_data='40')
    numbers_operations_btn = types.InlineKeyboardButton(text='Операции с числами', callback_data='41')
    n_back_btn = types.InlineKeyboardButton(text='back', callback_data='42')
    numbers_btn.add(int_btn)
    numbers_btn.add(float_btn)
    numbers_btn.add(complex_btn)
    numbers_btn.add(numbers_operations_btn)
    numbers_btn.add(n_back_btn)
    return numbers_btn
def create_oop_btn():
    oop_btn=types.InlineKeyboardMarkup()
    oop_1_btn = types.InlineKeyboardButton(text='Введение в ООП, Классы и Объекты', callback_data='44')
    oop_2_btn = types.InlineKeyboardButton(text='Поля, методы, атрибуты и уровни доступа', callback_data='45')
    oop_paradigms_btn = types.InlineKeyboardButton(text='Парадигмы ООП', callback_data='46')
    dop_btn = types.InlineKeyboardButton(text='Дополнительно', callback_data='47')
    oop_back_btn = types.InlineKeyboardButton(text='back', callback_data='48')
    oop_btn.add(oop_1_btn)
    oop_btn.add(oop_2_btn)
    oop_btn.add(oop_paradigms_btn)
    oop_btn.add(dop_btn)
    oop_btn.add(oop_back_btn)
    return oop_btn
def create_bd_btn():
    bd_btn=types.InlineKeyboardMarkup()
    bd_1_btn = types.InlineKeyboardButton(text='Типы таблиц и ключей в реляционных БД.', callback_data='49')
    bd_2_btn = types.InlineKeyboardButton(text='SQL, SQLite, Типы данных SQL', callback_data='50')
    bd_3_btn = types.InlineKeyboardButton(text='Отличие реляционных от нереляционных БД', callback_data='51')
    bd_example_btn = types.InlineKeyboardButton(text='Примеры БД', callback_data='52')
    bd_back_btn = types.InlineKeyboardButton(text='back', callback_data='53')
    bd_btn.add(bd_1_btn)
    bd_btn.add(bd_2_btn)
    bd_btn.add(bd_3_btn)
    bd_btn.add(bd_example_btn)
    bd_btn.add(bd_back_btn)
    return bd_btn
def create_bd2_btn():
    bd2_btn=types.InlineKeyboardMarkup()
    sqlite3_btn = types.InlineKeyboardButton(text='SQLite3', callback_data='54')
    mysql_btn = types.InlineKeyboardButton(text='MySQL', callback_data='55')
    postgresql_btn = types.InlineKeyboardButton(text='PostgreSQL', callback_data='56')
    bd2_back_btn = types.InlineKeyboardButton(text='back', callback_data='57')
    bd2_btn.add(sqlite3_btn)
    bd2_btn.add(mysql_btn)
    bd2_btn.add(postgresql_btn)
    bd2_btn.add(bd2_back_btn)
    return bd2_btn
def create_bd3_btn():
    bd3_btn=types.InlineKeyboardMarkup()
    select_from_btn = types.InlineKeyboardButton(text='SELECT, FROM ', callback_data='58')
    where_btn = types.InlineKeyboardButton(text='WHERE', callback_data='59')
    group_by_btn = types.InlineKeyboardButton(text='GROUP BY', callback_data='60')
    having_btn = types.InlineKeyboardButton(text='HAVING', callback_data='61')
    order_by_btn = types.InlineKeyboardButton(text='ORDER BY', callback_data='62')
    join_btn = types.InlineKeyboardButton(text='JOIN', callback_data='63')
    difference_btn = types.InlineKeyboardButton(text='Разница между Drop, Truncate и Delete', callback_data='64')
    bd3_back_btn = types.InlineKeyboardButton(text='back', callback_data='65')
    bd3_btn.row(select_from_btn,where_btn)
    bd3_btn.row(group_by_btn,having_btn)
    bd3_btn.row(order_by_btn,join_btn)
    bd3_btn.add(difference_btn)
    bd3_btn.add(bd3_back_btn)
    return bd3_btn
def create_modules_btn():
    modules_btn=types.InlineKeyboardMarkup()
    pyqt5_btn = types.InlineKeyboardButton(text='PyQt5', callback_data='66')
    pygame_btn = types.InlineKeyboardButton(text='PyGame', callback_data='67')
    telebot_btn = types.InlineKeyboardButton(text='Telebot', callback_data='68')
    m_back_btn = types.InlineKeyboardButton(text='back', callback_data='69')
    modules_btn.add(pyqt5_btn)
    modules_btn.add(pygame_btn)
    modules_btn.add(telebot_btn)
    modules_btn.add(m_back_btn)
    return modules_btn

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
    backkeyboard=create_backkeyboard()
    operators_btn = create_operators_btn()
    linear_operators_btn = create_linear_operators_btn()
    conditional_operators_btn= create_conditional_operators_btn()
    data_types_btn = create_data_types_btn()
    numbers_btn = create_numbers_btn()
    oop_btn = create_oop_btn()
    bd_btn = create_bd_btn()
    bd2_btn = create_bd2_btn()
    bd3_btn = create_bd3_btn()
    modules_btn = create_modules_btn()
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

        if call.data == "2":
            bot.send_message(call.message.chat.id, text='''Ход выполнения программы может быть <i><b>линейным</b></i>, когда выражения выполняются друг за другом, начиная с первого и заканчивая последним. Ни одна строка кода программы не пропускается.
    Часто в программах при выполнении кода, в зависимости от тех или иных условий, некоторые его участки могут быть опущены, в то время как другие – выполнены. Данные <i><b>ветвления</b></i> реализуются <i><b>условными</b></i> операторами и операторами <b>циклов</b> – особыми конструкциями языка программирования.''',
                                reply_markup=operators_btn, parse_mode='HTML')
        elif call.data == '16':
            bot.delete_message(call.message.chat.id, call.message.message_id)

        if call.data == "11":
            bot.send_message(call.message.chat.id, text="<b>Типы операторов:</b>", reply_markup=linear_operators_btn, parse_mode='HTML')
        elif call.data == '17':
            img = open('arithmetic operator.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                reply_markup=closekeyboard)
            img.close()
        elif call.data == '18':
            img = open('comparison operator.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                reply_markup=closekeyboard)
            img.close()
        elif call.data == '19':
            img = open('assignment operator.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                reply_markup=closekeyboard)
            img.close()
        elif call.data == '20':
            img = open('bitwise operator.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                reply_markup=closekeyboard)
            img.close()
        elif call.data == '21':
            img = open('logical-boolean operator.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                reply_markup=closekeyboard)
            img.close()
        elif call.data == '22':
            img = open('membership operators.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                reply_markup=closekeyboard)
            img.close()
        elif call.data == '23':
            img = open('identity operators.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                reply_markup=closekeyboard)
            img.close()
        elif call.data == '15':
            img = open('operator_priority.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                # caption="Картинка еда",
                reply_markup=closekeyboard)
            img.close()

        if call.data == "12":
            bot.send_message(call.message.chat.id, text='''    Оператор <b>if</b> используется для проверки условий: if /«если» условие «Верно» (булево значение True), выполняется блок выражений (называемый «if-блок»), «иначе» выполняется другой блок выражений (называемый «else-блок»).
    Блок <b>else</b>/«иначе/в противном случае» является необязательным, как и блок <b>elif</b> (для реализации выбора из нескольких альтернатив (осуществляет возможность множественного ветвления на одном уровне вложенности)).
    Конструкция «if логическое_выражение :» называется заголовком условного оператора. Выражения после двоеточия, обособленное  за счёт отступа из 4 пробелов (или клавише табуляции «Tab») – телом условного оператора. Тело может содержать как множество  выражений (инструкции), так и всего одно или даже быть пустым.
    В заголовке else никогда не бывает логического выражения, как в if и elif.
    После того, как Python заканчивает выполнение всего оператора if вместе с его частями elif и else, он переходит к следующему выражению в блоке, содержащем этот оператор if (в случае «if логическое_выражение :» как основного блока программы (в котором начинается выполнение программы), а следующее выражение – это print ('Завершено') – Python доходит до конца программы и просто выходит).''',
                             parse_mode='HTML', reply_markup=conditional_operators_btn)
        elif call.data == '24':
            bot.delete_message(call.message.chat.id, call.message.message_id)
        elif call.data == '25':
            img_1 = open('if.jpg','rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_1,reply_markup=closekeyboard)
            img_1.close()
            img_2 = open('if-else.jpg','rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_2,reply_markup=closekeyboard)
            img_2.close()
            img_3 = open('if-elif-else.jpg','rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_3,reply_markup=closekeyboard)
            img_3.close()

        if call.data == "13":
            img = open('for.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        if call.data == "14":
            img = open('while.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        if call.data == '3':
            img = open('standard_type_hierarchy.png', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Стандартная иерархия типов",
                reply_markup=closekeyboard)
            img.close()
            bot.send_message(call.message.chat.id, text='''    <u>Переменная Python</u> — это идентификатор для ссылки на значение в программе. Переменная содержит место в памяти объекта. Они позволяют программе Python получать доступ к другим объектам и вызывать их функции или выполнять другие операции.
    <u>Все данные в Python являются объектами.</u> Они могут создаваться нами вручную, либо быть изначально встроенными на уровне языка. Объект можно охарактеризовать, как особую область памяти, где хранятся некоторые значения и определённые для этих значений операции. Объекты можно классифицировать по их типам.
    <u>Python - язык типизированный.</u> А, раз в нём определено понятие "типа", то должен существовать и процесс распознавания и верификации этих самых "типов". Таким процессом и является типизация. В ходе её выполнения происходит подтверждение используемых типов и применение к ним соответствующих ограничений. Типизация может быть статической и динамической. В первом случае, проверка выполняется во время компиляции, во втором — непосредственно во время выполнения программного кода.
    <u>Python - язык с динамической типизацией.</u> И здесь, к примеру, одна и та же переменная, при многократной инициализации, может являть собой объекты разных типов.''',
                             parse_mode='HTML', reply_markup=data_types_btn)
        elif call.data == '26':
            bot.send_message(call.message.chat.id, text='''    <b>Числовые типы</b>
    <i>"Все сущее есть Число"</i> — сказал однажды мудрый грек по имени Пифагор. Числа — важнейший и фундаментальнейший из всех типов данных для всех языков программирования. В Python для их представления служит числовой тип данных.''',
                             parse_mode='HTML', reply_markup=numbers_btn)
        elif call.data == "38":
            img = open('int.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "39":
            img = open('float.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "40":
            img = open('complex.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "41":
            img_1 = open('operations with numbers 1.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_1, reply_markup=closekeyboard)
            img_1.close()
            img_2 = open('operations with numbers 2.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_2, reply_markup=closekeyboard)
            img_2.close()
            img_3 = open('number generator.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_3, reply_markup=closekeyboard)
            img_3.close()
        elif call.data == '42':
            bot.delete_message(call.message.chat.id, call.message.message_id)
        elif call.data == "27":
            img_1 = open('bool_1.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_1, reply_markup=closekeyboard)
            img_1.close()
            img_2 = open('bool_2.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_2, reply_markup=closekeyboard)
            img_2.close()
        elif call.data == "28":
            img_1 = open('bytes 1.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_1, reply_markup=closekeyboard)
            img_1.close()
            img_2 = open('bytes 2.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_2, reply_markup=closekeyboard)
            img_2.close()
            img_3 = open('bytearray.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_3, reply_markup=closekeyboard)
            img_3.close()
        elif call.data == "29":
            bot.send_message(call.message.chat.id, text='''     Последовательности – ещё одно понятие из математики. Там, последовательность – есть нумерованный набор элементов, в котором возможны их повторения, а порядок имеет значение. Определение Питона схоже с математическим: здесь последовательностью зовётся упорядоченная коллекция объектов.
    <b>Строка (String) str</b> в Python – <u>это последовательность символов, заключенная в кавычки, неизменяемый упорядоченный тип данных</u> (после создания строки её больше нельзя изменять).
    <a href="https://pythonchik.ru/osnovy/python-stroki">Больше информации по строкам в Python</a>''',
                             reply_markup=backkeyboard, parse_mode='HTML')
            img = open('string_methods 01.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
            img_2 = open('string_methods 02.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_2, reply_markup=closekeyboard)
            img_2.close()
        elif call.data == "30":
            bot.send_message(call.message.chat.id, text='''     <b>Списки list</b> в Python - <u>упорядоченные изменяемые коллекции объектов произвольных типов</u> (числовые, буквенные, а также списки) (почти как массив, но типы могут отличаться).
        <code>list = [1, ‘Hello’, ‘World’]</code> 
    Вложенные списки (список списков) выглядит следующим образом: <pre>а = [1, 2, 3, 4, [‘Hello’, ‘World’, 1.2], 5]</pre>        
    Для обращения к элементу вложенного списка нужно использовать два индекса: первый указывает на индекс главного списка, второй — индекс элемента во вложенном списке.
        <pre>print(a[4][1])</pre>    
    <a href="https://pythonchik.ru/osnovy/spiski-v-python">Больше информации по спискам в Python</a>''',
                             reply_markup=backkeyboard, parse_mode='HTML')
            img = open('list.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "31":
            bot.send_message(call.message.chat.id, text='''     <b>Словари dict</b> в Python - это <u>встроенный изменяемый тип данных с неупорядоченной структурой</u> (коллекцией произвольных данных) <u>(является ассоциативным массивом или хешем) и базируется на отображении пар (ключ:значение)</u>, с доступом по ключу.
    У элементов словаря нет индексов. Словарь – это некий аналог адресной книги, в которой можно найти адрес или контактную информацию о человеке, зная лишь его имя; т.е. некоторые ключи (имена) связаны со значениями (информацией).
    <b>Ключ</b> – это <u>уникальный элемент</u>, его можно сравнить с идентификационным номером. Значения словаря могут быть одинаковыми, но ключи разные. <u>В качестве ключей могут использоваться только неизменяемые объекты</u> (числа, строки, кортежи, frozenset), а <u>в качестве значений можно использовать как неизменяемые, так и изменяемые объекты.</u> Точнее говоря, в качестве ключей должны использоваться только простые объекты.
    Конструкцию словаря можно представить в виде списков кортежей, состоящих из двух элементов. Пары ключ-значение указываются в словаре следующим образом: 
        <code>d = {key1:value1, key2:value2}</code>
    <u>Пары ключ-значение в словаре не упорядочены.</u> Если необходим некоторый порядок, то придётся отдельно отсортировать словарь перед обращением к нему.
    Словари являются экземплярами/объектами класса dict.    
    <a href="https://pythonchik.ru/osnovy/slovari-v-python">Подробнее о словарях в Python</a>''',
                             reply_markup=backkeyboard, parse_mode='HTML')
            img = open('dict.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "32":
            bot.send_message(call.message.chat.id, text='''     <b>Кортежи tuple</b> в Python - это те же списки за одним исключением – <u>кортежи неизменяемые структуры данных</u> и без такой обширной функциональности, которую предоставляет класс списка. Кортеж <u>является упорядоченной последовательностью</u>. Так же как списки они <u>могут состоять из элементов разных типов, перечисленных через запятую</u>, по желанию их можно ещё заключить <u>в круглые скобки</u>.
        <code>a = (1, 2, 3, ‘hello’, ‘world’)</code> 
    Пустой кортеж – <code>myempty = ()</code> 
    Кортеж из одного элемента – <code>singleton = (2,)</code>
    Кортежи служат для хранения нескольких объектов вместе. В связи с тем, что они неизменяемы, так же, как и строки, то модифицировать кортежи невозможно. Кортежи обычно используются в тех случаях, когда оператор или пользовательская функция должны наверняка знать, что набор значений, т.е. кортеж значений, не изменится.
        <code>a = (1, 2, 3, 4)</code> и <code>b = (1, 2, (6, 7, 8))</code> 
        <code>print(len(a))</code>       Результат: 4 
        <code>print(a[2])</code>           Результат: 3
        <code>print(b[4][2])</code>     Результат: 8   
    <a href="https://pythonchik.ru/osnovy/kortezhi-v-python">Более подробная информация по кортежам в Python</a>''',
                             reply_markup=backkeyboard, parse_mode='HTML')
            img = open('tuple.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "33":
            bot.send_message(call.message.chat.id, text='''     <b>Множества set</b> в Python - это <u>структура данных, которые содержат неупорядоченные элементы. Элементы также не являются индексированными.</u> Как и список, множество позволяет внесение и удаление элементов.
    Однако, есть ряд особенных характеристик, которые определяют и отделяют множество от других структур данных:
    1. Множество не содержит дубликаты элементов;
    2. Элементы множества являются неизменными (их нельзя менять), однако само по себе множество является изменяемым, и его можно менять;
    3. Так как элементы не индексируются, множества не поддерживают никаких операций среза и индексирования.
    С множествами можно выполнять множество операций: находить объединение, пересечение, отнимать друг у друга...
    Множество может содержать любое количество элементов, и элементы могут быть разных типов, к примеру, целые числа, строки, кортежи и т. д. Однако, множество не поддерживает изменяемые элементы, такие как списки, словари, и так далее.
        <code>a={1, 2, 3, 4, 5}</code> 
        <code>b=set(['hello','world','Python'])</code>
        <code>print(a)</code>   Результат: <code>{1, 2, 3, 4, 5}</code>
        <code>print(b)</code>   Результат: <code>{'Python', 'hello', 'world'}</code>
        Пустое множество – <code>empty_set = set()</code> 
        <code>print(empty_set)</code>   Результат: <code>set()</code>
    <b>Frozenset</b> - единственное отличие set от frozenset заключается в том, что <u>set - изменяемый тип данных, а frozenset – нет</u>.          
        <code>my_type=frozenset(['hello','world','Python'])</code>  
        <code>print(my_type)</code>       
        Результат: <code>frozenset({'world', 'Python', 'hello'})</code>           
    <a href="https://pythonchik.ru/osnovy/mnozhestva-v-python">Подробней о множествах в Python</a>''',
                             reply_markup=backkeyboard, parse_mode='HTML')
            img = open('set.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "34":
            bot.send_message(call.message.chat.id, text='''     <b>Файл</b> - это всего лишь <u>набор данных, сохраненный в виде последовательности битов на компьютере. Информация хранится в куче данных (структура данных) и имеет название «имя файла» (filename).</u>
    В Python существует два типа файлов:
    1. <u>Текстовые</u> – это файлы с человекочитаемым содержимым. В них хранятся последовательности символов, которые понимает человек. Блокнот и другие стандартные редакторы умеют читать и редактировать этот тип файлов. Текст может храниться в двух форматах: (.txt) — простой текст и (.rtf) — «формат обогащенного текста».
    2. <u>Бинарные</u> - в бинарных файлах данные отображаются в закодированной форме (с использованием только нулей (0) и единиц (1) вместо простых символов). В большинстве случаев это просто последовательности битов. Они хранятся в формате .bin.
    Любую операцию с файлом можно разбить на три крупных этапа:
    1. Открытие файла
    2. Выполнение операции (запись, чтение)
    3. Закрытие файла
        <code>f = open('poem.txt', 'w')</code> # открываем для записи (writing)
        <code>f.write(poem)</code> # записываем текст в файл
        <code>f.close()</code> # закрываем файл
        <code>f = open('poem.txt')</code> # если не указан режим, по умолчанию подразумевается # режим чтения ('r'eading)
        <code>while True:</code>
            <code>line = f.readline()</code>
            <code>if len(line) == 0:</code> # Нулевая длина обозначает конец файла (EOF)
                <code>break</code>
            <code>print(line, end='')</code>
        <code>f.close()</code> # закрываем файл 
    <a href="https://docs.python.org/3/library/functions.html#open">Больше о режимах открытия можно почитать здесь</a>(Встроенные функции)''',
                             reply_markup=backkeyboard, parse_mode='HTML')
            img = open('file 1.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
            img_2 = open('file 2.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_2, reply_markup=closekeyboard)
            img_2.close()
        elif call.data == "35":
            img = open('range object.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "36":
            img = open('none.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == "43":
            img = open('work with types.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == '37':
            bot.delete_message(call.message.chat.id, call.message.message_id)

        if call.data == '4':
            bot.send_message(call.message.chat.id, text='''     <b>Функция function</b> - это многократно используемый <u>фрагмент программы, блок кода, который начинается</u> с определения функции зарезервированным ключевым <u>словом def, названия функции, пары скобок,</u> в которых можно указать имена некоторых переменных, <u>и двоеточия</u> в конце строки. <u>Далее следует блок команд,</u> составляющих функцию.
        <code>def tel_1():</code>
            <code>print('Hello World')</code>
        <code>tel_1()</code> 
    Результат: <code>Hello World</code>
        <code>def tel_2():</code> # пустая функция 
            <code>pass</code>    
        <code>tel_2()</code>
    Функция – это, пожалуй, наиболее важный строительный блок любой нетривиальной программы (на любом языке программирования).
    Есть <a href="https://pythonchik.ru/osnovy/vstroennye-funkcii-python">встроенные функции</a>, такие как len, <a href="https://pythonchik.ru/osnovy/python-range">range</a>, и функции структуры которых вы определяете сами. Вам нужно решить, будут ли в них аргументы, или нет. Вы можете добавить как аргументы ключевых слов, так и готовые по умолчанию.
    Функции позволяют дать имя определённому блоку команд с тем, чтобы впоследствии запускать этот блок по указанному имени в любом месте программы и сколь угодно много раз. Это называется вызовом функции. 
    Более подробно с функциями можно ознакомится на:
    <b>pythonchik.ru</b>  <a href="https://pythonchik.ru/osnovy/funkcii-v-python">Функции в Python</a>
    <b>docs-python.ru</b>  <a href="https://docs-python.ru/tutorial/2/">Справочник по языку Python3</a>
    <b>pythonru.com</b>  <a href="https://pythonru.com/osnovy/funkcii-v-python">Функции в Python</a> и <a href="https://pythonru.com/osnovy/funkcii-v-python-2">Функции в Python 2</a>
    <b>bestprog.net</b>  <a href="https://www.bestprog.net/ru/sitemap_ru/python-ru/">Python</a>''',
                             reply_markup=backkeyboard, parse_mode='HTML')
            img = open('func 1.jpg','rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
            img_2 = open('func 2.jpg','rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img_2, reply_markup=closekeyboard)
            img_2.close()

        if call.data == '5':
            bot.send_message(call.message.chat.id, text='''Более подробно c ООП можно ознакомиться на сайтах:
    https://smartiqa.ru/courses/python/lesson-6
    https://thecode.media/attrb-mthd/
    https://www.bestprog.net/ru/sitemap_ru/python-ru/
    https://codechick.io/tutorials/python/python-what-is-oop
    https://pythonworld.ru/osnovy/obektno-orientirovannoe-programmirovanie-obshhee-predstavlenie.html
    https://pythonchik.ru/osnovy/osnovy-oop-v-python-klassy-obekty-metody
    https://metanit.com/python/tutorial/7.1.php''',
                                 reply_markup=oop_btn, parse_mode='HTML')
        elif call.data == "44":
            img = open('oop 1.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
            bot.send_message(call.message.chat.id, text='''     <b>Объектно-ориентированное программирование (ООП)</b> – <u>парадигма программирования, в которой основными концепциями являются понятия объектов и классов</u>. В Пайтоне всё является объектами, а каждый объект имеет метод и значение по той причине, что все объекты базируются на классе. <u>Класс – это проект объекта, описывающий его устройство. Объект — это экземпляр класса</u>.
    Программа является набором взаимодействующих объектов, посылающих друг другу сообщения. Каждый объект имеет тип и собственную часть памяти и может иметь в составе другие объекты. Объекты одного типа могут принимать одни и те же сообщения (и выполнять одни и те же действия).
    Синтаксис для создания класса выглядит следующим образом. И в качестве примера создадим объект класса Car:
        <code>class Car():</code>
            <code>pass</code>
        <code>car_object=Car()</code>''',reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == "45":
            img = open('oop 2.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
            bot.send_message(call.message.chat.id, text='''     <b>Статические и динамические атрибуты класса.</b>
    Класс может содержать атрибуты и методы. Атрибут может быть статическим и динамическим (уровня объекта класса). Суть в том, что для работы со статическим атрибутом, вам не нужно создавать экземпляр класса, а для работы с динамическим – нужно.
    <code>class Rectangle:</code>
        <code>default_color = "green"</code>
        <code>def __init__(self, width, height):</code>
            <code>self.width = width</code>
            <code>self.height = height</code>
    В представленном выше классе, атрибут default_color – это статический атрибут, и доступ к нему, как было сказано выше, можно получить не создавая объект класса Rectangle
    >>> Rectangle.default_color - 'green'
    width и height – это динамические атрибуты, при их создании было использовано ключевое слово self. Для доступа к width и height предварительно нужно создать объект класса Rectangle:
    >>> rect = Rectangle(10, 20)
    >>> rect.width - '10'
    >>> rect.height - '20' ''',reply_markup=closekeyboard, parse_mode='HTML')
            bot.send_message(call.message.chat.id, text='''     <b>Свойства класса</b>
    <code>class Class1(object):</code>
        <code>def __init__(self, value):</code>
            <code>self.__var = value</code>
        <code>def getVar(self):</code> # Чтение
            <code>return self.__var</code>
        <code>def setVar(self, value):</code> # Запись
            <code>self.__var = value</code>
        <code>def delVar(self):</code> # Удаление
            <code>del self.__var</code>
        <code>v = property(getVar, setVar, delVar, "Строка документирования")</code>
    <code>c1 = Class1(5)</code>
    <code>c1.v = 35</code> # Вызывается метод setVar()
    <code>print(c1.v)</code> # Вызывается метод getVar()
    <code>del c1.v</code> # Вызывается метод delVar()
    В Python 2.6 были добавлены методы <b>getter()</b>, <b>setter()</b> и <b>deleter()</b>, позволяющие создавать свойства классов с помощью декораторов функций.
    <code>class Class1(object):</code> # Работает, начиная с версии Python 2.6
        <code>def __init__(self, value):</code>
            <code>self.__var = value</code>
        <code>@property</code>
        <code>def v(self):</code> # Чтение
            <code>return self.__var</code>
        <code>@v.setter</code>
        <code>def v(self, value):</code> # Запись
            <code>self.__var = value</code>
        <code>@v.deleter</code>
        <code>def v(self):</code> # Удаление
            <code>del self.__var</code>
    <code>c1 = Class1(5)</code>
    <code>c1.v = 35</code> # Запись
    <code>print(c1.v)</code> # Чтение
    <code>del c1.v</code> # Удаление''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            bot.send_message(call.message.chat.id, text='''     <b>Метод</b> – это функция, находящаяся внутри класса и выполняющая определенную работу.
    Методы бывают статическими, классовыми (среднее между статическими и обычными) и уровня класса (будем их называть просто словом метод).
    @staticmethod — используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван. Он просто получает переданные аргументы, без неявного первого аргумента, и его определение неизменяемо через наследование. Проще говоря, @staticmethod — это вроде обычной функции, определенной внутри класса, которая не имеет доступа к экземпляру, поэтому ее можно вызывать без создания экземпляра класса.
    @classmethod — это метод, который получает класс в качестве неявного первого аргумента, точно так же, как обычный метод экземпляра получает экземпляр. Это означает, что вы можете использовать класс и его свойства внутри этого метода, а не конкретного экземпляра. Проще говоря, @classmethod — это обычный метод класса, имеющий доступ ко всем атрибутам класса, через который он был вызван. Следовательно, classmethod — это метод, который привязан к классу, а не к экземпляру класса.
    Статический метод создается с декоратором @staticmethod, классовый – с декоратором @classmethod, первым аргументом в него передается cls, обычный метод создается без специального декоратора, ему первым аргументом передается self:
    <code>class MyClass:</code>
        <code>@staticmethod</code>
        <code>def ex_static_method():</code>
            <code>print("static method")</code>
        <code>@classmethod</code>
        <code>def ex_class_method(cls):</code>
            <code>print("class method")</code>
        <code>def ex_method(self):</code>
            <code>print("method")</code>
    Статический и классовый метод можно вызвать, не создавая экземпляр класса, для вызова ex_method() нужен объект:
    <code>MyClass.ex_static_method()</code>
    Результат: <code>‘static method’</code>
    <code>MyClass.ex_class_method()</code>
    Результат: <code>‘class method’</code>
    <code>m = MyClass()</code>
    <code>m.ex_method()</code>
    Результат: <code>‘method’</code>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == "46":
            img = open('oop_paradigms.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
            bot.send_message(call.message.chat.id, text='''     <b>Наследование.</b> В организации наследования участвуют как минимум два класса: класс родитель и класс потомок. 
        <code>Class Car:</code>
            <code>pass</code>
        <code>Class Small_car(Car):</code>
            <code>pass</code>
    По умолчанию все классы в Python являются наследниками от object.
    При этом возможно множественное наследование, в этом случае у класса потомка может быть несколько родителей. Синтаксически создание класса с указанием его родителя выглядит так: class имя_класса (имя_родителя1, [имя_родителя2,…, имя_родителя_n])''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            bot.send_message(call.message.chat.id, text='''     <b>Полиморфизм</b>, как правило, используется с позиции переопределения методов базового класса в классе наследнике. Это дает возможность использовать перегруженный метод в случаях, когда мы еще не знаем, для какого именно класса он будет вызван. Мы просто указываем имя метода, а объект класса, к которому он будет применен, определится по ходу выполнения программы. Также к полиморфизму относится свойство метода вести себя по-разному, в зависимости от количества или типа параметров.''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            bot.send_message(call.message.chat.id, text='''     <b>Инкапсуляция</b> — ограничение доступа к составляющим объект компонентам (методам и переменным). Инкапсуляция делает некоторые из компонентов доступными только внутри класса.
    Инкапсуляция в Python работает лишь на уровне соглашения между программистами о том, какие атрибуты являются общедоступными, а какие — внутренними.
    Одиночное подчеркивание в начале имени атрибута говорит о том, что переменная или метод не предназначен для использования вне методов класса, однако атрибут доступен по этому имени.
        <code>class A:</code> 
            <code>def _private(self):</code> 
                <code>print("Это приватный метод!")</code>
        <code>a = A()</code> 
        <code>a._private()</code> 
        Результат: <code>Это приватный метод!</code>
    Двойное подчеркивание в начале имени атрибута даёт большую защиту: атрибут становится недоступным по этому имени. Однако полностью это не защищает, так как атрибут всё равно остаётся доступным под именем _ИмяКласса__ИмяАтрибута:
        <code>class B:</code>
            <code>def __private(self):</code>
                <code>print("Это приватный метод!")</code>
        <code>b = B()</code>
        <code>b._B__private()</code>
        Результат: <code>Это приватный метод!</code>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == "47":
            bot.send_message(call.message.chat.id, text=''' Желающим поразмышлять:
    <u>Инкапсуляции в Питоне – НЕТ!</u> Она работает лишь на уровне соглашения между программистами. – с этим понятно.
    Вот с чем вопрос: <u><b>«магические методы перегружаем, а свои методы мы переопределяем»</b></u>!?.
    “<a href="https://docs-python.ru/tutorial/klassy-jazyke-python/peregruzka-metodov/">Python является динамически типизированным языком и следовательно, перегрузка методов здесь невозможна</a>, тем не менее, есть простой способ реализовать такое поведение в Python. … Это очень хрупкое решение, которое закрыто для расширения кода, а некоторые программисты называют его "костылем" или анти-паттерном.”
    (Из этой же статьи: “Для перегрузки методов требуется, чтобы язык программирования мог различать типы во время компиляции.” А Python интерпретируемый язык! Или нет?  “<a href="https://pylab.ru/znakomtes-python/">Несмотря на то, что во многих отношениях Python работает как интерпретируемый, его код перед выполнением компилируется</a>" И “<a href="https://pythobyte.com/is-python-compiled-interpreted-or-both-68582/">Python – это “СКОМПИЛИРОВАННЫЙ ИНТЕРПРЕТИРУЕМЫЙ” язык</a>.”)
    “Заметьте, что <a href="https://habr.com/ru/post/552922/">перегрузка методов (method overloading) — создание методов с одним и тем же именем, но с разными типами аргументов не поддерживается в питоне.</a>”
    “Важно отметить, что <a href="https://otus.ru/journal/polimorfizm-v-pajton/">в «Питоне» не поддерживается такой вариант method overriding, как создание методов с тем же самым именем, однако с различными типами аргументов.</a>”
    Ниже фрагмент видео-лекции Тимофея Хирьянова (Преподаватель кафедры информатики МФТИ, эксперт ЕГЭ. Работал программистом в компаниях мирового уровня — Parallels и Samsung Electronics. Разработчик системного программного обеспечения для операционной системы Tizen для мобильных платформ. Ассоциативный член фонда свободного программного обеспечения.):''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            img = open('peregryzka.MOV', 'rb') # можно img заменить на video (без разницы) (AVI, ASF, DIVX, FLV, MPEG, MPG, MKV, MOV, MP4, MSS2, WMA, WMV, XVID и другие.)
            bot.send_video(chat_id=call.message.chat.id, video=img, reply_markup=closekeyboard)
            img.close() # можно img заменить на video (нету разницы)
        elif call.data == '48':
            bot.delete_message(call.message.chat.id, call.message.message_id)

        if call.data == '6':
            img = open('bd.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
            bot.send_message(call.message.chat.id, text='''     <a href="https://github.com/vinta/awesome-python#database"><b>База данных (БД)</b></a> - это организованная структура, предназначенная для хранения информации. Обычно БД представляются в виде совокупности взаимосвязанных файлов или таблиц, предназначенных для решения конкретной задачи.
    С понятием БД тесно связано понятие системы управления базой данных (СУБД). СУБД — это комплекс программных средств, предназначенных для создания структуры новой базы, наполнения ее содержимым, редактирования содержимого и визуализации информации. СУБД освобождает разработчика от задач хранения, модификации и поиска данных. Его дело — указать, какие данные взять, и что с ними сделать. Все остальное сделает сама СУБД.
    Основным элементом БД является таблица. Столбцы таблицы БД называются полями, а строки — записями. Первым этапом создания таблицы БД является задание ее структуры, т.е. определение количества и типа полей. Вторым этапом является ввод и редактирование записей в таблицу. БД считается созданной, даже если она пустая. Поля таблицы просто определяют ее структуру и групповые свойства данных, записываемых в ячейках. 
    Основные свойства полей БД:
    • Имя поля — определяет как надо обращаться к данным поля (имена используются как заголовки таблиц);
    • Тип поля — определяет тип данных, которые могут содержаться в данном поле (текстовые, числовые, дата, Memo, денежный, счетчик и др.);
    • Размер поля — определяет предельную длину данных, которые могут размещаться в поле;
    • Формат поля — способ.''',
                             reply_markup=bd_btn, parse_mode='HTML')
        elif call.data == '49':
            bot.send_message(call.message.chat.id, text='''     Реляционные (табличные) базы данных характеризуются наличием некоторых типов таблиц и ключей, позволяющих определить отношения между таблицами.
    <b>Типы таблиц и ключей в реляционных базах данных:</b> 
    • Базовая таблица. В реляционной базе данных базовой таблицей называется таблица, которая включает один или несколько столбцов свойств объекта и содержит первичный ключ, который однозначно определяет этот объект. Более того, базовая таблица должна содержать первичный ключ. Базовые таблицы часто называют первичными, поскольку они имеют первичный ключ.
    • Промежуточная таблица. Таблица, не являющаяся базовой (т. к. она не объединяет свойства объекта или не содержит поле первичного ключа), которая используется для обеспечения связей между другими таблицами, называется таблицей отношений. Ключевые поля в таблицах отношений должны быть внешними ключами, связанными с первичными ключами базовой таблицы. Проще говоря, таблица отношений состоит только из внешних ключей и не содержит независимых элементов данных.
    • Первичный ключ. Первичный ключ состоит из набора значений, которые однозначно определяют запись базовой таблицы. Любому значению первичного ключа должна соответствовать одна и только одна строка таблицы. Первичный ключ включает одно поле только в том случае, если это поле не содержит повторяющихся значений.
    • Составные ключи. Если для выполнения условий, накладываемых на значения первичного ключа, заданный ключ включает несколько полей таблицы, то тогда он называется составным.
    • Внешние ключи. Внешний ключ — это столбец, значения которого соответствуют значениям первичного ключа другой связанной таблицы.''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '50':
            bot.send_message(call.message.chat.id, text='''<a href="https://blog.skillfactory.ru/glossary/sql/">SQL</a>
    Устав от написания бесконечных процедур поиска, вставки, удаления, замены, программисты переложили эту обязанность на саму СУБД. Для этого они создали язык структурированных запросов (<a href="https://tproger.ru/translations/sql-recap/">SQL</a>). Вместо тысячи строк кода пишется одна строка, которая сделает ровно то, о чем ее просили. Все изменения в базе данных выполняются одинаково, что позволяет при правильном администрировании легко и быстро восстановить исходное состояние при сбоях и ошибках.
    <a href="https://github.com/planetopendata/awesome-sqlite">SQLite</a> – это не столько СУБД, сколько библиотека, которая позволяет хранить данные в файле, обращаясь к нему как к базе данных с помощью SQL. Там тоже можно создавать таблицы и индексы, выполнять DML и запросы. Удобно в случае, если не хочется возиться с XML или создавать свой формат файла. Ныне имеется практически в каждом телефоне, хотя далеко не всякий разработчик знает, что это именно SQLite прячется за привычными вызовами Android-API.''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            img = open('dt_SQL.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
        elif call.data == '51':
            bot.send_message(call.message.chat.id, text='''     В Реляционных БД данные хранятся в виде таблиц и строк. Используется язык SQL (структурированных запросов) для обработки структурированных данных. Связь в такой табличной структуре происходит через ключи (или индексы), которые используются для уникальной идентификации. Для работы с данными необходимо сначала разместить эти данные внутри таблицы и описать. SQL масштабируется по вертикале (увеличение нагрузки на один сервер).
    Нереляционные БД размещают информацию в коллекциях документов JSON. Обеспечивают высокий уровень безопасности (такие БД сложнее взломать) и возможность обойти аппаратные ограничения (с помощью Sharding) (не надо создавать таблиц и размещать данные). Используется язык NoSQL - динамические схемы для неструктурированных данных позволяет: ориентировать информацию на столбцы или документу; основывать её на графике; организовывать в виде хранилища KeyValue; создавать документы без предварительного определения их структуры, использовать разный синтаксис; добавлять поля в процессе работы. NoSQL - основан на документах, парах ключ-значение, графовых БД, хранилищах с широкими столбцами. Масштабируется по горизонтали (разделение или добавление большого количества серверов) - удобно для работы с большим или меняющимися набором данных.
    В зависимости от конкретных задач проекта и типа данных происходит выбор того или иного приложения:
    • Если в БД есть предопределенная схема — используем SQL, если схема динамическая — NoSQL.
    • Выбираем приоритетное направление масштабирования — по горизонтали или по вертикали.
    • Определяем, что будет использоваться в задаче — неструктурированные данные или многострочные транзакции.
    SQL подойдет, если нужна обработка большого количества сложных запросов, или рутинного анализа данных. Лучше выбрать реляционную БД, если нужна надежная обработка транзакций и ссылочная целостность.
    Если объем данных большой, лучше использовать NoSQL. Отсутствие явных структурированных механизмов ускорит процесс обработки Big Data. Также если: необходимо хранить массивы в объектах JSON; записи хранятся в коллекции с разными полями или атрибутами; необходимо горизонтальное масштабирование.        
    В некоторых случаях необходимо обработать оба типа БД — тогда рекомендуется выбирать гибридное решение, например, PostgreSQL (объектно-ориентированная СУБД).''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '52':
            bot.send_message(call.message.chat.id, text='''     3 наиболее популярных Реляционных Систем Управления Базами Данных:
    • SQLite: очень мощная встраиваемая РСУБД.
    • MySQL: самая популярная и часто используемая РСУБД.
    • PostgreSQL: самая продвинутая и гибкая РСУБД.
    Ознакомиться с их сравнением можно на:
    <a href="https://tproger.ru/translations/sqlite-mysql-postgresql-comparison/">SQLite, MySQL и PostgreSQL: сравниваем популярные реляционные СУБД</a>
    <a href="https://russianblogs.com/article/4887448911/">SQLite, MySQL и PostgreSQL: сравнение реляционных баз данных</a>
    <a href="https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27">Как подружить Python и базы данных SQL. Подробное руководство</a>''',
                             reply_markup=bd2_btn, parse_mode='HTML')
        elif call.data == '54':
            img = open('SQLite.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, reply_markup=closekeyboard)
            img.close()
            bot.send_message(call.message.chat.id, text='''     <b>Структура sql-запросовости</b> Общая структура запроса выглядит следующим образом:
    • SELECT ('столбцы или * для выбора всех столбцов; обязательно')
    • FROM ('таблица; обязательно')
    • WHERE ('условие/фильтрация, например, city = 'Minsk'; необязательно')
    • GROUP BY ('столбец, по которому хотим сгруппировать данные; необязательно')
    • HAVING ('условие/фильтрация на уровне сгруппированных данных; необязательно')
    • ORDER BY ('столбец, по которому хотим отсортировать вывод; необязательно')
    подробнее ниже
    \n <b>CREATE TABLE</b> Для того, чтобы создать таблицу в SQL, используется выражение CREATE TABLE. Он принимает в качестве параметров все колонки, которые мы хотим внести, а также их типы данных. Cоздадим табличку с названием "Months", в которой будет три колонки:
    • id иными словами, порядковый номер месяца (целочисленный тип или int)
    • name название месяца (строка или varchar(10) (10 символов максимальная длина строки))
    • days число дней в конкретном месяце (целочисленный тип или int)
    <code>CREATE TABLE months (id int, name varchar(10), days int);</code>
    Также, когда создаются таблицы, принято добавлять так называемый primary key. Это колонка, значения в которой уникальны. Чаще всего primary key колонкой является id, но в нашем случае это может быть и name, так как имена всех месяцев уникальны.
    \n <b>INSERT</b> Ввод данных, добавим пару месяцев в нашу табличку. Сделать это можно с помощью команды INSERT. Есть два разных способа использовать INSERT:
    Первый способ не подразумевает указания названий колонок, а лишь принимает значения в том порядке, в котором они указаны в таблице.
    <code>INSERT INTO months VALUES (1,'January',31);</code>
    Первый способ короче второго, однако если в будущем мы захотим добавить дополнительные колонки, все предыдущие запросы работать не будут. Для решения данной проблемы следует использовать второй способ. Его суть в том, что перед вводом данных мы указываем названия колонок.
    <code>INSERT INTO months (id,name,days) VALUES (2,'February',29);</code>
    В случае, если мы не укажем одну из колонок, на её место будет записано NULL или заданное значение по умолчанию, но это уже совсем другая история.
    \n <b>UPDATE</b> Зачастую нам нужно изменить данные в таблице. В SQL это делается с помощью UPDATE. Использование UPDATE включает в себя:
    • выбор таблицы, в которой находится поле, которое мы хотим изменить
    • запись нового значения
    • использование WHERE, чтобы обозначить конкретное место в таблице
    \n <b>DELETE</b> <u>Удаление записи из таблицы</u> через SQL - очень простая операция. Всё, что нужно - это обозначить, что именно мы хотим удалить:
    <code>DELETE FROM tv_series WHERE id = 4;</code>
    Примечание: убедитесь, что используете WHERE, когда удаляете запись из таблицы. Иначе вы удалите все записи из таблицы, сами того не желая.
    <b>TRUNCATE</b> <u>Удаление таблиц.</u> Если мы хотим удалить все данные из таблицы, но при этом оставить саму таблицу, нам следует использовать команду TRUNCATE:
    <code>TRUNCATE TABLE table_name;</code>
    <b>DROP</b> В случае, если мы хотим <u>удалить саму таблицу</u>, то нам следует использовать команду DROP.''',
                             reply_markup=bd3_btn, parse_mode='HTML')
        elif call.data == '58':
            bot.send_message(call.message.chat.id, text='''     <b>SELECT, FROM</b> — обязательные элементы запроса, которые определяют выбранные столбцы, их порядок и источник данных.
    <code>SELECT * FROM characters</code>
    Результатом данного запроса будет таблица со всеми данными в таблице characters. Знак звёздочки (*) означает то, что мы хотим показать все столбцы из таблицы без исключений. Так как в базе данных обычно больше одной таблицы, нам необходимо указывать название таблицы, данные из которой мы хотим посмотреть. Сделать это мы можем, используя ключевое слово FROM.
    Когда вам нужны лишь некоторые столбцы из таблицы, то вы можете указать их имена через запятую вместо звёздочки.
    <code>SELECT name, weapon FROM characters</code>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '59':
            bot.send_message(call.message.chat.id, text='''     <b>WHERE</b> — необязательный элемент запроса, который используется, когда нужно отфильтровать данные по нужному условию. Очень часто внутри элемента where используются IN / NOT IN для фильтрации столбца по нескольким значениям, AND / OR для фильтрации таблицы по нескольким столбцам.
    • IN - сравнивает значение в столбце с несколькими возможными значениями и возвращает true, если значение совпадает хотя бы с одним значением
    • BETWEEN - проверяет, находится ли значение в каком-то промежутке
    • LIKE - ищет по шаблону
    Фильтрация по одному условию и одному значению:
    <code>select * from Customers WHERE City = 'London'</code>
    Фильтрация по одному условию и нескольким значениям с применением IN (включение) или NOT IN (исключение):
    <code>select * from Customers where City IN ('London', 'Berlin')</code>
    <code>select * from Customers where City NOT IN ('Madrid', 'Berlin','Bern')</code>
    Фильтрация по нескольким условиям с применением AND (выполняются все условия) или OR (выполняется хотя бы одно условие) и нескольким значениям:
    <code>select * from Customers where Country = 'Germany' AND City not in ('Berlin', 'Aachen') AND CustomerID > 15</code>
    <code>select * from Customers where City in ('London', 'Berlin') OR CustomerID > 4</code>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '60':
            bot.send_message(call.message.chat.id, text='''     <b>GROUP BY</b> — необязательный элемент запроса, с помощью которого можно задать агрегацию по нужному столбцу (например, если нужно узнать какое количество клиентов живет в каждом из городов). При использовании GROUP BY обязательно:
    • Перечень столбцов, по которым делается разрез, был одинаковым внутри SELECT и внутри GROUP BY
    • Агрегатные функции (SUM, AVG, COUNT, MAX, MIN) должны быть также указаны внутри SELECT с указанием столбца, к которому такая функция применяется.
    В SQL полно <a href="https://docs.microsoft.com/ru-ru/azure/databricks/sql/language-manual/sql-ref-functions-builtin">встроенных функций</a> для выполнения разных операций. Наиболее часто используемые:
    • COUNT() - возвращает число строк
    • SUM() - возвращает сумму всех полей с числовыми значениями в них
    • AVG() - возвращает среднее значение среди строк
    • MIN() / MAX() - возвращает минимальное/максимальное значение среди строк
    Группировка количества клиентов по городу: 
    <code>select City, count(CustomerID) from Customers GROUP BY City</code>
    Группировка количества клиентов по стране и городу: 
    <code>select Country, City, count(CustomerID) from Customers GROUP BY Country, City</code>
    Группировка продаж по ID товара с разными агрегатными функциями: количество заказов с данным товаром и количество проданных штук товара:
    <code>select ProductID, COUNT(OrderID), SUM(Quantity) from OrderDetails GROUP BY ProductID</code>
    Группировка продаж с фильтрацией исходной таблицы. В данном случае на выходе будет таблица с количеством клиентов по городам Германии:
    <code>select City, count(CustomerID) from Customers WHERE Country = 'Germany' GROUP BY City</code>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '61':
            bot.send_message(call.message.chat.id, text='''     <b>HAVING</b> — необязательный элемент запроса, который отвечает за фильтрацию на уровне сгруппированных данных (по сути, WHERE, но только на уровень выше). 
    Фильтрация агрегированной таблицы с количеством клиентов по городам, в данном случае оставляем в выгрузке только те города, в которых не менее 5 клиентов:
    <code>select City, count(CustomerID) from Customers group by City HAVING count(CustomerID) >= 5</code>
    В случае с переименованным столбцом внутри HAVING можно указать как и саму агрегирующую конструкцию count(CustomerID), так и новое название столбца number_of_clients:
    <code>select City, count(CustomerID) as number_of_clients from Customers group by City HAVING number_of_clients >= 5</code>
    Пример запроса, содержащего WHERE и HAVING. В данном запросе сначала фильтруется исходная таблица по пользователям, рассчитывается количество клиентов по городам и остаются только те города, где количество клиентов не менее 5:
    <code>select City, count(CustomerID) as number_of_clients from Customers WHERE CustomerName not in ('Around the Horn','Drachenblut Delikatessend') group by City HAVING number_of_clients >= 5</code>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '62':
            bot.send_message(call.message.chat.id, text='''     <b>ORDER BY</b> — необязательный элемент запроса, который отвечает за сортировку таблицы. Простой пример сортировки по одному столбцу. В данном запросе осуществляется сортировка по городу, который указал клиент: 
    <code>select * from Customers ORDER BY City</code>
    Осуществлять сортировку можно и по нескольким столбцам, в этом случае сортировка происходит по порядку указанных столбцов:
    <code>select * from Customers ORDER BY Country, City</code>
    По умолчанию сортировка происходит по возрастанию для чисел и в алфавитном порядке для текстовых значений. Если нужна обратная сортировка, то в конструкции ORDER BY после названия столбца надо добавить DESC.
    Обратная сортировка по одному столбцу и сортировка по умолчанию по второму:
    <code>select * from Customers order by Country DESC, City JOIN</code>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '63':
            bot.send_message(call.message.chat.id, text='''     <b>JOIN</b> — необязательный элемент, используется для объединения таблиц по ключу, который присутствует в обеих таблицах. Перед ключом ставится оператор ON.
    Запрос, в котором соединяем таблицы Order и Customer по ключу CustomerID, при этом перед названиям столбца ключа добавляется название таблицы через точку:
    <code>select * from Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID</code>
    Нередко может возникать ситуация, когда надо промэппить одну таблицу значениями из другой. В зависимости от задачи, могут использоваться разные типы присоединений. INNER JOIN — пересечение, RIGHT/LEFT JOIN для мэппинга одной таблицы значениями из другой:
    <code>select * from Orders join Customers on Orders.CustomerID = Customers.CustomerID where Customers.CustomerID >10</code>
    Внутри всего запроса JOIN встраивается после элемента from до элемента where
    Другие типы JOIN'ов можно увидеть на картинке ниже:''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            img = open('sql joins.jpg','rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img,reply_markup=closekeyboard)
            img.close()
            bot.send_message(call.message.chat.id, text='''     В сложных базах данных чаще всего у нас есть несколько связанных таблиц. К примеру, у нас есть две таблицы: про видеоигры и про разработчиков. В таблице video_games есть столбец developer_id, в данном случае он является так называемым foreign_key. Чтобы было проще понять, developer_id - это связывающее звено между двумя таблицами. Если мы хотим вывести всю информацию об игре, включая информацию о её разработчике, нам необходимо подключить вторую таблицу. Чтобы это сделать, можно использовать INNER JOIN:
    <code>SELECT video_games.name, video_games.genre, game_developers.name, game_developers.country FROM video_games INNER JOIN game_developers ON video_games.developer_id = game_developers.id;</code>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '64':
            bot.send_message(call.message.chat.id, text='''     <b>Разница между Drop, Truncate и Delete.</b>
    <u>Delete</u> «удаление данных в таблице» - это команда DML (язык манипулирования данных) - требует фиксации, производит запись в журнале транзакции каждой удалённой строки. Поэтому медленней, требует больше ресурсов системы. Не сбрасывает идентификатор автоинкремента таблицы и счётчик, запускает триггеры при удалении. Операция может быть отменена, а результат можно откатить. Можно применять к таблицам и таблицам внутри кластера. (С Where удаляет конкретные строки, без - все.)
    Обработка Delete зависит от конфигурации внешних ключей и ограничений (если удаляемая строка, хоть одна из удаляемых, нарушает триггер или ограничение - удаление отменяется).
    Инструкция Delete выполняется с помощью блокировки строк, каждая строка в таблице блокируется для удаления.
    Можно использовать в таблицах участвующих в репликации транзакций или слияний.
    (Может привести к взрыву сегмента журнала, если нужно удалить слишком много данных, а сегмента журнала недостаточно.)
    \n Drop и Truncate - операторы DDL (язык определения данных) - не требует фиксаций, операция вступает в силу немедленно, по этому и отката быть не может.
    <u>Drop</u> - удаляет структуру таблицы из БД. Все строки, индексы, ограничения, триггеры и привилегии таблицы - удаляются безвозвратно. Но функции и хранимые процедуры, которые зависят от таблицы, останутся, но станут недействительными. Триггеры DML не будут запущены.
    <u>Truncate</u> - «усечь» - удаляет все данные в таблице всех строк, освобождая страницы данных, используемые данными таблицами, и записывает только освобождение страницы в журнал транзакции (пространство занимаемое таблицами и индексами, восстанавливается до исходного состояния) (сбрасывает последовательность для типов столбцов идентификаторов, сбрасывает счётчик), но структура таблицы, столбцы, ограничения, индексы - остаются. Триггеры не запускаются и не может быть откат операции (есть нюанс: откат может быть осуществлён, только если усечение заключено в блок транзакций и сеанс не закрыт).
    Операция не может быть осуществлена, если внешний ключ имеет ссылку на данную таблицу. 
    Усечение: делает неиспользуемые индексы снова пригодными для использования; требует исключительной блокировки таблицы; не может быть выдано по ссылке БД;
    Усечённая таблица всегда блокирует таблицу и страницу, а не каждую строку. Truncate не активирует триггеры так как операция не регистрирует отдельные удаления строк
    (Усечение может непреднамеренно нарушить ссылочную целостность и другие ограничения.)''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '55':
            bot.send_message(call.message.chat.id, text='''Всё о MySQL:
        <a href="https://ru.hostings.info/schools/bazy-dannyh.html">Базы данных MySQL</a>    
        <a href="http://shlomi-noach.github.io/awesome-mysql/">круто-mysql</a>
        <a href="https://www.oracle.com/cis/mysql/">Oracle MySQL HeatWave</a>
        <a href="https://www.mysql.com/">Справочное руководство по MySQL 8.0</a>
        <a href="https://dev.mysql.com/doc/refman/8.0/en/">MySQL/Руководство для начинающих</a>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
        elif call.data == '56':
            bot.send_message(call.message.chat.id, text='''Всё о PostgreSQL:
    <a href="https://blog.skillfactory.ru/glossary/postgresql/">PostgreSQL</a>
    <a href="https://habr.com/ru/post/282764/">Чем PostgreSQL лучше других SQL?</a>
    <a href="http://www.sai.msu.su/~megera/postgres/talks/what_is_postgresql.html">Что такое PostgreSQL?</a>
    <a href="https://pythonru-com.turbopages.org/pythonru.com/s/biblioteki/vvedenie-v-postgresql-s-python-psycopg2">Введение в PostgreSQL с Python +Psycopg2</a>   
    <a href="https://github.com/dhamaniasad/awesome-postgres">круто-постгрес</a>
    <a href="https://postgrespro.ru/docs/postgresql/14/index">Документация к PostgreSQL 14.5</a>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            document = open('postgres-A4.pdf','rb')
            bot.send_document(chat_id=call.message.chat.id, document=document,reply_markup=closekeyboard)
            document.close()
        elif call.data == '65':
            bot.delete_message(call.message.chat.id, call.message.message_id)
        elif call.data == '57':
            bot.delete_message(call.message.chat.id, call.message.message_id)
        elif call.data == '53':
            bot.delete_message(call.message.chat.id, call.message.message_id)

        if call.data == '777':
            bot.send_message(call.message.chat.id, text='''     <u>В Python любой файл с кодом называется</u> <b>модулем</b> , который можно повторно использовать в других программах. Принято называть файлы в стиле snake_case: то есть с маленькой буквы и с разделением слов через символ подчеркивания: snake_case переводится как «змеиный регистр».
    Работать с кодом на тысячи строк намного проще, если он разбит на несколько модулей. В таком случае обычно работают с главным файлом, а отдельные функции помещают в разные модули. Затем модули импортируют в main.py с помощью ключевого слова import. В итоге команда разработчиков получает удобный читабельный код, который удобно обслуживать.
    Создадим файл с названием greeting.py. Затем внутри этого файла определим функцию say_hi() и переменную name:
        <i># file: greeting.py</i>
        <code>def say_hi():</code> <i># определяем функцию</i>
           <code>print('Hi!')</code>
        <code>name = 'Bob'</code> <i># определяем переменнную</i>
    Модуль-приветствие готов: он умеет печатать строку Hi! и обрабатывать переменную name. Чтобы воспользоваться нашим модулем, нужно импортировать его в главный модуль main.py.
    Для этого в Python есть три способа:
    • Импорт модуля целиком: используем ключевое слово import вместе с названием файла без расширения .py. Перейдем в главный файл main.py и импортируем туда наш модуль greeting.py:
        <i># file: main.py</i>
        <code>import greeting</code>
    Теперь к содержимому модуля можно обращаться «через точку». Так можно вызвать функцию модуля или отдельную переменную:
        <i># вызываем функцию модуля</i>
        <code>greeting.say_hi()</code>  <i># => Hi!</i>
        # выводим на экран отдельную переменную
        <code>print(greeting.name)</code>  <i># => Bob</i>
    • Импорт отдельных определений из модуля: из длинного и сложного модуля вам нужна всего пара функций или переменных. Нужно написать ключевое слово from с названием модуля без расширения .py. Затем в той же строке указываем ключевое слово import с названием определений, которые хотим использовать. 
        <i># file: main.py</i>
        <code>from greeting import say_hi, name</code> <i># импортируем отдельные компоненты модуля</i>
        <code>print(name)</code>  <i># используем импортированную переменную</i>
        <code>say_hi()</code>     <i># вызываем импортированную функцию</i>
    • Импорт всего содержимого модуля сразу. Если необходимо импортировать весь функционал, то вместо названий отдельных функций и переменных можно использовать символ зводочки * :
        <code>from greeting import  *</code>
    Более подробно о модулях:
    <a href="https://metanit.com/python/tutorial/2.10.php">Определение и подключение модулей</a>
    <a href="http://pythonicway.com/python-modules">Модули в Python</a>
    <a href="https://pythonworld.ru/moduli">Модули</a>
    <a href="https://codechick.io/tutorials/python/modules">Модули в Python</a> и <a href="https://codechick.io/tutorials/python/packages">Пакеты в Python</a>
    <a href="https://younglinux.info/python/modules">Модули</a>''',
                             reply_markup=modules_btn, parse_mode='HTML')
        elif call.data == '66':
            bot.send_message(call.message.chat.id, text='''     <b>PyQt</b> — это библиотека, которая позволяет использовать фреймворк Qt GUI (GUI — это графический интерфейс пользователя) в Python. Сам Qt, написан на C++. Используя его в Python, вы можете создавать приложения намного быстрее, не жертвуя при этом значительной частью производительности C++.
    <b>PyQt5</b> это самая последняя, пятая версия Qt. Еще можно найти в интернете случайное упоминание PyQt4, но эта версия устарела и больше не поддерживается.
    Более подробно о PyQt5:
    <a href="https://python-scripts.com/pyqt5">Руководство по PyQt5</a>
    <a href="https://habr.com/ru/post/651093/">PyQt5 для начинающих</a>
    <a href="https://pythonworld.ru/gui">GUI (графический интерфейс пользователя)</a>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            document = open('pyqt5-teoria.pdf', 'rb')
            bot.send_document(chat_id=call.message.chat.id, document=document, reply_markup=closekeyboard)
            document.close()
            file = open('calculator.DOCX', 'rb')
            bot.send_document(chat_id=call.message.chat.id, document=file, reply_markup=closekeyboard)
            file.close()
        elif call.data == '67':
            bot.send_message(call.message.chat.id, text='''     Библиотеку для рисования и манипуляцией графическими объектами – <b>PyGame</b>. Этот пакет лучше воспринимать именно как библиотеку, а не игровой движок или фреймворк. Она для этого слишком проста и ограничена. Но, вместе с тем, дает необходимый минимальный инструментарий для:
    • рисования графических объектов;
    • отслеживания различных событий (клавиатуры, мыши, таймера и т.п);
    • отслеживания и изменения состояний объектов (создание анимации, контроль столкновений);
    • быстрой отрисовки изменений на экране устройства пользователя;
    • работы со звуковыми эффектами.
    Используя эти возможности, программист имеет возможность создавать простые графические приложения, в том числе и несложные игры. Библиотека PyGame не содержит физического движка и всю физику в играх приходится прописывать самостоятельно на основе уравнений физики. Также в этой библиотеке нет понятий камер, и все изменения состояний на плоскости осуществляется путем простого перемещения объектов в области игрового пространства. Так что, PyGame определенно не игровой движок, но очень удобен, когда нужно быстро реализовать графическое приложение с элементарной анимацией на плоскости и некоторыми звуковыми эффектами.
    Вообще, PyGame – это Python-обертка над С++ - библиотекой Simple Directmedia Layer (SDL)
    Более подробно о  PyGame:
    <a href="https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/18-pygame.html">Основы PyGame</a>
    <a href="https://python-scripts.com/category/pygame">Создание игр на PyGame</a>
    <a href="https://github.com/pygame/pygame">PyGame</a>         
    <a href="https://www.pygame.org/">PyGame</a>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            document = open('pygame-teoria.pdf', 'rb')
            bot.send_document(chat_id=call.message.chat.id, document=document, reply_markup=closekeyboard)
            document.close()
            file = open('snake.DOCX', 'rb')
            bot.send_document(chat_id=call.message.chat.id, document=file, reply_markup=closekeyboard)
            file.close()
        elif call.data == '68':
            bot.send_message(call.message.chat.id, text='''     <b>Модуль Telebot</b>
    Telegram-боты - это увлечение которые позволяют вам играть в игры, находить друзей, находить новых ботов и даже создавать ботов - возможности безграничны
    Есть 3 звена: наш компьютер с Python, сервер Телеграма и Телеграм-клиент.
    На компьютере работает интерпретатор Python, а внутри интерпретатора крутится наша программа на Python. Она отвечает за весь контент: в неё заложены все шаблоны текста, вся логика, всё поведение.
    Внутри программы на Python работает библиотека, которая отвечает за общение с сервером Телеграма. В библиотеку мы вшили секретный ключ, чтобы сервер Телеграма понимал, что наша программа связана с определённым ботом.
    Когда клиент с Телеграмом запрашивает у бота гороскоп, запрос приходит на сервер, а сервер отправляет его на наш компьютер. Запрос обрабатывается программой на Python, ответ идёт на сервер Телеграма, сервер отдаёт ответ клиенту.
    Более подробно о Telebot:    
    <a href="https://habr.com/ru/post/580408/">Telebot быстро и понятно</a>
    <a href="https://pypi.org/project/pyTelegramBotAPI/">pyTelegramBotAPI</a>
    <a href="https://dev-gang.ru/article/ja-postroil-telegrafnyi-bot-dlja-borby-s-pisczevymi-othodami-vot-kak-eto-delaetsja-inaqfmq470/">Полное руководство по созданию Telegram Bot</a>
    <a href="https://github.com/python-telegram-bot/python-telegram-bot">python-telegram-bot</a>
    <a href="https://core.telegram.org/bots">Боты: введение для разработчиков</a> и <a href="https://core.telegram.org/bots/api">Telegram Бот API</a>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            document = open('bot-teoria.pdf', 'rb')
            bot.send_document(chat_id=call.message.chat.id, document=document, reply_markup=closekeyboard)
            document.close()
            file = open('shporka.DOCX', 'rb')
            bot.send_document(chat_id=call.message.chat.id, document=file, reply_markup=closekeyboard)
            file.close()
        elif call.data == '69':
            bot.delete_message(call.message.chat.id, call.message.message_id)

        if call.data == '7':
            bot.send_message(call.message.chat.id, text='''     <b>Git</b> – система контроля версий текстового файла (хранит разницу от того что было и что стало)
    Всё о Git на:
    <a href="https://python.ru/post/57/">Просто про Git</a>
    <a href="https://pyneng.readthedocs.io/ru/latest/book/02_git_github/index.html">Использование Git и GitHub</a>
    <a href="https://github.com/arslanbilal/git-cheat-sheet#readme">Шпаргалка по Git и Git Flow</a>
    <a href="https://github.com/phillipadsmith/awesome-github#readme">Круто-github</a>''',
                             reply_markup=closekeyboard, parse_mode='HTML')
            document = open('git.pdf','rb')
            bot.send_document(chat_id=call.message.chat.id, document=document, reply_markup=closekeyboard)
            document.close()
        if call.data == '8': # кнопка обратного вызова - всплывающее сообщение
            bot.answer_callback_query(callback_query_id=call.id, text='I do apologize, unfortunately, this button have not done yet.')
        if call.data == '9':
            bot.answer_callback_query(callback_query_id=call.id, text='I do apologize, unfortunately, this button have not done yet.')
        if call.data == '10':
            bot.delete_message(call.message.chat.id, call.message.message_id)

#---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__": # конструкция гарантирующая, что сервер запустится только при непосредственном...main скрипта)
    bot.remove_webhook() # устанваливаем и обнавляем webhook для нашего бота (удаляем текущий и устанавливаем новый)
#------------------------------------------------------------------------
    bot.polling(none_stop=True)
#------------------------------------------------------------------------
    # bot.set_webhook(url=APP_URL) # устанваливаем url нашего приложения
    # server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) # запускаем сервер с помощью метода run,
    # # передав в него аргументы: host с нулями (это позволит сделать сервер публичным, а не локальным)
    # # и port: воспользуемся модулем os и возьмём переменную PORT и значение
