from aiogram.fsm.state import StatesGroup, State


class Botstate(StatesGroup):
    language = State()

class RestaurantMenu(StatesGroup):
    salads = State()
    fast_foods = State()
    hot_foods = State()
