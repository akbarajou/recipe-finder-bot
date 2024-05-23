
# Recipe Finder Bot

This is a Telegram bot that finds recipes based on ingredients provided by the user. The bot uses the Spoonacular API to fetch recipe suggestions.

## Features

- Responds to the `/start` command with a welcome message.
- Takes a list of ingredients as input and returns up to 5 recipe suggestions.
- Provides recipe titles and links to the full recipes.

## Requirements

- Python 3.10.12
- `aiogram` library version 2.25.1
- `requests` library

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/recipe-finder-bot.git
   cd recipe-finder-bot

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate
 
3. Install the required libraries:
   ```sh
   pip install -r requirements.txt

4. Replace <b>TELEGRAM_BOT_TOKEN</b> and <b>SPOONACULAR_API_KEY</b> with your token and API