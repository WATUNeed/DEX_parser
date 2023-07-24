import asyncio
from datetime import datetime
import aiogram
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from dodo import dodo_resp
from inch import inch_resp


# bot = Bot(token='6513422565:AAGcdhP9Dh12HcZ2diNKPEJYQJu6msULyJw')
#
# dp = Dispatcher(bot)


# folowers = []


# @dp.message_handler(commands=['start'])
# async def start_command_handler(msg: aiogram.types.Message):
#     folowers.append(msg.chat.id)
#     await msg.answer('подключен. ждите связку')


# async def st(dp: Dispatcher):
#     i = 0
#     while True:
#         if folowers:
#             for item in folowers:
#                 await bot.send_message(item, 'test')
#         try:
#             dodo_data = await dodo_resp()
#             inch_data = await inch_resp(dodo_data[0])
#             if float(inch_data[0]) >= 100:
#                 data = f'[{datetime.now()}] DODO: USDT = 100 -> MATIC = {dodo_data[0]} | fee: {dodo_data[1]} \n[{datetime.now()}] 1INCH: MATIC = {dodo_data[0]} -> USDT = {inch_data[0]} | fee: {inch_data[1]}'
#                 print(data)
#                 if folowers:
#                     for item in folowers:
#                         await bot.send_message(item, data)
#         except Exception as e:
#             with open('exceptions.txt', 'a+') as f:
#                 f.write(str(e))
#             pass
#         with open('resp.txt', 'w') as f:
#             f.write(str(i) + '\n')
#         i += 1


if __name__ == '__main__':
    i = 0
    while True:
        try:
            dodo_data = dodo_resp()
            inch_data = inch_resp(dodo_data[0])
            if float(inch_data[0]) >= 100:
                data = f'[{datetime.now()}] DODO: USDT = 100 -> MATIC = {dodo_data[0]} | fee: {dodo_data[1]} \n[{datetime.now()}] 1INCH: MATIC = {dodo_data[0]} -> USDT = {inch_data[0]} | fee: {inch_data[1]}'
                print(data)
        except Exception as e:
            with open('exceptions.txt', 'a+') as f:
                f.write(str(e))
            pass
        with open('resp.txt', 'w') as f:
            f.write(str(i) + '\n')
        i += 1

