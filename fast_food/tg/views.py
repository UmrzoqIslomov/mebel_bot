from .models import Log, User
from .Buttons import *
from .Globals import TEXTS


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.message = {"state": 0}
        tglog.save()
    log = tglog.messages

    tg_user = User.objects.filter(user_id=user.id).first()

    if not tg_user:
        tg_user = User()
        tg_user.user_id = user.id
        tg_user.username = user.username
        tg_user.save()
        log['state'] = 0

    tglog.messages = log
    tglog.save()

    if not tg_user.lang:
        update.message.reply_text(TEXTS['START'], reply_markup=btns())
    else:
        if log.get('state', 0) >= 10:
            update.message.reply_text(TEXTS["BOSH_MENU"][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            log['state'] = 10
            tglog.messages = log
            tglog.save()
        else:
            update.message.reply_text("iltimos so'ralgan narsani kiriting")


def message_handler(update, context):
    user = update.message.from_user

    tg_user = User.objects.get(user_id=user.id)
    tglog = Log.objects.filter(user_id=user.id).first()
    msg = update.message.text
    log = tglog.messages
    state = log.get('state', 0)

    if state == 0:
        log['state'] = 1
        if msg == "🇺🇿Uz":
            tg_user.lang = 1
            tg_user.save()
        elif msg == "🇷🇺Ru":
            print("A")
            tg_user.lang = 2
            tg_user.save()
        else:
            update.message.reply_text(TEXTS['START'], reply_markup=btns())
            return 0
        update.message.reply_text(TEXTS["CONTACT"][tg_user.lang], reply_markup=btns('contact', lang=tg_user.lang))
        tglog.messages = log
        tglog.save()
        return 0

    elif log['state'] == 1:
        update.message.reply_text(TEXTS["CONTACT2"][tg_user.lang])

    elif log['state'] == 11:
        log['state'] = 12
        update.message.reply_text(TEXTS['BOSH_MENU'], reply_markup=btns('menu'))
        print("qwerty")

    if msg == TEXTS['BTN_MENU'][1] or msg == TEXTS['BTN_MENU'][2]:
        log['state'] = 13
        update.message.reply_text(TEXTS["Bosh Menu 👇"][tg_user.lang], reply_markup=btns('ctgs', lang=tg_user.lang))

    # elif log['state'] == 13:
    #     log['state'] = 14
    #     log['ctg'] = msg
    #     ctg = Category.objects.get(content=msg)
    #     update.message.reply_text("Выберите ниже⬇:", reply_markup=btns("subctg", subctg_id=ctg.id))

    tglog.messages = log
    tglog.save()


def contact_handler(update, context):
    contact = update.message.contact
    user = update.message.from_user
    tg_user = User.objects.get(user_id=user.id)
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages

    print(log)
    if log['state'] == 1:
        tg_user.phone = contact.phone_number
        tg_user.save()
        log.clear()

        log["state"] = 10
        update.message.reply_text(TEXTS["BOSH_MENU"][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))

    tglog.messages = log
    tglog.save()

