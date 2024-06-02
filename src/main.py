from fastapi import FastAPI
from typing import List
from queries.core import async_create_all, sync_create_all, drop_table, insert_data, get_tables_list
import asyncio


app = FastAPI(
    title='Asterisk\'s api'
)


drop_table('roles')
sync_create_all()
# insert_data()

# get_tables_list()