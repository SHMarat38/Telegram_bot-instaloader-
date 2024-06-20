import telebot 
import requests
import re
import instaloader
import shutil
import os
from pytube import YouTube
from telebot import types
bot = telebot.TeleBot('7391042227:AAE8fkruVvR2fIsEi3YaWxCFDyqPbvSq3e8')
def is_youtube_link(link):
    youtube_pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$"
    return re.match(youtube_pattern, link)
def is_instagram_link(link):
    instagram_pattern = r"(https?://)?(www\.)?(instagram\.com)/.+$"
    return re.match(instagram_pattern, link)
@bot.message_handler(commands=['start'])
def star(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton('YouTube')
        btn2=types.KeyboardButton('Instagram')
        markup.row(btn1)
        btn3=types.KeyboardButton('Help')
        markup.row(btn2, btn3)
        bot.send_message(message.chat.id, f'Добро пожаловать {message.from_user.first_name}. Данный бот работает медленно это связанно с техническими проблемами.Выберите социальную сеть' ,  reply_markup=markup)
        bot.register_next_step_handler(message, tru)
def tru(message):
        if message.text == "YouTube":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn8= types.KeyboardButton('Video')
                btn7= types.KeyboardButton('Audio')
                btn6 = types.KeyboardButton('Назад')
                markup.row(btn8,btn7)
                markup.row(btn6)
                bot.send_message(message.chat.id, 'Выберите метод', reply_markup=markup)
                bot.register_next_step_handler(message, method)
        elif message.text == 'Instagram':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('Назад')
                markup.row(btn1)
                bot.send_message(message.chat.id, 'Отправьте ссылку на Reels видео.....', reply_markup=markup)
                bot.register_next_step_handler(message, instagram)
        elif message.text == 'Help':
                 markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                 btn1=types.KeyboardButton('YouTube')
                 btn2=types.KeyboardButton('Instagram')
                 markup.row(btn1)
                 btn3=types.KeyboardButton('Help')
                 markup.row(btn2, btn3)
                 bot.send_message(message.chat.id, 'Данный раздел находится в разработке ⚙', reply_markup=markup)
                 bot.register_next_step_handler(message, tru )
def method(message):
        if message.text =='Video':
                bot.send_message(message.chat.id, "Отправьте ссылку")
                bot.register_next_step_handler(message, method_video)
        elif message.text == "Audio":
                bot.send_message(message.chat.id, 'Отправьте ссылку')
                bot.register_next_step_handler(message, method_audio)
        elif message.text == "Назад":
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1=types.KeyboardButton('YouTube')
                btn2=types.KeyboardButton('Instagram')
                markup.row(btn1)
                btn3=types.KeyboardButton('Help')
                markup.row(btn2, btn3)
                bot.send_message(message.chat.id, 'Выберите социальную сеть', reply_markup=markup)
                bot.register_next_step_handler(message, tru)
        else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn8= types.KeyboardButton('Video')
                btn7= types.KeyboardButton('Audio')
                btn6 = types.KeyboardButton('Назад')
                markup.row(btn8,btn7)
                markup.row(btn6)
                bot.send_message(message.chat.id, 'Выберите метод', reply_markup=markup)
                bot.register_next_step_handler(message, method)
def method_video(message):
        if is_youtube_link(message.text):
                linkyoutube = message.text 
                yt = YouTube(linkyoutube)
                bot.send_message(message.chat.id, 'Ожидайте скачивания файла.Примерное время скачивания файла от 1-5минут.(Такая медленная скорость скачивания связанно с техническими проблемами)')
                stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
                video_file_path = stream.download(timeout=600000)
                with open(video_file_path, "rb") as  video:
                        bot.send_video(message.chat.id, video, timeout=60000)              
                os.remove(video_file_path)
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1=types.KeyboardButton('YouTube')
                btn2=types.KeyboardButton('Instagram')
                markup.row(btn1)
                btn3=types.KeyboardButton('Help')
                markup.row(btn2, btn3)
                bot.send_message(message.chat.id, 'Установка завершена', reply_markup=markup)
                bot.register_next_step_handler(message, tru)
        elif message.text=='Назад':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1=types.KeyboardButton('YouTube')
                btn2=types.KeyboardButton('Instagram')
                markup.row(btn1)
                btn3=types.KeyboardButton('Help')
                markup.row(btn2, btn3)
                bot.send_message(message.chat.id, 'Выберите социальную сеть', reply_markup=markup)
                bot.register_next_step_handler(message, tru)
        elif message.text == 'start' or '/start' or 'Start' or '/Start':
                 markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                 btn1=types.KeyboardButton('YouTube')
                 btn2=types.KeyboardButton('Instagram')
                 markup.row(btn1)
                 btn3=types.KeyboardButton('Help')
                 markup.row(btn2, btn3)
                 bot.send_message(message.chat.id, 'Выберите социальную сеть', reply_markup=markup)
                 bot.register_next_step_handler(message, tru)     
        else:
                bot.send_message(message.chat.id, 'Введите корректную ссылку')
                bot.register_next_step_handler(message, method_video)
def method_audio(message):
         if is_youtube_link(message.text):
                 linkyoutube = message.text 
                 yt = YouTube(linkyoutube)
                 bot.send_message(message.chat.id, 'Ожидайте скачивания файла.//.Примерное время скачивания файла от 1-5минут.(Такая медленная скорость скачивания связанно с техническими проблемами)')
                 stream = yt.streams.get_audio_only()               
                 audio_file_path = stream.download(timeout=600000)
                 with open(audio_file_path, "rb") as audio:
                         bot.send_audio(message.chat.id, audio, timeout=60000)
                 os.remove(audio_file_path)
                 markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                 btn1=types.KeyboardButton('YouTube')
                 btn2=types.KeyboardButton('Instagram')
                 markup.row(btn1)
                 btn3=types.KeyboardButton('Help')
                 markup.row(btn2, btn3)
                 bot.send_message(message.chat.id, 'Установка завершена', reply_markup=markup)
                 bot.register_next_step_handler(message, tru)
         elif message.text=='Назад':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1=types.KeyboardButton('YouTube')
                btn2=types.KeyboardButton('Instagram')
                markup.row(btn1)
                btn3=types.KeyboardButton('Help')
                markup.row(btn2, btn3)
                bot.send_message(message.chat.id, 'Выберите социальную сеть', reply_markup=markup)
                bot.register_next_step_handler(message, tru)
         elif message.text == 'start' or '/start' or 'Start' or '/Start':
                 markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                 btn1=types.KeyboardButton('YouTube')
                 btn2=types.KeyboardButton('Instagram')
                 markup.row(btn1)
                 btn3=types.KeyboardButton('Help')
                 markup.row(btn2, btn3)
                 bot.send_message(message.chat.id, 'Выберите социальную сеть', reply_markup=markup)
                 bot.register_next_step_handler(message, tru)
         else:
                bot.send_message(message.chat.id, 'Введите корректную ссылку')
                bot.register_next_step_handler(message, method_audio)
def instagram(message):
        if is_instagram_link(message.text):
                loader = instaloader.Instaloader()
                bot.send_message(message.chat.id, 'Ожидайте скачивание файла.///.Примерное время скачивания файла от 1-5минут.(Такая медленная скорость скачивания связанно с техническими проблемами)')
                post_url = message.text
                post = instaloader.Post.from_shortcode(loader.context, post_url.split("/")[-2])
                a = loader.download_post(post, target='insta')

                directory = 'insta'
                for filename in os.listdir(directory):
                        file_path = os.path.join(directory, filename)
                        if os.path.isfile(file_path) and file_path.lower().endswith('.mp4'):
                                with open(file_path, 'rb') as video:
                                        bot.send_video(message.chat.id, video, timeout=600000)


                for filename in os.listdir(directory):
                        file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path) and file_path.lower().endswith('.mp4'):
                        os.remove(file_path)
                shutil.rmtree(directory)   
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1=types.KeyboardButton('YouTube')
                btn2=types.KeyboardButton('Instagram')
                markup.row(btn1)
                btn3=types.KeyboardButton('Help')
                markup.row(btn2, btn3)
                bot.send_message(message.chat.id, 'Выберите социальную сеть', reply_markup=markup)
                bot.register_next_step_handler(message, tru)
        elif message.text=='Назад':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1=types.KeyboardButton('YouTube')
                btn2=types.KeyboardButton('Instagram')
                markup.row(btn1)
                btn3=types.KeyboardButton('Help')
                markup.row(btn2, btn3)
                bot.send_message(message.chat.id, 'Выберите социальную сеть', reply_markup=markup)
                bot.register_next_step_handler(message, tru)
        elif bot.message_handler(commands=['start']):
                bot.register_next_step_handler(message, star)

        else:
                bot.send_message(message.chat.id, 'Введите корректную ссылку')
                bot.register_next_step_handler(message, instagram)




bot.polling(none_stop=True)