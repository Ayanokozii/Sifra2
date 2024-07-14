import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "21189715"))

API_HASH = getenv("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")

BOT_TOKEN = getenv("BOT_TOKEN","7026867682:AAFycHPHsYqgPAocCrzqjhmyuS1JITJ6DE4")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ayanosuvii0925:subhichiku123@cluster0.uw8yxkl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1001956979385"))

OWNER_ID = int(getenv("OWNER_ID", "7181106700"))

BOT_USERNAME = getenv("BOT_USERNAME" , "SIFRABABYBOT")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ayanokozii/Sifra2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Anya")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/the_galaxiess")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+M8_IeSaHIzUxOGQ9")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION",  "BQFDVFMAUfdfYKLuy3xKlT9Vi5xu3Ch2Juz34jwR-qpWv4iRDtWK-3edMY7s4harMZKyGMVgTGhFjgFwIvJApXlHIYORgTw6LT0xEzuUtx4dw8Ry6y5PV1W5OvnL5-3uorKryTG71z4iIMQrCh978qEut6gRn0SwdDlNtDsomPGtkmIwlpWxCsRtf6KiFgLDxqy1dT7oq8pHe1Q006qc4SL2CT8AH8-bWtD7m_jpxEyfmYFECYbp-MkRG4GI2hpxXLkFziStnyfFbU1rq-Izi-dBHcYJNMM_ym4pQv5PWgz9e44i4U-SfwQvo75ZceBx7qQzlkGAcfB4vReRMfLVK_TsukvgAAAAGSN1vtAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/35e597d603805ff589220.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/4a7c28726502e24ea0fe0.jpg"
TELEGRAM_AUDIO_URL = "ttps://telegra.ph/file/81df44f3679946babd8c3.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/16d7dd76f4ce8b8b01fdf.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/53f1a295e172d39eaa39d.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
YOUTUBE_IMG_URL = "ttps://telegra.ph/file/81df44f3679946babd8c3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/35e597d603805ff589220.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
