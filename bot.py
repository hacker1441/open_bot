import logging 

from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
from keyboards import *


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "5806211557:AAG2-zPKu0JkTYy7qxNWVYiEfXA7tq5glQw"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    btn = await start_menu()
    await message.answer("""Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin.

Unutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.

🚀 Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.
Telefon raqamingizni +998901234567 shaklida yuboring.""", reply_markup=btn)

@dp.message_handler(text=['🗳 Ovoz berish'])
async def start_bot(message: Message):
    # btn = await start_menu()
    await message.answer("""📞 Ovoz berish uchun telefon raqamingizni kiriting:

Na'muna: +998991234567

✅ Ovoz berish muvaffaqiyatli o'tganda, hisobingizga o'tkazib beriladigan summa: 12000 UZS""")

@dp.message_handler(text=['💰 Balans'])
async def start_bot(message: Message):
    btn = await balans_menu()
    await message.answer("""💰 Sizning hisobingiz: 0 so'm
📥 Yechib olish uchun minimal summa: 5000 so'm

📌 Pulingizni yechib olish uchun «💳 Yechib olish» tugmasidan foydalaning.""", reply_markup=btn)

@dp.message_handler(text=['💳 Yechib olish'])
async def start_bot(message: Message):
    # btn = await balans_menu()
    await message.answer("""💳 Telefon yoki karta raqamingizni kiriting:

⚠️ Bot Humans nomerga to'lov qilmaydi.

📄 Na'muna:
📱 Telefon raqam: +998912345678
💳 Karta raqam: 8600111122223333""")
    
@dp.message_handler(text=['✖️ Bekor qilish'])
async def start_bot(message: Message):
    btn = await start_menu()
    await message.answer("""Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin.

Unutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.

🚀 Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.
Telefon raqamingizni +998901234567 shaklida yuboring""", reply_markup=btn)
    
@dp.message_handler(text=['🔗 Referal ssilka'])
async def start_bot(message: Message):
    btn = await ehe_list()
    photo = InputFile("ob.jpg")
    await message.answer_photo(photo=photo, caption="""🔗 Referallaringiz soni: 0 ta
💸 Referal uchun to'lov: 5000 so'm

Sizning referal ssilkangiz👇🏻
https://t.me/OpenBudgetgaOvoz_Bot?start=1599341582""", reply_markup=btn)

@dp.message_handler(text="📝 Qo'llanma")
async def start_bot(message: Message):
    # btn = await ehe_list()
    video = InputFile("open2.mp4")
    await message.answer_video(video=video, caption="""📌 Botdan foydalanish qo'llanmasi:

1. «🗳 Ovoz berish» knopkasini bosing va nomeringizni yozib qoldiring.

2. Bot sizga matemtik misol beradi shuni javobini botga yuboring misol uchun 2+3= shunaqa misol yuborsa 5 deb javobni o'zini yuborasiz.

3. Nomerizga sms kod keladi shuni botga yozb qoldiring va bot sizga 12000 ming so'm pul beradi.

Pulni nomerizga Paynet qilib yoki plastik raqamizga «💰 Balans» knopkasi orqali pulni yechib olishiz mumkun 🥳""")


if __name__ == "__main__":
    executor.start_polling(dp)