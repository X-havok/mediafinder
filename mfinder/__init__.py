import os
import re
import logging
import logging.config
from dotenv import load_dotenv


load_dotenv()


id_pattern = re.compile(r"^.\d+$")

# vars
APP_ID = os.environ.get("APP_ID", "21575315")
API_HASH = os.environ.get("API_HASH", "acdbe0573a6babdf1dfa88d113ed02c3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8244467113:AAEDT7JdLQ4MoTKSLtevvrSuP1peGf74aDA")
DB_URL = os.environ.get("DB_URL", "postgresql://postgres:qizCtxi0LMCeo0VH@db.dbjedxgpalanniklrmyi.supabase.co:5432/postgres")
OWNER_ID = int(os.environ.get("OWNER_ID", "8211074909"))
ADMINS = [
    int(user) if id_pattern.search(user) else user
    for user in os.environ.get("ADMINS", "8211074909").split()
] + [OWNER_ID]
DB_CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in os.environ.get("DB_CHANNELS", "-1003576663047").split()
]

try:
    import const
except Exception:
    import sample_const as const

START_MSG = const.START_MSG
START_KB = const.START_KB
HELP_MSG = const.HELP_MSG
HELP_KB = const.HELP_KB


# logging Conf
logging.config.fileConfig(fname="config.ini", disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

