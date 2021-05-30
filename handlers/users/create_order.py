from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp, bot
from data.items import POST_FAST_SHIPPING, POST_REGULAR_SHIPPING, PICKUP_SHIPPING, Xiaomi_Poco_X3_Pro, \
    Xiaomi_Redmi_Note_10, Xiaomi_Mi_11_Lite, Xiaomi_Mi_Smart_Band_6, Xiaomi_Deerma_TB800, Xiaomi_Mi_Body_Scale_2

"""
Доп информация:

https://core.telegram.org/bots/api#sendinvoice
https://surik00.gitbooks.io/aiogram-lessons/content/chapter4.html
"""


@dp.message_handler(Command("smartphone_x3"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **Xiaomi_Poco_X3_Pro.generate_invoice(),
                           payload="123456")

@dp.message_handler(Command("smartphone_note_10"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **Xiaomi_Redmi_Note_10.generate_invoice(),
                           payload="123457")

@dp.message_handler(Command("smartphone_11_lite"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **Xiaomi_Mi_11_Lite.generate_invoice(),
                           payload="123457")


#Товары из раздела "ДЕВАЙСЫ"

@dp.message_handler(Command("devices_smart_band"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **Xiaomi_Mi_Smart_Band_6.generate_invoice(),
                           payload="1234578")

@dp.message_handler(Command("devices_deerma_tb800"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **Xiaomi_Deerma_TB800.generate_invoice(),
                           payload="12345789")

@dp.message_handler(Command("devices_body_scale_2"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **Xiaomi_Mi_Body_Scale_2.generate_invoice(),
                           payload="12345789")



#Выбор доставки

@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code == "BY":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[POST_FAST_SHIPPING, POST_REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    elif query.shipping_address.country_code == "US":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Сюда не доставляем")
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[POST_REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Спасибо за покупку! Ожидайте отправку")
