# C5.3. Создание Telegram-бота
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Что такое боты Telegram?
#
# Боты — это сторонние приложения, которые запускаются внутри Telegram.
# Приложения могут быть написаны на любом языке программирования, универсальность взаимодействия обеспечивается
# благодаря протоколу HTTP (по сути, то, что мы делали с вами в прошлом юните через библиотеку Requests).
# Пользователи могут взаимодействовать с ботами, отправляя им сообщения, команды и встроенные запросы.
#
# Приведем краткий список того, что умеют делать боты:
#
# Получение индивидуальных уведомлений и новостей. Бот может работать как умная газета, которая будет отправлять
# интересующий вас контент, как только он будет опубликован.
# Интеграция с другими сервисам. Бот может дополнять чаты Telegram возможностями из внешних сервисов, например,
# Gmail Bot, GIF bot, IMDB bot, Wiki bot, Music bot, Youtube bot, GitHub bot.
# Создание собственных инструментов. Бот может предоставлять вам оповещения о различных действиях, прогнозы погоды,
# переводы, форматирование или другие услуги. Например,  Markdown bot, Sticker bot, Vote bot, Like bot
# Как работают боты?
# По сути, боты Telegram — это особые учетные записи, для которых не требуется дополнительный номер телефона.
#
# Пользователи могут взаимодействовать с ботами двумя способами:
#
#
# 1 Отправлять сообщения и команды ботам, открывая с ними чат или добавляя их в группы.
#
# Предлагаемые команды. Команды начинаются с символа «/».
#
#
# 2 Отправлять запросы прямо из поля ввода, вводя @username бота и запрос. Это позволяет отправлять контент от встроенных
#   ботов прямо в любой чат, группу или канал.
#
# Источник: core.telegram.org
# Пользователи могут ввести имя пользователя бота в любом чате, а затем ввести запрос, не отправляя никаких сообщений.
#
# Сообщения, команды и запросы, отправленные пользователями, передаются программному обеспечению, работающему на вашем
# сервере. Сервер — это компьютер, поэтому сервером может выступать и ваш домашний компьютер. Сервер Telegram отвечает
# за шифрование и пересылку сообщений. Вы общаетесь с сервером Telegram через интерфейс по протоколу HTTP, и этот
# интерфейс называется Bot API.
#
# В части Bot API есть набор определенных методов, которые позволяют получить от Telegram сообщение, которое
# пользователь прислал боту и отправить ответ обратно. С этими функциями мы познакомимся чуть позже. То есть API
# представляет собой промежуточное звено между клиентом Telegram и вашим скриптом.
#
# Источник: d.line-scdn.net
# Как создать бота?
#
# Для того, чтобы создать бота есть … бот. :) Вам необходимо написать @BotFather и выполнить несколько простых шагов.
#
# Используйте команду /newbot, чтобы создать нового бота.
#
# Затем необходимо:
#
# Установить имя (name) вашего бота.
# Имя вашего бота отображается в контактной информации и в других местах.
# Установить имя пользователя (username) вашего бота.
# Имя пользователя — это короткое имя, которое будет использовать для идентификации вашего бота и обращению к нему.
# Имена пользователей состоят из 5–32 символов и нечувствительны к регистру, могут включать только латинские символы,
# числа и символы подчеркивания. Имя пользователя вашего бота должно заканчиваться на «bot», например, «tetris_bot»
# или «TetrisBot».
# Получить токен (token).
# Токен представляет собой строку вида 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw. Он необходим для авторизации
# (подтверждения, что именно вы владелец этого бота, чтобы в программе было понятно, к какому именно боту
# привязываются все обработчики) вашей программы, в которой реализована логика бота. Токен — это пароль от вашего бота,
# поэтому храните свой токен в безопасности.
# С более подробной информацией о возможностях @BotFather можно ознакомиться в официальной документации.
#
# Создание Python Telegram-бота
# После того как мы получили токен для доступа к боту, можно приступать к созданию скрипта, который будет реализовывать
# всю логику Телеграм-бота. Но перед этим необходимо изучить некоторые типы данных, которыми API Bot позволяет оперировать.
#
# Первое, с чем нам необходимо познакомиться, это доступная информация о чатах. API Bot дает доступ к множеству
# объектов, с которыми он работает.
#
# Мы разберем два основных:
#
# * чат,

# * сообщение.

# Каждый из них обладает определенным набором информации.
#
# Например, часть полей, доступных для объекта «Чат»:
#
# Поле	Описание
# id	Уникальный идентификатор данного чата.
# type	Тип чата может быть «private», «group», «supergroup» или «channel».
# username	Необязательное поле. Имя пользователя для приватных чатов, супергрупп и каналов, если доступно.
# Все сообщения в Telegram приходят в какой-либо чат. Чтобы его идентифицировать, например, для того, чтобы
# отправить ответное сообщение, необходимо знать его id. Также можно определить тип чата и реализовать различную
# логику для моментов, когда бот будет использоваться в личных сообщениях или групповых чатах. Username может
# использоваться для приветствия и обращения к пользователю.
#
# Поля, доступные для объекта «Сообщение»:
#
# Поле	Описание
# message_id	Уникальный идентификатор сообщения в данном чате.
# from	Необязательное поле. Отправитель сообщения. Если сообщение отправлено каналом, то поле будет пустым.
# date	Дата отправки сообщения в Unix-формате.
# chat	Чат, куда было отправлено сообщение.
# text	Необязательное поле. Текст сообщения.
# Зная id сообщения, можно отправить ответ именно на это сообщение. Отправителя можно использовать для
# персонализированного ответа. Чат нужен, чтобы понять, куда нужно отправить ответ. Поле с текстом позволяет
# анализировать и обрабатывать сообщения и команды, отправленные пользователем.
#
# Сообщения могут содержать контент следующих типов:
#
# audio — аудиозапись;
# photo — фотография, картинка;
# voice — голосовое сообщение;
# video — видеозапись;
# document — документ;
# text — текстовое сообщение;
# location — геолокация;
# contact — контакт;
# sticker — стикер.
# Можно реализовать различную обработку сообщений с соответствующим контентом.
#
# Чтобы взаимодействовать с этими объектами, в Python есть специальная библиотека pyTelegramBotAPI.
# Установить её вы можете с помощью команды:
#

# pip3 install pyTelegramBotAPI.

# После установки необходимо создать новый файл, импортировать туда модуль telebot и создать объект bot,
# используя токен, полученный при регистрации.
#
# import telebot
#
# TOKEN = "6646417095:AAFWGEe6po2QSjPVpvC7ZDY7wZBV-5sx73c"
#
# bot = telebot.TeleBot(TOKEN)

# Чтобы запустить бота, нужно воспользоваться методом polling.
#
# bot.polling(none_stop=True)

# Параметр none_stop=True говорит, что бот должен стараться не прекращать работу при возникновении каких-либо ошибок.
#
# Обработчики сообщений
# Обработчик сообщений — это функция, которая будет выполняться при получении определённого сообщения.
# Для того чтобы из обычной функции сделать обработчик сообщений для бота, надо воспользоваться декоратором
# @bot.message_handler. Обработчики сообщений состоят из одного или нескольких фильтров.
#
# Обработчик сообщений объявляется следующим образом (при условии, что bot — это экземпляр класса TeleBot):
#
# import telebot
#
# TOKEN = "6646417095:AAFWGEe6po2QSjPVpvC7ZDY7wZBV-5sx73c"
#
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(filters)
# def function_name(message):
#     bot.reply_to(message, "This is a message handler")
# Давайте разберемся, что мы с вами написали.
#
# Начнем с filters в аргументах к обработчику.
#
# filters — фильтры, определяющие, следует ли вызывать декорированную функцию для соответствующего сообщения
# или нет. У одного обработчика может быть несколько фильтров.
#
# Мы с вами разберем два основных фильтра:
#
# * тип контента;
#
# * команды.

# Название фильтра	Аргумент	Условие выполнения функции
# content_types	Список строк, по умолчанию ['text']	Если тип контента, содержащегося в сообщении совпадает с
# типом указанным в качестве аргумента. То есть обработчик по умолчанию реагирует на все текстовые сообщения.
# commands	Список строк	Если сообщение начинается с команды, указанной в списке.
# Для обработчиков сообщений разрешено любое имя функции, поэтому function_name может принимать любое значение.
# Функция должна принимать не более одного аргумента, который будет сообщением, которое функция должна обработать.
# Аргумент message имеет все поля перечисленные здесь.
#
#
# import telebot
#
# TOKEN = '6646417095:AAFWGEe6po2QSjPVpvC7ZDY7wZBV-5sx73c'
# bot = telebot.TeleBot("TOKEN")
#
# # Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(content_types=['voice', ])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'У тебя очень красивый голос!')
#
# bot.polling(none_stop=True)
# # Обрабатывается все документы и аудиозаписи
# # @bot.message_handler(content_types=['document', 'audio'])
# # def handle_docs_audio(message):
# #     pass
#

# import telebot
#
# TOKEN = '6646417095:AAFWGEe6po2QSjPVpvC7ZDY7wZBV-5sx73c'
# bot = telebot.TeleBot("TOKEN")
#
# # Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(content_types=['start', 'help'])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'У тебя очень красивый голос!')
#     print(f'',bot.send_message(message.chat.id, 'У тебя очень красивый голос!'))
#
# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass

# 5.3.1

# Задание
#
# Допишите обработчик так, чтобы он из сообщения брал username и выдавал
# приветственное сообщение с привязкой к пользователю.
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")

# import telebot
# token = '5834725956:AAFgZ83Yqn2D9G3M4LGoM4WmU1nlpb2jVI8'
# bot = telebot.TeleBot(token)
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Привет ✌️ ")
#     bot.infinity_poling()
