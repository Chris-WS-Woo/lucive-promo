"""v21 · TTS for Story 1 PROLOGUE · ElevenLabs v3 + STRONG emotion tags.

v21 prologue lean cliffhanger uses only 3 voice lines:
  - raon_05_run        "뛰어요. 지금."         (urgent shout under breath)
  - dex_01_surrender   "...라온. 투항해."      (cold antagonist)
  - raon_c2_yeonwoo    "...연우."              (broken whisper · breaking point)

v20 lines kept for backward-compat with older versions (v17–v20):
  raon_01_check, raon_02_intro, raon_03_warn, raon_04_cmd,
  raon_a1_ok, raon_a2_behind, raon_b1_name, raon_b2_alive

NOTE on v3 emotion tags · v21 escalates intensity because previous outputs felt
too calm. v3 weights tag emphasis by stability + style settings AND tag count;
we drop stability and stack 2-3 strong emotion tags per line to force dramatic
delivery. Korean text + English emotion tags is supported by v3.

Regenerate with:
  ELEVENLABS_API_KEY="..." python _gen_voices.py
"""
import os, json, urllib.request, urllib.error, sys, re
sys.stdout.reconfigure(encoding='utf-8')

KEY = os.environ['ELEVENLABS_API_KEY']
MODEL = "eleven_v3"

# v21 · stability LOW · style HIGH · v3 honors tags much harder
SETTINGS_DRAMATIC = {
  "stability": 0.30, "similarity_boost": 0.85, "style": 0.85, "use_speaker_boost": True,
}
SETTINGS_RAON = {
  "stability": 0.45, "similarity_boost": 0.85, "style": 0.65, "use_speaker_boost": True,
}
SETTINGS_DEX = {
  "stability": 0.32, "similarity_boost": 0.82, "style": 0.85, "use_speaker_boost": True,
}

VOICE_RAON = "qSSLFjgzC2qvkt4Uba0s"
VOICE_DEX  = "qSSLFjgzC2qvkt4Uba0s"

# Lines · (name, voice_id, settings, text)
# v21 · core 3 dramatic lines used by current prologue
LINES = [
  # === v21 PROLOGUE CORE (only 3 lines used in cliffhanger) ===
  ("raon_05_run",   VOICE_RAON, SETTINGS_DRAMATIC,
    "[urgent][shouting under breath][panicked][harsh whisper] 뛰어요. [shouted whisper] 지금."),
  ("dex_01_surrender", VOICE_DEX, SETTINGS_DEX,
    "[ice cold][slow][menacing][slight smirk]…라온. [chillingly polite][taunting] 투항해."),
  ("raon_c2_yeonwoo", VOICE_RAON, SETTINGS_DRAMATIC,
    "[breaking voice][whispered][almost crying][trembling][devastated]…연우."),

  # === LEGACY · kept for v17–v20 compatibility (re-tagged stronger) ===
  ("raon_01_check", VOICE_RAON, SETTINGS_RAON,
    "[low voice][controlled tension][quiet] 연우 씨, [softer] 자리 확인 부탁드려요."),
  ("raon_02_intro", VOICE_RAON, SETTINGS_RAON,
    "[low voice][quiet][professional but tense] 호위 맡은 라온입니다. [firmer][quietly urgent] 지금 일어나지 마세요."),
  ("raon_03_warn",  VOICE_RAON, SETTINGS_RAON,
    "[low voice][tense whisper][cautious] 우측 출구 근처에. [pause][harder whisper] 모르는 얼굴 셋."),
  ("raon_04_cmd",   VOICE_RAON, SETTINGS_RAON,
    "[low voice][urgent][hissed][controlled panic] 3초 뒤. [short][harder] 왼쪽 화장실 방향으로."),
  ("raon_a1_ok",    VOICE_RAON, SETTINGS_RAON,
    "[breathless][concerned][quiet][voice rough] 괜찮아?"),
  ("raon_a2_behind", VOICE_RAON, SETTINGS_RAON,
    "[low voice][resigned][weary][soft] 그럼 말고. [gentle][protective] 내 등 뒤에 있어."),
  ("raon_b1_name",  VOICE_RAON, SETTINGS_DRAMATIC,
    "[low voice][relieved][quietly broken][choked] 연우."),
  ("raon_b2_alive", VOICE_RAON, SETTINGS_DRAMATIC,
    "[low voice][soft][broken][almost a sigh][relieved] 죽지 않았네. [quietly][trembling] 그거면 됐어."),
]

def strip_tags(text):
  return re.sub(r"\[[^\]]+\]", "", text).replace("  ", " ").strip()

def gen(name, voice_id, settings, text):
  url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
  body = {
    "text": text if MODEL == "eleven_v3" else strip_tags(text),
    "model_id": MODEL,
    "voice_settings": settings,
  }
  data = json.dumps(body, ensure_ascii=False).encode("utf-8")
  req = urllib.request.Request(url, data=data, method="POST",
    headers={
      "xi-api-key": KEY,
      "Content-Type": "application/json; charset=utf-8",
      "Accept": "audio/mpeg",
    })
  try:
    with urllib.request.urlopen(req, timeout=120) as r:
      audio = r.read()
      with open(f"{name}.mp3", "wb") as f:
        f.write(audio)
      print(f"[ok] {name}.mp3 ({len(audio)//1024} KB)")
  except urllib.error.HTTPError as e:
    print(f"[err] {name}: HTTP {e.code} {e.read().decode(errors='replace')[:300]}")
  except Exception as e:
    print(f"[err] {name}: {e}")

print(f"[info] model={MODEL}")
for name, voice_id, settings, text in LINES:
  gen(name, voice_id, settings, text)
print("[done]")
