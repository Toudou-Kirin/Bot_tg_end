from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Функции')
b2 = KeyboardButton('/Виды_примеров')
b3 = KeyboardButton('/Статистика')
b4 = KeyboardButton('/Примерсложение') 
b5 = KeyboardButton('/Примервычитание') 
b6 = KeyboardButton('/Примерумножение') 
b7 = KeyboardButton('/Примерделение') 

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7)