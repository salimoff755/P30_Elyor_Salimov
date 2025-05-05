import asyncio
import logging
import sys

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from bot.main import main_router
from db import db
from envirements.utils import Env

dp = Dispatcher()

TOKEN = Env().bot.TOKEN


async def on_startup():
    db.init()
    await db.create_all()


async def main() -> None:
    i18n = I18n(path='locales', domain='messages')
    bot = Bot(token=Env().bot.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.startup.register(on_startup)
    dp.include_router(main_router)
    dp.update.outer_middleware(FSMI18nMiddleware(i18n=i18n))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
