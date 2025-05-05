from os import getenv

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from dotenv import load_dotenv

from bot.buttons.reply import menu_buttons, language_buttons, language_text, uz_text, ru_text, en_text, main_text, \
    info_text
from bot.states import Botstate
from bot.utils_function import check_user

load_dotenv()
TOKEN = getenv('TOKEN')

main_router = Router()


@main_router.message(Botstate.language, F.text == __(main_text))
@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await check_user(message)
    await message.answer(_("Hello, {}! Please, choose the buttons!".format(message.from_user.full_name)),
                         reply_markup=menu_buttons())


@main_router.message(F.text == __(language_text))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Botstate.language)
    await message.answer(_("Please, choose the language!"), reply_markup=language_buttons())


@main_router.message(F.text == __(info_text))
async def command_start_handler(message: Message):
    await message.answer(_('''This is a food ordering bot. You can order your favorite dishes by selecting 
    the Restaurant menu and pressing the appropriate buttons. Bon appetit'''), reply_markup=menu_buttons())


@main_router.message(Botstate.language, F.text.in_([uz_text, ru_text, en_text]))
async def command_start_handler(message: Message, state: FSMContext, i18n) -> None:
    map_ = {uz_text: "uz", ru_text: "ru", en_text: "en"}
    await state.set_data({"locale": map_.get(message.text)})
    i18n.current_locale = map_.get(message.text)
    await message.answer(_("Please, choose the language!"), reply_markup=language_buttons())

