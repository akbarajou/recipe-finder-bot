import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
import requests



# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# # Telegram bot token and spoonacular api
TELEGRAM_BOT_TOKEN = '7147713355:AAGWW1p2nSdWxYMdFymg0Fa4Gd7JcEwOsxg'
SPOONACULAR_API_KEY = 'e96e7383653c408f904671a4683c5abd'


# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Hi! I am Recipe Finder Bot. Send me ingredients separated by commas, and I will find recipes for you!"
    )


def find_recipes(ingredients):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        'apiKey': SPOONACULAR_API_KEY,
        'ingredients': ingredients,
        'number': 5
    }
    response = requests.get(url, params=params)
    return response.json()

@dp.message_handler()
async def get_recipe(message: types.Message):
    ingredients = message.text
    recipes = find_recipes(ingredients)
    if not recipes:
        await message.reply("Sorry, I couldn't find any recipes with those ingredients.")
        return
    
    for recipe in recipes:
        title = recipe['title']
        recipe_id = recipe['id']
        recipe_url = f"https://spoonacular.com/recipes/{title.replace(' ', '-')}-{recipe_id}"
        await message.reply(f"[{title}]({recipe_url})", parse_mode=ParseMode.MARKDOWN)



if __name__ == '__main__':
    # Start polling
    executor.start_polling(dp, skip_updates=True)

