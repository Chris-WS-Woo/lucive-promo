"""v22 · TTS for Story 1 PROLOGUE · ElevenLabs v3 · MAX intensity.

User feedback in v21: "TTS too calm, no urgency". The Dogjoy voice itself is
trained as "calm Korean male". To force dramatic delivery on a calm-trained
voice, we combine THREE pressure mechanisms in v22:

  (1) settings · stability LOW (0.18) + style MAX (1.0) + similarity_boost HIGH
      · low stability lets the model swing emotionally on every sample
      · max style aggressively honors emotion tags
  (2) text-side punctuation/emphasis pressure ·
      · ALL CAPS for shouts, repeated punctuation, ellipsis for breath
      · multiple short bursts ("뛰어! 뛰어요!! 지금!!") give the model
        explicit acceleration cues that calm-voice training cannot ignore
  (3) tag stacking · 3-5 emotion tags per line, escalating
      · [BREATHLESS][lungs burning][adrenaline][hissed shouting]…

Lines actually used in v21+ prologue (only 3 dramatic):
  raon_05_run        → urgent run command (peak escape)
  dex_01_surrender   → cold antagonist demand
  raon_c2_yeonwoo    → broken whisper (player name · before cut)

Other lines retained for legacy v17–v20 backward compat.

Usage:
  ELEVENLABS_API_KEY="..." python _gen_voices.py
"""
import os, json, urllib.request, urllib.error, sys, re
sys.stdout.reconfigure(encoding='utf-8')

KEY = os.environ['ELEVENLABS_API_KEY']
MODEL = "eleven_v3"

# v22 · settings tuned per character
# RAON_PEAK · max emotional swing (low stab · max style)
SETTINGS_RAON_PEAK = {
  "stability": 0.18, "similarity_boost": 0.92, "style": 1.0, "use_speaker_boost": True,
}
# DEX · cold restraint, slightly higher stability so the menace stays controlled
SETTINGS_DEX = {
  "stability": 0.28, "similarity_boost": 0.85, "style": 0.95, "use_speaker_boost": True,
}
# RAON_REGULAR · used for legacy non-peak lines · still moderately emotional
SETTINGS_RAON = {
  "stability": 0.40, "similarity_boost": 0.88, "style": 0.78, "use_speaker_boost": True,
}

VOICE_RAON = "qSSLFjgzC2qvkt4Uba0s"  # Dogjoy (calm-trained · we force emotion)
VOICE_DEX  = "qSSLFjgzC2qvkt4Uba0s"

# Lines · (name, voice_id, settings, text)
LINES = [
  # === v22 PROLOGUE CORE · max dramatic ===
  # raon_05_run · urgent shout under breath · "RUN. NOW."
  # repeated punctuation + ALL CAPS forces acceleration the calm voice can't ignore
  ("raon_05_run", VOICE_RAON, SETTINGS_RAON_PEAK,
    "[BREATHLESS][LUNGS BURNING][adrenaline][hissed shouting through teeth]"
    "뛰어요!! [PANICKED HARSH WHISPER]지금!! [GASPING]지금!!"),
  # dex_01_surrender · ice cold antagonist · slow venom
  ("dex_01_surrender", VOICE_DEX, SETTINGS_DEX,
    "[ICE COLD][SLOW][menacing low voice][slight smirk in voice]"
    "…라온. [CHILLINGLY POLITE PAUSE][taunting whisper]투항해."),
  # raon_c2_yeonwoo · breaking voice · whispered name · the moment before the cut
  ("raon_c2_yeonwoo", VOICE_RAON, SETTINGS_RAON_PEAK,
    "[BROKEN VOICE][shaking gasping sob][devastated whisper][trembling]"
    "…연우……… [BARELY AUDIBLE BREATH]연우……"),

  # === LEGACY · v17–v20 backward compat (re-tagged stronger) ===
  ("raon_01_check", VOICE_RAON, SETTINGS_RAON,
    "[low voice][controlled tension][quiet] 연우 씨, [softer] 자리 확인 부탁드려요."),
  ("raon_02_intro", VOICE_RAON, SETTINGS_RAON,
    "[low voice][quiet][professional but tense] 호위 맡은 라온입니다. [firmer][quietly urgent] 지금 일어나지 마세요."),
  ("raon_03_warn", VOICE_RAON, SETTINGS_RAON,
    "[low voice][tense whisper][cautious] 우측 출구 근처에. [pause][harder whisper] 모르는 얼굴 셋."),
  ("raon_04_cmd", VOICE_RAON, SETTINGS_RAON,
    "[low voice][URGENT][hissed][controlled panic] 3초 뒤. [harder] 왼쪽 화장실 방향으로!"),
  ("raon_a1_ok", VOICE_RAON, SETTINGS_RAON,
    "[breathless][concerned][quiet][voice rough] 괜찮아?"),
  ("raon_a2_behind", VOICE_RAON, SETTINGS_RAON,
    "[low voice][resigned][weary][soft] 그럼 말고. [gentle][protective] 내 등 뒤에 있어."),
  ("raon_b1_name", VOICE_RAON, SETTINGS_RAON_PEAK,
    "[low voice][relieved][quietly broken][choked] 연우…"),
  ("raon_b2_alive", VOICE_RAON, SETTINGS_RAON_PEAK,
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
