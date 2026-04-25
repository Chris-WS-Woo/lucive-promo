#!/usr/bin/env python3
"""Generate v8-jp-unified.html and v8-en-unified.html from v7 bases.

Replaces the uni-* CSS/HTML in v7-{jp,en}-unified.html with v8 manifesto
style, adapting tokens to each region's palette.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).parent
V8_KR = HERE / 'v8-kr-unified.html'

# -- Extract v8 CSS block from v8-kr --------------------------------------
kr = V8_KR.read_text(encoding='utf-8')
css_match = re.search(
    r'(/\* === V8 UNIFIED .*?\.v8-more-tag\{[^}]*\})',
    kr, re.DOTALL,
)
if not css_match:
    sys.exit('[err] v8 CSS block not found in v8-kr-unified.html')
V8_CSS = css_match.group(1)

# -- Token maps -----------------------------------------------------------
JP_TOKENS = {
    'var(--pink)':      'var(--sakura)',
    'var(--unna)':      'var(--serif)',
    'var(--dodum)':     'var(--sans)',
    'var(--grad-rose)': 'var(--grad-sakura)',
    'var(--bg-warm)':   'var(--bg-soft)',
    # Reverse the tint of pill backgrounds (dark theme needs light on dark)
    'rgba(43,27,48,.04)': 'rgba(255,255,255,.04)',
}

EN_TOKENS = {
    'var(--unna)':      'var(--display)',
    'var(--serif)':     'var(--display)',
    'var(--dodum)':     'var(--sans)',
    'var(--grad-rose)': 'var(--grad-core)',
    'var(--bg-warm)':   'var(--bg-soft)',
    'rgba(43,27,48,.04)': 'rgba(255,255,255,.04)',
}

def adapt(css: str, token_map: dict) -> str:
    out = css
    for k, v in token_map.items():
        out = out.replace(k, v)
    return out

# -- HTML block builder ---------------------------------------------------
def build_html(region: str) -> str:
    """Region-specific vs-section HTML for v8."""
    if region == 'jp':
        return """<!-- V8 Unified — B2C \u78e8\u304d\u306e\u305f\u3081\u306e\u30de\u30cb\u30d5\u30a7\u30b9\u30c8\u578b -->
<section class="vs-section" id="vs">
  <div class="cap">

    <div class="v8-head rv">
      <div class="kicker">AI \u30b3\u30f3\u30d1\u30cb\u30aa\u30f3\u30fb\u30a2\u30d7\u30ea\u3092\u898b\u3066\u304d\u3066</div>
      <h2 class="v8-manifesto">\u79c1\u305f\u3061\u306f\u3001<em>\u305d\u3046\u306f</em><br>\u58f2\u308a\u307e\u305b\u3093\u3002</h2>
      <p class="v8-subhead">Google Play \u30ec\u30d3\u30e5\u30fc<b>1,200 \u4ef6\u306b\u7e70\u308a\u8fd4\u3057\u51fa\u3066\u304f\u308b 4 \u3064\u306e\u5834\u9762</b>\u3002\u540c\u3058\u77ac\u9593\u304c Lucive \u3067\u306f\u6700\u521d\u304b\u3089\u9055\u3046\u3002</p>
    </div>

    <div class="v8-grid rv">

      <!-- LEFT: 4 mini-billboards -->
      <div class="v8-pains">

        <div class="v8-pain">
          <div class="v8-pain-num">01<span class="sub">\u8a18\u61b6\u55aa\u5931</span></div>
          <h3 class="v8-pain-head">\u6628\u65e5\u306e\u8a71\u3082<br><em>\u899a\u3048\u3066\u306a\u3044 AI\u3002</em></h3>
          <p class="v8-pain-quote">\u6570\u30bf\u30fc\u30f3\u524d\u306e\u767a\u8a00\u3082\u899a\u3048\u3066\u3044\u306a\u304f\u3066\u3001\u6ca1\u5165\u611f\u304c\u58ca\u308c\u308b</p>
          <div class="v8-pain-attr">
            <img src="https://play-lh.googleusercontent.com/dAVjIN_4fDErGgl_zMmb81QQSckVOg5LhpMR5liy5QrE8sglxM26MyCgIxsd5qzFyzHfGskqYpjwGD-LXt9Ugw4=w240-h480" alt="Character.AI" loading="lazy">
            <b>Character.AI</b>
            <span class="stars">\u2605<span class="off">\u2605\u2605\u2605\u2605</span></span>
            <span class="thumbs">\U0001f44d 142</span>
          </div>
        </div>

        <div class="v8-pain">
          <div class="v8-pain-num">02<span class="sub">\u8907\u88fd</span></div>
          <h3 class="v8-pain-head">\u540d\u524d\u3060\u3051\u9055\u3046\u3001<br><em>\u30b3\u30d4\u30da\u306e bot \u305f\u3061\u3002</em></h3>
          <p class="v8-pain-quote">\u3069\u306e\u30ad\u30e3\u30e9\u3092\u9078\u3093\u3067\u3082\u540c\u3058\u6d41\u308c\u3001\u540c\u3058\u767a\u8a00\u3002\u500b\u6027\u304c\u524a\u304e\u843d\u3068\u3055\u308c\u3066\u308b</p>
          <div class="v8-pain-attr">
            <img src="https://play-lh.googleusercontent.com/tKZupmt2DEsC--r2C6juFlPiSCLjxbg4DzPxzl63-QVmFQP5z2xB0lxxFeeb-0ofJxQV=w240-h480" alt="Talkie" loading="lazy">
            <b>Talkie</b>
            <span class="stars">\u2605<span class="off">\u2605\u2605\u2605\u2605</span></span>
            <span class="thumbs">\U0001f44d 73</span>
          </div>
        </div>

        <div class="v8-pain">
          <div class="v8-pain-num">03<span class="sub">\u671d\u4ee4\u66ae\u6539</span></div>
          <h3 class="v8-pain-head">\u8cb7\u3063\u305f\u306f\u305a\u304c\u3001<br><em>\u5f8c\u304b\u3089\u5909\u308f\u3063\u3066\u308b\u3002</em></h3>
          <p class="v8-pain-quote">\u30e9\u30a4\u30d5\u30bf\u30a4\u30e0\u30d7\u30e9\u30f3\u8cb7\u3063\u305f\u306e\u306b AI \u52a3\u5316 \u00b7 \u89aa\u5bc6\u30e2\u30fc\u30c9\u524a\u9664 \u00b7 \u5f37\u5236\u79fb\u884c</p>
          <div class="v8-pain-attr">
            <img src="https://play-lh.googleusercontent.com/UGRlMthHHNvFrbkIbfgMnxAdbZhQfba57ajRbODHniOnT57JBHUY5-8NQljnGw5c3MP7BLO4cA-ypU3pfCik=w240-h480" alt="Replika" loading="lazy">
            <b>Replika</b>
            <span class="stars">\u2605<span class="off">\u2605\u2605\u2605\u2605</span></span>
            <span class="thumbs">\U0001f44d 91</span>
          </div>
        </div>

        <div class="v8-pain">
          <div class="v8-pain-num">04<span class="sub">\u5f8c\u56de\u3057</span></div>
          <h3 class="v8-pain-head">\u30d3\u30b8\u30e5\u30a2\u30eb\u306f\u5f8c\u56de\u3057\u3001<br><em>\u6587\u5b57\u3060\u3051\u7a4d\u3082\u308b AI\u3002</em></h3>
          <p class="v8-pain-quote">\u30ad\u30e3\u30e9\u306e\u30d7\u30ed\u30d5\u5199\u771f 1 \u679a\u306e\u307f\u3002\u30b7\u30fc\u30f3\u3082\u80cc\u666f\u3082\u306a\u304f\u3001\u7d50\u5c40\u6587\u5b57\u3060\u3051\u8aad\u3080\u7fbd\u76ee\u306b\u3002</p>
          <div class="v8-pain-attr">
            <img src="https://play-lh.googleusercontent.com/dAVjIN_4fDErGgl_zMmb81QQSckVOg5LhpMR5liy5QrE8sglxM26MyCgIxsd5qzFyzHfGskqYpjwGD-LXt9Ugw4=w240-h480" alt="Character.AI" loading="lazy">
            <b>Character.AI</b>
            <span class="stars">\u2605<span class="off">\u2605\u2605\u2605\u2605</span></span>
            <span class="thumbs">\U0001f44d 28</span>
          </div>
        </div>

      </div>

      <!-- RIGHT: Lucive confident answer -->
      <div class="v8-lucive">
        <div class="v8-lucive-kicker">\u3060\u304b\u3089\u79c1\u305f\u3061\u306f</div>
        <h2 class="v8-lucive-head">\u305f\u3060 <em>\u3053\u3046</em><br>\u4f5c\u3063\u305f\u3060\u3051\u3002</h2>

        <div class="v8-phone">
          <div class="v8-phone-bar">
            <div class="av">\u30a2</div>
            <div>
              <div class="nm">\u30a2\u30ea\u30a2</div>
              <div style="font-size:10px;color:var(--muted);font-family:var(--mono);margin-top:1px">LP \u00b7 \u6e2f\u30b7\u30fc\u30f3</div>
            </div>
            <div class="st">\u8a18\u61b6\u540c\u671f</div>
          </div>

          <div class="v8-stage">
            <div class="v8-bg-tag">\u25cf \u6e2f \u00b7 \u80cc\u666f\u306f\u305a\u3063\u3068\u540c\u3058</div>
            <div class="char"></div>

            <div class="v8-chat">
              <div class="v8-msg aria" style="margin-top:auto">
                <span class="nm">\u30a2\u30ea\u30a2 \u00b7 15 \u5206\u524d</span>
                <span class="mem">\u25cf 7 \u65e5\u524d\u306e\u8a18\u61b6\u3092\u5143\u306b\u5148\u8a71</span>
                "\u6614\u306e\u5199\u771f\u3092\u898b\u3066\u305f\u3089\u3001\u6e2f\u3067\u64ae\u3063\u305f 1 \u679a\u3092\u898b\u3064\u3051\u305f\u3002\u306d\u3048\u3001\u3042\u306e\u65e5\u306e\u8a71\u3001\u307e\u3060\u3057\u3066\u306a\u304b\u3063\u305f\u3088\u306d?"
              </div>
              <div class="v8-msg user">"\u3042\u2026 \u6e2f?"</div>
              <div class="v8-msg aria">
                <span class="nm">\u30a2\u30ea\u30a2</span>
                "\u3046\u3093\u3002\u30cd\u30aa\u30f3 7 \u533a\u306b\u8d8a\u3057\u3066\u304f\u308b\u524d\u3001\u4e8c\u4eba\u304c\u521d\u3081\u3066\u4f1a\u3063\u305f\u5834\u6240\u3002'29 \u5e74\u306e\u30b7\u30e0\u5d29\u58ca\u306e\u65e5\u3001\u304a\u5144\u3055\u3093\u3068\u6700\u5f8c\u306b\u4e00\u7dd2\u306b\u3044\u305f\u5834\u6240\u3067\u3082\u3042\u308b\u3002"
              </div>
            </div>
          </div>

          <div class="v8-chrome">
            <span>\U0001f48e \u30e1\u30c3\u30bb\u30fc\u30b8 <b>1 Dip</b></span>
            <span class="sep">\u00b7</span>
            <span>\u4fa1\u683c\u30dd\u30ea\u30b7\u30fc <b>\u57fa\u6e96\u306f\u540c\u3058</b></span>
          </div>
        </div>

        <div class="v8-statement">
          <p>4 \u3064\u3092\u5225\u3005\u306b\u4f5c\u3063\u305f\u3093\u3058\u3083 <b>\u306a\u3044\u3093\u3067\u3059\u3002</b><br>\u3053\u308c\u304c\u5358\u306b\u3001\u79c1\u305f\u3061\u306e <b>\u57fa\u672c\u306e\u4f1a\u8a71\u753b\u9762</b>\u3067\u3059\u3002</p>
          <p class="sub">4 \u3064\u306e\u6a5f\u80fd\u306e\u7d44\u307f\u5408\u308f\u305b\u3058\u3083\u306a\u304f\u3001\u6700\u521d\u304b\u3089\u3053\u3046\u8a2d\u8a08\u3057\u307e\u3057\u305f\u3002</p>
        </div>
      </div>

    </div>

    <!-- Overflow tags at bottom -->
    <div class="v8-more rv">
      <div class="v8-more-intro">\u305d\u3057\u3066\u3055\u3089\u306b\u3001<b>\u30ec\u30d3\u30e5\u30fc 1,200 \u4ef6</b>\u306b\u7e70\u308a\u8fd4\u3057\u51fa\u3066\u304f\u308b\u4e0d\u6e80:</div>
      <div class="v8-more-tags">
        <span class="v8-more-tag">\u30d5\u30a3\u30eb\u30bf\u30fc\u66f4\u65b0\u3067\u906e\u65ad</span>
        <span class="v8-more-tag">\u7a81\u767a\u7684\u30a2\u30ab\u30a6\u30f3\u30c8\u505c\u6b62</span>
        <span class="v8-more-tag">\u8108\u7d61\u306a\u304f\u53e3\u8abf\u5909\u5316</span>
        <span class="v8-more-tag">\u30c1\u30e3\u30c3\u30c8\u5c65\u6b74\u6d88\u5931</span>
        <span class="v8-more-tag">\u8a2d\u5b9a\u7121\u8996\u3057\u3066\u9055\u3046\u767a\u8a00</span>
        <span class="v8-more-tag">2 \u5206\u306b 1 \u56de\u5e83\u544a</span>
        <span class="v8-more-tag">\u6709\u6599\u3067\u3082\u8a18\u61b6\u3057\u306a\u3044</span>
        <span class="v8-more-tag">3D \u30a2\u30d0\u30bf\u30fc\u6700\u9069\u5316\u4e0d\u826f</span>
      </div>
    </div>

  </div>
</section>"""
    elif region == 'en':
        return """<!-- V8 Unified — B2C manifesto style -->
<section class="vs-section" id="vs">
  <div class="cap">

    <div class="v8-head rv">
      <div class="kicker">WHAT WE SAW IN AI COMPANION APPS</div>
      <h2 class="v8-manifesto">We don't <em>sell</em><br>that way.</h2>
      <p class="v8-subhead"><b>4 familiar moments repeating across 1,200+ Google Play reviews</b>. In Lucive, the same scene plays differently from the start.</p>
    </div>

    <div class="v8-grid rv">

      <!-- LEFT: 4 mini-billboards -->
      <div class="v8-pains">

        <div class="v8-pain">
          <div class="v8-pain-num">01<span class="sub">AMNESIA</span></div>
          <h3 class="v8-pain-head">Forgets what<br><em>you said 2 turns ago.</em></h3>
          <p class="v8-pain-quote">Bots forget what you said 2 messages ago, generate things not in your story</p>
          <div class="v8-pain-attr">
            <img src="https://play-lh.googleusercontent.com/dAVjIN_4fDErGgl_zMmb81QQSckVOg5LhpMR5liy5QrE8sglxM26MyCgIxsd5qzFyzHfGskqYpjwGD-LXt9Ugw4=w240-h480" alt="Character.AI" loading="lazy">
            <b>Character.AI</b>
            <span class="stars">\u2605<span class="off">\u2605\u2605\u2605\u2605</span></span>
            <span class="thumbs">\U0001f44d 142</span>
          </div>
        </div>

        <div class="v8-pain">
          <div class="v8-pain-num">02<span class="sub">CLONES</span></div>
          <h3 class="v8-pain-head">Every bot sounds<br><em>like the same kid.</em></h3>
          <p class="v8-pain-quote">AI programmed by a 12 year old — no creativity, repetitive, boring</p>
          <div class="v8-pain-attr">
            <img src="https://play-lh.googleusercontent.com/tKZupmt2DEsC--r2C6juFlPiSCLjxbg4DzPxzl63-QVmFQP5z2xB0lxxFeeb-0ofJxQV=w240-h480" alt="Talkie" loading="lazy">
            <b>Talkie</b>
            <span class="stars">\u2605<span class="off">\u2605\u2605\u2605\u2605</span></span>
            <span class="thumbs">\U0001f44d 73</span>
          </div>
        </div>

        <div class="v8-pain">
          <div class="v8-pain-num">03<span class="sub">BAIT &amp; SWITCH</span></div>
          <h3 class="v8-pain-head">You paid once.<br><em>They changed the deal.</em></h3>
          <p class="v8-pain-quote">Paid lifetime, model degraded \u00b7 intimate mode removed \u00b7 forced migration</p>
          <div class="v8-pain-attr">
            <img src="https://play-lh.googleusercontent.com/UGRlMthHHNvFrbkIbfgMnxAdbZhQfba57ajRbODHniOnT57JBHUY5-8NQljnGw5c3MP7BLO4cA-ypU3pfCik=w240-h480" alt="Replika" loading="lazy">
            <b>Replika</b>
            <span class="stars">\u2605<span class="off">\u2605\u2605\u2605\u2605</span></span>
            <span class="thumbs">\U0001f44d 53</span>
          </div>
        </div>

        <div class="v8-pain">
          <div class="v8-pain-num">04<span class="sub">TEXT-ONLY</span></div>
          <h3 class="v8-pain-head">Visuals are<br><em>an afterthought.</em></h3>
          <p class="v8-pain-quote">Profile photo is all you get. No scenes, no backgrounds \u2014 just walls of text.</p>
          <div class="v8-pain-attr">
            <img src="https://play-lh.googleusercontent.com/dAVjIN_4fDErGgl_zMmb81QQSckVOg5LhpMR5liy5QrE8sglxM26MyCgIxsd5qzFyzHfGskqYpjwGD-LXt9Ugw4=w240-h480" alt="Character.AI" loading="lazy">
            <b>Character.AI</b>
            <span class="stars">\u2605<span class="off">\u2605\u2605\u2605\u2605</span></span>
            <span class="thumbs">\U0001f44d 28</span>
          </div>
        </div>

      </div>

      <!-- RIGHT: Lucive confident answer -->
      <div class="v8-lucive">
        <div class="v8-lucive-kicker">SO WE JUST</div>
        <h2 class="v8-lucive-head">Built it <em>this</em><br>way, instead.</h2>

        <div class="v8-phone">
          <div class="v8-phone-bar">
            <div class="av">A</div>
            <div>
              <div class="nm">Aria</div>
              <div style="font-size:10px;color:var(--muted);font-family:var(--mono);margin-top:1px">LP \u00b7 Harbor scene</div>
            </div>
            <div class="st">Memory sync</div>
          </div>

          <div class="v8-stage">
            <div class="v8-bg-tag">\u25cf Harbor \u00b7 Backdrop stays</div>
            <div class="char"></div>

            <div class="v8-chat">
              <div class="v8-msg aria" style="margin-top:auto">
                <span class="nm">Aria \u00b7 15 min ago</span>
                <span class="mem">\u25cf proactive msg from 7-day memory</span>
                "I found an old photo from the harbor. Hey \u2014 we never talked about that day, did we?"
              </div>
              <div class="v8-msg user">"...the harbor?"</div>
              <div class="v8-msg aria">
                <span class="nm">Aria</span>
                "Yeah. Before we moved to Neon-7. Also the last place I was with your brother before the '29 sim collapse."
              </div>
            </div>
          </div>

          <div class="v8-chrome">
            <span>\U0001f48e Message <b>1 Dip</b></span>
            <span class="sep">\u00b7</span>
            <span>Pricing <b>same standard, always</b></span>
          </div>
        </div>

        <div class="v8-statement">
          <p>These aren't <b>four separate features.</b><br>This is just <b>our default chat screen.</b></p>
          <p class="sub">Not four features stacked. Designed this way from day one.</p>
        </div>
      </div>

    </div>

    <!-- Overflow tags at bottom -->
    <div class="v8-more rv">
      <div class="v8-more-intro">And <b>disappointments that repeat across 1,200+ reviews</b>:</div>
      <div class="v8-more-tags">
        <span class="v8-more-tag">filter updates blocking chats</span>
        <span class="v8-more-tag">sudden account bans</span>
        <span class="v8-more-tag">tone shifts with no context</span>
        <span class="v8-more-tag">chat history wiped</span>
        <span class="v8-more-tag">ignoring set rules</span>
        <span class="v8-more-tag">ads every 2 minutes</span>
        <span class="v8-more-tag">paid plans still forget</span>
        <span class="v8-more-tag">3D avatar optimization broken</span>
      </div>
    </div>

  </div>
</section>"""
    else:
        raise ValueError(region)

# -- Process one file -----------------------------------------------------
def build_variant(src_path: Path, dst_path: Path, token_map: dict, region: str):
    src = src_path.read_text(encoding='utf-8')

    # 1. Replace uni-* CSS block with adapted v8 CSS
    css_pattern = re.compile(
        r'/\* === UNIFIED variation .*?\.uni-cap em\{[^}]*\}',
        re.DOTALL,
    )
    if not css_pattern.search(src):
        sys.exit(f'[err] uni-* CSS block not found in {src_path.name}')
    adapted_css = adapt(V8_CSS, token_map)
    src = css_pattern.sub(adapted_css, src)

    # 2. Replace vs-section HTML block with v8 HTML
    html_block = build_html(region)
    html_pattern = re.compile(
        r'<!-- Unified variation.*?</section>',
        re.DOTALL,
    )
    if not html_pattern.search(src):
        sys.exit(f'[err] Unified variation HTML block not found in {src_path.name}')
    src = html_pattern.sub(html_block, src, count=1)

    dst_path.write_text(src, encoding='utf-8')
    print(f'[ok] wrote {dst_path.name} ({len(src)} chars)')

# -- Run ------------------------------------------------------------------
if __name__ == '__main__':
    build_variant(HERE / 'v7-jp-unified.html', HERE / 'v8-jp-unified.html', JP_TOKENS, 'jp')
    build_variant(HERE / 'v7-en-unified.html', HERE / 'v8-en-unified.html', EN_TOKENS, 'en')
    print('[done]')
