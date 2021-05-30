from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import allowed_users
from loader import dp, bot


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать при этом на кнопку",
                    parse_mode="HTML"
                ),
            ),
        ],

        cache_time=5)


@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_users:
        await query.answer(
            results=[],
            switch_pm_text="Бот недоступен. Подключить бота",
            switch_pm_parameter="connect_user",
            cache_time=5)
        return
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Смартфон Xiaomi Poco X3 Pro",
                input_message_content=types.InputTextMessageContent(
                    message_text="/smartphone_x3",
                ),
                url="https://xiaomi-store.by/catalog/smartfony/smartfon-xiaomi-poco-x3-pro",
                thumb_url="https://xiaomi-store.by/models/1416/2/smartfon-xiaomi-poco-x3-pro-1.jpg",
                description="Смартфон POCO X3 Pro идеально подойдет любителям Xiaomi, или тем, кто хочет стать таковым. Смартфон практически не отличается от предыдущих моделей — удобный размер, и привычная система. Перебраться со старенького Xiaomi на новый POCO не составит труда. В отличие от AMOLED дисплеев, использованный качественный IPS-экран не мерцает, имеет высокое разрешение, а также частоту обновления 120 Гц."
            ),
            types.InlineQueryResultArticle(
                id="2",
                title="Смартфон Xiaomi Redmi Note 10",
                input_message_content=types.InputTextMessageContent(
                    message_text="/smartphone_note_10",
                ),
                url="https://xiaomi-store.by/catalog/smartfony/smartfon-xiaomi-redmi-note-10",
                thumb_url="https://xiaomi-store.by/models/1400/2/smartfon-xiaomi-redmi-note-10-1.jpg",
                description="Оперативная память: 4/6 Гб, LPDDR4x. Постоянная память: 64/128 Гб, UFS 2.2. Основная камера: основной модуль: 48 Мп Sony IMX582 (f/1.79) / широкоугольный 8 Мп Sony IMX355 / макродатчик 2 Мп GalaxyCore GC02M1 / датчик глубины 2 Мп OmniVision OV02B1B. Фронтальная камера: 13 Мп Omnivision OV13B10."
            ),
            types.InlineQueryResultArticle(
                id="3",
                title="Смартфон Xiaomi Mi 11 Lite",
                input_message_content=types.InputTextMessageContent(
                    message_text="/smartphone_11_lite",
                ),
                url="https://xiaomi-store.by/catalog/smartfony/smartfon-xiaomi-mi-11-lite",
                thumb_url="https://xiaomi-store.by/models/1399/2/smartfon-xiaomi-mi-11-lite-1.jpg",
                description="Экран: AMOLED, 6,55 дюйма, 2400 × 1080, 402 ppi, Gorilla Glass 5, HDR 10, 90 Гц; Память: 6 или 8 ГБ оперативной, 64 или 128 ГБ встроенной, слот для microSD; Камеры: основная 64 Мп, 26 мм (f/1.8); сверхширокоугольная 8 Мп, 119° (f/2.2); макро 5 Мп (f/2.4); фронтальная 16 Мп, 25 мм (f/2.5)"
            ),
            types.InlineQueryResultArticle(
                id="4",
                title="Фитнес браслет с пульсометром Xiaomi Mi Smart Band 6",
                input_message_content=types.InputTextMessageContent(
                    message_text="/devices_smart_band",
                ),
                url="https://xiaomi-store.by/catalog/umnye-chasy-fitnes-braslety-gps-trekery/fitnes-braslet-s-pulsometrom-xiaomi-mi-smart-band-6",
                thumb_url="https://xiaomi-store.by/models/1414/2/fitnes-braslet-s-pulsometrom-xiaomi-mi-smart-band-6--1.jpg",
                description="Сенсор спортивной активности «прокачали» — Xiaomi MiBand 6 умеет отслеживать уровень кислорода в крови SpO2, мониторить сон и стресс, параметры активности с высокой точностью. ... Новая долгожданная модель Xiaomi была разработана, как и все предыдущие популярные фитнес-браслеты, в сотрудничестве с Huami."
            ),
            types.InlineQueryResultArticle(
                id="5",
                title="Швабра с распылителем Evolution Powered by Deerma TB800 2F",
                input_message_content=types.InputTextMessageContent(
                    message_text="/devices_deerma_tb800",
                ),
                url="https://xiaomi-store.by/catalog/bytovaya-tehnika/shvabra-s-raspylitelem-evolution-powered-by-deerma-tb800-2f",
                thumb_url="https://xiaomi-store.by/models/1248/2/shvabra-s-raspylitelem-evolution-powered-by-deerma-tb800-2f-0.jpg",
                description="Швабра с распылителем EVOLUTION TB800 2F - компактное устройство, которое не занимает много места в доме и обеспечивает быстрый и долговременный эффект от уборки. За счёт использования в процессе работы жидкости, можно сэкономить время и силы и за меньший срок обработать более значительное пространство. Раньше приходилось несколько раз наклоняться и мочить тряпку, теперь достаточно лишь наполнить водой резервуар, чтобы без лишних усилий вымыть пол в своем доме. Чтобы обеспечить еще большую чистоту в квартире, можно добавить в резервуар различные чистящие и дезинфицирующие средства. От грязи и вредных веществ не останется ни следа!"
            ),
            types.InlineQueryResultArticle(
                id="6",
                title="Умные напольные весы Xiaomi Mi Body Composition Scale 2",
                input_message_content=types.InputTextMessageContent(
                    message_text="/devices_body_scale_2",
                ),
                url="https://xiaomi-store.by/catalog/krasota-i-zdorove/umnye-napolnye-vesy-xiaomi-mi-body-composition-scale-2",
                thumb_url="https://xiaomi-store.by/models/817/2/umnye-napolnye-vesy-xiaomi-mi-body-composition-scale-2-2.jpg",
                description="Xiaomi Mi Body Composition Scale 2 умеет с высокой точностью измерять вес больших тел и малых тел массой до 100 г. Измерение может происходить как в динамическом, так и в статическом режиме."
            )

        ],
    )


@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer("Вы подключены",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                     text="Войти в инлайн режим",
                                     switch_inline_query_current_chat="Выбрать")

                                 ]
                             ]

                         ))
