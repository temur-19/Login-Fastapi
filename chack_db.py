import asyncio
import os

import asyncpg
from dotenv import load_dotenv
from sqlalchemy.engine import make_url

load_dotenv()

raw = os.getenv("ASYNC_DATABASE_URL")
url = make_url(raw)
print("URL:", url.render_as_string(hide_password=True))


async def main():
    conn = await asyncpg.connect(
        user=url.username,
        password=url.password,
        host=url.host,
        port=url.port,
        database=url.database,
    )
    print("OK, current_user =", await conn.fetchval("select current_user"))
    await conn.close()


asyncio.run(main())