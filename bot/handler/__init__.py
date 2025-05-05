from bot.handler.admin import *
from bot.handler.main import *
from bot.handler.restaurant_menu import *
from bot.main import main_router

dp = {
    *[main_router,
      rest_menu
      ]
}