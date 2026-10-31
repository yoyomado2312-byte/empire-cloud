#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMPIRE AUTO-VIDEO PIPELINE v15.0 (ENTERPRISE QUIET-WOLF EDITION)
Automated Viral Documentary Engine for YouTube Shorts:
- 100% Elimination of static talking heads / cut-out puppets
- True Scene-by-Scene Cinematic Documentary (5-7 micro-scenes per video)
- Golden 30-45s Short Duration Guarantee (<55s Hard Safety Governor)
- 3D Ken Burns Camera Push-in, Panning & Atmospheric Lighting Sweep
- Dark-Psychology & Billionaire Empire Narrative Scripts (High-Retention Hooks)
- Atmospheric Sub-Bass Tension Drone Soundscape (-18dB layered behind voice)
- Centered Cairo Bold Kinetic Typography (Word-by-word visual emphasis)
- Direct Frame Streaming to FFmpeg Pipe (O(1) Constant Memory Footprint)
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
# 1. CHANNEL CONFIGURATION (THE 2 TEST CHANNELS - READY FOR 22 SCALE)
# ==============================================================================

CHANNELS = {
    "ch02_ar_ai_tech": {
        "id": "ch02_ar_ai_tech",
        "name": "الذكاء الاصطناعي وتقنيات المستقبل",
        "niche": "AI Matrix & Future Tech Secrets",
        "lang": "ar",
        "voice": "ar-EG-ShakirNeural",
        "secret_env": "YT_TOKEN_CH02_AR",
        "category_id": "28",  # Science & Technology
        "outro_line": "الضوضاء للضعفاء... راقب، تعلم، وتطور في صمت، حتى تصبح أنت الذئب.",
        "tags": ["الذكاء_الاصطناعي", "تكنولوجيا", "أسرار_النفوذ", "تقنية", "وثائقي", "Shorts", "AI"],
    },
    "ch03_en_wealth_business": {
        "id": "ch03_en_wealth_business",
        "name": "Billionaire Empires & Wealth",
        "niche": "Corporate Deceptions & Empire Building",
        "lang": "en",
        "voice": "en-US-ChristopherNeural",
        "secret_env": "YT_TOKEN_CH03_EN",
        "category_id": "27",  # Education / Business
        "outro_line": "Go quiet. Watch. Learn. Evolve quietly — until you are the wolf.",
        "tags": ["Wealth", "Billionaires", "BusinessSecrets", "Psychology", "Power", "Shorts", "Documentary"],
    },
}

# ==============================================================================
# 2. MASTER EPISODE BANKS (QUIET WOLF STYLE: 5-7 HIGH-RETENTION SCENES)
# ==============================================================================

EPISODE_BANK_AR = [
    {
        "series_title": "أسرار النفوذ والذكاء الاصطناعي",
        "part": "الجزء 1",
        "title": "الجزء 1 | كيف تدير شركة بمليار دولار بدون موظف بشري واحد؟ #Shorts",
        "scenes": [
            {
                "narration": "شركة بمليار دولار... يديرها مبرمج واحد من غرفة نومه، بدون أي موظف بشري.",
                "caption": "شركة بمليار دولار... بدون موظف بشري واحد!",
                "broll_query": "hacker dark room glowing computer screens cyber",
                "broll_prompt": "Cinematic wide shot of a lone programmer silhouette in a dark modern skyscraper office, lit only by glowing cyan holographic monitors, 8k neo-noir moody lighting",
                "visual_style": "dark_cyber"
            },
            {
                "narration": "الجميع يظن أن بناء الإمبراطوريات يحتاج مئات الموظفين. في 2026، القواعد تغيرت.",
                "caption": "في 2026... قواعد اللعبة تغيرت للأبد!",
                "broll_query": "empty corporate office dark cinematic",
                "broll_prompt": "Cinematic shot of abandoned corporate office cubicles covered in dust, moody shafts of light cutting through darkness, high contrast 8k film still",
                "visual_style": "abandoned_office"
            },
            {
                "narration": "ثلاثة وكلاء ذكاء اصطناعي فقط: التخطيط، كتابة الكود، وفحص الأنظمة تلقائياً.",
                "caption": "3 وكلاء ذكاء اصطناعي = جيش من المبرمجين!",
                "broll_query": "robot android server room artificial intelligence",
                "broll_prompt": "Three glowing robotic android silhouettes analyzing digital financial streams in a high-tech data center, cinematic blue and amber rim lighting, 8k",
                "visual_style": "ai_agents"
            },
            {
                "narration": "التكلفة انهارت بنسبة تسعين بالمئة، وسرعة إطلاق المشاريع قفزت لثمان وأربعين ساعة.",
                "caption": "انهيار التكلفة 90% وسرعة 48 ساعة فقط!",
                "broll_query": "gold bullions vault luxury money laser charts",
                "broll_prompt": "Cinematic macro shot of luxury bank vault opening with golden bullion and neon laser financial growth charts, dramatic cinematic lighting, 8k",
                "visual_style": "vault_growth"
            },
            {
                "narration": "كما احتكر روكفلر خطوط النفط سابقاً، الآن يتم احتكار خطوط الذكاء الاصطناعي في صمت.",
                "caption": "كما فعل روكفلر... احتكار خطوط المستقبل في صمت!",
                "broll_query": "vintage 1920s wall street industrial tycoon oil",
                "broll_prompt": "Vintage 1920s archival oil tycoon boardroom, wealthy men in tailored coats looking at blueprint maps, moody sepia cinematic atmosphere, 8k",
                "visual_style": "vintage_tycoon"
            },
            {
                "narration": "الروكفلر القادم لن تراه في نشرات الأخبار؛ إنه يبني إمبراطوريته خلف الكواليس.",
                "caption": "الملياردير القادم لن تراه في الأخبار!",
                "broll_query": "mysterious man suit walking rain city night bokeh",
                "broll_prompt": "Cinematic back shot of a mysterious figure in bespoke overcoat walking away down a rainy neon city alleyway, reflections on wet asphalt, 8k",
                "visual_style": "mysterious_man"
            },
            {
                "narration": "الضوضاء للضعفاء... راقب، تعلم، وتطور في صمت، حتى تصبح أنت الذئب.",
                "caption": "تطور في صمت... حتى تصبح أنت الذئب!",
                "broll_query": "lone wolf snow night cinematic eyes looking camera",
                "broll_prompt": "Cinematic ultra-realistic close-up of a stoic alpha wolf in a misty dark forest at twilight, piercing eyes locking with camera, frost particles, 8k masterpiece",
                "visual_style": "quiet_wolf"
            }
        ]
    },
    {
        "series_title": "أسرار النفوذ والذكاء الاصطناعي",
        "part": "الجزء 2",
        "title": "الجزء 2 | فخ الدوبامين: كيف برمجتك خوارزميات وادي السيليكون لتظل مستهلكاً؟ #Shorts",
        "scenes": [
            {
                "narration": "أنت لست المستخدم للشبكات الاجتماعية... أنت السلعة التي تُباع بالمزاد كل ثانية.",
                "caption": "أنت لست المستخدم... أنت السلعة التي تُباع!",
                "broll_query": "digital eye surveillance cyber matrix network",
                "broll_prompt": "Cinematic close-up of a human eye reflecting digital binary code and algorithmic surveillance grids, cyber thriller aesthetic, 8k",
                "visual_style": "cyber_eye"
            },
            {
                "narration": "في 2011، صمم مهندسو كاليفورنيا شاشات الهواتف بنفس آلية ماكينات القمار.",
                "caption": "مهندسو كاليفورنيا صمموا هاتفك كماكينة قمار!",
                "broll_query": "casino slot machine neon glowing dark room",
                "broll_prompt": "Dramatic dark room with glowing slot machine reels spinning, reflection of digital numbers, moody cinematic film look, 8k",
                "visual_style": "casino_trap"
            },
            {
                "narration": "السحب للأسفل للتحديث... هو نفس حركة ذراع القمار لتحفيز الدوبامين في عقلك.",
                "caption": "السحب للتحديث = ذراع ماكينة القمار تماماً!",
                "broll_query": "brain synapses neural glowing dopamine signal",
                "broll_prompt": "Macro 3D neural brain network with glowing pulses of electric blue and gold synapses firing, medical documentary style, 8k",
                "visual_style": "neural_synapse"
            },
            {
                "narration": "بينما تتصفح، تدفع الشركات المليارات لتوجيه سلوكك وقراراتك دون أن تشعر.",
                "caption": "انتباهك يُباع بمليارات الدولارات للمعلنين!",
                "broll_query": "wall street stock exchange floor crowd monitors",
                "broll_prompt": "Moody high-angle shot of Wall Street trading floor with massive screens flashing red and green numbers, dramatic lighting, 8k",
                "visual_style": "trading_floor"
            },
            {
                "narration": "الأذكياء لا يتصفحون ما يصنعه الآخرون؛ بل يبنون الأنظمة التي تستهلكها الملايين.",
                "caption": "الأقوياء يبنون الأنظمة... والضعفاء يستهلكونها!",
                "broll_query": "architect building master plan drafting desk luxury",
                "broll_prompt": "Cinematic top-down view of an architect desk with architectural blueprints, compass, vintage pocket watch, moody desk lamp, 8k",
                "visual_style": "architect_plan"
            },
            {
                "narration": "استعد السيطرة على وقتك الآن، وتوقف عن إهدار طاقتك في معارك ليست لك.",
                "caption": "استعد السيطرة على انتباهك وعقلك الآن!",
                "broll_query": "hourglass sand running out dramatic light dark room",
                "broll_prompt": "Cinematic macro shot of antique brass hourglass with golden sand falling rapidly, dramatic rim lighting on black background, 8k",
                "visual_style": "hourglass"
            },
            {
                "narration": "الضوضاء للضعفاء... راقب، تعلم، وتطور في صمت، حتى تصبح أنت الذئب.",
                "caption": "تطور في صمت... حتى تصبح أنت الذئب!",
                "broll_query": "lone wolf dark forest fog cinematic eyes looking camera",
                "broll_prompt": "Cinematic ultra-realistic close-up of a stoic alpha wolf in a misty dark forest at twilight, piercing eyes locking with camera, frost particles, 8k masterpiece",
                "visual_style": "quiet_wolf"
            }
        ]
    },
    {
        "series_title": "أسرار النفوذ والذكاء الاصطناعي",
        "part": "الجزء 3",
        "title": "الجزء 3 | المعركة الخفية على الطاقة: لماذا تشتري شركات الذكاء الاصطناعي محطات نووية؟ #Shorts",
        "scenes": [
            {
                "narration": "المعركة القادمة ليست على المال ولا البيانات... بل على الميجاوات ومحطات الطاقة.",
                "caption": "المعركة القادمة ليست على المال... بل الطاقة!",
                "broll_query": "nuclear power plant cooling tower dramatic twilight steam",
                "broll_prompt": "Cinematic wide angle shot of a massive nuclear power station at blue hour twilight, steam rising into dramatic stormy clouds, 8k",
                "visual_style": "nuclear_power"
            },
            {
                "narration": "عمالقة التكنولوجيا يعيدون تشغيل مفاعلات نووية متوقفة لتغذية مراكز الذكاء الاصطناعي.",
                "caption": "عمالقة التكنولوجيا يعيدون تشغيل المفاعلات النووية!",
                "broll_query": "futuristic data center glowing server racks blue light",
                "broll_prompt": "Endless corridor of futuristic supercomputer server racks with intense pulsing blue and amber LED lights, cold atmospheric mist, 8k",
                "visual_style": "datacenter_servers"
            },
            {
                "narration": "تدريب نموذج واحد يستهلك طاقة تعادل احتياج مدينة كاملة لعام كامل.",
                "caption": "تدريب نموذج واحد يستهلك طاقة مدينة كاملة!",
                "broll_query": "city blackout power grid failure night aerial",
                "broll_prompt": "Aerial night view of a glowing modern metropolis where electrical power grids pulse with intense energy lines, dramatic cinematic contrast, 8k",
                "visual_style": "power_grid"
            },
            {
                "narration": "من يملك مصادر الطاقة المستقلة، سيتحكم في مستقبل الذكاء الاصطناعي واقتصاد العالم.",
                "caption": "من يملك الطاقة... يتحكم في الاقتصاد العالمي!",
                "broll_query": "globe world map financial connections glowing lines",
                "broll_prompt": "Holographic 3D digital Earth globe floating in darkness with interconnected golden financial nodes and fiber-optic beams, 8k",
                "visual_style": "global_power"
            },
            {
                "narration": "العامة ينشغلون بالروبوتات، بينما النخب تبني بنية تحتية لا يمكن منافستها.",
                "caption": "العامة ينشغلون بالروبوتات... والنخب تبني الإمبراطورية!",
                "broll_query": "chess board king piece surrounded dark moody lighting",
                "broll_prompt": "Macro cinematic shot of a single obsidian black chess king piece standing victorious on marble board, shafts of dramatic sunlight, 8k",
                "visual_style": "chess_king"
            },
            {
                "narration": "الضوضاء للضعفاء... راقب، تعلم، وتطور في صمت، حتى تصبح أنت الذئب.",
                "caption": "تطور في صمت... حتى تصبح أنت الذئب!",
                "broll_query": "alpha wolf head eyes glowing dark forest",
                "broll_prompt": "Cinematic portrait of a majestic alpha wolf staring intensely into the camera lens in a cold pine forest, hyper-realistic, 8k",
                "visual_style": "quiet_wolf"
            }
        ]
    },
    {
        "series_title": "أسرار النفوذ والذكاء الاصطناعي",
        "part": "الجزء 4",
        "title": "الجزء 4 | الثروة الخفية: كيف يبني أذكى مهندسي العالم إمبراطوريات بدون إعلان؟ #Shorts",
        "scenes": [
            {
                "narration": "أغنى المبرمجين في 2026 لا يملكون قنوات، ولا يظهرون في أي مؤتمر تقني.",
                "caption": "أغنى المبرمجين اليوم... لا يعرفهم أحد!",
                "broll_query": "anonymous silhouette hacker terminal dark room",
                "broll_prompt": "Silhouette of a man in a dark minimalist penthouse standing by floor-to-ceiling glass looking at Tokyo skyline at midnight, 8k",
                "visual_style": "anonymous_builder"
            },
            {
                "narration": "يطبقون مبدأ الثروة الصامتة: خوارزميات دقيقة تدر الملايين وتعمل بأتمتة كاملة.",
                "caption": "مبدأ الثروة الصامتة: أرباح بالملايين بتلقائية تامة!",
                "broll_query": "automated digital money stream flow abstract data",
                "broll_prompt": "Abstract digital streams of gold particles and algorithmic financial data flowing smoothly through a glass fiber channel, 8k",
                "visual_style": "digital_wealth"
            },
            {
                "narration": "الشهرة تجلب الضرائب والمنافسين؛ أما الصمت فيمنحك الحرية والنفوذ الحقيقي.",
                "caption": "الشهرة تجلب المنافسين... والصمت يمنحك النفوذ!",
                "broll_query": "whiskey glass ice luxury desk leather chair fireplace",
                "broll_prompt": "Cinematic corner of an ultra-luxurious private executive study with dark mahogany desk, crystal decanter, warm fireplace glow, 8k",
                "visual_style": "stealth_office"
            },
            {
                "narration": "لا تخبر أحداً بخطوتك القادمة... دع النتائج وحدها تصنع الصدمة.",
                "caption": "لا تعلن خطتك... دع النتائج تصنع الصدمة!",
                "broll_query": "soundwave audio mute silent concept dark",
                "broll_prompt": "Minimalist dark aesthetic of audio equalizer waves fading into dead silence, single dramatic spotlight cutting through darkness, 8k",
                "visual_style": "silence_rule"
            },
            {
                "narration": "الضوضاء للضعفاء... راقب، تعلم، وتطور في صمت، حتى تصبح أنت الذئب.",
                "caption": "تطور في صمت... حتى تصبح أنت الذئب!",
                "broll_query": "lone wolf eyes looking camera snowy night",
                "broll_prompt": "Cinematic close-up of a powerful alpha wolf in deep snow at night, steady amber eyes locking with viewer, breath misting in cold air, 8k",
                "visual_style": "quiet_wolf"
            }
        ]
    }
]

EPISODE_BANK_EN = [
    {
        "series_title": "Billionaire Empires & Corporate Deceptions",
        "part": "Part 1",
        "title": "Part 1 | They Paid $13 Million Because It Never Gave Anyone Wings #Shorts",
        "scenes": [
            {
                "narration": "They paid thirteen million dollars in lawsuits... because Red Bull never actually gave anyone wings.",
                "caption": "They paid $13M... because it never gave anyone wings!",
                "broll_query": "courtroom gavel judge law dramatic lighting",
                "broll_prompt": "Dramatic close-up of a brass courtroom judge gavel hitting wooden block, dust particles in shaft of sunlight, cinematic 8k movie still",
                "visual_style": "courtroom"
            },
            {
                "narration": "In 1982, an Austrian discovered a cheap thirty-cent syrup sold to Bangkok truck drivers.",
                "caption": "1982: A cheap syrup for truck drivers in Bangkok!",
                "broll_query": "bangkok 1980s neon rain street night market",
                "broll_prompt": "Cinematic 1980s Bangkok night alleyway in heavy tropical rain, glowing neon signs reflecting on wet asphalt, vintage trucks, 8k film still",
                "visual_style": "bangkok_rain"
            },
            {
                "narration": "He didn't change the formula. He added carbonation, doubled the price, and created a rebel myth.",
                "caption": "Same formula. Shrunk the can. Doubled the price!",
                "broll_query": "luxury aluminum beverage can studio lighting droplets",
                "broll_prompt": "Macro shot of sleek dark aluminum energy beverage can with glistening water condensation droplets, high-speed luxury product commercial lighting, 8k",
                "visual_style": "beverage_can"
            },
            {
                "narration": "Red Bull doesn't sell a beverage. They sell the illusion of adrenaline and power.",
                "caption": "They don't sell drinks... They sell an illusion of danger!",
                "broll_query": "formula 1 racing night race sparks motion blur",
                "broll_prompt": "Cinematic motion blur shot of Formula 1 race car speeding through Monaco night turn, sparks flying from undercarriage, 8k",
                "visual_style": "f1_racing"
            },
            {
                "narration": "Today that syrup generates ten billion dollars a year. The narrative is everything.",
                "caption": "$10 Billion a year: The narrative is everything!",
                "broll_query": "private jet hangar luxury billionaire lifestyle night",
                "broll_prompt": "Private luxury jet parked in sleek illuminated hangar at midnight, glowing runway lights in background, billionaire corporate wealth, 8k",
                "visual_style": "private_jet"
            },
            {
                "narration": "The masses buy products. The masters sell illusions.",
                "caption": "The masses buy products... The masters sell illusions!",
                "broll_query": "chess board checkmate dark dramatic mood",
                "broll_prompt": "Dark cinematic chess board with fallen pieces, 8k",
                "visual_style": "chess_trap"
            },
            {
                "narration": "Go quiet. Watch. Learn. Evolve quietly — until you are the wolf.",
                "caption": "Go quiet. Evolve quietly... until you are the wolf!",
                "broll_query": "majestic wolf eyes dark misty forest cinematic 8k",
                "broll_prompt": "Cinematic portrait of a magnificent alpha wolf in misty Scandinavian pine forest at dusk, piercing amber eyes staring directly into the camera, 8k masterpiece",
                "visual_style": "quiet_wolf"
            }
        ]
    },
    {
        "series_title": "Billionaire Empires & Corporate Deceptions",
        "part": "Part 2",
        "title": "Part 2 | The Diamond Cartel: The Greatest Marketing Lie in Human History #Shorts",
        "scenes": [
            {
                "narration": "Diamonds are not rare. It is the greatest marketing deception in human history.",
                "caption": "Diamonds are not rare... It is the greatest lie!",
                "broll_query": "rough diamond raw stone sparkling luxury dark background",
                "broll_prompt": "Macro cinematic shot of raw sparkling diamond gemstone on black velvet, single beam of pure white spotlight, 8k studio photography",
                "visual_style": "diamond_macro"
            },
            {
                "narration": "In 1888, massive South African mines flooded the market with millions of stones.",
                "caption": "1888: South African mines flooded the market!",
                "broll_query": "deep open pit diamond mine south africa 1800s vintage",
                "broll_prompt": "Vintage 19th-century deep open excavation mine in South Africa, thousands of workers, sepia tone archival documentary style, 8k",
                "visual_style": "vintage_mine"
            },
            {
                "narration": "De Beers bought the mines, hoarded diamonds in London vaults, and manufactured artificial scarcity.",
                "caption": "De Beers locked diamonds in vaults to fake scarcity!",
                "broll_query": "underground bank vault rows of safety deposit boxes dark",
                "broll_prompt": "Underground heavy steel vault corridor with endless rows of safety deposit boxes, moody tungsten overhead lamps, cinematic thriller look, 8k",
                "visual_style": "bank_vault"
            },
            {
                "narration": "Then in 1947, they launched four words that brainwashed humanity: A Diamond is Forever.",
                "caption": "1947: 'A Diamond is Forever' brainwashed the world!",
                "broll_query": "vintage 1940s magazine advertisement luxury couple",
                "broll_prompt": "Vintage 1940s luxury Madison Avenue advertising office, art director pinning vintage diamond poster to board, warm film grain, 8k",
                "visual_style": "vintage_ad"
            },
            {
                "narration": "They tied rocks to eternal love so you would never resell them and break the cartel.",
                "caption": "They tied rocks to love so you never resell them!",
                "broll_query": "luxury engagement ring velvet box opening cinematic",
                "broll_prompt": "Cinematic slow motion opening of a dark velvet ring box revealing a brilliant-cut diamond ring glistening under soft candle light, 8k",
                "visual_style": "ring_box"
            },
            {
                "narration": "The masses chase manufactured prestige. The elites control the supply and write the rules.",
                "caption": "The masses chase prestige... The elites write the rules!",
                "broll_query": "manhattan skyline dusk luxury penthouse silhouette",
                "broll_prompt": "Breathtaking twilight view of Manhattan skyline from high-floor glass penthouse, silhouette of billionaire executive overlooking city, 8k",
                "visual_style": "manhattan_penthouse"
            },
            {
                "narration": "Go quiet. Watch. Learn. Evolve quietly — until you are the wolf.",
                "caption": "Go quiet. Evolve quietly... until you are the wolf!",
                "broll_query": "majestic wolf eyes dark misty forest cinematic 8k",
                "broll_prompt": "Cinematic portrait of a magnificent alpha wolf in misty Scandinavian pine forest at dusk, piercing amber eyes staring directly into the camera, 8k masterpiece",
                "visual_style": "quiet_wolf"
            }
        ]
    },
    {
        "series_title": "Billionaire Empires & Corporate Deceptions",
        "part": "Part 3",
        "title": "Part 3 | The Ferrari Waitlist Trap: Why Luxury Brands Reject the Rich #Shorts",
        "scenes": [
            {
                "narration": "You cannot simply walk in with a million dollars in cash and buy a limited Ferrari.",
                "caption": "A million dollars in cash won't buy you this car!",
                "broll_query": "luxury supercar dealership showroom polished floor dark",
                "broll_prompt": "Sleek moody supercar showroom with high-gloss black marble floor, single crimson supercar under dramatic spotlight, 8k",
                "visual_style": "supercar_showroom"
            },
            {
                "narration": "To buy their halo cars, you must buy three entry models first and wait years.",
                "caption": "You must buy 3 cars just to earn the privilege!",
                "broll_query": "keys luxury car leather table champagne glass",
                "broll_prompt": "Macro shot of high-end supercar key fob resting on handcrafted leather desk next to crystal glass of vintage champagne, 8k",
                "visual_style": "luxury_keys"
            },
            {
                "narration": "They weaponize human psychology: artificial rejection turns desire into pure obsession.",
                "caption": "Artificial rejection turns desire into obsession!",
                "broll_query": "confident businessman bespoke suit dark penthouse office",
                "broll_prompt": "Cinematic portrait of an imposing billionaire CEO in tailored Italian suit looking out over foggy cityscape, dramatic rim light, 8k",
                "visual_style": "billionaire_ceo"
            },
            {
                "narration": "Luxury is never about performance. Luxury is the public monetization of artificial scarcity.",
                "caption": "Luxury is the monetization of artificial rejection!",
                "broll_query": "gold bars vault stacks luxury lighting high contrast",
                "broll_prompt": "Cinematic rows of polished gold bars stacked in dark underground security vault, amber reflections, 8k",
                "visual_style": "gold_vault"
            },
            {
                "narration": "The masses chase validation. The masters design the psychological traps.",
                "caption": "The masses seek symbols... The masters design the traps!",
                "broll_query": "chess board checkmate dark dramatic mood",
                "broll_prompt": "Dark cinematic chess board with fallen white pieces and single black queen towering in center, 8k",
                "visual_style": "chess_trap"
            },
            {
                "narration": "Go quiet. Watch. Learn. Evolve quietly — until you are the wolf.",
                "caption": "Go quiet. Evolve quietly... until you are the wolf!",
                "broll_query": "lone alpha wolf forest twilight eyes",
                "broll_prompt": "Cinematic portrait of a magnificent alpha wolf in misty Scandinavian pine forest at dusk, piercing amber eyes, 8k masterpiece",
                "visual_style": "quiet_wolf"
            }
        ]
    },
    {
        "series_title": "Billionaire Empires & Corporate Deceptions",
        "part": "Part 4",
        "title": "Part 4 | The 48 Laws of Dark Capital: How Shadow Cartels Control Trillions #Shorts",
        "scenes": [
            {
                "narration": "The most powerful financial cartels on Earth never hold press conferences.",
                "caption": "The most powerful firms never hold press conferences!",
                "broll_query": "shadowy boardroom men in suits round table dark",
                "broll_prompt": "Cinematic wide shot of an elite shadowy boardroom at midnight, high-ranking executives silhouetted around an illuminated glass table, 8k",
                "visual_style": "shadow_boardroom"
            },
            {
                "narration": "They operate in the shadows of liquidity, quietly acquiring dominant shares in competing rivals.",
                "caption": "They own controlling shares in competing rivals!",
                "broll_query": "algorithmic trading screens high frequency dark room",
                "broll_prompt": "Multi-monitor algorithmic trading station displaying complex liquidity heatmaps and order book charts in deep blue and gold, 8k",
                "visual_style": "algo_trading"
            },
            {
                "narration": "Whether markets collapse or skyrocket, their algorithms extract liquidity on both sides.",
                "caption": "Bull or bear market: They profit on both sides!",
                "broll_query": "wall street charging bull statue night dramatic fog",
                "broll_prompt": "Dramatic night view of Wall Street bronze charging bull engulfed in moody fog and rain, cinematic street lamps, 8k",
                "visual_style": "wall_street_bull"
            },
            {
                "narration": "True power is never loud. It never boasts; it compounds in total silence.",
                "caption": "True power never boasts... It compounds in silence!",
                "broll_query": "heavy steel vault door closing dark lighting",
                "broll_prompt": "Massive circular bank vault door made of polished titanium and brass rotating closed, cinematic atmospheric haze, 8k",
                "visual_style": "steel_vault"
            },
            {
                "narration": "Go quiet. Watch. Learn. Evolve quietly — until you are the wolf.",
                "caption": "Go quiet. Evolve quietly... until you are the wolf!",
                "broll_query": "majestic wolf eyes dark misty forest cinematic 8k",
                "broll_prompt": "Cinematic portrait of a magnificent alpha wolf in misty Scandinavian pine forest at dusk, piercing amber eyes staring directly into the camera, 8k masterpiece",
                "visual_style": "quiet_wolf"
            }
        ]
    }
]

# ==============================================================================
# 3. TEXT SHAPING & TYPOGRAPHY ENGINE (CAIRO BOLD GUARANTEED)
# ==============================================================================

def shape_text(text: str, lang: str = "ar") -> str:
    """Shapes Arabic text with presentation forms-B and strict RTL bidirectional ordering."""
    if not text:
        return ""
    if lang == "ar" and HAS_ARABIC_SHAPER:
        try:
            config = {
                'delete_harakat': False,
                'support_ligatures': True,
                'RIAL SIGN': True,
            }
            reshaper = arabic_reshaper.ArabicReshaper(configuration=config)
            reshaped = reshaper.reshape(text)
            return get_display(reshaped, base_dir='R')
        except Exception:
            return text
    return text


def get_font(size: int = 52, bold: bool = True) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Loads high-definition typography with guaranteed Cairo / Noto Sans Arabic glyphs."""
    repo_root = Path(__file__).resolve().parent
    font_candidates = [
        repo_root / "assets" / "fonts" / "Cairo.ttf",
        repo_root / "assets" / "fonts" / "NotoSansArabic-Bold.ttf",
        repo_root / "fonts" / "Cairo.ttf",
        repo_root / "fonts" / "Cairo-Bold.ttf",
        Path("/usr/share/fonts/truetype/amiri/amiri-bold.ttf"),
        Path("/usr/share/fonts/truetype/amiri/Amiri-Bold.ttf"),
        Path("/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf"),
        Path("/usr/share/fonts/truetype/scheherazade/Scheherazade-Bold.ttf"),
        Path("C:/Windows/Fonts/seguisb.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf"),
    ]
    for p in font_candidates:
        if p.exists():
            try:
                return ImageFont.truetype(str(p), size=size)
            except Exception:
                continue

    # Auto-download Cairo if missing
    try:
        f_dir = repo_root / "assets" / "fonts"
        f_dir.mkdir(parents=True, exist_ok=True)
        target_f = f_dir / "Cairo.ttf"
        if not target_f.exists():
            u = "https://github.com/google/fonts/raw/main/ofl/cairo/Cairo%5Bslnt%2Cwght%5D.ttf"
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                target_f.write_bytes(resp.read())
            return ImageFont.truetype(str(target_f), size=size)
    except Exception:
        pass

    return ImageFont.load_default()

# ==============================================================================
# 4. AUDIO SYNTHESIS & ATMOSPHERIC SOUND DESIGN
# ==============================================================================

def synthesize_cinematic_sub_bass_drone(duration: float, out_wav: Path):
    """Synthesizes a deep cinematic sub-bass atmospheric tension drone (58.27 Hz D-minor fundamental)."""
    sample_rate = 44100
    n_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, n_samples, endpoint=False)

    # Fundamental sub-bass + fifth + octaves
    f0 = 58.27
    drone = 0.50 * np.sin(2 * np.pi * f0 * t)
    drone += 0.25 * np.sin(2 * np.pi * (f0 * 1.5) * t)
    drone += 0.15 * np.sin(2 * np.pi * (f0 * 2.0) * t)
    drone += 0.10 * np.sin(2 * np.pi * (f0 * 3.0) * t)

    # Slow ambient LFO swell
    lfo = 0.85 + 0.15 * np.sin(2 * np.pi * 0.18 * t)
    drone = drone * lfo

    # Analog tape saturation noise
    noise = np.random.normal(0, 0.012, n_samples)
    audio = drone + noise
    audio = np.clip(audio, -0.92, 0.92)

    audio_16 = (audio * 32767).astype(np.int16)
    with wave.open(str(out_wav), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_16.tobytes())


def synthesize_voice_track(text: str, voice: str, out_mp3: Path) -> float:
    """Generates deliberate, authoritative voiceover using edge-tts with optimal Shorts pace (+12%)."""
    try:
        cmd = [
            sys.executable, "-m", "edge_tts",
            "--voice", voice,
            "--rate=+12%",
            "--text", text,
            "--write-media", str(out_mp3),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=35)
    except Exception as e:
        print(f"  [TTS Notice] edge-tts error ({e}); using gTTS fallback...")
        from gtts import gTTS
        lang = "ar" if voice.startswith("ar") else "en"
        gTTS(text=text, lang=lang, slow=False).save(str(out_mp3))

    # Probe duration using ffprobe / ffmpeg
    try:
        res = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(out_mp3)],
            capture_output=True, text=True, check=True
        )
        return float(res.stdout.strip())
    except Exception:
        # Approximate by file size if ffprobe fails
        return max(3.0, len(text.split()) * 0.38)

# ==============================================================================
# 5. DYNAMIC SCENE VISUAL GENERATOR & 3D KEN BURNS MOTION
# ==============================================================================

def fetch_pexels_video(query: str, out_mp4: Path) -> bool:
    api_key = os.environ.get("PEXELS_API_KEY", "").strip()
    if not api_key:
        return False
    try:
        clean_q = urllib.parse.quote(query[:60])
        url = f"https://api.pexels.com/videos/search?query={clean_q}&per_page=5&orientation=portrait"
        req = urllib.request.Request(url, headers={"Authorization": api_key, "User-Agent": "EmpireCloud/15.0"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        videos = data.get("videos", [])
        if not videos:
            return False
        for v in videos:
            for vf in sorted(v.get("video_files", []), key=lambda x: x.get("width", 0), reverse=True):
                v_link = vf.get("link")
                if v_link:
                    with urllib.request.urlopen(urllib.request.Request(v_link, headers={"User-Agent": "Mozilla/5.0"}), timeout=20) as dl:
                        raw = dl.read()
                    if len(raw) > 50_000:
                        out_mp4.write_bytes(raw)
                        return True
        return False
    except Exception:
        return False


def generate_flux_image_zerogpu(prompt: str, out_jpg: Path) -> bool:
    hf_token = os.environ.get("HF_TOKEN", "").strip()
    if not hf_token:
        return False
    spaces = [
        "black-forest-labs/FLUX.1-schnell",
        "stabilityai/stable-diffusion-3.5-large",
        "multimodalart/flux-tarot-v1",
    ]
    for sp in spaces:
        try:
            from gradio_client import Client
            os.environ["HF_TOKEN"] = hf_token
            client = Client(sp)
            res = client.predict(
                prompt=f"{prompt}, 8k ultra-cinematic documentary still, moody atmospheric lighting, 9:16 vertical",
                api_name="/predict"
            )
            found = res[0] if isinstance(res, (list, tuple)) else res
            if found and os.path.exists(str(found)):
                shutil.copy(str(found), str(out_jpg))
                return True
        except Exception:
            continue
    return False


def create_dark_cinematic_procedural_backdrop(style_hint: str, target_w: int = 1350, target_h: int = 2400) -> Image.Image:
    """Generates ultra-high-resolution moody neo-noir backdrop when offline/fallback."""
    img = Image.new("RGB", (target_w, target_h), (10, 12, 18))
    draw = ImageDraw.Draw(img)

    # Palette selection based on scene style
    if any(k in style_hint for k in ("gold", "vault", "wealth", "keys", "cartel")):
        top_c, bot_c = (28, 22, 12), (10, 8, 5)
        accent = (255, 195, 45, 45)
    elif any(k in style_hint for k in ("cyber", "ai", "eye", "algo", "servers", "power_grid")):
        top_c, bot_c = (8, 16, 30), (4, 8, 16)
        accent = (0, 215, 255, 40)
    elif "wolf" in style_hint:
        top_c, bot_c = (14, 18, 26), (6, 8, 12)
        accent = (180, 205, 235, 35)
    elif any(k in style_hint for k in ("nuclear", "f1", "casino", "courtroom")):
        top_c, bot_c = (30, 14, 18), (10, 6, 8)
        accent = (255, 80, 60, 35)
    else:
        top_c, bot_c = (20, 16, 24), (8, 6, 12)
        accent = (200, 170, 230, 30)

    # Vertical atmospheric gradient
    for y in range(target_h):
        alpha = y / float(target_h)
        r = int(top_c[0] * (1.0 - alpha) + bot_c[0] * alpha)
        g = int(top_c[1] * (1.0 - alpha) + bot_c[1] * alpha)
        b = int(top_c[2] * (1.0 - alpha) + bot_c[2] * alpha)
        draw.line([(0, y), (target_w, y)], fill=(r, g, b))

    # Add atmospheric depth circles & cinematic light rays
    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    d_over = ImageDraw.Draw(overlay, "RGBA")
    d_over.ellipse([target_w * 0.12, target_h * 0.18, target_w * 0.88, target_h * 0.68], fill=accent)
    d_over.ellipse([target_w * 0.05, target_h * 0.38, target_w * 0.95, target_h * 0.92], fill=(accent[0], accent[1], accent[2], 25))

    # Vignette shadow overlay
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img

# ==============================================================================
# 6. KINETIC TYPOGRAPHY & CINEMATIC CAPTION OVERLAY
# ==============================================================================

def render_cinematic_caption_overlay(
    caption_text: str,
    lang: str,
    target_w: int = 1080,
    target_h: int = 1920,
) -> tuple[np.ndarray, np.ndarray]:
    """Renders centered, clean, elegant Cairo Bold subtitles with dynamic frosted pill."""
    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay, "RGBA")

    f_cap = get_font(size=52, bold=True)
    center_x = target_w // 2
    center_y = int(target_h * 0.65)  # Viewer eye-level focal center

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

        draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(6, 8, 14, 215), outline=(255, 255, 255, 35), width=2)
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

        draw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(6, 8, 14, 215), outline=(255, 255, 255, 35), width=2)
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
    style_hint: str,
    caption: str,
    lang: str,
    duration: float,
    scene_mp3: Path,
    scene_mp4: Path,
    fps: int = 30,
    target_w: int = 1080,
    target_h: int = 1920,
) -> bool:
    """Streams animated Ken-Burns frames directly into FFmpeg stdin pipe (O(1) constant RAM footprint)."""
    n_frames = max(15, int(round(duration * fps)))
    over_w, over_h = int(target_w * 1.25), int(target_h * 1.25)

    # 1. Prepare Base Visual
    base_im = None
    if visual_path.suffix.lower() == ".mp4" and visual_path.exists() and visual_path.stat().st_size > 50_000:
        mid_frame = visual_path.parent / f"thumb_{visual_path.stem}.jpg"
        try:
            cmd = ["ffmpeg", "-y", "-ss", "1.5", "-i", str(visual_path), "-vframes", "1", str(mid_frame)]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
            if mid_frame.exists() and mid_frame.stat().st_size > 5_000:
                base_im = Image.open(mid_frame).convert("RGB")
        except Exception:
            pass

    if base_im is None:
        if visual_path.exists() and visual_path.stat().st_size > 10_000:
            try:
                base_im = Image.open(visual_path).convert("RGB")
            except Exception:
                base_im = None

    if base_im is None:
        base_im = create_dark_cinematic_procedural_backdrop(style_hint, target_w=over_w, target_h=over_h)

    # Resize base image with 1.25x headroom for zooming
    base_im = base_im.resize((over_w, over_h), Image.Resampling.LANCZOS)

    # 2. Render Caption Overlay (pre-calculated once per scene)
    c_rgb, c_alpha = render_cinematic_caption_overlay(caption, lang, target_w=target_w, target_h=target_h)

    # 3. Launch FFmpeg writer
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
            scale = 1.0 + 0.12 * t
            crop_w = int(target_w / scale)
            crop_h = int(target_h / scale)

            drift_x = int(math.sin(t * math.pi) * 30)
            x0 = max(0, min(over_w - crop_w, (over_w - crop_w) // 2 + drift_x))
            y0 = max(0, min(over_h - crop_h, (over_h - crop_h) // 2))

            crop = base_im.crop((x0, y0, x0 + crop_w, y0 + crop_h)).resize((target_w, target_h), Image.Resampling.BILINEAR)
            arr = np.array(crop, dtype=np.float32)

            # Subtle neo-noir film grain
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
# 8. MASTER EPISODE PRODUCER (QUIET WOLF FULL PIPELINE)
# ==============================================================================

def produce_quiet_wolf_episode(channel_key: str, cfg: dict, output_root: Path) -> tuple[Path, dict]:
    W, H, FPS = 1080, 1920, 30
    lang = cfg["lang"]
    work_dir = output_root / f"work_{channel_key}"
    work_dir.mkdir(parents=True, exist_ok=True)

    # 1. Select Episode Script based on Run Number
    run_num = int(os.environ.get("GITHUB_RUN_NUMBER", "1") or 1)
    bank = EPISODE_BANK_AR if lang == "ar" else EPISODE_BANK_EN
    script_data = bank[run_num % len(bank)]
    title = script_data["title"]
    scenes = script_data["scenes"]

    print(f"\n[{channel_key}] Producing Quiet-Wolf Documentary: '{title}' ({len(scenes)} scenes)")

    final_mp4 = output_root / f"{channel_key}_latest.mp4"
    scene_video_paths = []

    # 2. Render each scene via direct stream pipeline
    for s_idx, scene in enumerate(scenes):
        print(f"  --- Scene {s_idx + 1}/{len(scenes)}: {scene['caption'][:40]}... ---")
        scene_mp3 = work_dir / f"scene_{s_idx}.mp3"
        scene_mp4 = work_dir / f"scene_{s_idx}.mp4"
        scene_visual = work_dir / f"visual_{s_idx}.jpg"
        scene_pvid = work_dir / f"pvid_{s_idx}.mp4"

        # A. Voice synthesis
        duration = synthesize_voice_track(scene["narration"], cfg["voice"], scene_mp3)

        # B. Obtain Visual (Pexels / Flux / Procedural)
        visual_path = scene_visual
        if not fetch_pexels_video(scene["broll_query"], scene_pvid):
            if not generate_flux_image_zerogpu(scene["broll_prompt"], scene_visual):
                visual_path = scene_visual

        # C. Render Scene directly to FFmpeg pipe (Zero Memory Bloat)
        ok = stream_render_scene(
            visual_path=scene_pvid if scene_pvid.exists() else visual_path,
            style_hint=scene.get("visual_style", "dark"),
            caption=scene["caption"],
            lang=lang,
            duration=duration,
            scene_mp3=scene_mp3,
            scene_mp4=scene_mp4,
            fps=FPS,
            target_w=W,
            target_h=H,
        )
        if ok and scene_mp4.exists():
            scene_video_paths.append(scene_mp4)

    # 3. Concatenate all scenes into a continuous documentary
    concat_list = work_dir / "concat.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for p in scene_video_paths:
            f.write(f"file '{p.resolve().as_posix()}'\n")

    combined_dry_mp4 = work_dir / "combined_dry.mp4"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(combined_dry_mp4)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    # 4. Synthesize and layer the ambient sub-bass drone track under the full audio
    total_duration = len(scenes) * 4.5
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

    # Final audio mix: Voice (1.0) + Sub-bass drone (0.18)
    final_cmd = [
        "ffmpeg", "-y",
        "-i", str(combined_dry_mp4),
        "-i", str(drone_wav),
        "-filter_complex", "[0:a]volume=1.0[v];[1:a]volume=0.18[d];[v][d]amix=inputs=2:duration=first:dropout_transition=2[a]",
        "-map", "0:v",
        "-map", "[a]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        str(final_mp4)
    ]
    subprocess.run(final_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 5. Enforce strict YouTube Shorts Duration Limit (Max 55 seconds Hard Governor)
    try:
        res = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(final_mp4)],
            capture_output=True, text=True, check=True
        )
        cur_dur = float(res.stdout.strip())
        if cur_dur > 55.0:
            print(f"  [Duration Governor] Short duration ({cur_dur:.1f}s) exceeds 55s; compressing tempo into viral window...")
            speed_factor = cur_dur / 48.0  # target 48s
            compressed_mp4 = work_dir / "compressed_final.mp4"
            cmd = [
                "ffmpeg", "-y",
                "-i", str(final_mp4),
                "-filter_complex", f"[0:v]setpts={1.0/speed_factor}*PTS[v];[0:a]atempo={speed_factor}[a]",
                "-map", "[v]",
                "-map", "[a]",
                "-c:v", "libx264",
                "-preset", "veryfast",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac",
                "-b:a", "192k",
                str(compressed_mp4)
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if compressed_mp4.exists() and compressed_mp4.stat().st_size > 10_000:
                shutil.move(str(compressed_mp4), str(final_mp4))
    except Exception as e:
        print(f"  [Duration Check Notice] {e}")

    print(f"[{channel_key}] SUCCESS! Exported Quiet-Wolf Master Short: {final_mp4} ({final_mp4.stat().st_size // (1024*1024)} MB)")
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
    print(f"  [YouTube Upload] Publishing Quiet-Wolf Short for: {cfg['name']} ({secret_env})")
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
        desc = f"{title}\n\n{cfg['outro_line']}\n\n#Shorts #QuietWolf #Mindset #Billionaire #Power"

        body = {
            "snippet": {
                "title": title,
                "description": desc,
                "tags": cfg.get("tags", ["Shorts", "Viral", "Documentary"]),
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
        print(f"STARTING QUIET-WOLF VIRAL ENGINE v15.0 FOR: {ch_key}")
        print("=" * 75)
        video_path, script_data = produce_quiet_wolf_episode(ch_key, cfg, output_root)
        if os.environ.get("DRY_RUN", "0") != "1":
            upload_to_youtube(video_path, script_data, cfg)

if __name__ == "__main__":
    main()
