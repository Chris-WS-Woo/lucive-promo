"""v18 · TTS for Story 1 Prologue · ElevenLabs v3 + emotion tags.

Lines from FLOW (Start_Funeral + N_NeonAlley converge):
  Raon (호위 · 차분한 위험 · low/calm tense): main speaker (~10 lines)
  Dex (히트맨 · cold/flat · 한 줄): "라온. 투항해."
  Yeonwoo (player) lines · skipped (player typed, no TTS)

Voice IDs:
  Dogjoy  qSSLFjgzC2qvkt4Uba0s   (calm Korean male) — primary for Raon
  For Dex we use a different style ID. Falling back to Dogjoy with stronger
  v3 tags to differentiate is also acceptable for prototype.

Usage:
  ELEVENLABS_API_KEY="..." python _gen_voices.py
"""
import os, json, urllib.request, urllib.error, sys, re
sys.stdout.reconfigure(encoding='utf-8')

KEY = os.environ['ELEVENLABS_API_KEY']
MODEL = "eleven_v3"

# Voice settings · stability slightly low for emotion variance, style high so v3 honors tags
SETTINGS_RAON = {
  "stability": 0.55, "similarity_boost": 0.85, "style": 0.55, "use_speaker_boost": True,
}
SETTINGS_DEX = {
  "stability": 0.42, "similarity_boost": 0.82, "style": 0.7, "use_speaker_boost": True,
}

# Voice IDs · using Dogjoy for both with strong tag differentiation
VOICE_RAON = "qSSLFjgzC2qvkt4Uba0s"
VOICE_DEX  = "qSSLFjgzC2qvkt4Uba0s"

# Lines as list of (name, voice_id, settings, text) tuples
LINES = [
  # === RAON · Start_Funeral ===
  ("raon_01_check",   VOICE_RAON, SETTINGS_RAON,
    "[low voice][calm controlled] 연우 씨, 자리 확인 부탁드려요."),
  ("raon_02_intro",   VOICE_RAON, SETTINGS_RAON,
    "[low voice][quiet][professional] 호위 맡은 라온입니다. [firmer] 지금 일어나지 마세요."),
  ("raon_03_warn",    VOICE_RAON, SETTINGS_RAON,
    "[low voice][cautious][quiet] 우측 출구 근처에. [pause] 모르는 얼굴 셋."),
  ("raon_04_cmd",     VOICE_RAON, SETTINGS_RAON,
    "[low voice][urgent][controlled] 3초 뒤. [short] 왼쪽 화장실 방향으로."),
  ("raon_05_run",     VOICE_RAON, SETTINGS_RAON,
    "[urgent][strained][low whisper] 뛰어. [harder] 지금."),
  ("raon_a1_ok",      VOICE_RAON, SETTINGS_RAON,
    "[breathless][concerned] 괜찮아?"),
  ("raon_a2_behind",  VOICE_RAON, SETTINGS_RAON,
    "[low voice][resigned] 그럼 말고. [gentle] 내 등 뒤에 있어."),
  ("raon_b1_name",    VOICE_RAON, SETTINGS_RAON,
    "[low voice][relieved][quiet] 연우."),
  ("raon_b2_alive",   VOICE_RAON, SETTINGS_RAON,
    "[low voice][soft][a little broken] 죽지 않았네. [quietly] 그거면 됐어."),
  ("raon_c2_yeonwoo", VOICE_RAON, SETTINGS_RAON,
    "[breaking][whispered][almost crying]…연우."),
  ("dex_01_surrender", VOICE_DEX, SETTINGS_DEX,
    "[flat][cold][slight smirk]…라온. [chillingly polite] 투항해."),
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
