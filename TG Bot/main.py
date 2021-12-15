import telebot 
from telebot import types 
import psycopg2 
import datetime 
from datetime import datetime 
 
bot = telebot.TeleBot('') 
 
def clav_message(): 
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btnDd = types.KeyboardButton('Другой день') 
    btnTd = types.KeyboardButton('Сегодня') 
    btnTm = types.KeyboardButton('Завтра') 
    markup.add(btnDd) 
    markup.add(btnTd) 
    markup.add(btnTm) 
    return markup 
 
@bot.message_handler(commands=['help']) 
def help_message(message): 
    bot.send_message(message.chat.id, 'Привет я помогу тебе ориентороваться в этом боте. Базовые команды бота: \n/start-начать работу бота \n/help-командный помощник \n/button- вызов кнопки бота') 
 
@bot.message_handler(commands=['start']) 
def start_message(message): 
    bot.send_message(message.chat.id, 'Привет, вызови команду /button чтобы продолжить работу с ботом')
 
@bot.message_handler(commands=['button']) 
def button_message(message): 
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)  
    btnTd = types.KeyboardButton('Сегодня') 
    btnTm = types.KeyboardButton('Завтра') 
    btnDd = types.KeyboardButton('Другой день')
    markup.add(btnDd) 
    markup.add(btnTd) 
    markup.add(btnTm) 
    bot.send_message(message.chat.id, 'Выбери на какой день ты хочешь увидеть расписание', reply_markup=markup)
 
@bot.message_handler(content_types='text') 
def reply_message(message): 
    if message.text == 'Другой день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnPn = types.KeyboardButton('Понедельник')
        btnVt = types.KeyboardButton('Вторник')
        btnSr = types.KeyboardButton('Среда')
        btnCht = types.KeyboardButton('Четверг')
        btnPt = types.KeyboardButton('Пятница')
        btnSb = types.KeyboardButton('Суббота')
        markup.add(btnPn)
        markup.add(btnVt)
        markup.add(btnSr)
        markup.add(btnCht)
        markup.add(btnPt)
        markup.add(btnSb)
        bot.send_message(message.chat.id, 'Выбери на какой день', reply_markup=markup) 
         
    if message.text == 'Понедельник':  
        conn= psycopg2.connect(database = "raspisanie",
                                user="postgres",
                                password="123",
                                host="localhost",
                                port="5433")
        cursor = conn.cursor() 
        cursor.execute("SELECT subject,room_numb, start_time FROM timetable WHERE day='понедельник'") 
        records=cursor.fetchall() 
        result='' 
        for arr in records :
            for word in arr:
                result=result +str(word)
                result+='\n'      
        bot.send_message(message.chat.id, result, reply_markup=clav_message())
           
    if message.text == 'Вторник': 
        conn = psycopg2.connect(database = "raspisanie",
                                user="postgres",
                                password="123",
                                host="localhost",
                                port="5433")
        cursor = conn.cursor() 
        cursor.execute("SELECT subject,room_numb, start_time FROM timetable WHERE day='вторник'") 
        records=cursor.fetchall() 
        result='' 
        for arr in records :
            for word in arr:
                result=result +str(word)
                result+='\n'           
        bot.send_message(message.chat.id, result, reply_markup=clav_message()) 
          
    if message.text == 'Среда': 
        conn = psycopg2.connect(database = "raspisanie",
                                user="postgres",
                                password="123",
                                host="localhost",
                                port="5433")
        cursor = conn.cursor() 
        cursor.execute("SELECT subject,room_numb, start_time FROM timetable WHERE day='среда'") 
        records=cursor.fetchall() 
        result='' 
        for arr in records :
            for word in arr:
                result=result +str(word)
                result+='\n'   
        bot.send_message(message.chat.id, result, reply_markup=clav_message()) 
    if message.text == 'Четверг': 
        conn = psycopg2.connect(database = "raspisanie",
                                user="postgres",
                                password="123",
                                host="localhost",
                                port="5433")
        cursor = conn.cursor() 
        cursor.execute("SELECT subject,room_numb, start_time FROM timetable WHERE day='четверг'") 
        records=cursor.fetchall() 
        result='' 
        for arr in records :
            for word in arr:
                result=result +str(word)
                result+='\n'  
        bot.send_message(message.chat.id, result, reply_markup=clav_message())   
    if message.text == 'Пятница': 
        conn = psycopg2.connect(database = "raspisanie",
                                user="postgres",
                                password="123",
                                host="localhost",
                                port="5433")
        cursor = conn.cursor()
        cursor.execute("SELECT subject,room_numb, start_time FROM timetable WHERE day='пятница'") 
        records=cursor.fetchall() 
        result='' 
        for arr in records :
            for word in arr:
                result=result +str(word)
                result+='\n'    
        bot.send_message(message.chat.id, result, reply_markup=clav_message()) 
 
    if message.text == 'Суббота': 
        conn = psycopg2.connect(database = "raspisanie",
                                user="postgres",
                                password="123",
                                host="localhost",
                                port="5433")
        cursor = conn.cursor()
        cursor.execute("SELECT subject,room_numb, start_time FROM timetable WHERE day='суббота'") 
        records=cursor.fetchall() 
        result='' 
        for arr in records :
            for word in arr:
                result=result +str(word)
                result+='\n'   
        bot.send_message(message.chat.id, result, reply_markup=clav_message()) 
     
 
    if message.text == 'Сегодня': 
        today=datetime.today().weekday() 
        if today==6: 
            bot.send_message(message.chat.id, 'Выходной') 
        else:  
            days= ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье'] 
            ceg=str(days[today]) 
            bot.send_message(message.chat.id, ceg) 
            conn = psycopg2.connect(database = "raspisanie",
                                user="postgres",
                                password="123",
                                host="localhost",
                                port="5433")
            cursor = conn.cursor()
            cursor.execute("SELECT subject,room_numb, start_time FROM timetable WHERE day=%s",[ceg]) 
            records=cursor.fetchall() 
            result='' 
            for arr in records :
                for word in arr:
                    result=result +str(word)
                    result+='\n' 
            bot.send_message(message.chat.id, result)  
            

    if message.text == 'Завтра': 
        today=datetime.today().weekday()+1 
        if today==7: 
            today=0 
        days= ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье'] 
        ceg=str(days[today]) 
        bot.send_message(message.chat.id, ceg) 
        conn = psycopg2.connect(database = "raspisanie",
                                user="postgres",
                                password="123",
                                host="localhost",
                                port="5433")
        cursor = conn.cursor() 
        cursor.execute("SELECT subject,room_numb, start_time FROM timetable WHERE day=%s",[ceg]) 
        records=cursor.fetchall() 
        result='' 
        for arr in records :
            for word in arr:
                result=result +str(word)
                result+='\n' 
        bot.send_message(message.chat.id, result)  
        
        
bot.infinity_polling()