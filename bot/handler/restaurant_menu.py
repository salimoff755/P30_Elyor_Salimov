from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __


from bot.buttons.reply import Rest_menu_buttons, restaurant_text
from bot.states import RestaurantMenu

rest_menu = Router()

@rest_menu.message(F.text == __(restaurant_text))
async def rest_handler(message: Message, state: FSMContext):
    await state.set_state(RestaurantMenu.salads)
    await message.answer(_("Select the menu"), reply_markup=Rest_menu_buttons())