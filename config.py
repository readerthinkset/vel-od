"""VELOCITY ODIA - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY ODIA"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "ODIA"
HANDLE = "@velocityodia"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "or",
    "name": "Odia",
    "native_name": "ଓଡ଼ିଆ",
    "history_key": "odia",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "",
    "native_fallback_voice": "",
    "native_engine": "mms",
    "native_lang_code": "or",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "ଓଡ଼ିଆ",
    "translit_label": "SAY IT LIKE",
    "greeting": "ନମସ୍କାର!",
    "encouragement": "ଅଦ୍ଭୁତ!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "NotoSansOriya-Bold.ttf",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "ନମସ୍କାର", "hand", "#1CB0F6"),
    ("Basic Phrases", "ମୌଳିକ ବାକ୍ୟ", "chat", "#58CC02"),
    ("Common Expressions", "ସାଧାରଣ ଅଭିବ୍ୟକ୍ତି", "chat", "#1CB0F6"),
    ("Travel", "ଯାତ୍ରା", "plane", "#1CB0F6"),
    ("Restaurant", "ରେଷ୍ଟୁରାଣ୍ଟ", "fork", "#FF7A00"),
    ("Shopping", "କିଣାବିକା", "bag", "#E056A0"),
    ("Emergency", "ଜରୁରୀକାଳୀନ", "siren", "#FF4B4B"),
    ("Family Terms", "ପରିବାର ଶବ୍ଦ", "heart", "#E056A0"),
    ("Numbers", "ସଂଖ୍ୟା", "hash", "#A560E8"),
    ("Time", "ସମୟ", "clock", "#00A889"),
    ("Motivation", "ପ୍ରେରଣା", "rocket", "#A560E8"),
    ("Love", "ପ୍ରେମ", "heart", "#FF4B4B"),
    ("Success", "ସଫଳତା", "trophy", "#F5A700"),
    ("Wisdom", "ଜ୍ଞାନ", "book", "#A560E8"),
    ("Happiness", "ଖୁସି", "smile", "#F5A700"),
    ("Self Improvement", "ଆତ୍ମ-ଉନ୍ନତି", "leaf", "#58CC02"),
    ("Gratitude", "କୃତଜ୍ଞତା", "heart", "#FF7A00"),
    ("Friendship", "ବନ୍ଧୁତା", "users", "#00A889"),
    ("Hope", "ଆଶା", "sun", "#FF7A00"),
    ("Creativity", "ସୃଜନଶୀଳତା", "palette", "#E056A0"),
    ("Inner Peace", "ଆନ୍ତରିକ ଶାନ୍ତି", "lotus", "#00A889"),
    ("Confidence", "ଆତ୍ମବିଶ୍ୱାସ", "shield", "#1CB0F6"),
    ("Perseverance", "ଦୃଢ଼ତା", "mountain", "#FF7A00"),
    ("Inspiration", "ପ୍ରେରଣା", "sparkles", "#A560E8"),
    ("Positive Life", "ସକାରାତ୍ମକ ଜୀବନ", "sun", "#58CC02"),
    ("Courage", "ସାହସ", "shield", "#FF4B4B"),
    ("Kindness", "ଦୟା", "heart", "#E056A0"),
    ("Patience", "ଧୈର୍ଯ୍ୟ", "hourglass", "#00A889"),
    ("Forgiveness", "କ୍ଷମା", "hands", "#FF7A00"),
    ("Strength", "ଶକ୍ତି", "dumbbell", "#FF4B4B"),
    ("Joy", "ଆନନ୍ଦ", "smile", "#F5A700"),
    ("Balance", "ସନ୍ତୁଳନ", "scale", "#00A889"),
    ("Growth", "ବୃଦ୍ଧି", "sprout", "#58CC02"),
    ("Purpose", "ଉଦ୍ଦେଶ୍ୟ", "target", "#A560E8"),
    ("Mindfulness", "ସଚେତନତା", "lotus", "#00A889"),
    ("Daily Routine", "ଦୈନିକ ରୁଟିନ୍", "calendar", "#1CB0F6"),
    ("Weather", "ପାଣିପାଗ", "cloud", "#1CB0F6"),
    ("Feelings", "ଭାଵନା", "smile", "#E056A0"),
    ("Food", "ଖାଦ୍ଯ", "fork", "#FF7A00"),
    ("Health", "ସ୍ୱାସ୍ଥ୍ଯ", "heart", "#58CC02"),
    ("Work", "କାମ", "briefcase", "#1CB0F6"),
    ("Technology", "ଟେକ୍ନୋଲୋଜି", "chip", "#A560E8"),
    ("Nature", "ପ୍ରକୃତି", "leaf", "#58CC02"),
    ("Animals", "ପ୍ରାଣୀ", "paw", "#FF7A00"),
    ("Colors", "ରଙ୍ଗ", "palette", "#E056A0"),
    ("Directions", "ଦିଗ", "compass", "#1CB0F6"),
    ("Body Parts", "ଶରୀରର ଅଂଶ", "hand", "#00A889"),
    ("Clothes", "ପୋଷାକ", "shirt", "#E056A0"),
    ("Music", "ସଙ୍ଗୀତ", "music", "#A560E8"),
    ("Sports", "ଖେଳ", "ball", "#FF7A00"),
    ("Holidays", "ଛୁଟିଦିନ", "gift", "#FF4B4B"),
    ("Education", "ଶିକ୍ଷା", "book", "#1CB0F6"),
    ("Culture", "ସଙ୍ସ୍କୃତି", "globe", "#00A889"),
    ("Finance", "ଅର୍ଥ", "coin", "#58CC02"),
    ("Relationships", "ସମ୍ପର୍କ", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnodia",
    "#odialessons",
    "#odiaforbeginners",
    "#languagelearning",
    "#odiavocabulary",
    "#velocityodia",
    "#dailyodia",
    "#odia",
    "#learnlanguages",
    "#speakodia",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
