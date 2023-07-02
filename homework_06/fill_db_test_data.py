"""
Заполняет тестовыми данными БД
"""
import asyncio

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import ProgrammingError, IntegrityError

from models import Post
from jsonplaceholder_requests import fetch_posts_data
from config import Config




engine = create_engine(url=Config.SQLALCHEMY_DATABASE_URI)

def create_posts(session: Session, posts_data: list[dict]):
    """Создание постов"""
    for post in posts_data:
        post = Post(title=post['title'], body=post['body'])
        session.add(post)


async def async_main():
    with Session(engine) as session:
        posts_data: list[dict]
        posts_data = await fetch_posts_data()
        create_posts(session=session, posts_data=posts_data)
        try:
            session.commit()
        except (ProgrammingError, IntegrityError):
            print("Данные в БД уже есть")

def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
