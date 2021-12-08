from fastapi import FastAPI
from .routes import main_router
from .db import create_db_and_tables, engine

app = FastAPI(
    title="jellysmack_test",
    description="jellysmack_test API 🚀",
    version="1.0.0",
    contact={
        "name": "valentincosson",
        "url": "https://valentin-cosson.fr",
        "email": "contact@valentin-cosson.fr",
    },
)

app.include_router(main_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)
