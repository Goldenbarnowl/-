from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
#from pydantic_settings import BaseSettings

# class Secrets(BaseSettings):
#     token: str
#     admin_id: int
#     supabase_url: str
#     supabase_key: str
#     redis_url: str
#
#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#
#
# secrets = Secrets()

# Инициализация бота
default = DefaultBotProperties(parse_mode='HTML', protect_content=False)
bot = Bot(token="8014287736:AAFE9Go0_C8BpkJYBuyzHnYvEq2raEbQ66E", default=default)
dp = Dispatcher()
