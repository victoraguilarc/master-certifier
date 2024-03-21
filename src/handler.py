from mangum import Mangum
from mangum.types import LambdaContext

from src.fastapi_app import app

handler = Mangum(app=app)


def wrapped_handler(event: dict, context: LambdaContext):
    if event.get('source') == 'serverless-plugin-warmup':
        return
    return handler(event, context)
