"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from models import Base, User, Post, async_engine, Session, AsyncSession
from jsonplaceholder_requests import fetch_posts_data, fetch_users_data


def create_users(session: AsyncSession, users_data: list[dict]):
    """Создание пользователей """
    for user in users_data:
        user = User(id=int(user['id']), name=user['name'], username=user['username'], email=user['email'])
        session.add(user)
        print("created user", user)


def create_posts(session: AsyncSession, posts_data: list[dict]):
    """Создание постов"""
    for post in posts_data:
        post = Post(user_id=int(post['userId']), title=post['title'], body=post['body'])
        session.add(post)


async def async_main():
    async with Session() as session:
        async with async_engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        async with async_engine.begin() as connection:
            users_data: list[dict]
            posts_data: list[dict]
            users_data, posts_data = await asyncio.gather(fetch_users_data(),
                                                          fetch_posts_data())
            create_users(session=session, users_data=users_data)
            create_posts(session=session, posts_data=posts_data)
            await session.commit()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
