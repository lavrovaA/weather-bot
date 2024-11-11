import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'API_TOKEN = '7875187497:AAFUJY8hrrnbSOhROzVvRnKebKVpg_bcXN0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):


    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


    def get_weather_samara():
        city = "Самара"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={'a5850ea17889ef4a54e03e21cbfdb6f2'}&units=metric&lang=ru"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather_desc = data['weather'][0]['description'].capitalize()
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            city_name = data['name']
            country = data['sys']['country']
            return (
                f"🌤 Погода в {city_name}, {country}:\n"
                f"Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"Описание: {weather_desc}\n"
                f"Влажность: {humidity}%\n"
                f"Скорость ветра: {wind_speed} м/с"
            )
        else:
            return '❌ Не удалось получить данные о погоде.'