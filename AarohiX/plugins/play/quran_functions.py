# quran_functions.py

from pyrogram.types import InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb
import json

def get_quran_keyboard():
    quran = json.loads(open("AarohiX/assets/quran.json").read())["s"]
    keyboard = []
    list = []
    for i in range(1, 11):
        if len(list) == 2:
            copy_list = list.copy()
            keyboard.append(copy_list)
            list.clear()
        name = quran[i - 1]["surah"]
        list.append(ikb(name, callback_data=f"play-{i - 1}"))
    keyboard.append(list)
    keyboard.append([ikb(". التالي .", callback_data="next-1")])
    return ikm(keyboard)
