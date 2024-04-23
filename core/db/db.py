import aiosqlite

DATABASE_FILE = 'core/db/db.db'


# запуск бд (создание таблицы с пользователями)
async def init_db() -> None:
    async with aiosqlite.connect(DATABASE_FILE) as db:
        await db.execute(
            'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, telegram_id INTEGER UNIQUE)')
        await db.commit()


# добавление пользователя в бд
async def add_user(telegram_id: int) -> None:
    async with aiosqlite.connect(DATABASE_FILE) as db:
        await db.execute('INSERT OR IGNORE INTO users (telegram_id) VALUES (?)', (telegram_id,))
        await db.commit()


# получение всех пользователей
async def get_users():
    async with aiosqlite.connect(DATABASE_FILE) as db:
        cursor = await db.execute('SELECT telegram_id FROM users')
        users = await cursor.fetchall()
        return users
