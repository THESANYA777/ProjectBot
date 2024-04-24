import sys
import asyncio
import logging
import requests

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import date

from config import TOKEN
from core.handlers import cmdstart
from core.db.db import init_db, get_users
from core.handlers.every_hour_handler import Request

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
scheduler = AsyncIOScheduler()


# асинхронный вызов оповещение ежечасно
async def send_course():
    request = Request()
    bitcoin = request.bitcoin_request()
    ton = request.ton_request()
    sol = request.sol_request()
    matic = request.matic_request()
    near = request.near_request()
    atom = request.atom_request()

    text = (f'Актуальный курс на {date.today()}\n\n'
            f'Bitcoin: {bitcoin}\n'
            f'Ton: {ton}\n'
            f'SOL: {sol}\n'
            f'MATIC: {matic}\n'
            f'NEAR: {near}\n'
            f'ATOM: {atom}\n\n'
            f'Спасибо что используете наш сервис!')

    users_ids = await get_users()

    for id_ in users_ids:
        try:
            requests.get(
                url=f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id_[0]}&text={text}&parse_mode=html')
        except Exception as e:
            print(e)


# запуск бота
async def main() -> None:
    dp.include_routers(
        cmdstart.router,
    )

    scheduler.add_job(send_course, trigger='interval', hours=1)
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# проверка имён, и запуск бота
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_db())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Bot stopped')
