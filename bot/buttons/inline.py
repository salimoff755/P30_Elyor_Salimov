from aiogram.utils.keyboard import InlineKeyboardBuilder


def make_inline(btns: list, sizes: list):
    ikb = InlineKeyboardBuilder()
    ikb.add(*btns)
    ikb.adjust(*sizes)
    return ikb.as_markup()