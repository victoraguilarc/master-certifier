import lambdawarmer
from mangum import Mangum
from src.fastapi_app import app

handler = Mangum(app=app)


@lambdawarmer.warmer
def wrapper(event, context):
    return handler(event, context)
