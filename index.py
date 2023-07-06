from fastapi import FastAPI
from routes.user import user

app = FastAPI()


#connects to the router user

app.include_router(user)


