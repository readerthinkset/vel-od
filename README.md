# Velocity Odia - Automated Facebook Reels Bot

**Automated Odia (Oriya) learning content generator for social media**

Generates and posts 5x daily to Facebook, Instagram, YouTube and other platforms with:
- AI-generated Odia phrases with English translations
- Professional text-to-speech (Edge TTS - or-IN-PrabodhNeural Odia)
- Beautiful gradient backgrounds with text overlays
- Perfect audio-video synchronization
- Velocity Odia branding
- **NEVER repeats phrases** (permanent history tracking)

---

## Daily Schedule (American EST/EDT)

| Post | Time (EST) | Time (UTC) | Theme |
|------|------------|------------|-------|
| 1 | 7:00 AM | 12:00 UTC | Morning motivation |
| 2 | 9:00 AM | 14:00 UTC | Morning break |
| 3 | 12:00 PM | 17:00 UTC | Lunch break |
| 4 | 3:00 PM | 20:00 UTC | Afternoon pick-me-up |
| 5 | 7:00 PM | 00:00 UTC | Evening inspiration |

---

## Available Categories (35 Total)

### Essential Odia Learning (Priority)
1. Greetings (ନମସ୍କାର)
2. Basic Phrases (ମୌଳିକ ବାକ୍ୟ)
3. Common Expressions (ସାଧାରଣ ଅଭିବ୍ୟକ୍ତି)
4. Travel (ଯାତ୍ରା)
5. Restaurant (ରେଷ୍ଟୁରାଣ୍ଟ)
6. Shopping (କିଣାବିକା)
7. Emergency (ଜରୁରୀକାଳୀନ)
8. Family Terms (ପରିବାର ଶବ୍ଦ)
9. Numbers (ସଂଖ୍ୟା)
10. Time (ସମୟ)

### Motivational Categories
11. Motivation (ପ୍ରେରଣା)
12. Love (ପ୍ରେମ)
13. Success (ସଫଳତା)
14. Wisdom (ଜ୍ଞାନ)
15. Happiness (ଖୁସି)
16. Self Improvement (ଆତ୍ମ-ଉନ୍ନତି)
17. Gratitude (କୃତଜ୍ଞତା)
18. Friendship (ବନ୍ଧୁତା)
19. Hope (ଆଶା)
20. Creativity (ସୃଜନଶୀଳତା)
21. Inner Peace (ଆନ୍ତରିକ ଶାନ୍ତି)
22. Confidence (ଆତ୍ମବିଶ୍ୱାସ)
23. Perseverance (ଦୃଢ଼ତା)
24. Inspiration (ପ୍ରେରଣା)
25. Positive Life (ସକାରାତ୍ମକ ଜୀବନ)
26. Courage (ସାହସ)
27. Kindness (ଦୟା)
28. Patience (ଧୈର୍ଯ୍ୟ)
29. Forgiveness (କ୍ଷମା)
30. Strength (ଶକ୍ତି)
31. Joy (ଆନନ୍ଦ)
32. Balance (ସନ୍ତୁଳନ)
33. Growth (ବୃଦ୍ଧି)
34. Purpose (ଉଦ୍ଦେଶ୍ୟ)
35. Mindfulness (ସଚେତନତା)

---

## GitHub Actions Setup

### Step 1: Add Secrets to GitHub Repository

Go to your GitHub repository > Settings > Secrets and variables > Actions

**Required Secrets:**

```bash
# Pollinations AI (for content generation)
POLLINATIONS_API_KEY=sk_your_api_key_here

# Facebook (for Reels upload)
FACEBOOK_ACCESS_TOKEN=your_token
FACEBOOK_PAGE_ID=your_page_id

# Instagram (for Reels upload)
INSTAGRAM_ACCESS_TOKEN=your_token
INSTAGRAM_ACCOUNT_ID=your_account_id

# Optional: Other platforms
VK_ACCESS_TOKEN=your_token
VK_GROUP_ID=your_group_id
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHANNEL_ID=your_channel_id
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_SECRET=your_secret
```

### Step 2: Enable GitHub Actions

1. Go to Actions tab in your GitHub repository
2. Enable workflows if disabled
3. The workflow will automatically run 5x daily

### Step 3: Manual Testing

You can manually trigger the workflow:
1. Go to Actions > "Velocity Odia - Daily 5x Upload"
2. Click "Run workflow"
3. Select branch (main/master)
4. Click "Run workflow"

---

## Local Testing

### Prerequisites

```bash
# Install Python 3.11+
# Install FFmpeg
# Install dependencies
pip install -r requirements.txt
```

### Generate Single Reel

```bash
python facebook_reels_automation.py
```

### Upload to Social Media

```bash
cd upload
python ../upload_all_platforms.py
```

---

## Project Structure

```
velocity odia/
  ├── .env                              # API keys and credentials
  ├── .github/
  │   └── workflows/
  │       └── daily_5x_upload.yml      # GitHub Actions workflow
  ├── facebook_reels_automation.py     # Main generation script
  ├── upload_all_platforms.py          # Unified upload script
  ├── upload/
  │   ├── upload_facebook.py
  │   ├── upload_instagram.py
  │   ├── upload_to_youtube.py
  │   ├── upload_vk.py
  │   └── ...
  ├── output/
  │   ├── video/                       # Generated reels
  │   ├── history/                     # Phrase history (NEVER delete!)
  │   └── daily_summary_*.json        # Daily generation logs
  └── requirements.txt
```

---

## Video Specifications

- **Resolution:** 1080x1920 (9:16 vertical)
- **Format:** MP4 (H.264 + AAC)
- **Duration:** ~30-50 seconds (5 phrases)
- **Frame Rate:** 30 FPS
- **Audio:** Edge TTS (en-US-GuyNeural EN, or-IN-PrabodhNeural OR)

---

## Phrase History

All generated phrases are stored in:
```
output/history/all_generated_phrases.json
```

**This file is PERMANENT and should NEVER be deleted.**

It ensures:
- No phrase is ever repeated
- Fresh content every day
- Tracking of all generated content

---

## Troubleshooting

### Video Generation Fails

```bash
# Check FFmpeg installation
ffmpeg -version

# Reinstall if needed
sudo apt-get install ffmpeg  # Linux
brew install ffmpeg          # macOS
```

### Audio Upload Fails

```bash
# Check .env file
cat .env | grep FACEBOOK
cat .env | grep INSTAGRAM

# Verify tokens are valid
# Regenerate if expired
```

---

## Performance Metrics

- **Generation Time:** ~2-3 minutes per reel
- **Upload Time:** ~1-2 minutes per platform
- **Total Workflow:** ~5-10 minutes per post
- **Daily Capacity:** 5 posts x 5 phrases = 25 phrases/day
- **Category Rotation:** 35 categories = 7+ days before repeat

---

## Key Features

### Perfect Audio-Video Sync
- Each image displays for exact audio duration
- English + 500ms pause + Odia timing preserved
- No early transitions or cut-offs

### Natural Speech
- Phrases include commas for breathing room
- TTS sounds natural, not robotic

### Professional Design
- Multi-stop gradient backgrounds
- Distinct colors: Navy (EN) / Maroon (OR) / Gray (Transliteration)
- Velocity Odia branding on every frame

### Never Repeats
- Permanent phrase history tracking
- AI generates fresh content every time
- Checks all phrases before generation

---

**Made for Odia learners worldwide**

Learn Odia with Velocity Odia!
