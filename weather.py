import asyncio
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import Command
import requests
from ali import *


API_KEY =  "eb8b255c8d239e70fe1a5863b74b6375"

bot = Bot(token="7684934155:AAH_sSnKzsUT3GjoQc6aySBsN4D_gRWF6zE")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Ob-havo botga hush kelibsiz")

@dp.message()
async def weather(message:types.Message):
    city_name= message.text
    url = f"https://api.weatherstack.com/current?access_key={API_KEY}&query={city_name}"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "current" not in data:
        await message.reply("Iltimos shahar nomini kiriting.")
        return

    location = data.get("location", {})
    current_weather = data.get("current", {})

    city = location.get("name", "Noma'lum")
    country = location.get("country", "")
    temperature = current_weather.get("temperature", "N/A")
    weather_desc = current_weather.get("weather_descriptions", ["No description available"])[0]
    humidity = current_weather.get("humidity", "N/A")
    wind_speed = current_weather.get("Windspeed", "N/A")

    weather_message = f"🌍 Shahar: {city}, {country}\n" \
                      f"🌡 Temperatur: {temperature}°C\n" \
                      f"☁️ Ob-havo: {weather_desc}\n" \
                      f"💧 Namlik: {humidity}%\n" \

    await message.reply(weather_message)

@dp.message()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())