from database import async_engine, sync_engine, session_factory, async_session_factory
from models.models import metadata, roles, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text, insert


# async def async_create_all():
#     await metadata.create_all(async_engine)


def sync_create_all():
    sync_engine.echo = False
    metadata.create_all(sync_engine)
    Base.metadata.create_all(sync_engine)


async def async_get_all():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('select version()'))
        print(f'{res.first()}')


def drop_table(table_name):
    base = declarative_base()
    table = metadata.tables.get(table_name)
    if table is not None:
        print(f'Drop table: {table}')
        metadata.drop_all(sync_engine, [table], checkfirst=True)


def insert_data():
    sync_engine.echo = True
    with sync_engine.connect() as conn:
        # stmt = """ INSERT INTO roles (name) VALUES
        #         ('manager'),
        #         ('admin'); """
        stmt = insert(roles).values(
            [
                {'name': 'admin'},
                {'name': 'manager'},
                {'name': 'admin'},
            ]
        )
        # conn.execute(text(stmt))
        conn.execute(stmt)
        conn.commit()


def get_tables_list():
    for t in metadata.tables:
        print(t)
