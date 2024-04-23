from aiogram import F, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command

from core.db.db import add_user
from core.handlers.every_hour_handler import Request

router = Router()


# обработчик команды /start
@router.message(CommandStart())
async def say_hello(message: Message):
    await add_user(message.from_user.id)  # добавляем юзера в базу данных
    await message.answer_photo(photo=FSInputFile('core/data/hello_p.jpg'),
                               caption='Привет! Вы подписались на ежечасную отправку актуального курса следующих криптовалют:\n'
                                       '<blockquote>Bitcoin\n'
                                       'USDT\n'
                                       'SOL\n'
                                       'Ton\n'
                                       'Matic\n'
                                       'NEAR\n'
                                       'ATOM</blockquote>')
