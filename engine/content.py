"""AI phrase generation with permanent no-repeat history."""

from __future__ import annotations

import json
import random
import time
from datetime import datetime

import requests

import config
from config import CATEGORIES, CATEGORIES_NATIVE, HISTORY_DIR, MAX_RECENT_CATEGORIES

PHRASE_HISTORY_FILE = HISTORY_DIR / "all_generated_phrases.json"
RECENT_CATEGORIES_FILE = HISTORY_DIR / "recent_categories.json"

PHRASE_KEY = config.LANGUAGE["history_key"]
LANGUAGE_NAME = config.LANGUAGE["name"]
NATIVE_NAME = config.LANGUAGE["native_name"]

# ==== FALLBACK PHRASES START ====
FALLBACK_PHRASES = [
    {"english": "Hello, nice to meet you.", "native": "ନମସ୍କାର, ଆପଣଙ୍କୁ ଭେଟି ଖୁସି ଲାଗିଲା।", "transliteration": "Namaskar, apananku bheti khusi lagila."},
    {"english": "Thank you very much.", "native": "ଆପଣଙ୍କୁ ବହୁତ ଧନ୍ୟବାଦ।", "transliteration": "Apananku bahut dhanyabad."},
    {"english": "Good morning, have a great day.", "native": "ସୁପ୍ରଭାତ, ଆପଣଙ୍କ ଦିନଟି ଭଲ କଟିବା।", "transliteration": "Suprabhat, apananka dinati bhalo katiba."},
    {"english": "I love learning new languages.", "native": "ମୁଁ ନୂଆ ଭାଷା ଶିଖିବାକୁ ଭଲପାଏ।", "transliteration": "Mu nua bhasha sikhikubaku bhalapae."},
    {"english": "Never give up on your dreams.", "native": "ଆପଣଙ୍କ ସ୍ୱପ୍ନକୁ କେବେବି ଛାଡନ୍ତୁ ନାହିଁ।", "transliteration": "Apananka swapnaku kebebi chhadantu nahin."},
    {"english": "Every day is a fresh start.", "native": "ପ୍ରତିଦିନ ଏକ ନୂତନ ଆରମ୍ଭ।", "transliteration": "Pratidin ek nutan arambha."},
    {"english": "Believe in yourself always.", "native": "ସର୍ବଦା ନିଜ ଉପରେ ବିଶ୍ୱାସ କରନ୍ତୁ।", "transliteration": "Sarbadha nija upare biswas karantu."},
    {"english": "Small steps lead to big changes.", "native": "ଛୋଟ ଛୋଟ ପାଦ ବଡ ପରିବର୍ତ୍ତନ ଆଣନ୍ତି।", "transliteration": "Chhota chhota pad bada paribartan aananti."},
    {"english": "You are stronger than you think.", "native": "ଆପଣ ଯାହା ଭାବନ୍ତି ତା ଠାରୁ ଅଧିକ ଶକ୍ତିଶାଳୀ।", "transliteration": "Apan yaha bhabanti ta tharu adhika shaktishali."},
    {"english": "Happiness is a choice, choose it.", "native": "ଖୁସି ଏକ ପସନ୍ଦ, ତାକୁ ବାଛନ୍ତୁ।", "transliteration": "Khusi ek pasanda, taku bachantu."},
    {"english": "What time is it please.", "native": "ଦୟାକରି ସମୟ କେତେ ହେଲା?", "transliteration": "Dayakari samaya kete hala?"},
    {"english": "Where is the train station.", "native": "ରେଳ ଷ୍ଟେସନ କେଉଁଠାରେ ଅଛି?", "transliteration": "Rel station keunthare achhi?"},
    {"english": "How much does this cost.", "native": "ଏହାର ମୂଲ୍ୟ କେତେ?", "transliteration": "Ehara mulya kete?"},
    {"english": "Can you help me please.", "native": "ଦୟାକରି ମୋତେ ସାହାଯ୍ୟ କରିପାରିବେ?", "transliteration": "Dayakari mote sahajya kariparibe?"},
    {"english": "I would like a coffee please.", "native": "ମୁଁ ଗୋଟିଏ କଫି ଚାହେଁ, ଦୟାକରି।", "transliteration": "Mu gotie coffee chahen, dayakari."},
    {"english": "The food is delicious today.", "native": "ଆଜି ଖାଦ୍ୟ ବହୁତ ସ୍ୱାଦିଷ୍ଟ।", "transliteration": "Aji khadya bahut swadishta."},
    {"english": "Have a wonderful weekend.", "native": "ଆପଣଙ୍କ ସପ୍ତାହ ଶେଷ ଭଲ କଟିବା।", "transliteration": "Apananka saptaha shesha bhalo katiba."},
    {"english": "Take care of yourself.", "native": "ଆପଣଙ୍କର ଯତ୍ନ ନିଅନ୍ତୁ।", "transliteration": "Apanankara yatna nieantu."},
    {"english": "See you tomorrow my friend.", "native": "କାଲି ଦେଖା ହେବ ମୋ ବନ୍ଧୁ।", "transliteration": "Kali dekha heba mo bandhu."},
    {"english": "The weather is beautiful outside.", "native": "ବାହାରେ ପାଣିପାଗ ବହୁତ ସୁନ୍ଦର।", "transliteration": "Bahare panipaga bahut sundara."},
    {"english": "I am very happy today.", "native": "ମୁଁ ଆଜି ବହୁତ ଖୁସି।", "transliteration": "Mu aji bahut khusi."},
    {"english": "Learning a language opens new doors.", "native": "ଭାଷା ଶିଖିବା ନୂଆ ଦ୍ୱାର ଖୋଲିଦିଏ।", "transliteration": "Bhasha sikhia nua dwar kholidie."},
    {"english": "Keep practicing every single day.", "native": "ପ୍ରତିଦିନ ଅଭ୍ୟାସ କରନ୍ତୁ।", "transliteration": "Pratidin abhyasa karantu."},
    {"english": "You can achieve anything you want.", "native": "ଆପଣ ଯାହା ଚାହାଁନ୍ତି ତାହା ହାସଲ କରିପାରିବେ।", "transliteration": "Apan yaha chahanti taha hasala kariparibe."},
    {"english": "Rest when you are tired.", "native": "କ୍ଳାନ୍ତ ହେଲେ ବିଶ୍ରାମ ନିଅନ୍ତୁ।", "transliteration": "Klanta hele bisrama nieantu."},
    {"english": "Focus on the positive things.", "native": "ସକରାତ୍ମକ ବିଷୟଗୁଡିକ ଉପରେ ଧ୍ୟାନ ଦିଅନ୍ତୁ।", "transliteration": "Sakaratmaka bisayagudika upare dhyana dieantu."},
    {"english": "Learn from your mistakes.", "native": "ଆପଣଙ୍କ ଭୁଲରୁ ଶିଖନ୍ତୁ।", "transliteration": "Apananka bhularu sikhantu."},
    {"english": "Trust the process completely.", "native": "ପ୍ରକ୍ରିୟା ଉପରେ ସମ୍ପୂର୍ଣ୍ଣ ଭାବରେ ବିଶ୍ୱାସ କରନ୍ତୁ।", "transliteration": "Prakriya upare sampurna bhabare biswas karantu."},
    {"english": "Breathe deeply and stay calm.", "native": "ଗଭୀର ନିଃଶ୍ୱାସ ନିଅନ୍ତୁ ଏବଂ ଶାନ୍ତ ରୁହନ୍ତୁ।", "transliteration": "Gabhira nishwas nieantu ebang shanta ruhantu."},
    {"english": "Enjoy the little moments in life.", "native": "ଜୀବନର ଛୋଟ ମୁହୂର୍ତ୍ତଗୁଡିକ ଉପଭୋଗ କରନ୍ତୁ।", "transliteration": "Jibanara chhota muhurtagudika upabhoga karantu."},
    {"english": "Smile more, worry less.", "native": "ଅଧିକ ହସନ୍ତୁ, କମ ଚିନ୍ତା କରନ୍ତୁ।", "transliteration": "Adhika hasantu, kama chinta karantu."},
    {"english": "Be kind to everyone you meet.", "native": "ଆପଣ ଯାହାକୁ ଭେଟନ୍ତି ତାଙ୍କ ପ୍ରତି ଦୟାଳୁ ହୁଅନ୍ତୁ।", "transliteration": "Apan jahanku bhetanti tanka prati dayalu huantu."},
    {"english": "Help others without expecting anything back.", "native": "ଅନ୍ୟମାନଙ୍କୁ କିଛି ପ୍ରତ୍ୟାଶା ନକରି ସାହାଯ୍ୟ କରନ୍ତୁ।", "transliteration": "Anyamananku kichhi pratyaasha nakari sahajya karantu."},
    {"english": "Forgive yourself and move forward.", "native": "ଆପଣଙ୍କୁ କ୍ଷମା କରନ୍ତୁ ଏବଂ ଆଗକୁ ବଢନ୍ତୁ।", "transliteration": "Apananku kshama karantu ebang agaku badhantu."},
    {"english": "Stay strong in difficult times.", "native": "କଠିନ ସମୟରେ ଦୃଢ ରୁହନ୍ତୁ।", "transliteration": "Kathina samayare drudha ruhantu."},
    {"english": "Every moment is a new beginning.", "native": "ପ୍ରତି ମୁହୂର୍ତ୍ତ ଏକ ନୂତନ ଆରମ୍ଭ।", "transliteration": "Prati muhurta ek nutan arambha."},
    {"english": "Listen to your heart always.", "native": "ସର୍ବଦା ଆପଣଙ୍କ ହୃଦୟର କଥା ଶୁଣନ୍ତୁ।", "transliteration": "Sarbadha apananka hrudayara katha shrunantu."},
    {"english": "Do what makes you happy.", "native": "ଯାହା ଆପଣଙ୍କୁ ଖୁସି କରେ ତାହା କରନ୍ତୁ।", "transliteration": "Yaha apananku khusi kare taha karantu."},
    {"english": "Your potential is unlimited.", "native": "ଆପଣଙ୍କ ସାମର୍ଥ୍ୟ ଅସୀମ।", "transliteration": "Apananka samarthya aseema."},
    {"english": "Be brave and take risks.", "native": "ସାହସୀ ହୁଅନ୍ତୁ ଏବଂ ବିପଦ ନିଅନ୍ତୁ।", "transliteration": "Sahasi huantu ebang bipada nieantu."},
    {"english": "Celebrate your progress every day.", "native": "ପ୍ରତିଦିନ ଆପଣଙ୍କ ପ୍ରଗତିକୁ ଉତ୍ସବ ଭାବରେ ପାଳନ କରନ୍ତୁ।", "transliteration": "Pratidin apananka pragatikku utsav bhabare palana karantu."},
    {"english": "Surround yourself with good people.", "native": "ଆପଣଙ୍କୁ ଭଲ ଲୋକମାନଙ୍କ ଦ୍ୱାରା ଘେରି ରଖନ୍ତୁ।", "transliteration": "Apananku bhalo lokamananka dwara gheri rakhantu."},
    {"english": "Read books and grow your mind.", "native": "ପୁସ୍ତକ ପଢନ୍ତୁ ଏବଂ ଆପଣଙ୍କ ମନକୁ ବୃଦ୍ଧି କରନ୍ତୁ।", "transliteration": "Pustaka padhantu ebang apananka manaku bruddhi karantu."},
    {"english": "Travel and discover new places.", "native": "ଭ୍ରମଣ କରନ୍ତୁ ଏବଂ ନୂଆ ସ୍ଥାନଗୁଡିକ ଆବିଷ୍କାର କରନ୍ତୁ।", "transliteration": "Bhramana karantu ebang nua sthanagudika abishkara karantu."},
    {"english": "Appreciate what you already have.", "native": "ଆପଣଙ୍କ ପାଖରେ ଯାହା ଅଛି ତାକୁ ପ୍ରଶଂସା କରନ୍ତୁ।", "transliteration": "Apananka pakha re yaha achhi taku prasansa karantu."},
    {"english": "Dance like nobody is watching.", "native": "ନାଚନ୍ତୁ ଯେପରି କେହି ଦେଖୁନାହାଁନ୍ତି।", "transliteration": "Nachantu yepari kehi dekhunahanti."},
    {"english": "Sing from your heart out loud.", "native": "ଆପଣଙ୍କ ହୃଦୟରୁ ଜୋରରେ ଗୀତ ଗାଆନ୍ତୁ।", "transliteration": "Apananka hrudayaru jorare gita gaantu."},
    {"english": "Plant seeds of kindness everywhere.", "native": "ସର୍ବତ୍ର ଦୟାର ବିହନ ବୁଣନ୍ତୁ।", "transliteration": "Sarbatra dayara bihana bunantu."},
    {"english": "Let go of what you cannot control.", "native": "ଯାହାକୁ ଆପଣ ନିୟନ୍ତ୍ରଣ କରିପାରନ୍ତି ନାହିଁ ତାକୁ ଛାଡିଦିଅନ୍ତୁ।", "transliteration": "Yahaku apan niyantrana karipare nahi taku chhadidieantu."},
    {"english": "Be present in the here and now.", "native": "ଏଠାରେ ଏବଂ ଏବେ ଉପସ୍ଥିତ ରୁହନ୍ତୁ।", "transliteration": "Ethare ebang ebe upasthita ruhantu."},
]
# ==== FALLBACK PHRASES END ====


def _load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_phrase_history():
    data = _load_json(PHRASE_HISTORY_FILE, {"phrases": [], "last_updated": None})
    data.setdefault("phrases", [])
    return data


def save_phrase_history(data):
    data["last_updated"] = datetime.now().isoformat()
    _save_json(PHRASE_HISTORY_FILE, data)


def is_phrase_used(english):
    english_lower = english.lower().strip()
    for p in load_phrase_history()["phrases"]:
        if p.get("english", "").lower().strip() == english_lower:
            return True
    return False


def _history_native(p):
    for key in (PHRASE_KEY, "vietnamese", "native", "translation", "target"):
        value = p.get(key)
        if value:
            return str(value)
    return ""


def add_phrases_to_history(phrases, category):
    history = load_phrase_history()
    for phrase in phrases:
        history["phrases"].append({
            "english": phrase["english"],
            PHRASE_KEY: phrase["native"],
            "transliteration": phrase.get("transliteration", ""),
            "category": category,
            "generated_at": datetime.now().isoformat(),
        })
    save_phrase_history(history)
    print(f"[content] Saved {len(phrases)} phrases (history total: {len(history['phrases'])})")


def get_available_category():
    data = _load_json(RECENT_CATEGORIES_FILE, {"recent_categories": [], "last_updated": None})
    recent = data.get("recent_categories", [])
    available = [c for c in CATEGORIES if c not in recent]
    if not available:
        recent = recent[-5:]
        available = [c for c in CATEGORIES if c not in recent]
        print("[rotation] Reset recent categories")
    selected = random.choice(available)
    recent.append(selected)
    data["recent_categories"] = recent[-MAX_RECENT_CATEGORIES:]
    data["last_updated"] = datetime.now().isoformat()
    _save_json(RECENT_CATEGORIES_FILE, data)
    print(f"[rotation] Category: {selected} ({len(available)} available)")
    return selected


def _normalize_phrase(item):
    if not isinstance(item, dict):
        return None
    english = str(item.get("english", "")).strip()
    native = str(
        item.get(PHRASE_KEY)
        or item.get("native")
        or item.get("vietnamese")
        or item.get("translation")
        or ""
    ).strip()
    translit = str(item.get("transliteration") or item.get("romanization") or item.get("romaji") or "").strip()
    if not english or not native:
        return None
    if len(english.split()) > 16:
        return None
    if "/" in native or "|" in native:
        native = native.split("/")[0].split("|")[0].strip()
    return {
        "english": english.replace("  ", " ").strip(),
        "native": native.strip(),
        "transliteration": translit.strip().strip("[]"),
    }


def _history_keys(history):
    used_en = set()
    used_nat = set()
    for p in history.get("phrases", []):
        en = str(p.get("english", "")).lower().strip()
        nat = _history_native(p).lower().strip()
        if en:
            used_en.add(en)
        if nat:
            used_nat.add(nat)
    return used_en, used_nat


def generate_phrases(category_english: str, num_phrases: int = 5) -> list:
    category_native = CATEGORIES_NATIVE[category_english]
    history = load_phrase_history()
    used_en, used_nat = _history_keys(history)
    recent_english = [
        p["english"] for p in history["phrases"] if p.get("category") == category_english
    ][-30:]

    models = [config.AI_MODEL]
    if "gemini-fast" not in models:
        models.append("gemini-fast")

    if config.POLLINATIONS_API_KEY:
        for attempt in range(5):
            model = models[0] if attempt < 3 else models[-1]
            try:
                phrases = _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model)
                unique = []
                for item in phrases:
                    p = _normalize_phrase(item)
                    if not p:
                        continue
                    key_en = p["english"].lower().strip()
                    key_nat = p["native"].lower().strip()
                    if key_en in used_en or key_nat in used_nat:
                        continue
                    if any(key_en == u["english"].lower().strip() for u in unique):
                        continue
                    used_en.add(key_en)
                    used_nat.add(key_nat)
                    unique.append(p)
                    if len(unique) >= num_phrases:
                        break
                if len(unique) >= num_phrases:
                    add_phrases_to_history(unique[:num_phrases], category_english)
                    return unique[:num_phrases]
                print(f"[content] Attempt {attempt + 1}: only {len(unique)} fresh phrases (need {num_phrases})")
            except Exception as exc:  # noqa: BLE001 - network boundary
                print(f"[content] Attempt {attempt + 1} failed ({model}): {exc}")
            time.sleep(1.5 * (attempt + 1))
    else:
        print("[content] No POLLINATIONS_API_KEY, using fallback phrases")

    fresh_fallback = []
    for p in FALLBACK_PHRASES:
        if p["english"].lower().strip() in used_en or p["native"].lower().strip() in used_nat:
            continue
        fresh_fallback.append(p)
    if not fresh_fallback:
        raise RuntimeError("Phrase API unavailable and no unused fallback phrases left; refusing to reuse phrases")
    chosen = fresh_fallback[:num_phrases]
    if len(chosen) < num_phrases:
        print(f"[content] Only {len(chosen)} fresh fallback phrases; building a shorter lesson")
    add_phrases_to_history(chosen, category_english)
    return chosen


def _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model=None):
    avoid = ""
    if recent_english:
        avoid = "\nDo NOT reuse any of these phrases:\n" + "\n".join(f"- {p}" for p in recent_english)

    prompt = f"""Create {num_phrases * 6} unique {category_english} phrases for English speakers learning {LANGUAGE_NAME}.
{avoid}

Rules:
1. Keep every phrase short and natural (4-11 words in English).
2. Use natural commas for TTS breathing pauses.
3. Each phrase must be speakable in 2-4 seconds.
4. Write clean {LANGUAGE_NAME} in {NATIVE_NAME} with correct accents and orthography. One translation only, no slashes.
5. Transliteration is a friendly Roman-script pronunciation guide for English speakers (not IPA).
6. Vary the sentence patterns and emotions. No duplicates.
7. Phrases must feel like real everyday language, not textbook filler.

Return ONLY a JSON array:
[{{"english": "...", "native": "...", "transliteration": "..."}}]"""

    response = requests.post(
        "https://gen.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.POLLINATIONS_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model or config.AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a {LANGUAGE_NAME} teacher creating short, natural, varied bilingual phrases. Reply with JSON only."},
                {"role": "user", "content": prompt},
            ],
            "temperature": min(0.95 + attempt * 0.02, 1.0),
        },
        timeout=90,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in content:
        content = content.split("```", 1)[1].split("```", 1)[0].strip()

    start = content.find("[")
    end = content.rfind("]")
    if start >= 0 and end > start:
        content = content[start:end + 1]

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("AI did not return a JSON array")
    return data
