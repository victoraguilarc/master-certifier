from mangum import Mangum
from src.fastapi_app import app

handler = Mangum(app=app)
