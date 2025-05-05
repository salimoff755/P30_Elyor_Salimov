from aiogram.types import KeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder

language_text = "🔴 Language"
info_text = "📝 Information"
uz_text = "🇺🇿 Uzbek"
ru_text = "🇷🇺 Russian"
en_text = "🇬🇧 English"
main_text = "🗄 Main panel"

salads_text = "🥗 Salads"
fast_food_text = "🍕 Fast Food"
hot_text = "🫕 Hot Foods"
restaurant_text = "🍽 Resourant menu"
call_us_text = "☎️ Call us"

def make_reply(btns: list, sizes: list):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*btns)
    rkb.adjust(*sizes)
    return rkb.as_markup(resize_keyboard=True)


def menu_buttons():
    btn1 = KeyboardButton(text=_("🔴 Language"))
    btn2 = KeyboardButton(text=_("🍽 Resourant menu"))
    btn3 = KeyboardButton(text=_("☎️ Call us"))
    btn4 = KeyboardButton(text=_("📝 Information"))
    buttons = [btn1, btn2, btn3, btn4]
    size = [1, 2, 1]
    return make_reply(buttons, size)


def language_buttons():
    uzbek = KeyboardButton(text="🇺🇿 Uzbek")
    russian = KeyboardButton(text="🇷🇺 Russian")
    english = KeyboardButton(text="🇬🇧 English")
    main_panel = KeyboardButton(text=_("🗄 Main panel"))
    buttons = [uzbek, russian, english, main_panel]
    size = [1, 2, 1]
    return make_reply(buttons, size)


def Rest_menu_buttons():
    btn1 = KeyboardButton(text="🥗 Salads")
    btn2 = KeyboardButton(text="🍕 Fast Food")
    btn3 = KeyboardButton(text="🫕 Hot Foods")
    main_panel = KeyboardButton(text=_("🗄 Main panel"))
    buttons = [btn1, btn2, btn3, main_panel]
    size = [1, 2, 1]
    return make_reply(buttons, size)
