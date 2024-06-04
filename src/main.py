from fastapi import FastAPI
from typing import List
from queries.core import sync_create_all, drop_table, insert_data, get_tables_list, async_get_all
import asyncio


app = FastAPI(
    title='Asterisk\'s api'
)


asyncio.run(async_get_all())

drop_table('roles')
drop_table('users')
sync_create_all()
# insert_data()

# get_tables_list()
