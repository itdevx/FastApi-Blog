from fastapi import FastAPI
from routers.users import router as user_router
from routers.posts import router as post_router
from db.engine import Base, engine

app = FastAPI()


@app.on_event('startup')
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(user_router, prefix='/users')
app.include_router(post_router, prefix='/article')