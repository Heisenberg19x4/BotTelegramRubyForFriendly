'''
Created on Feb 18, 2022

@author: Heisenberg
'''
# Модуль telegram.ext содержит классы 
#telegram.ext.Updater - обновления, после запуска слушает сервер телеграма
#telegram.ext.Dispatcher - 

from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup 
from telegram import ReplyKeyboardRemove #Удаляет кнопку
from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import Filters #позволяет выстраивать логику ответов на сообщения (Filters.text - метод #позволяющий отвечать только на текстовые сообщения)
from telegram.ext import MessageHandler #обработчик ,позволяющий определять к какой функции подходит данное #сообщение

#создадим глобальную переменную куда запишем имя кнопки, именно через нее отслеживаем нажатие
button_appeal='Обращение'
button_immigration='Иммиграция'
button_media='Фильмы, сериалы, книги'
button_media_film='Фильмы'
button_media_serial='Cериалы'
button_media_book='Книги'
button_media_horoskope='Гороскоп'
button_media_back='Назад'

TELEGRAM_SUPPORT_CHAT_ID='-1001706064535' #айди чата куда отправляем обращения
flag_message_polzovatel=0
flag_message_immigration=0
flag_message_media=0
user_info={} # словарь для хранения данных пользователя
films='1. Связь 1996 \n2. Джиа 1998 \n3.Бархатные ножки 2002\n4.Монстр 2003\n5.Представь нас вместе 2005\n6.Я не могу думать гетеросексуально 2008\n7.Тайные дневники мисс Энн Листер\n8.Ниже ее губ 2016\n9.Портрет девушки в огне 2019\n10.Аммонит 2020'
serials='1.Секс в другом городе 2004-…\n2.Отбросы 2009-2013\n3.Оранжевый - хит сезона 2013 - 2019\n4.Уэнтворт 2013-2021\n5.Визави 2015-2019\n6.Цыганка 2017\n7.Эйфория 2019-…\n8.Джентльмен Джек 2019-…\n9.Чувствую себя хорошо (Feel Good) 2020\n10.Сестра Рэтчед 2020'
books='1.Тонкая работа - Сара Уотерс\n2.Бархатные коготки - Сара Уотерс\n3.Дэнни Флаг «Жареные зеленые помидоры»\n4.Харуки Мураками «Мой любимый sputnik»\n5.Джерри Хилл «Я больше не одна»\n6.Ирвин Уэлш «Сексуальная жизнь сиамских близнецов»\n7.Федор Достаевский «Неточка Незванова»\n8.Маргарет Рэдклифф-Холл «Колодец одиночества»\n9.Соня Адлер «Я тебя люблю, и я тебя тоже нет»\n10.Эрин Даттон «Полное погружение»'

def button_media_film_handler(update, context):
    global flag_message_media
    flag_message_media=1
    update.message.reply_text(text=films,reply_markup=ReplyKeyboardRemove())
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_media_back),
            ]                 
        ],
        resize_keyboard=True
    )   
    update.message.reply_text(text='Назад для возвращения в меню',reply_markup=reply_markup)
    
    
def button_media_serial_handler(update, context):
    global flag_message_media
    flag_message_media=1
    update.message.reply_text(text=serials,reply_markup=ReplyKeyboardRemove())
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_media_back),
            ]                 
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text='Назад для возвращения в меню',reply_markup=reply_markup)
    
def button_media_book_handler(update, context):
    global flag_message_media
    flag_message_media=1
    update.message.reply_text(text=books,reply_markup=ReplyKeyboardRemove())
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_media_back),
            ]                 
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text='Назад для возвращения в меню',reply_markup=reply_markup)
    
def button_media_horoskope_handler(update, context):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Игривый,как лев ленивый'),
            ]                 
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text='Выбери свой знак',reply_markup=reply_markup)

def forward_to_user(update, context):
    print('Функция forward_to_user начало')
    global flag_message_polzovatel
    global flag_message_immigration
    text = update.message.text
    user_info=update.message.from_user.to_dict()
    text+= '\n|  username=@'
    text+=user_info['username']
    
    if flag_message_polzovatel==1:
        text+= '\n|  Обращение'
        flag_message_polzovatel=0
    else:
        if flag_message_immigration==1:
            text+= '\n|  Страна для иммиграции'
            flag_message_immigration=0
    
    print(text)
    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=text
    )
    update.message.reply_text(text='Спасибо за обращение!',reply_markup=ReplyKeyboardRemove())



def button_appeal_handler(update:Update, context:CallbackContext):
    print('Функция button_appeal_handler начало')
    update.message.reply_text(text='Напиши нам обращение: сотрудничество, реклама, предложение, мы обязательно ответим',reply_markup=ReplyKeyboardRemove())#Удаляет кнопку
    user_info = update.message.from_user.to_dict() # прислать в чат поддержки о том, что подключился новый юзер
    print(user_info)
    print('Функция button_appeal_handler конец')


def button_immigration_handler(update:Update, context:CallbackContext):
    global flag_message_immigration
    update.message.reply_text(text='Данный модуль пока в разработке. Хочешь помочь нам стать лучше? Напиши страну в которые ты хотел бы отправиться? А мы добавим методичку для иммиграции',reply_markup=ReplyKeyboardRemove())
    
    
    
def button_media_handler(update:Update, context:CallbackContext):
    update.message.reply_text(text='Фильм, сериал или книга?',reply_markup=ReplyKeyboardRemove())
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_media_film),
            ],
            [
                KeyboardButton(text=button_media_serial),
            ],
            [
                KeyboardButton(text=button_media_book),
            ],
            [
                KeyboardButton(text=button_media_back),
            ]                 
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text='Выбери кнопку ниже',reply_markup=reply_markup)
    
def start(update:Update, context:CallbackContext):
    update.message.reply_text(text='Привет, я Руби, чем я могу тебе помочь? ',reply_markup=ReplyKeyboardRemove())
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_appeal),
            ],
            [
                KeyboardButton(text=button_immigration),
            ],
            [
                KeyboardButton(text=button_media),
            ]      
            ,
            [
                KeyboardButton(text=button_media_horoskope),
            ]            
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text='Выбери кнопку ниже',reply_markup=reply_markup)

#Update- то самое сообщение которое пришло нам из API телеграмма , а 
#CallbackContext-пользовательский контекст ,который передается от обработчика к обработчику. В него можно сохранять любые пользовательские состояния

def message_handler(update:Update, context:CallbackContext): #метод обрабатывающий приходящие кнопки и выбирающий дальнейший сценарий событий
    text = update.message.text  # update.message.text - текст полученного сообщения
    global flag_message_polzovatel
    global flag_message_immigration
    global flag_message_media
    
    print(flag_message_polzovatel)
    if (flag_message_polzovatel==0) and (flag_message_immigration==0):
        if  text==button_appeal:
            flag_message_polzovatel=1
            return button_appeal_handler(update=update, context=context)
        else:
            if  text==button_immigration:
                flag_message_immigration=1
                return button_immigration_handler(update=update, context=context)
            else:
                if  text==button_media:
                    return button_media_handler(update=update, context=context)
                else:
                    if  text==button_media_film:
                            return button_media_film_handler(update=update, context=context)
                    else:
                        if  text==button_media_serial:
                            return button_media_serial_handler(update=update, context=context)
                        else:
                            if  text==button_media_book:
                                return button_media_book_handler(update=update, context=context)
                            else:
                                if  text==button_media_back and flag_message_media==1:
                                    flag_message_media=0
                                    return button_media_handler(update=update, context=context)
                                else:
                                    if  text==button_media_horoskope:
                                        return button_media_horoskope_handler(update=update, context=context)
                                    else:
                                        return start(update=update, context=context)
                    
                
    else:
        if flag_message_polzovatel==1: 
            return forward_to_user(update=update, context=context)
        else:
            if flag_message_immigration==1:
                return forward_to_user(update=update, context=context)
            
    
    print('Работаю')
    

def main():

    
    token="5159837170:AAF1hnUOGyxVbcwzeJtrkbiuCVmBTaqB3_U"
    updater = Updater(token, use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler("start", start))
    
#Экземпляр класса Updater будет получать запросы из API и дальше прогонять по всем функциям
#updater=Updater(TOKEN='5159837170:AAF1hnUOGyxVbcwzeJtrkbiuCVmBTaqB3_U',use_context=True)    
        
# метод обработки любого события    
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all,callback=message_handler))
    
# Для пересылки из бота в чат поддержки
    updater.dispatcher.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))

# Для пересылки ответа из чата обратно пользователю

#    dispatcher.add_error_handler(error) 
    
    updater.start_polling()  #запускаем
    updater.idle()   #код работает,пока не выключим
    
       
    
if __name__ == '__main__':
    main()
    
    


