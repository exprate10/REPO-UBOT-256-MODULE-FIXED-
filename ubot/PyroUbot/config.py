import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "9999"))

DEVS = list(map(int, os.getenv("DEVS", "1311431740").split()))

API_ID = int(os.getenv("API_ID", "38773229"))

API_HASH = os.getenv("API_HASH", "e1885e331667b7e028d7970862aa9594")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8603580422:AAGFTEh2_QSU8PmNhFc6S943pTypCtcOlew")

OWNER_ID = int(os.getenv("OWNER_ID", "1311431740"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003836888284").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://dwiputrasiswantofahrel_db_user:7s4Xzy6GwzscxNSD@cluster0.j1fmojl.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003841423220"))

OWNER_USERNAME = os.getenv("OWNER_USERNAME", "RanzOffc")

MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "AboutRanzOffc")

NOTIFY_CHANNEL = os.getenv("NOTIFY_CHANNEL", "AllTestiRanzOffc")

PAKASIR_BASE_URL = os.getenv("PAKASIR_BASE_URL", "https://app.pakasir.com/api")

PAKASIR_PROJECT = os.getenv("PAKASIR_PROJECT", "")

PAKASIR_API_KEY = os.getenv("PAKASIR_API_KEY", "")

PAYMENT_TIMEOUT = int(os.getenv("PAYMENT_TIMEOUT", "600"))

PAYMENT_CHECK_INTERVAL = int(os.getenv("PAYMENT_CHECK_INTERVAL", "10"))

NOTIFY_THUMBNAIL = os.getenv("NOTIFY_THUMBNAIL", "https://files.catbox.moe/pgaypk.jpg")

START_PHOTO = os.getenv("START_PHOTO", "https://files.catbox.moe/pgaypk.jpg")

ROLE_PRICES = {
    "member": {"1": int(os.getenv("PRICE_MEMBER_BULAN", "5000")), "0": int(os.getenv("PRICE_MEMBER_PERMA", "10000"))},
    "seles": {"1": int(os.getenv("PRICE_SELES_BULAN", "10000")), "0": int(os.getenv("PRICE_SELES_PERMA", "20000"))},
    "admin": {"1": int(os.getenv("PRICE_ADMIN_BULAN", "20000")), "0": int(os.getenv("PRICE_ADMIN_PERMA", "35000"))},
}
