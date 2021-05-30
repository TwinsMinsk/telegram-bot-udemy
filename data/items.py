from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.item import Item

Xiaomi_Poco_X3_Pro = Item(
    title="Смартфон Xiaomi Poco X3 Pro",
    description="Смартфон POCO X3 Pro идеально подойдет любителям Xiaomi, или тем, кто хочет стать таковым."
                "Смартфон практически не отличается от предыдущих моделей — удобный размер, и привычная система."
                "Перебраться со старенького Xiaomi на новый POCO не составит труда."
                "В отличие от AMOLED дисплеев, использованный качественный IPS-экран не мерцает, имеет высокое разрешение, а также частоту обновления 120 Гц.",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Xiaomi Poco X3 Pro",
            amount=999_00
        )
    ],
    start_parameter="create_invoice_xiaomi_poco_x3_pro",
    photo_url="https://xiaomi-store.by/models/1416/2/smartfon-xiaomi-poco-x3-pro-1.jpg",
)

Xiaomi_Redmi_Note_10 = Item(
    title="Смартфон Xiaomi Redmi Note 10",
    description="Оперативная память: 4/6 Гб, LPDDR4x. Постоянная память: 64/128 Гб, UFS 2.2."
                "Основная камера: основной модуль: 48 Мп Sony IMX582 (f/1.79)"
                "Щирокоугольный 8 Мп Sony IMX355 / макродатчик 2 Мп GalaxyCore GC02M1 / датчик глубины 2 Мп OmniVision OV02B1B."
                "Фронтальная камера: 13 Мп Omnivision OV13B10.",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Xiaomi",
            amount=35_000_00
        ),
        LabeledPrice(
            label="Доставка",
            amount=15_000_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-5_000_00
        ),
        LabeledPrice(
            label="НДС",
            amount=10_000_00
        ),
    ],
    need_shipping_address=True,
    start_parameter="create_invoice_xiaomi_redmi_note_10",
    photo_url="https://xiaomi-store.by/models/1400/2/smartfon-xiaomi-redmi-note-10-1.jpg",
    photo_size=600,
    is_flexible=True
)

Xiaomi_Mi_11_Lite = Item(
    title="Смартфон Xiaomi Mi 11 Lite",
    description="Экран: AMOLED, 6,55 дюйма, 2400 × 1080, 402 ppi, Gorilla Glass 5, HDR 10, 90 Гц;"
                "Память: 6 или 8 ГБ оперативной, 64 или 128 ГБ встроенной, слот для microSD;"
                "Камеры: основная 64 Мп, 26 мм (f/1.8); сверхширокоугольная 8 Мп, 119° (f/2.2); макро 5 Мп (f/2.4); фронтальная 16 Мп, 25 мм (f/2.5)",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Xiaomi",
            amount=25_000_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-5_000_00
        ),
    ],
    need_shipping_address=True,
    start_parameter="create_invoice_xiaomi_mi_11_lite",
    photo_url="https://xiaomi-store.by/models/1399/2/smartfon-xiaomi-mi-11-lite-1.jpg",
    photo_size=600,
    is_flexible=True
)

# Товары из раздела "РАЗНОЕ"

Xiaomi_Mi_Smart_Band_6 = Item(
    title="Фитнес браслет с пульсометром Xiaomi Mi Smart Band 6",
    description="Сенсор спортивной активности «прокачали» — Xiaomi MiBand 6 умеет отслеживать уровень кислорода в крови SpO2,"
                "мониторить сон и стресс, параметры активности с высокой точностью. ..."
                "Новая долгожданная модель Xiaomi была разработана, как и все предыдущие популярные фитнес-браслеты, в сотрудничестве с Huami.",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Xiaomi_Mi_Band",
            amount=8_000_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-1_000_00
        ),
    ],
    need_shipping_address=True,
    start_parameter="create_invoice_xiaomi_mi_smart_band_6",
    photo_url="https://xiaomi-store.by/models/1414/2/fitnes-braslet-s-pulsometrom-xiaomi-mi-smart-band-6--1.jpg",
    photo_size=600,
    is_flexible=True
)

Xiaomi_Deerma_TB800 = Item(
    title="Швабра с распылителем Evolution Powered by Deerma TB800 2F",
    description="Швабра с распылителем EVOLUTION TB800 2F - компактное устройство,"
                "которое не занимает много места в доме и обеспечивает быстрый и долговременный эффект от уборки."
                "За счёт использования в процессе работы жидкости, можно сэкономить время и силы "
                "и за меньший срок обработать более значительное пространство.",

    currency="RUB",
    prices=[
        LabeledPrice(
            label="Xiaomi_Deerma_TB800",
            amount=10_000_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-1_500_00
        ),
    ],
    need_shipping_address=True,
    start_parameter="create_invoice_xiaomi_deerma_tb800",
    photo_url="https://xiaomi-store.by/models/1248/2/shvabra-s-raspylitelem-evolution-powered-by-deerma-tb800-2f-0.jpg",
    photo_size=600,
    is_flexible=True
)

Xiaomi_Mi_Body_Scale_2 = Item(
    title="Умные напольные весы Xiaomi Mi Body Composition Scale 2",
    description="Xiaomi Mi Body Composition Scale 2 умеет с высокой точностью измерять вес больших тел и малых тел массой до 100 г." \
                "Измерение может происходить как в динамическом, так и в статическом режиме.",

    currency="RUB",
    prices=[
        LabeledPrice(
            label="Xiaomi_Mi_Body_Scale_2",
            amount=10_000_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-1_500_00
        ),
    ],
    need_shipping_address=True,
    start_parameter="create_invoice_xiaomi_mi_body_scale",
    photo_url="https://xiaomi-store.by/models/817/2/umnye-napolnye-vesy-xiaomi-mi-body-composition-scale-2-2.jpg",
    photo_size=600,
    is_flexible=True
)




#Виды доставки



POST_REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Почтой',
    prices=[
        types.LabeledPrice(
            'Обычная коробка', 0),
        types.LabeledPrice(
            'Почтой обычной', 1000_00),
    ]
)
POST_FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Почтой (vip)',
    prices=[
        types.LabeledPrice(
            'Супер прочная коробка', 1000_00),
        types.LabeledPrice(
            'Почтой срочной - DHL (3 дня)', 3000_00),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title='Самовывоз',
                                       prices=[
                                           types.LabeledPrice('Самовывоз из магазина', -100_00)
                                       ])
