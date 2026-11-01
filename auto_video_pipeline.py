#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMPIRE AUTO-VIDEO PIPELINE v16.0 (PROPRIETARY ANIMATED UNIVERSE EDITION)
Automated Viral Dual-Character Animated Drama for YouTube Shorts:
- 100% Original Intellectual Property (Lord Sterling the Raven & Felix the Fox)
- Two-Character Conversational Drama (Mentor vs Consumer)
- 9-Scene Master Dramatic Arc (Hook -> Confrontation -> Flashback -> Epiphany -> Outro)
- Multi-Voice Audio Synthesis (Deep Baritone Mentor vs Expressive Consumer)
- Procedural Foley Sound Effects (Cash register, heartbeat, whoosh, sub-bass drop, scratch)
- High-Definition Animated Character Stills (Savile Row pinstripe suit, vintage cafe)
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
# 1. VOICE & CHARACTER PROFILES (THE DUAL-CHARACTER VOCAL DRAMA)
# ==============================================================================

VOICE_PROFILES = {
    "ar": {
        "mentor": {
            "name": "Lord Sterling (شاهين / الغراب الحكيم)",
            "voice": "ar-EG-ShakirNeural",
            "rate": "+0%",
        },
        "consumer": {
            "name": "Felix the Fox (فيلكس الثعلب المكافح)",
            "voice": "ar-SA-HamedNeural",
            "rate": "+4%",
        }
    },
    "en": {
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
    }
}

CHANNELS = {
    "ch02_ar_ai_tech": {
        "id": "ch02_ar_ai_tech",
        "name": "الذكاء الاصطناعي وتقنيات المستقبل",
        "niche": "AI Matrix & Future Tech Secrets",
        "lang": "ar",
        "secret_env": "YT_TOKEN_CH02_AR",
        "category_id": "28",  # Science & Technology
        "outro_line": "الضوضاء للمستهلكين... راقب، تعلم، وتطور في صمت. حتى تصبح أنت سيد اللعبة.",
        "tags": ["الذكاء_الاصطناعي", "تكنولوجيا", "أسرار_النفوذ", "كرتون", "قصص_واقعية", "Shorts", "AI"],
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
# 2. MASTER V16 EPISODE BANKS (9-SCENE DUAL-CHARACTER DRAMATIC ARCS)
# ==============================================================================

EPISODE_BANK_AR = [
    {
        "series_title": "أسرار النفوذ والمال",
        "part": "الجزء 1",
        "title": "الجزء 1 | فخ استراحة القهوة: كيف برمجوك لتدفع ثمن تعبك؟ #Shorts",
        "scenes": [
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "ثماني ساعات عمل متواصلة... القهوة دي هي المكافأة الوحيدة اللي بتخليني أكمل يومي.",
                "caption": "ثماني ساعات عمل... والقهوة مكافأتي الوحيدة!",
                "sfx_cue": None,
                "visual_prompt": "An anthropomorphic young red fox named Felix wearing a brown corduroy vest and newsboy cap, taking a satisfied sip from a steaming coffee mug at a vintage cafe counter, 1930s neo-noir animation style, 9:16 vertical",
                "visual_style": "cafe_consumer"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "مكافأة؟ تفتكر مين اللي أقنعك إنك محتاج 'استراحة قهوة' علشان تشتغل أكتر؟",
                "caption": "مين اللي اخترع فكرة 'استراحة القهوة'؟",
                "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Lord Sterling the anthropomorphic raven in an immaculate charcoal pinstripe suit and burgundy tie, checking a gold pocket watch with a cynical smirk, dark oak study library background, 9:16 vertical",
                "visual_style": "mentor_study"
            },
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "يعني إيه؟ دي استراحة قانونية من حقي... إيه دخل الاختراع هنا؟",
                "caption": "دي استراحة قانونية... إيه دخل الاختراع؟",
                "sfx_cue": "sfx_scratch",
                "visual_prompt": "Felix the fox lowering his coffee cup in shock, wide bewildered eyes, dropped jaw, cartoon disbelief expression at the cafe counter, 9:16 vertical",
                "visual_style": "cafe_shock"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "في عام 1952، مبيعات البن انهارت بعد الحرب. فاجتمع كبار المسوقين في نيويورك بحملة أطلقت كلمة واحدة: كوفي بريك.",
                "caption": "1952: اختراع مصطلح 'Coffee Break' لإنقاذ المبيعات!",
                "sfx_cue": None,
                "visual_prompt": "1952 Madison Avenue vintage boardroom, smoky air, advertising executives in tailored coats pointing at billboard sketches of steaming coffee cups, archival film grain, 9:16 vertical",
                "visual_style": "madison_boardroom"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "أقنعوا المصانع إن إعطاء العامل 15 دقيقة لشرب الكافيين يرفع الإنتاجية عشرين بالمئة. الاستراحة لم تكن لراحتك؛ كانت لمضاعفة إنتاج الآلة.",
                "caption": "الاستراحة لم تكن لراحتك... بل لمضاعفة إنتاج الآلة!",
                "sfx_cue": None,
                "visual_prompt": "1950s industrial factory floor, massive heavy steel gears, assembly line workers drinking coffee while factory managers smile at speedometers, moody steam, 9:16 vertical",
                "visual_style": "factory_production"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "ثم حولوها من وقود للمصانع إلى رمز للمكانة الاجتماعية. كوب يكلفهم ثلاثين سنتاً، يبيعونه لك بثمانية دولارات.",
                "caption": "تكلفة 30 سنتاً... يُباع لك بـ 8 دولارات!",
                "sfx_cue": "sfx_register",
                "visual_prompt": "Sleek modern luxury cafe counter, glowing neon chalkboard menu showing overpriced coffee, gold coins spilling over cash register counter, 9:16 vertical",
                "visual_style": "luxury_cafe_pricing"
            },
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "يعني أنا بدفع فلوسي علشان أشتري طاقة أصرفها في شغل مش ملكي؟",
                "caption": "بدفع ثمن طاقة أستهلكها في شغل مش ملكي؟",
                "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Close-up of Felix the fox staring down at his coffee mug in dread, realization dawning on his face, dark moody lighting, 9:16 vertical",
                "visual_style": "consumer_epiphany"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "المستهلك يدفع ثمن استراحته مرتين: من صحته ومن محفظته. الأذكياء لا يشربون القهوة للهروب من واقعهم؛ بل يبنون الأنظمة التي تستفيد من جهد الملايين.",
                "caption": "الأذكياء لا يهربون من واقعهم... بل يبنون الأنظمة!",
                "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Dramatic close-up of Lord Sterling adjusting his cufflinks, glowing amber eyes piercing the shadows, atmospheric library background, 9:16 vertical",
                "visual_style": "mentor_axiom"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "الضوضاء للمستهلكين... راقب، تعلم، وتطور في صمت. حتى تصبح أنت سيد اللعبة. اشترك لمتابعة الجزء القادم.",
                "caption": "تطور في صمت... حتى تصبح أنت سيد اللعبة!",
                "sfx_cue": None,
                "visual_prompt": "Lord Sterling turning toward a large mahogany door, silhouette against warm library chandelier, mysterious stoic departure, 9:16 vertical",
                "visual_style": "mentor_outro"
            }
        ]
    },
    {
        "series_title": "أسرار النفوذ والذكاء الاصطناعي",
        "part": "الجزء 2",
        "title": "الجزء 2 | فخ كورسات الذكاء الاصطناعي: كيف تصنع ثروة حقيقية بالوكلاء المستقلين؟ #Shorts",
        "scenes": [
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "اشتريت كورس الذكاء الاصطناعي ده بألف دولار... الأسبوع الجاي هبدأ أحقق أول عشرة آلاف!",
                "caption": "اشتريت كورس بـ 1000 دولار... والأسبوع الجاي هبقى مليونير!",
                "sfx_cue": None,
                "visual_prompt": "Felix the fox proudly holding his glowing smartphone showing a $997 course checkout screen, excited hopeful expression, newsboy cap, cafe background, 9:16 vertical",
                "visual_style": "course_buyer"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "ألف دولار؟ في حمى الذهب، لم يغتني المنقبون؛ بل اغتنى من باعهم المجارف.",
                "caption": "في حمى الذهب... لم يغتني إلا من باع المجارف!",
                "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Lord Sterling the raven in his dark pinstripe suit, leaning back in his leather chair with a knowing smirk, holding an antique gold coin, 9:16 vertical",
                "visual_style": "mentor_gold_axiom"
            },
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "مجارف إيه؟ الكورس فيه كل الأسرار... إزاي أكتب برومبت للروبوت يجاوبني بسرعة!",
                "caption": "الكورس فيه أسرار كتابة البرومبت!",
                "sfx_cue": "sfx_scratch",
                "visual_prompt": "Felix the fox looking defensive and confused, tapping his phone screen frantically, wide cartoon eyes, cafe counter, 9:16 vertical",
                "visual_style": "consumer_defensive"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "الدردشة مع الروبوتات مضيعة لوقت الهواة. الشركات المليارية لا تكتب برومبت؛ بل تبني شبكات من الوكلاء المستقلين الذين يبرمجون وينشرون الأنظمة بأنفسهم.",
                "caption": "الشركات المليارية لا تكتب برومبت... بل تبني وكلاء مستقلين!",
                "sfx_cue": None,
                "visual_prompt": "Futuristic high-tech data center, three holographic autonomous androids interconnected by glowing fiber optics, compiling code autonomously, 9:16 vertical",
                "visual_style": "autonomous_agents"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "وكيل يخطط، وكيل يبرمج، ووكيل يختبر ويصلح الأخطاء في ثوانٍ معدودة. مبرمج واحد يقود جيشاً كاملاً دون أن يدفع رواتب.",
                "caption": "3 وكلاء ذكاء اصطناعي = جيش مبرمجين بدون رواتب!",
                "sfx_cue": None,
                "visual_prompt": "Lone cybernetic figure in a dark penthouse skyscraper commanding glowing screens of automated code compilation and server diagnostics, 9:16 vertical",
                "visual_style": "lone_architect"
            },
            {
                "speaker": "mentor",
                "character_focus": "flashback",
                "narration": "بينما أنت تدفع لصاحب الكورس ثمن تذاكر أوهامه، هو يربح الملايين من بيع الوهم، وليس من التكنولوجيا ذاتها.",
                "caption": "هو يربح الملايين من بيع الوهم... وليس التكنولوجيا!",
                "sfx_cue": "sfx_register",
                "visual_prompt": "Luxury penthouse desk stacked with credit card payment notifications and online course subscriber counts, gold sparkles, 9:16 vertical",
                "visual_style": "course_seller_wealth"
            },
            {
                "speaker": "consumer",
                "character_focus": "consumer",
                "narration": "يعني القوة مش في معرفة الأداة... القوة في امتلاك النظام التلقائي؟",
                "caption": "القوة ليست في الأداة... بل في امتلاك النظام التلقائي؟",
                "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Felix the fox staring at his hands in awe, dropping the phone on the desk, eyes wide open in realization, 9:16 vertical",
                "visual_style": "consumer_epiphany"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "العامة يتعلمون كيف يسألون الذكاء الاصطناعي. النخب تجعل الذكاء الاصطناعي يعمل نيابة عنهم في صمت تام.",
                "caption": "العامة يسألون الذكاء... والنخب تجعله يعمل نيابة عنهم!",
                "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Lord Sterling the raven closing a heavy leather-bound ledger, gold watch chain gleaming, powerful confident gaze, 9:16 vertical",
                "visual_style": "mentor_axiom"
            },
            {
                "speaker": "mentor",
                "character_focus": "mentor",
                "narration": "الضوضاء للمستهلكين... راقب، تعلم، وتطور في صمت. حتى تصبح أنت سيد اللعبة. اشترك لمتابعة الجزء القادم.",
                "caption": "تطور في صمت... حتى تصبح أنت سيد اللعبة!",
                "sfx_cue": None,
                "visual_prompt": "Lord Sterling walking toward glowing tall arched windows overlooking a dark city skyline, neo-noir atmosphere, 9:16 vertical",
                "visual_style": "mentor_outro"
            }
        ]
    }
]

EPISODE_BANK_EN = [
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

# ==============================================================================
# 3. TEXT SHAPING & KINETIC TYPOGRAPHY ENGINE (FLAWLESS ARABIC BOLD GUARANTEED)
# ==============================================================================

def shape_text(text: str, lang: str = "ar") -> str:
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


def get_font(size: int = 52, lang: str = "ar", bold: bool = True) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
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
        # Default subtle tap
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
    text: str,
    speaker: str,
    lang: str,
    sfx_cue: str | None,
    out_mp3: Path,
    work_dir: Path
) -> float:
    """Synthesizes crystal-clear dual-character voice acting (Lord Sterling vs Felix) with Foley SFX."""
    profile = VOICE_PROFILES.get(lang, VOICE_PROFILES["ar"]).get(speaker, VOICE_PROFILES["ar"]["mentor"])
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
# 5. VISUAL GENERATION & CHARACTER ASSET PIPELINE
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
    character_focus: str,
    style_hint: str,
    visual_prompt: str,
    scene_idx: int,
    out_jpg: Path
) -> Path:
    """Resolves character and scene visuals with guaranteed variety and character continuity."""
    repo_root = Path(__file__).resolve().parent
    chars_dir = repo_root / "assets" / "characters"
    scenes_dir = repo_root / "assets" / "scenes"

    # 1. Direct scene-specific asset mapping
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

    # 2. Character-specific shots & expressions
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

    # 3. Flashbacks: Dedicated scene artwork (never fallback to fox!)
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

        for s_file in scenes_dir.glob("*.jpg"):
            if s_file.exists():
                return s_file

        # Fallback to procedural neo-noir backdrop
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
) -> tuple[np.ndarray, np.ndarray]:
    """Renders crisp, centered, elegant subtitles in frosted dark container with gold accents."""
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

    rgba = np.array(overlay)
    rgb = rgba[:, :, :3].astype(np.float32)
    alpha = (rgba[:, :, 3:4].astype(np.float32)) / 255.0
    return rgb, alpha


# ==============================================================================
# 7. HIGH-PERFORMANCE DIRECT-STREAMING RENDERER (O(1) CONSTANT RAM)
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
    """Streams animated Ken-Burns frames directly into FFmpeg stdin pipe with alternating camera dynamics."""
    n_frames = max(15, int(round(duration * fps)))
    over_w, over_h = int(target_w * 1.25), int(target_h * 1.25)

    base_im = None
    if visual_path.exists() and visual_path.stat().st_size > 10_000:
        try:
            base_im = Image.open(visual_path).convert("RGB")
        except Exception:
            base_im = None

    if base_im is None:
        base_im = Image.new("RGB", (over_w, over_h), (14, 18, 26))

    base_im = base_im.resize((over_w, over_h), Image.Resampling.LANCZOS)
    c_rgb, c_alpha = render_cinematic_caption_overlay(caption, lang, target_w=target_w, target_h=target_h)

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-pix_fmt", "rgb24",
        "-s", f"{target_w}x{target_h}",
        "-r", str(fps),
        "-i", "-",
        "-i", str(scene_mp3),
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
            # Alternating camera kinematics per scene
            if scene_idx % 2 == 0:
                scale = 1.0 + 0.12 * t
                drift_x = int(math.sin(t * math.pi) * 25)
            else:
                scale = 1.15 - 0.10 * t
                drift_x = int(-math.sin(t * math.pi) * 25)

            crop_w = int(target_w / scale)
            crop_h = int(target_h / scale)

            x0 = max(0, min(over_w - crop_w, (over_w - crop_w) // 2 + drift_x))
            y0 = max(0, min(over_h - crop_h, (over_h - crop_h) // 2))

            crop = base_im.crop((x0, y0, x0 + crop_w, y0 + crop_h)).resize((target_w, target_h), Image.Resampling.BILINEAR)
            arr = np.array(crop, dtype=np.float32)

            grain = np.random.normal(0, 2.5, arr.shape).astype(np.float32)
            arr = np.clip(arr + grain, 0, 255)

            comp = (arr * (1.0 - c_alpha) + c_rgb * c_alpha).astype(np.uint8)
            proc.stdin.write(comp.tobytes())

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
# 8. MASTER V16 EPISODE PRODUCER
# ==============================================================================

def produce_v16_animated_episode(channel_key: str, cfg: dict, output_root: Path) -> tuple[Path, dict]:
    W, H, FPS = 1080, 1920, 30
    lang = cfg["lang"]
    work_dir = output_root / f"work_{channel_key}"
    work_dir.mkdir(parents=True, exist_ok=True)

    # 1. Select Episode Script
    run_num = int(os.environ.get("GITHUB_RUN_NUMBER", "1") or 1)
    bank = EPISODE_BANK_AR if lang == "ar" else EPISODE_BANK_EN
    script_data = bank[run_num % len(bank)]
    title = script_data["title"]
    scenes = script_data["scenes"]

    print(f"\n[{channel_key}] Producing V16 Animated Drama: '{title}' ({len(scenes)} scenes)")

    final_mp4 = output_root / f"{channel_key}_latest.mp4"
    scene_video_paths = []

    # 2. Render each scene
    for s_idx, scene in enumerate(scenes):
        speaker = scene.get("speaker", "mentor")
        sfx_cue = scene.get("sfx_cue")
        print(f"  --- Scene {s_idx + 1}/{len(scenes)} [{speaker.upper()}]: {scene['caption'][:35]}... (SFX: {sfx_cue}) ---")

        scene_mp3 = work_dir / f"scene_{s_idx}.mp3"
        scene_mp4 = work_dir / f"scene_{s_idx}.mp4"
        scene_visual = work_dir / f"visual_{s_idx}.jpg"

        # A. Multi-Character Voice Synthesis with Foley SFX
        duration = synthesize_dual_voice_scene(
            text=scene["narration"],
            speaker=speaker,
            lang=lang,
            sfx_cue=sfx_cue,
            out_mp3=scene_mp3,
            work_dir=work_dir
        )

        # B. Resolve Character Asset (Lord Sterling / Felix the Fox / Flashback)
        visual_path = resolve_character_visual(
            character_focus=scene.get("character_focus", "mentor"),
            style_hint=scene.get("visual_style", "dark"),
            visual_prompt=scene.get("visual_prompt", ""),
            scene_idx=s_idx,
            out_jpg=scene_visual
        )

        # C. Render animated scene directly to FFmpeg pipe
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

    print(f"[{channel_key}] SUCCESS! Exported V16 Master Short: {final_mp4} ({final_mp4.stat().st_size // (1024*1024)} MB, {total_duration:.1f}s)")
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
    print(f"  [YouTube Upload] Publishing V16 Short for: {cfg['name']} ({secret_env})")
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
        except Exception as ref_err:
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
        desc = f"{title}\n\n{cfg['outro_line']}\n\n#Shorts #LordSterling #Animation #Mindset #Billionaire #Power"

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
        print(f"STARTING V16.0 PROPRIETARY ANIMATION ENGINE FOR: {ch_key}")
        print("=" * 75)
        video_path, script_data = produce_v16_animated_episode(ch_key, cfg, output_root)
        if os.environ.get("DRY_RUN", "0") != "1":
            upload_to_youtube(video_path, script_data, cfg)

if __name__ == "__main__":
    main()
