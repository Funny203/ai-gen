from config import TOKEN
from PIL import Image
import base64
from io import BytesIO
import telebot
#from telebot.types import ReplyKeyboardMarkup, KeyboardButton
bot = telebot.TeleBot(TOKEN)
#keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat,id, 'Привет! Я бот для генерации картинок.')


@bot.message_handler(commands=['image'])
def generate_image(message):
    input_file = "C:/Users/User/Desktop/asdfghjkl/text.txt"
    output_image = "C:/Users/User/Desktop/asdfghjkl/image.png"
    with open(input_file, "r") as file:
        base64_text = file.read()
        image_data = base64.b64decode(base64_text)
        image = Image.open(BytesIO(image_data))
        image.save(output_image)


        with open(output_image, "rb") as photo:
            bot.send_photo(message.chat.id, photo, 'Вот сгенерированная картинка!')




bot.infinity_polling()