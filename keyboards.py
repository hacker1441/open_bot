from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def start_menu():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    [
    btn.row("🗳 Ovoz berish", "💰 Balans")
    ]
    [
    btn.row("🔗 Referal ssilka", "📝 Qo'llanma")
    ]
    return btn


async def balans_menu():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    [
    btn.row("💳 Yechib olish")
    ]
    [
    btn.row("✖️ Bekor qilish")
    ]
    return btn

async def ehe_list():
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("Do'stlarmi taklif qilish", callback_data='n1'),
    )
    return btn