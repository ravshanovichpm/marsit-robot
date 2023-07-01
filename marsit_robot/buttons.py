from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

glavniy_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍👩‍👧‍👦Я Родитель", callback_data="Я Родитель"),
            InlineKeyboardButton(text="🧑‍🎓Я Студент", callback_data="Я Студент"),
            InlineKeyboardButton(text="👦Я Гость", callback_data="Я Гость"),
        ]
    ]
)


ota_ona_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏫О школе"),
            KeyboardButton(text="👨‍👩‍👧‍👦Добавить ребёнка"),
        ],
    ],
    resize_keyboard=True
)

uchenik_keyboard = ReplyKeyboardMarkup( 
    keyboard=[
        [
            KeyboardButton(text="🧑‍🎓Профиль"),
            KeyboardButton(text="🪙Мои монеты"),
            KeyboardButton(text="💥Space shop"),
        ],
        [
            KeyboardButton(text="🏫О школе"),
            KeyboardButton(text="✍️Оставить отзыв"),
        ],
    ],
    resize_keyboard=True
)

space_shop_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="MARS mini", callback_data="MARS mini"),
            InlineKeyboardButton(text="MARS Sticker", callback_data="MARS Sticker"),
        ],
        [
            InlineKeyboardButton(text="Usb fleshka", callback_data="Usb fleshka"),
            InlineKeyboardButton(text="MARS chocolate", callback_data="MARS chocolate"),
        ],
        [
            InlineKeyboardButton(text="Mouse", callback_data="Mouse"),
            InlineKeyboardButton(text="Strobar", callback_data="Strobar"),
        ],
    ],
)

mars_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Имя", callback_data="Имя"),
            InlineKeyboardButton(text="Фамилия", callback_data="Фамилия"),
        ],
        [
            InlineKeyboardButton(text="Язык", callback_data="Язык"),
            InlineKeyboardButton(text="Телефон", callback_data="Телефон"),
        ],
        [
            InlineKeyboardButton(text="Город", callback_data="Город"),
        ],
    ]
)

shkola_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Работы учеников", callback_data="Работы учеников"),
            InlineKeyboardButton(text="Преподователи", callback_data="Преподователи"),
        ],
        [
            InlineKeyboardButton(text="Отзывы", callback_data="Отзывы"),
            InlineKeyboardButton(text="Экскурсия по школе", callback_data="Экскурсия по школе"),
        ],
        [
            InlineKeyboardButton(text="Философия школы", callback_data="Философия школы"),
        ],
    ]
)

# otziv_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="14-16 лет", callback_data="14-16 лет"),
#             InlineKeyboardButton(text="8-10 лет", callback_data="8-10 лет")
#         ]
#     ]
# )