#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMPIRE AUTO-VIDEO PIPELINE v16.2 (MULTIVERSE ANIMATION & LIP-SYNC EDITION)
Automated High-Performance Viral Animated Universe for YouTube Shorts:
- 100% Channel Separation (AI Educational Explainer vs Elite Wealth Noir)
- Channel 1 (ch02_ar_ai_tech): "الدحيح التكنولوجي" hosted by Dr. Rayan (د. ريان)
  100% Modern Standard Arabic (الفصحى السلسة الراقية), Educational Storytelling,
  Real-time Frame-by-Frame Audio-Driven Lip-Sync, AI History & Autonomous Agents.
- Channel 2 (ch03_en_wealth_business): "Billionaire Empires & Wealth"
  Lord Sterling the Raven Mastermind & Felix the Fox, 9-Scene Dual-Character Drama,
  Audio-Driven Jaw & Beak Articulation, Procedural Foley SFX, Madison Ave Noir.
- Direct Frame Streaming to FFmpeg (O(1) Constant Memory Footprint)
- Golden 65-85s YouTube Shorts Storytelling Window
- Automatic YouTube OAuth2 Publishing with Token Refresh
"""

import os
import sys
import json
import math
import time
import glob
import random
import shutil
import wave
import urllib.parse
import urllib.request
import subprocess
from pathlib import Path

# Force UTF-8 on Windows and Linux runners
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    HAS_ARABIC_SHAPER = True
except Exception:
    HAS_ARABIC_SHAPER = False

_hf_tok = os.environ.get("HF_TOKEN", "").strip()
if _hf_tok:
    os.environ["HF_TOKEN"] = _hf_tok

# ==============================================================================
# 1. VOICE & CHARACTER PROFILES (THE MULTIVERSE VOCAL CAST)
# ==============================================================================

VOICE_PROFILES = {
    "ch02_ar_ai_tech": {
        "rayan": {
            "name": "د. ريان (The Tech Daheeh)",
            "voice": "ar-EG-ShakirNeural",
            "rate": "+2%",
        },
        "mentor": {
            "name": "د. ريان (The Tech Daheeh)",
            "voice": "ar-EG-ShakirNeural",
            "rate": "+2%",
        },
        "consumer": {
            "name": "د. ريان (The Tech Daheeh)",
            "voice": "ar-EG-ShakirNeural",
            "rate": "+2%",
        }
    },
    "ch03_en_wealth_business": {
        "mentor": {
            "name": "Lord Sterling (The Raven Mastermind)",
            "voice": "en-US-ChristopherNeural",
            "rate": "+0%",
        },
        "consumer": {
            "name": "Felix the Fox (The Ambitious Striver)",
            "voice": "en-US-BrianNeural",
            "rate": "+4%",
        }
    },
    # Backwards-compatible / language fallbacks
    "ar": {
        "rayan": {"name": "د. ريان", "voice": "ar-EG-ShakirNeural", "rate": "+2%"},
        "mentor": {"name": "د. ريان", "voice": "ar-EG-ShakirNeural", "rate": "+2%"},
        "consumer": {"name": "د. ريان", "voice": "ar-EG-ShakirNeural", "rate": "+2%"},
    },
    "en": {
        "mentor": {"name": "Lord Sterling", "voice": "en-US-ChristopherNeural", "rate": "+0%"},
        "consumer": {"name": "Felix the Fox", "voice": "en-US-BrianNeural", "rate": "+4%"},
    }
}

CHANNELS = {
    "ch02_ar_ai_tech": {
        "id": "ch02_ar_ai_tech",
        "name": "الذكاء الاصطناعي وتقنيات المستقبل",
        "niche": "The Tech Daheeh | AI History & Future Architecture",
        "lang": "ar",
        "secret_env": "YT_TOKEN_CH02_AR",
        "category_id": "28",  # Science & Technology
        "outro_line": "العالم يتغيّر بسرعة خارقة... لا تكن مجرد مشاهد سلبي، بل تعلّم، افهم، واصنع مستقبلك بيدك. اشترك لمتابعة رحلة الذكاء الاصطناعي!",
        "tags": ["الذكاء_الاصطناعي", "تكنولوجيا", "آلان_تورينج", "تاريخ_التكنولوجيا", "الدحيح", "اختبار_تورينج", "Shorts", "AI", "Technology"],
    },
    "ch03_en_wealth_business": {
        "id": "ch03_en_wealth_business",
        "name": "Billionaire Empires & Wealth",
        "niche": "Corporate Deceptions & Empire Building",
        "lang": "en",
        "secret_env": "YT_TOKEN_CH03_EN",
        "category_id": "27",  # Education / Business
        "outro_line": "The noise is for the crowd. Watch, learn, and evolve quietly — until you control the board.",
        "tags": ["Wealth", "Billionaires", "BusinessSecrets", "Psychology", "Power", "Shorts", "Animation"],
    },
}

# ==============================================================================
# 2. MASTER EPISODE BANKS (CHANNEL 1: TECH DAHEEH vs CHANNEL 2: WEALTH NOIR)
# ==============================================================================

# CHANNEL 1: The Tech Daheeh Format (100% Pure Modern Standard Arabic / الفصحى السلسة)
EPISODE_BANK_AR_AI = [
    {
        "series_title": "الدحيح التكنولوجي | أسرار الذكاء الاصطناعي",
        "part": "الحلقة 1",
        "title": "كيف بدأت فكرة الذكاء الاصطناعي؟ من لغز آلان تورينج إلى عصر الوكلاء الأذكياء #Shorts",
        "scenes": [
            {
                "speaker": "rayan",
                "character_focus": "rayan_hook",
                "narration": "هل يمكن للآلة أن تفكّر حقاً؟ في خريف عام 1950، طرح عالم عبقري سؤالاً واحداً... أحدث زلزالاً غيّر تاريخ البشرية إلى الأبد!",
                "caption": "هل يمكن للآلة أن تفكّر حقاً؟",
                "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Dr. Rayan an enthusiastic young Middle Eastern scientist in tweed jacket and round glasses leaning forward excitedly in a vintage laboratory, 9:16 vertical",
                "visual_style": "rayan_hook"
            },
            {
                "speaker": "rayan",
                "character_focus": "scene_bombe",
                "narration": "كان صاحب السؤال هو آلان تورينج، الرجل الذي فكك شيفرة إنيجما المعقدة أثناء الحرب العالمية الثانية بآلته الكهروميكانيكية العبقرية.",
                "caption": "آلان تورينج... العبقري الذي قهر إنيجما!",
                "sfx_cue": None,
                "visual_prompt": "1940 authentic British Bletchley Park Turing Bombe electromechanical codebreaking machine with rotating bronze drums, 9:16 vertical",
                "visual_style": "scene_bombe"
            },
            {
                "speaker": "rayan",
                "character_focus": "rayan_paper",
                "narration": "تورينج نشر ورقته التاريخية الشهيرة: 'آلات الحوسبة والذكاء'، واقترح فيها لعبة المحاكاة التي نعرفها اليوم باسم اختبار تورينج.",
                "caption": "1950: ولادة اختبار تورينج لذكاء الآلات!",
                "sfx_cue": "sfx_scratch",
                "visual_prompt": "Dr. Rayan holding up the authentic 1950 manuscript Computing Machinery and Intelligence by A. M. Turing with passionate scholarly smile, 9:16 vertical",
                "visual_style": "rayan_paper"
            },
            {
                "speaker": "rayan",
                "character_focus": "scene_dartmouth",
                "narration": "وبعد ست سنوات، في صيف عام 1956، اجتمع نخبة من علماء الرياضيات في كلية دارتموث، ليصكّوا رسمياً مصطلح: الذكاء الاصطناعي.",
                "caption": "1956: إطلاق مصطلح 'الذكاء الاصطناعي' رسمياً!",
                "sfx_cue": None,
                "visual_prompt": "1956 Dartmouth Summer Research Project on Artificial Intelligence conference room, chalkboard with mathematical equations, 9:16 vertical",
                "visual_style": "scene_dartmouth"
            },
            {
                "speaker": "rayan",
                "character_focus": "scene_neural",
                "narration": "الفكرة كانت ثورية: محاكاة الخلايا العصبية في الدماغ البشري، وبناء شبكات رياضية تتعلّم وتتحسّن ذاتياً بالتجربة والخطأ.",
                "caption": "محاكاة خلايا الدماغ... شبكات تتعلّم ذاتياً!",
                "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Deep neural network architecture showing glowing biological brain synapses transitioning into turquoise artificial neural nodes, 9:16 vertical",
                "visual_style": "scene_neural"
            },
            {
                "speaker": "rayan",
                "character_focus": "scene_mainframe",
                "narration": "انتقلنا من صمامات مفرغة ضخمة تملأ غرفاً كاملة، إلى رقائق سيليكون نانوية فائقة القوة تتدفق عبرها مليارات العمليات الحسابية في الثانية.",
                "caption": "من صمامات تملأ غرفاً... إلى رقائق نانوية فائقة!",
                "sfx_cue": None,
                "visual_prompt": "1960s room-sized IBM mainframe computer with spinning magnetic tape reels transitioning into glowing microchips, 9:16 vertical",
                "visual_style": "scene_mainframe"
            },
            {
                "speaker": "rayan",
                "character_focus": "scene_matrix",
                "narration": "واليوم، لم يعد الذكاء مجرد آلة حاسبة سريعة، بل أصبح وكلاء أذكياء يتخذون القرارات، يكتبون الشيفرات، وينسقون المهام باستقلالية تامة.",
                "caption": "اليوم: وكلاء أذكياء يعملون باستقلالية تامة!",
                "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Futuristic autonomous multi-agent matrix, interconnected autonomous neural AI agents collaborating across data streams, 9:16 vertical",
                "visual_style": "scene_matrix"
            },
            {
                "speaker": "rayan",
                "character_focus": "rayan_epiphany",
                "narration": "السؤال الحقيقي لم يعد هل يمكن للآلة أن تفكّر، بل هل أنت مستعد للتعامل مع عالم يفوق فيه تفكير الآلة خيالك؟",
                "caption": "السؤال الآن: هل أنت مستعد لما هو قادم؟",
                "sfx_cue": None,
                "visual_prompt": "Dr. Rayan gesturing with open hands in an intellectual eureka epiphany moment under glowing overhead lamp in tech lab, 9:16 vertical",
                "visual_style": "rayan_epiphany"
            },
            {
                "speaker": "rayan",
                "character_focus": "rayan_outro",
                "narration": "العالم يتغيّر بسرعة خارقة... لا تكن مجرد مشاهد سلبي، بل تعلّم، افهم، واصنع مستقبلك بيدك. اشترك معنا، ونلتقي في الحلقة القادمة!",
                "caption": "تعلّم واصنع مستقبلك بيدك... اشترك الآن!",
                "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Dr. Rayan adjusting his round glasses with a subtle confident intellectual smile, cozy tech study background, 9:16 vertical",
                "visual_style": "rayan_outro"
            }
        ]
    }
]

# CHANNEL 2: Dual-Character Elite Business Noir Format (Lord Sterling & Felix the Fox)
EPISODE_BANK_EN_WEALTH = [
    {
        "series_title": "Corporate Illusions & Wealth Architecture",
        "part": "Part 1",
        "title": "Part 1 | The Coffee Trap: How They Monetized Your Exhaustion #Shorts",
        "scenes": [
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "Eight hours on the grind... This eight-dollar latte is the only reward keeping my sanity intact.",
                "caption": "8 hours on the grind... This latte is my only reward!",
                "sfx_cue": None,
                "visual_prompt": "An anthropomorphic young red fox named Felix wearing a brown corduroy vest and newsboy cap, taking a satisfied sip from a steaming coffee mug at a vintage cafe counter, 1930s neo-noir animation style, 9:16 vertical",
                "visual_style": "cafe_consumer"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "A reward? Who convinced you that you need a 'coffee break' just to serve their machine harder?",
                "caption": "Who convinced you that you need a 'Coffee Break'?",
                "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Lord Sterling the anthropomorphic raven in an immaculate charcoal pinstripe suit and burgundy tie, checking a gold pocket watch with a cynical smirk, dark oak study library background, 9:16 vertical",
                "visual_style": "mentor_study"
            },
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "What are you talking about? It's a legally protected union break. What does manipulation have to do with it?",
                "caption": "It's my legal right... What manipulation?",
                "sfx_cue": "sfx_scratch",
                "visual_prompt": "Felix the fox lowering his coffee cup in shock, wide bewildered eyes, dropped jaw, cartoon disbelief expression at the cafe counter, 9:16 vertical",
                "visual_style": "cafe_shock"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "In 1952, post-war coffee sales collapsed. So Madison Avenue advertising cartels met in Manhattan and launched two words: 'Coffee Break.'",
                "caption": "1952: Madison Avenue invented the 'Coffee Break'!",
                "sfx_cue": None,
                "visual_prompt": "1952 Madison Avenue vintage boardroom, smoky air, advertising executives in tailored coats pointing at billboard sketches of steaming coffee cups, archival film grain, 9:16 vertical",
                "visual_style": "madison_boardroom"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "They convinced factory owners that a fifteen-minute caffeine hit boosts worker throughput by twenty percent. The break was never for your rest; it was to grease the gears of the factory.",
                "caption": "The break was never for your rest... but for factory output!",
                "sfx_cue": None,
                "visual_prompt": "1950s industrial factory floor, massive heavy steel gears, assembly line workers drinking coffee while factory managers smile at speedometers, moody steam, 9:16 vertical",
                "visual_style": "factory_production"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "Then they rebranded factory fuel into a luxury lifestyle badge. A beverage that costs thirty cents to brew... sold to you for eight dollars.",
                "caption": "Brewed for 30 cents... Sold to you for $8!",
                "sfx_cue": "sfx_register",
                "visual_prompt": "Sleek modern luxury cafe counter, glowing neon chalkboard menu showing overpriced coffee, gold coins spilling over cash register counter, 9:16 vertical",
                "visual_style": "luxury_cafe_pricing"
            },
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "So I'm paying with my own money... just to borrow energy for a company I don't even own?",
                "caption": "I pay to borrow energy... for a company I don't own?",
                "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Close-up of Felix the fox staring down at his coffee mug in dread, realization dawning on his face, dark moody lighting, 9:16 vertical",
                "visual_style": "consumer_epiphany"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "The consumer pays for his rest twice: once with his health, and once with his wallet. The wise never drink to escape reality; they architect the systems that harvest the crowd's labor.",
                "caption": "The wise never escape reality... They architect the systems!",
                "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Dramatic close-up of Lord Sterling adjusting his cufflinks, glowing amber eyes piercing the shadows, atmospheric library background, 9:16 vertical",
                "visual_style": "mentor_axiom"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "The noise is for the crowd. Watch, learn, and evolve quietly — until you control the board. Subscribe for Part 2.",
                "caption": "Evolve quietly... until you control the board!",
                "sfx_cue": None,
                "visual_prompt": "Lord Sterling turning toward a large mahogany door, silhouette against warm library chandelier, mysterious stoic departure, 9:16 vertical",
                "visual_style": "mentor_outro"
            }
        ]
    }
]

# Legacy alias for backward compatibility
EPISODE_BANK_AR = EPISODE_BANK_AR_AI
EPISODE_BANK_EN = EPISODE_BANK_EN_WEALTH

# ==============================================================================
# 3. TEXT SHAPING & KINETIC TYPOGRAPHY ENGINE (FLAWLESS ARABIC BOLD GUARANTEED)
# ==============================================================================

def shape_text(text: str, lang: str = "ar") -> str:
    """Prepares text with correct RTL shaping, character replacement, and zero glyph corruption."""
    if not text:
        return ""
    if lang == "ar":
        text = text.replace("$", " دولار").replace("  ", " ")
        if HAS_ARABIC_SHAPER:
            try:
                config = {'delete_harakat': True, 'support_ligatures': False}
                reshaper = arabic_reshaper.ArabicReshaper(configuration=config)
                reshaped = reshaper.reshape(text)
                return get_display(reshaped)
            except Exception:
                return text
    return text


def get_font(size: int = 48, lang: str = "ar", bold: bool = True) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Retrieves high-legibility bold fonts for video typography."""
    repo_root = Path(__file__).resolve().parent
    if lang == "ar":
        font_candidates = [
            repo_root / "assets" / "fonts" / "NotoSansArabic-Bold.ttf",
            repo_root / "assets" / "fonts" / "Amiri-Bold.ttf",
            Path("C:/Windows/Fonts/seguisb.ttf"),
            Path("C:/Windows/Fonts/segoeui.ttf"),
            Path("/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf"),
            Path("/usr/share/fonts/truetype/amiri/amiri-bold.ttf"),
            Path("/usr/share/fonts/truetype/amiri/Amiri-Bold.ttf"),
            repo_root / "assets" / "fonts" / "Cairo.ttf",
        ]
    else:
        font_candidates = [
            repo_root / "assets" / "fonts" / "Cairo.ttf",
            repo_root / "assets" / "fonts" / "Amiri-Bold.ttf",
            Path("C:/Windows/Fonts/arialbd.ttf"),
            Path("C:/Windows/Fonts/segoeui.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        ]

    for p in font_candidates:
        if p.exists():
            try:
                return ImageFont.truetype(str(p), size=size)
            except Exception:
                continue

    try:
        f_dir = repo_root / "assets" / "fonts"
        f_dir.mkdir(parents=True, exist_ok=True)
        target_f = f_dir / "NotoSansArabic-Bold.ttf" if lang == "ar" else f_dir / "Cairo.ttf"
        if not target_f.exists():
            u = "https://github.com/googlefonts/noto-arabic/raw/main/hinted/ttf/NotoSansArabic/NotoSansArabic-Bold.ttf" if lang == "ar" else "https://github.com/google/fonts/raw/main/ofl/cairo/Cairo%5Bslnt%2Cwght%5D.ttf"
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                target_f.write_bytes(resp.read())
            return ImageFont.truetype(str(target_f), size=size)
    except Exception:
        pass

    return ImageFont.load_default()

# ==============================================================================
# 4. PROCEDURAL FOLEY SFX & AUDIO SYNTHESIS ENGINE
# ==============================================================================

def generate_procedural_sfx(sfx_name: str, out_wav: Path):
    """Generates broadcast-grade procedural Foley sound effects using pure mathematics."""
    sr = 44100
    if sfx_name == "sfx_register":
        t = np.linspace(0, 0.8, int(sr * 0.8), endpoint=False)
        bell = (np.sin(2 * np.pi * 1850 * t) * 0.5 + np.sin(2 * np.pi * 2470 * t) * 0.3) * np.exp(-t * 6.0)
        click = np.random.normal(0, 0.3, len(t)) * (t < 0.05) * np.exp(-t * 40.0)
        audio = bell + click
    elif sfx_name == "sfx_heartbeat":
        t = np.linspace(0, 0.8, int(sr * 0.8), endpoint=False)
        p1 = np.sin(2 * np.pi * 55 * t) * np.exp(-((t - 0.15) / 0.06)**2)
        p2 = np.sin(2 * np.pi * 50 * t) * np.exp(-((t - 0.40) / 0.07)**2) * 0.8
        audio = (p1 + p2) * 0.85
    elif sfx_name == "sfx_whoosh":
        t = np.linspace(0, 0.6, int(sr * 0.6), endpoint=False)
        noise = np.random.normal(0, 0.4, len(t))
        env = np.sin(np.pi * t / 0.6)**2
        audio = noise * env
    elif sfx_name == "sfx_subdrop":
        t = np.linspace(0, 1.2, int(sr * 1.2), endpoint=False)
        freq = 90.0 - 55.0 * (1.0 - np.exp(-t * 4.0))
        phase = 2 * np.pi * np.cumsum(freq) / sr
        audio = np.sin(phase) * np.exp(-t * 2.2) * 0.95
    elif sfx_name == "sfx_scratch":
        t = np.linspace(0, 0.4, int(sr * 0.4), endpoint=False)
        f_sweep = np.linspace(1200, 100, len(t))
        scratch = np.sin(2 * np.pi * np.cumsum(f_sweep) / sr) * np.exp(-t * 5.0)
        scratch += np.random.normal(0, 0.15, len(t)) * np.exp(-t * 8.0)
        audio = scratch * 0.75
    else:
        t = np.linspace(0, 0.1, int(sr * 0.1), endpoint=False)
        audio = np.sin(2 * np.pi * 800 * t) * np.exp(-t * 30.0)

    audio_16 = (np.clip(audio, -0.95, 0.95) * 32767).astype(np.int16)
    with wave.open(str(out_wav), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(audio_16.tobytes())


def synthesize_cinematic_sub_bass_drone(duration: float, out_wav: Path):
    """Synthesizes deep cinematic atmospheric tension drone (58.27 Hz D-minor fundamental)."""
    sample_rate = 44100
    n_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, n_samples, endpoint=False)

    f0 = 58.27
    drone = 0.50 * np.sin(2 * np.pi * f0 * t)
    drone += 0.25 * np.sin(2 * np.pi * (f0 * 1.5) * t)
    drone += 0.15 * np.sin(2 * np.pi * (f0 * 2.0) * t)
    drone += 0.10 * np.sin(2 * np.pi * (f0 * 3.0) * t)

    lfo = 0.85 + 0.15 * np.sin(2 * np.pi * 0.18 * t)
    drone = drone * lfo

    noise = np.random.normal(0, 0.012, n_samples)
    audio = np.clip(drone + noise, -0.92, 0.92)

    audio_16 = (audio * 32767).astype(np.int16)
    with wave.open(str(out_wav), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_16.tobytes())


def synthesize_dual_voice_scene(
    channel_key: str,
    text: str,
    speaker: str,
    lang: str,
    sfx_cue: str | None,
    out_mp3: Path,
    work_dir: Path
) -> float:
    """Synthesizes crystal-clear voice acting with Foley SFX."""
    ch_profiles = VOICE_PROFILES.get(channel_key, VOICE_PROFILES.get(lang, VOICE_PROFILES["ar"]))
    profile = ch_profiles.get(speaker, ch_profiles.get("mentor", {"name": "Host", "voice": "ar-EG-ShakirNeural", "rate": "+2%"}))
    voice = profile["voice"]
    rate = profile.get("rate", "+0%")

    raw_voice_mp3 = work_dir / f"raw_{out_mp3.name}"

    try:
        cmd = [
            sys.executable, "-m", "edge_tts",
            "--voice", voice,
            f"--rate={rate}",
            "--text", text,
            "--write-media", str(raw_voice_mp3),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=35)
    except Exception as e:
        print(f"  [TTS Notice] edge-tts error ({e}); using gTTS fallback...")
        from gtts import gTTS
        gTTS(text=text, lang=lang, slow=False).save(str(raw_voice_mp3))

    # If Foley SFX cue is specified, mix SFX without attenuating dialogue (normalize=0)
    if sfx_cue:
        sfx_wav = work_dir / f"{sfx_cue}.wav"
        generate_procedural_sfx(sfx_cue, sfx_wav)
        try:
            mix_cmd = [
                "ffmpeg", "-y",
                "-i", str(raw_voice_mp3),
                "-i", str(sfx_wav),
                "-filter_complex", "[0:a]volume=1.0[v];[1:a]volume=0.32[s];[v][s]amix=inputs=2:duration=first:normalize=0[a]",
                "-map", "[a]",
                "-c:a", "aac",
                "-b:a", "192k",
                str(out_mp3)
            ]
            subprocess.run(mix_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=15)
        except Exception:
            shutil.copy(str(raw_voice_mp3), str(out_mp3))
    else:
        shutil.copy(str(raw_voice_mp3), str(out_mp3))

    # Probe duration
    try:
        res = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(out_mp3)],
            capture_output=True, text=True, check=True
        )
        return float(res.stdout.strip())
    except Exception:
        return max(3.5, len(text.split()) * 0.45)

# ==============================================================================
# 5. VISUAL GENERATION & MULTIVERSE ASSET RESOLUTION
# ==============================================================================

def create_dark_cinematic_procedural_backdrop(style_hint: str, target_w: int = 1080, target_h: int = 1920) -> Image.Image:
    """Generates high-contrast neo-noir background when offline/fallback."""
    img = Image.new("RGB", (target_w, target_h), (12, 14, 20))
    draw = ImageDraw.Draw(img)

    if any(k in style_hint for k in ("boardroom", "madison", "1952", "vintage")):
        top_c, bot_c = (24, 20, 16), (8, 6, 6)
        accent = (255, 195, 65, 40)
    elif any(k in style_hint for k in ("factory", "production", "gear", "machine")):
        top_c, bot_c = (20, 22, 26), (6, 8, 10)
        accent = (200, 215, 230, 35)
    elif any(k in style_hint for k in ("luxury", "pricing", "gold", "coins")):
        top_c, bot_c = (28, 22, 12), (8, 6, 4)
        accent = (255, 215, 60, 45)
    elif any(k in style_hint for k in ("tech", "matrix", "agent", "neural")):
        top_c, bot_c = (10, 24, 38), (4, 8, 16)
        accent = (0, 225, 255, 40)
    else:
        top_c, bot_c = (18, 16, 24), (8, 6, 12)
        accent = (220, 180, 240, 30)

    for y in range(target_h):
        alpha = y / float(target_h)
        r = int(top_c[0] * (1.0 - alpha) + bot_c[0] * alpha)
        g = int(top_c[1] * (1.0 - alpha) + bot_c[1] * alpha)
        b = int(top_c[2] * (1.0 - alpha) + bot_c[2] * alpha)
        draw.line([(0, y), (target_w, y)], fill=(r, g, b))

    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    d_over = ImageDraw.Draw(overlay, "RGBA")
    d_over.ellipse([target_w * 0.1, target_h * 0.15, target_w * 0.9, target_h * 0.65], fill=accent)
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def resolve_character_visual(
    channel_key: str,
    character_focus: str,
    style_hint: str,
    visual_prompt: str,
    scene_idx: int,
    out_jpg: Path
) -> Path:
    """Resolves character and scene visuals with 100% channel separation and character continuity."""
    repo_root = Path(__file__).resolve().parent
    chars_dir = repo_root / "assets" / "characters"
    scenes_dir = repo_root / "assets" / "scenes"

    # =========================================================================
    # CHANNEL 1: The Tech Daheeh (ch02_ar_ai_tech)
    # Strictly Dr. Rayan poses and historical AI scene visuals! Zero animal assets.
    # =========================================================================
    if channel_key == "ch02_ar_ai_tech":
        ai_map = {
            "rayan_hook": chars_dir / "rayan_hook.jpg",
            "scene_bombe": scenes_dir / "turing_bombe_1940.jpg",
            "rayan_paper": chars_dir / "rayan_turing_paper.jpg",
            "scene_dartmouth": scenes_dir / "dartmouth_conference_1956.jpg",
            "scene_neural": scenes_dir / "neural_network_synapse.jpg",
            "scene_mainframe": scenes_dir / "vintage_mainframe_1960.jpg",
            "scene_matrix": scenes_dir / "autonomous_agent_matrix.jpg",
            "rayan_epiphany": chars_dir / "rayan_epiphany.jpg",
            "rayan_outro": chars_dir / "rayan_outro.jpg",
        }

        # Check by character_focus or style_hint
        for key, p in ai_map.items():
            if (key in character_focus or key in style_hint) and p.exists():
                return p

        # Check by content keywords
        vp = visual_prompt.lower()
        if "bombe" in vp or "1940" in vp or "enigma" in vp:
            p = scenes_dir / "turing_bombe_1940.jpg"
            if p.exists(): return p
        if "dartmouth" in vp or "1956" in vp:
            p = scenes_dir / "dartmouth_conference_1956.jpg"
            if p.exists(): return p
        if "neural" in vp or "synapse" in vp or "brain" in vp:
            p = scenes_dir / "neural_network_synapse.jpg"
            if p.exists(): return p
        if "mainframe" in vp or "1960" in vp or "vacuum" in vp:
            p = scenes_dir / "vintage_mainframe_1960.jpg"
            if p.exists(): return p
        if "agent" in vp or "matrix" in vp:
            p = scenes_dir / "autonomous_agent_matrix.jpg"
            if p.exists(): return p
        if "paper" in vp or "manuscript" in vp:
            p = chars_dir / "rayan_turing_paper.jpg"
            if p.exists(): return p
        if "epiphany" in vp or "eureka" in vp:
            p = chars_dir / "rayan_epiphany.jpg"
            if p.exists(): return p
        if "outro" in vp or "glasses" in vp:
            p = chars_dir / "rayan_outro.jpg"
            if p.exists(): return p

        # Default to Rayan hook
        p = chars_dir / "rayan_hook.jpg"
        if p.exists(): return p

        bd = create_dark_cinematic_procedural_backdrop("tech_matrix")
        bd.save(str(out_jpg))
        return out_jpg

    # =========================================================================
    # CHANNEL 2: Wealth & Empires Noir (ch03_en_wealth_business)
    # Lord Sterling the Raven, Felix the Fox, and Madison Ave Noir.
    # =========================================================================
    style_map = {
        "madison_boardroom": scenes_dir / "madison_boardroom_1952.jpg",
        "factory_production": scenes_dir / "factory_production_floor.jpg",
        "luxury_cafe_pricing": scenes_dir / "luxury_cafe_pricing.jpg",
        "cafe_consumer": chars_dir / "felix_fox_consumer.jpg",
        "cafe_shock": chars_dir / "felix_fox_shock.jpg",
        "consumer_epiphany": chars_dir / "felix_fox_epiphany.jpg",
        "mentor_study": chars_dir / "sterling_raven_mentor.jpg",
        "mentor_axiom": chars_dir / "sterling_raven_cufflinks.jpg",
        "mentor_outro": chars_dir / "sterling_raven_mentor.jpg",
    }
    for key, p in style_map.items():
        if key in style_hint and p.exists():
            return p

    # Character-specific shots & expressions
    if character_focus == "consumer":
        if ("shock" in style_hint or scene_idx == 2) and (chars_dir / "felix_fox_shock.jpg").exists():
            return chars_dir / "felix_fox_shock.jpg"
        if ("epiphany" in style_hint or scene_idx >= 6) and (chars_dir / "felix_fox_epiphany.jpg").exists():
            return chars_dir / "felix_fox_epiphany.jpg"
        if (chars_dir / "felix_fox_consumer.jpg").exists():
            return chars_dir / "felix_fox_consumer.jpg"

    if character_focus == "mentor":
        if ("axiom" in style_hint or "cufflinks" in style_hint or scene_idx == 7) and (chars_dir / "sterling_raven_cufflinks.jpg").exists():
            return chars_dir / "sterling_raven_cufflinks.jpg"
        if (chars_dir / "sterling_raven_mentor.jpg").exists():
            return chars_dir / "sterling_raven_mentor.jpg"

    # Flashbacks: Dedicated scene artwork
    if character_focus == "flashback":
        if "boardroom" in visual_prompt.lower() or "1952" in visual_prompt:
            p = scenes_dir / "madison_boardroom_1952.jpg"
            if p.exists(): return p
        if "factory" in visual_prompt.lower() or "gear" in visual_prompt.lower():
            p = scenes_dir / "factory_production_floor.jpg"
            if p.exists(): return p
        if "luxury" in visual_prompt.lower() or "price" in visual_prompt.lower() or "cafe" in visual_prompt.lower():
            p = scenes_dir / "luxury_cafe_pricing.jpg"
            if p.exists(): return p

        bd = create_dark_cinematic_procedural_backdrop(style_hint)
        bd.save(str(out_jpg))
        return out_jpg

    # Final fallback
    if (chars_dir / "sterling_raven_mentor.jpg").exists():
        return chars_dir / "sterling_raven_mentor.jpg"
    return out_jpg

# ==============================================================================
# 6. KINETIC TYPOGRAPHY & CINEMATIC CAPTION OVERLAY
# ==============================================================================

def render_cinematic_caption_overlay(
    caption_text: str,
    lang: str,
    target_w: int = 1080,
    target_h: int = 1920,
) -> Image.Image:
    """Renders crisp, centered, elegant subtitles in frosted dark container with gold accents as a PIL RGBA overlay."""
    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay, "RGBA")

    f_cap = get_font(size=46, lang=lang, bold=True)
    center_x = target_w // 2
    center_y = int(target_h * 0.72)  # Centered in lower third to keep character faces clear

    words = caption_text.split()
    if len(words) > 6:
        mid = len(words) // 2
        l1 = " ".join(words[:mid])
        l2 = " ".join(words[mid:])

        r1 = shape_text(l1, lang)
        r2 = shape_text(l2, lang)

        bb1 = draw.textbbox((0, 0), r1, font=f_cap)
        bb2 = draw.textbbox((0, 0), r2, font=f_cap)
        w1, h1 = bb1[2] - bb1[0], bb1[3] - bb1[1]
        w2, h2 = bb2[2] - bb2[0], bb2[3] - bb2[1]

        max_w = max(w1, w2)
        line_spacing = 22
        total_h = h1 + h2 + line_spacing
        pad_x, pad_y = 38, 20

        x0 = max(40, center_x - max_w // 2 - pad_x)
        y0 = center_y - total_h // 2 - pad_y
        x1 = min(target_w - 40, center_x + max_w // 2 + pad_x)
        y1 = center_y + total_h // 2 + pad_y

        draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(8, 10, 16, 225), outline=(255, 215, 60, 45), width=2)
        draw.text((center_x, center_y - (h2 // 2 + line_spacing // 2)), r1, font=f_cap, fill=(255, 255, 255, 255), anchor="mm")
        draw.text((center_x, center_y + (h1 // 2 + line_spacing // 2)), r2, font=f_cap, fill=(255, 215, 60, 255), anchor="mm")
    else:
        shaped = shape_text(caption_text, lang)
        bb = draw.textbbox((0, 0), shaped, font=f_cap)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        pad_x, pad_y = 36, 18

        x0 = max(40, center_x - tw // 2 - pad_x)
        y0 = center_y - th // 2 - pad_y
        x1 = min(target_w - 40, center_x + tw // 2 + pad_x)
        y1 = center_y + th // 2 + pad_y

        draw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(8, 10, 16, 225), outline=(255, 215, 60, 45), width=2)
        draw.text((center_x, center_y), shaped, font=f_cap, fill=(255, 215, 60, 255), anchor="mm")

    return overlay

# ==============================================================================
# 7. AUDIO-DRIVEN LIP-SYNC & DIRECT-STREAMING RENDERER (O(1) CONSTANT RAM)
# ==============================================================================

def stream_render_scene(
    visual_path: Path,
    caption: str,
    lang: str,
    duration: float,
    scene_mp3: Path,
    scene_mp4: Path,
    scene_idx: int = 0,
    fps: int = 30,
    target_w: int = 1080,
    target_h: int = 1920,
) -> bool:
    """
    Renders video frames with real-time frame-by-frame audio lip-sync and camera dynamics,
    streaming directly to FFmpeg stdin pipe without buffering the full video in RAM.
    """
    repo_root = Path(__file__).resolve().parent
    chars_dir = repo_root / "assets" / "characters"

    n_frames = max(15, int(round(duration * fps)))

    # 1. Extract audio RMS envelope frame-by-frame for lip-sync modulation
    wav_temp = scene_mp3.with_suffix(".tmp.wav")
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(scene_mp3), "-ar", "24000", "-ac", "1", str(wav_temp)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        with wave.open(str(wav_temp), 'rb') as wf:
            sr = wf.getframerate()
            n_samples = wf.getnframes()
            raw_bytes = wf.readframes(n_samples)
            audio = np.frombuffer(raw_bytes, dtype=np.int16).astype(np.float32) / 32768.0
    except Exception:
        sr = 24000
        n_samples = int(duration * sr)
        audio = np.zeros(n_samples, dtype=np.float32)
    finally:
        if wav_temp.exists():
            try: os.remove(wav_temp)
            except Exception: pass

    samples_per_frame = max(1, int(sr / fps))
    envelope = []
    for f in range(n_frames):
        start = f * samples_per_frame
        end = min(len(audio), start + samples_per_frame)
        chunk = audio[start:end]
        rms = np.sqrt(np.mean(chunk**2)) if len(chunk) > 0 else 0.0
        envelope.append(rms)

    env = np.array(envelope)
    if env.max() > 0:
        env = env / env.max()
    smoothed = np.convolve(env, [0.15, 0.70, 0.15], mode='same')

    # 2. Identify character visual & load sprites
    fname = visual_path.name.lower()
    is_rayan = "rayan" in fname
    is_fox = "fox" in fname
    is_raven = "raven" in fname or "sterling" in fname

    base_raw = None
    if visual_path.exists() and visual_path.stat().st_size > 10_000:
        try:
            base_raw = Image.open(visual_path).convert("RGB")
        except Exception:
            base_raw = None

    if base_raw is None:
        base_raw = create_dark_cinematic_procedural_backdrop("noir", 768, 1376)

    bw, bh = base_raw.size

    # Prepare Dr. Rayan Lip Sync sprites if applicable
    m_closed = None
    m_open = None
    r_mask = None
    rayan_mx0, rayan_my0 = 344, 453
    if is_rayan:
        c_p = chars_dir / "rayan_mouth_closed.jpg"
        o_p = chars_dir / "rayan_mouth_open.jpg"
        if c_p.exists() and o_p.exists():
            try:
                m_closed = Image.open(c_p).convert("RGB")
                m_open = Image.open(o_p).convert("RGB")
                mw, mh = m_closed.size
                r_mask = Image.new("L", (mw, mh), 0)
                d_m = ImageDraw.Draw(r_mask)
                d_m.ellipse([int(mw * 0.08), int(mh * 0.12), int(mw * 0.92), int(mh * 0.88)], fill=255)
                r_mask = r_mask.filter(ImageFilter.GaussianBlur(radius=5))
                if "epiphany" in fname:
                    rayan_mx0, rayan_my0 = 350, 455
                elif "hook" in fname:
                    rayan_mx0, rayan_my0 = 346, 455
            except Exception:
                m_closed, m_open, r_mask = None, None, None

    # Prepare Fox jaw sprite if applicable
    fox_jaw = None
    fox_mask = None
    fjx0, fjy0, fjx1, fjy1 = int(bw * 0.42), int(bh * 0.37), int(bw * 0.58), int(bh * 0.46)
    if is_fox:
        try:
            fox_jaw = base_raw.crop((fjx0, fjy0, fjx1, fjy1))
            jw, jh = fjx1 - fjx0, fjy1 - fjy0
            fox_mask = Image.new("L", (jw, jh), 0)
            d_f = ImageDraw.Draw(fox_mask)
            d_f.ellipse([int(jw * 0.1), int(jh * 0.15), int(jw * 0.9), int(jh * 0.85)], fill=255)
            fox_mask = fox_mask.filter(ImageFilter.GaussianBlur(radius=3))
        except Exception:
            fox_jaw, fox_mask = None, None

    # Prepare Raven beak sprite if applicable
    raven_beak = None
    raven_mask = None
    rbx0, rby0, rbx1, rby1 = int(bw * 0.43), int(bh * 0.28), int(bw * 0.57), int(bh * 0.37)
    if is_raven:
        try:
            raven_beak = base_raw.crop((rbx0, rby0, rbx1, rby1))
            rw, rh = rbx1 - rbx0, rby1 - rby0
            raven_mask = Image.new("L", (rw, rh), 0)
            d_r = ImageDraw.Draw(raven_mask)
            d_r.ellipse([int(rw * 0.1), int(rh * 0.15), int(rw * 0.9), int(rh * 0.85)], fill=255)
            raven_mask = raven_mask.filter(ImageFilter.GaussianBlur(radius=3))
        except Exception:
            raven_beak, raven_mask = None, None

    # Pre-render caption overlay
    caption_overlay = render_cinematic_caption_overlay(caption, lang, target_w=target_w, target_h=target_h)

    # Launch FFmpeg streaming process with noise filter for cinematic broadcast texture
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-pix_fmt", "rgb24",
        "-s", f"{target_w}x{target_h}",
        "-r", str(fps),
        "-i", "-",
        "-i", str(scene_mp3),
        "-vf", "noise=c1s=3:c0f=t",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        str(scene_mp4)
    ]
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        for f in range(n_frames):
            t = f / float(n_frames)
            eng = float(smoothed[f]) if f < len(smoothed) else 0.0

            # -------------------------------------------------------------
            # A. Dynamic Character Articulation (Frame-by-Frame)
            # -------------------------------------------------------------
            frame_char = base_raw.copy()

            if is_rayan and m_closed is not None and m_open is not None and r_mask is not None:
                # Dr. Rayan Lip-Sync Syllable Blending
                if eng < 0.07:
                    frame_char.paste(m_closed, (rayan_mx0, rayan_my0), r_mask)
                else:
                    syllable = 0.50 + 0.50 * abs(math.sin(f * 1.55))
                    alpha = min(1.0, (eng - 0.07) * 3.2) * syllable
                    blended = Image.blend(m_closed, m_open, alpha)
                    frame_char.paste(blended, (rayan_mx0, rayan_my0), r_mask)

            elif is_fox and fox_jaw is not None and fox_mask is not None:
                # Felix Fox Jaw / Snout Articulation
                if eng >= 0.08:
                    stretch = 1.0 + (0.16 * eng * (0.50 + 0.50 * abs(math.sin(f * 1.6))))
                    jw, jh = fox_jaw.size
                    jaw_str = fox_jaw.resize((jw, max(1, int(jh * stretch))), Image.Resampling.BILINEAR)
                    jaw_crop = jaw_str.crop((0, int(jh * (stretch - 1.0)), jw, int(jh * (stretch - 1.0)) + jh))
                    frame_char.paste(jaw_crop, (fjx0, fjy0 + int(eng * 5)), fox_mask)

            elif is_raven and raven_beak is not None and raven_mask is not None:
                # Lord Sterling Beak Articulation
                if eng >= 0.08:
                    stretch = 1.0 + (0.14 * eng * (0.50 + 0.50 * abs(math.sin(f * 1.5))))
                    rw, rh = raven_beak.size
                    beak_str = raven_beak.resize((rw, max(1, int(rh * stretch))), Image.Resampling.BILINEAR)
                    beak_crop = beak_str.crop((0, int(rh * (stretch - 1.0)), rw, int(rh * (stretch - 1.0)) + rh))
                    frame_char.paste(beak_crop, (rbx0, rby0 + int(eng * 4)), raven_mask)

            # -------------------------------------------------------------
            # B. Speaking Movement: Head Bob, Saccades & Idle Breathing
            # -------------------------------------------------------------
            head_dy = int(math.sin(f * 0.45) * 5 * eng) + int(math.sin(f * 0.12) * 2)
            head_dx = int(math.cos(f * 0.30) * 3 * eng)

            # -------------------------------------------------------------
            # C. Cinematic Camera Kinematics (Ken Burns Zoom & Drift)
            # -------------------------------------------------------------
            if scene_idx % 2 == 0:
                scale = 1.0 + 0.08 * t
                cam_x = int(math.sin(t * math.pi) * 12) + head_dx
                cam_y = head_dy
            else:
                scale = 1.08 - 0.08 * t
                cam_x = int(-math.sin(t * math.pi) * 12) + head_dx
                cam_y = head_dy

            # Crop directly on character coordinates (aspect ratio 9:16)
            cw = int(bw / scale)
            ch = int(cw * (target_h / target_w))
            if ch > bh:
                ch = bh
                cw = int(ch * (target_w / target_h))

            cx0 = max(0, min(bw - cw, (bw - cw) // 2 + cam_x))
            cy0 = max(0, min(bh - ch, (bh - ch) // 2 + cam_y))

            frame_crop = frame_char.crop((cx0, cy0, cx0 + cw, cy0 + ch)).resize((target_w, target_h), Image.Resampling.BILINEAR)

            # Composite subtitle overlay
            frame_crop.paste(caption_overlay, (0, 0), caption_overlay)

            # Stream direct to FFmpeg pipe
            proc.stdin.write(frame_crop.tobytes())

        proc.stdin.close()
        proc.wait()
        return scene_mp4.exists() and scene_mp4.stat().st_size > 10_000
    except Exception as e:
        print(f"  [Render Error] Scene streaming failed: {e}")
        try:
            proc.kill()
        except Exception:
            pass
        return False

# ==============================================================================
# 8. MASTER EPISODE PRODUCER
# ==============================================================================

def produce_v16_animated_episode(channel_key: str, cfg: dict, output_root: Path) -> tuple[Path, dict]:
    """Produces a broadcast-ready YouTube Short with dedicated formatting per channel."""
    W, H, FPS = 1080, 1920, 30
    lang = cfg["lang"]
    work_dir = output_root / f"work_{channel_key}"
    work_dir.mkdir(parents=True, exist_ok=True)

    # 1. Select Episode Script with 100% Channel Separation
    run_num = int(os.environ.get("GITHUB_RUN_NUMBER", "1") or 1)
    if channel_key == "ch02_ar_ai_tech":
        bank = EPISODE_BANK_AR_AI
    elif channel_key == "ch03_en_wealth_business":
        bank = EPISODE_BANK_EN_WEALTH
    else:
        bank = EPISODE_BANK_AR_AI if lang == "ar" else EPISODE_BANK_EN_WEALTH

    script_data = bank[run_num % len(bank)]
    title = script_data["title"]
    scenes = script_data["scenes"]

    print(f"\n[{channel_key}] Producing Multiverse Short: '{title}' ({len(scenes)} scenes)")

    final_mp4 = output_root / f"{channel_key}_latest.mp4"
    scene_video_paths = []

    # 2. Render each scene
    for s_idx, scene in enumerate(scenes):
        speaker = scene.get("speaker", "mentor")
        sfx_cue = scene.get("sfx_cue")
        print(f"  --- Scene {s_idx + 1}/{len(scenes)} [{speaker.upper()}]: {scene['caption'][:40]}... (SFX: {sfx_cue}) ---")

        scene_mp3 = work_dir / f"scene_{s_idx}.mp3"
        scene_mp4 = work_dir / f"scene_{s_idx}.mp4"
        scene_visual = work_dir / f"visual_{s_idx}.jpg"

        # A. Voice Synthesis with procedural Foley SFX
        duration = synthesize_dual_voice_scene(
            channel_key=channel_key,
            text=scene["narration"],
            speaker=speaker,
            lang=lang,
            sfx_cue=sfx_cue,
            out_mp3=scene_mp3,
            work_dir=work_dir
        )

        # B. Resolve Character Asset with strict channel separation
        visual_path = resolve_character_visual(
            channel_key=channel_key,
            character_focus=scene.get("character_focus", "mentor"),
            style_hint=scene.get("visual_style", "dark"),
            visual_prompt=scene.get("visual_prompt", ""),
            scene_idx=s_idx,
            out_jpg=scene_visual
        )

        # C. Render animated scene directly to FFmpeg pipe with audio-reactive lip sync
        ok = stream_render_scene(
            visual_path=visual_path,
            caption=scene["caption"],
            lang=lang,
            duration=duration,
            scene_mp3=scene_mp3,
            scene_mp4=scene_mp4,
            scene_idx=s_idx,
            fps=FPS,
            target_w=W,
            target_h=H,
        )
        if ok and scene_mp4.exists():
            scene_video_paths.append(scene_mp4)

    # 3. Concatenate all scenes
    concat_list = work_dir / "concat.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for p in scene_video_paths:
            f.write(f"file '{p.resolve().as_posix()}'\n")

    combined_dry_mp4 = work_dir / "combined_dry.mp4"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(combined_dry_mp4)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    # 4. Layer procedural D-minor sub-bass tension drone under full audio
    total_duration = len(scenes) * 7.5
    try:
        res = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(combined_dry_mp4)],
            capture_output=True, text=True, check=True
        )
        total_duration = float(res.stdout.strip())
    except Exception:
        pass

    drone_wav = work_dir / "ambient_sub_bass_drone.wav"
    synthesize_cinematic_sub_bass_drone(total_duration + 2.0, drone_wav)

    # Final audio mix: Dialogue (1.0) + Sub-bass drone (0.15) with normalize=0 to preserve speech power
    final_cmd = [
        "ffmpeg", "-y",
        "-i", str(combined_dry_mp4),
        "-i", str(drone_wav),
        "-filter_complex", "[0:a]volume=1.0[v];[1:a]volume=0.15[d];[v][d]amix=inputs=2:duration=first:normalize=0[a]",
        "-map", "0:v",
        "-map", "[a]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        str(final_mp4)
    ]
    subprocess.run(final_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"[{channel_key}] SUCCESS! Exported Master Short: {final_mp4} ({final_mp4.stat().st_size // (1024*1024)} MB, {total_duration:.1f}s)")
    return final_mp4, script_data

# ==============================================================================
# 9. YOUTUBE PUBLISHER (WITH REFRESH TOKEN & SCOPE AUTO-HANDLING)
# ==============================================================================

def upload_to_youtube(video_path: Path, script_data: dict, cfg: dict) -> str | None:
    secret_env = cfg["secret_env"]
    token_raw = os.environ.get(secret_env, "").strip()
    client_id = os.environ.get("YT_CLIENT_ID", "").strip()
    client_secret = os.environ.get("YT_CLIENT_SECRET", "").strip()

    if not token_raw:
        print(f"  [YouTube Upload] {secret_env} is empty or not set in environment; skipping upload.")
        return None

    print("\n" + "=" * 70)
    print(f"  [YouTube Upload] Publishing Short for: {cfg['name']} ({secret_env})")
    print(f"  [YouTube Upload] Video file: {video_path} ({video_path.stat().st_size / (1024*1024):.2f} MB)")
    print("=" * 70)

    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload

        creds = None
        if token_raw.startswith("{"):
            token_info = json.loads(token_raw)
            creds = Credentials.from_authorized_user_info(token_info)
        else:
            creds = Credentials(
                token=None,
                refresh_token=token_raw,
                token_uri="https://oauth2.googleapis.com/token",
                client_id=client_id,
                client_secret=client_secret,
                scopes=None,
            )

        print("  [YouTube Upload] Refreshing access token with Google OAuth2...")
        try:
            creds.refresh(Request())
        except Exception:
            creds = Credentials(
                token=None,
                refresh_token=token_raw,
                token_uri="https://oauth2.googleapis.com/token",
                client_id=client_id,
                client_secret=client_secret,
                scopes=["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.force-ssl"],
            )
            creds.refresh(Request())
        print(f"  [YouTube Upload] Access token refreshed successfully! Valid: {creds.valid}")

        youtube = build("youtube", "v3", credentials=creds)
        title = script_data.get("title", f"{cfg['name']} #Shorts")[:98]
        desc = f"{title}\n\n{cfg['outro_line']}\n\n#Shorts #Animation #Viral #Science #Education #Future"

        body = {
            "snippet": {
                "title": title,
                "description": desc,
                "tags": cfg.get("tags", ["Shorts", "Animation", "Viral", "Documentary"]),
                "categoryId": cfg.get("category_id", "28"),
            },
            "status": {
                "privacyStatus": "public",
                "selfDeclaredMadeForKids": False,
            },
        }

        print(f"  [YouTube Upload] Uploading '{title}'...")
        media = MediaFileUpload(str(video_path), chunksize=1024 * 1024, resumable=True, mimetype="video/mp4")
        req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

        resp = None
        while resp is None:
            status, resp = req.next_chunk()
            if status:
                print(f"  [YouTube Upload] Upload progress: {int(status.progress() * 100)}%")

        vid_id = resp.get("id")
        print(f"  [YouTube Upload] SUCCESS! Video published: https://youtu.be/{vid_id}")
        return vid_id
    except Exception as e:
        print(f"  [YouTube Upload] ERROR during YouTube upload: {e}")
        import traceback
        traceback.print_exc()
        return None

# ==============================================================================
# 10. CLI MAIN ENTRY POINT
# ==============================================================================

def main():
    output_root = Path("output_videos")
    output_root.mkdir(parents=True, exist_ok=True)
    target_filter = os.environ.get("TARGET_CHANNEL", "all").strip().lower()

    for ch_key, cfg in CHANNELS.items():
        if target_filter not in ("all", "", ch_key.lower()):
            continue
        print("\n" + "=" * 75)
        print(f"STARTING MULTIVERSE ANIMATION PIPELINE FOR: {ch_key}")
        print("=" * 75)
        video_path, script_data = produce_v16_animated_episode(ch_key, cfg, output_root)
        if os.environ.get("DRY_RUN", "0") != "1":
            upload_to_youtube(video_path, script_data, cfg)

if __name__ == "__main__":
    main()
