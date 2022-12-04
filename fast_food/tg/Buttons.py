from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from tg.Globals import *
from tg.models import *


def btns(type=None, ctg=None, ctgs=None, subctg_id=None, lang=1):
    btn = []
    if type == "menu":
        btn = [
            [KeyboardButton(TEXTS['BTN_MENU'][lang])],
            [KeyboardButton(TEXTS['BTN_MENU1'][lang]), KeyboardButton(TEXTS['BTN_MENU2'][lang])],
        ]
    elif type == 'contact':
        btn = [
            [KeyboardButton(TEXTS['PHONE_CONTACT'][lang], request_contact=True)]
        ]

    elif type == "ctgs":
        btn = []
        ctgs = Category.objects.all()

        for i in range(1, len(ctgs), 2):
            btn1 = ctgs[i - 1].name_uz if lang == 1 else ctgs[i - 1].name_ru
            btn2 = ctgs[i].name_uz if lang == 1 else ctgs[i].name_ru

            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(ctgs) % 2:
            btn1 = ctgs[len(ctgs) - 1].name_uz if lang == 1 else ctgs[len(ctgs) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['BACK'][lang])])

    elif type == "sub":
        btn = []
        lan = 'uz' if lang == 1 else 'ru'
        filter = {
            f'name_{lan}': ctg
        }
        ctgs = Category.objects.filter(**filter).first()
        if not ctgs:
            return []
        course = SubCategory.objects.filter(ctg=ctgs)
        if not course:
            return []
        for i in range(1, len(course), 2):
            btn1 = course[i - 1].name_uz if lang == 1 else course[i - 1].name_ru
            btn2 = course[i].name_uz if lang == 1 else course[i].name_ru
            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(course) % 2:
            btn1 = course[len(course) - 1].name_uz if lang == 1 else course[len(course) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['BACK'][lang])])
    else:
        btn = [
            [KeyboardButton("🇺🇿Uz"), KeyboardButton("🇷🇺Ru")]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)