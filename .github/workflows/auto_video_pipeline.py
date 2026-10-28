#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMPIRE AUTO-VIDEO PIPELINE v11.0 (NEURAL WAV2LIP ONNX + REAL MOVING PRESENTER VIDEOS + MULTI-PART SERIES)
- Guaranteed Real Video Movement on Every Frame (0% Static Images):
  1. Downloads real 30-FPS HD studio presenter video clips (natural head movement, blinking, gestures)
     from Hugging Face CDN (`LivePortrait` / `Wav2Lip` studio host videos) + Pexels Video API + Wikimedia
     Commons video search.
  2. Runs real Neural Lip-Sync on CPU using `wav2lip_gan.onnx` / `wav2lip.onnx` (`onnxruntime`) so the
     human presenter's actual mouth, lips, and teeth articulate every Arabic & English word!
  3. Includes an Enhanced 2D Piecewise-Affine Facial Mesh Warper + Viseme Articulator as an instant
     backup if ONNX weights are still downloading, ensuring the presenter's head, eyes, eyebrows, torso,
     and mouth move continuously on every frame.
  4. Dynamic 3-Camera Broadcast Switching (Full-Screen Presenter, 50/50 Vertical Split-Screen with
     Moving Video B-Roll, and Picture-in-Picture over Full-Screen Moving B-Roll) + Animated 60-FPS
     Equalizer & Live Data Ticker so no pixel of the screen is ever static.
  5. Dynamic Multi-Part Series Engine (`الجزء 1`, `الجزء 2`... / `Part 1`, `Part 2`...) indexed by
     `GITHUB_RUN_NUMBER` + Gemini 2.5 Flash so every single video has a fresh, gripping script.
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

import numpy as np
from scipy import signal
from PIL import Image, ImageDraw, ImageFont

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    HAS_ARABIC_SHAPER = True
except Exception:
    HAS_ARABIC_SHAPER = False


# ==============================================================================
# 1. CHANNEL CONFIGURATION & MULTI-PART SERIES BANK
# ==============================================================================

CHANNELS = {
    "ch02_ar_ai_tech": {
        "name": "الذكاء الاصطناعي وتقنيات المستقبل",
        "lang": "ar",
        "voice": "ar-EG-ShakirNeural",
        "secret_env": "YT_TOKEN_CH02_AR",
        "presenter_prompt": (
            "Hyper-realistic medium close-up studio portrait of a charismatic 30-year-old Arab male tech presenter, "
            "looking directly into the camera lens, neutral closed mouth, symmetrical face, wearing a sleek dark "
            "smart-casual blazer, modern futuristic podcast studio background with soft cyan and warm amber bokeh lights, "
            "8k DSLR photography, sharp focus on eyes and face, vertical 9:16 composition"
        ),
        "presenter_video_urls": [
            "https://huggingface.co/spaces/KlingTeam/LivePortrait/resolve/main/assets/examples/driving/d0.mp4",
            "https://huggingface.co/spaces/KlingTeam/LivePortrait/resolve/main/assets/examples/driving/d3.mp4",
            "https://huggingface.co/spaces/WeReCooking/wav2lip/resolve/main/examples/woman_512_4s.mp4",
        ],
        "presenter_fallback_urls": [
            "https://huggingface.co/spaces/vinthony/SadTalker/resolve/main/examples/source_image/full_body_1.png",
            "https://huggingface.co/spaces/vinthony/SadTalker/resolve/main/examples/source_image/people_0.png",
            "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1080&q=85",
            "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=1080&q=85",
        ],
    },
    "ch03_en_wealth_business": {
        "name": "Billionaire Empires & Wealth",
        "lang": "en",
        "voice": "en-US-ChristopherNeural",
        "secret_env": "YT_TOKEN_CH03_EN",
        "presenter_prompt": (
            "Hyper-realistic medium close-up studio portrait of a charismatic 34-year-old financial documentary host, "
            "looking directly into the camera lens, neutral closed mouth, symmetrical face, wearing a tailored charcoal suit "
            "with open collar, luxury Manhattan penthouse office background at dusk with warm golden and navy lighting, "
            "8k Sony A7R IV photography, sharp focus on eyes and face, vertical 9:16 composition"
        ),
        "presenter_video_urls": [
            "https://huggingface.co/spaces/KlingTeam/LivePortrait/resolve/main/assets/examples/driving/d3.mp4",
            "https://huggingface.co/spaces/KlingTeam/LivePortrait/resolve/main/assets/examples/driving/d0.mp4",
            "https://huggingface.co/spaces/WeReCooking/wav2lip/resolve/main/examples/woman_512_4s.mp4",
        ],
        "presenter_fallback_urls": [
            "https://huggingface.co/spaces/vinthony/SadTalker/resolve/main/examples/source_image/full_body_2.png",
            "https://huggingface.co/spaces/vinthony/SadTalker/resolve/main/examples/source_image/happy.png",
            "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=1080&q=85",
            "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=1080&q=85",
        ],
    },
}

EPISODE_BANK_AR = [
    {
        "series_title": "أسرار إمبراطوريات الذكاء الاصطناعي",
        "part": "الجزء 1",
        "title": "الجزء 1 | كيف بنى مهندس واحد شركة ذكاء اصطناعي بمليار دولار بدون موظفين؟ #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "تخيل إن شركة قيمتها مليار دولار بتشتغل النهاردة بالكامل من غير موظف بشري واحد! في الجزء الأول من سلسلتنا، هكشفلك السر اللي الشركات الكبرى بتخبيه عنك.",
                "caption": "شركة بمليار دولار بدون موظفين! (الجزء 1)",
                "broll_query": "Artificial intelligence server room data center",
                "broll_prompt": "Futuristic glowing AI data center server racks with holographic financial graphs, 8k cinematic",
                "stat_badge": "AI EMPIRE • PART 1"
            },
            {
                "layout": "split_screen",
                "narration": "السر كله في وكلاء الذكاء الاصطناعي المستقلين، أو AI Agents. بدل ما تعين عشرين مبرمج، بتربط تلات نماذج ببعض: واحد يخطط، والتاني يكتب الكود، والتالت يختبر ويصلح الأخطاء تلقائياً.",
                "caption": "وكلاء الذكاء الاصطناعي يبرمجون ٢٤ ساعة",
                "broll_query": "Robot arm microchip technology",
                "broll_prompt": "Autonomous AI software engineering dashboard showing live code generation and neural network nodes, 8k",
                "stat_badge": "3 AI AGENTS = 20 DEVS"
            },
            {
                "layout": "pip_broll",
                "narration": "النتيجة؟ المنتج اللي كان بياخد ست شهور بقى يخلص في ثمانٍ وأربعين ساعة بس، وبتكلفة أقل بتسعين في المية!",
                "caption": "من ٦ شهور إلى ٤٨ ساعة فقط بتكلفة أقل ٩٠٪",
                "broll_query": "High speed futuristic city time lapse",
                "broll_prompt": "Futuristic skyscraper holograms showing 90 percent cost reduction and rocket launch speed, 8k",
                "stat_badge": "48 HOURS • -90% COST"
            },
            {
                "layout": "presenter_full",
                "narration": "في الجزء التاني هشرحلك بالخطوات إزاي تبني أول وكيل ذكاء اصطناعي يشتغل لحسابك مجاناً. اشترك دلوقتي عشان يوصلك الجزء التاني أول ما ينزل!",
                "caption": "اشترك الآن لمتابعة الجزء الثاني!",
                "broll_query": "Artificial intelligence brain network",
                "broll_prompt": "Glowing golden digital brain network in studio, 8k",
                "stat_badge": "تابع الجزء 2 غداً"
            }
        ]
    },
    {
        "series_title": "أسرار إمبراطوريات الذكاء الاصطناعي",
        "part": "الجزء 2",
        "title": "الجزء 2 | الصدمة: كيف يستبدل وكيل الذكاء الاصطناعي قسم تسويق كامل في ٥ دقائق؟ #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "في الجزء الأول شوفنا إزاي الذكاء الاصطناعي بيبني الشركات، بس النهاردة في الجزء التاني هتشوف إزاي بيقود حملات تسويق بملايين الدولارات في خمس دقايق بس!",
                "caption": "الجزء ٢: وكيل تسويق ذكي بملايين الدولارات",
                "broll_query": "Digital marketing analytics screen",
                "broll_prompt": "Holographic viral marketing dashboard with millions of views counting up in real time, 8k",
                "stat_badge": "AI EMPIRE • PART 2"
            },
            {
                "layout": "split_screen",
                "narration": "النظام الجديد بيحلل أكتر من مية ألف فيديو رائج كل ساعة، بيكتشف الكلمات اللي بتشد الانتباه في أول تلات ثواني، وبيولد سكريبتات وصوت ومونتاج كامل بضغطة زر.",
                "caption": "تحليل ١٠٠ ألف فيديو رائج كل ساعة تلقائياً",
                "broll_query": "Social media data stream network",
                "broll_prompt": "Glowing neural network scanning thousands of vertical smartphone video screens simultaneously, 8k",
                "stat_badge": "100,000 VIDEOS / HR"
            },
            {
                "layout": "pip_broll",
                "narration": "الشركات اللي طبقت التقنية دي ضاعفت مبيعاتها أربع مرات في تلاتين يوم من غير ما تدفع دولار واحد زيادة في الإعلانات!",
                "caption": "مضاعفة المبيعات ٤٠٠٪ في ٣٠ يوماً فقط",
                "broll_query": "Stock market bull chart rising",
                "broll_prompt": "3D emerald green revenue chart skyrocketing upward 400 percent in modern glass office, 8k",
                "stat_badge": "+400% REVENUE IN 30d"
            },
            {
                "layout": "presenter_full",
                "narration": "فاضل سر واحد أخطر في الجزء التالت: إزاي تحمي وظيفتك وتخلي الذكاء الاصطناعي يضاعف دخلك. اشترك وفعل الجرس عشان ما يفوتكش الجزء التالت!",
                "caption": "اشترك الآن لمتابعة الجزء الثالث غداً!",
                "broll_query": "Futuristic hologram interface",
                "broll_prompt": "Futuristic AI shield protecting digital career assets, 8k",
                "stat_badge": "تابع الجزء 3"
            }
        ]
    },
    {
        "series_title": "أسرار إمبراطوريات الذكاء الاصطناعي",
        "part": "الجزء 3",
        "title": "الجزء 3 | معركة الرقائق: لماذا تشتري الشركات شريحة إنفيديا السرية بـ ٤٠ ألف دولار؟ #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "ليه أكبر شركات العالم واقفة في طابور طويل عشان تشتري شريحة سيليكون واحدة سعرها أربعين ألف دولار؟ أهلاً بيك في الجزء التالت من أسرار الذكاء الاصطناعي!",
                "caption": "الجزء ٣: شريحة إنفيديا بسعر ٤٠ ألف دولار!",
                "broll_query": "Computer microchip wafer silicon",
                "broll_prompt": "Extreme macro shot of a glowing gold and black AI GPU microchip wafer in cleanroom, 8k",
                "stat_badge": "AI EMPIRE • PART 3"
            },
            {
                "layout": "split_screen",
                "narration": "الشريحة دي فيها أكتر من ميتين مليار ترانزستور، وتقدر تدرب عقل اصطناعي كامل في أسبوع واحد بدل عشر سنين على الكمبيوترات العادية.",
                "caption": "٢٠٠ مليار ترانزستور يختصر ١٠ سنوات في أسبوع",
                "broll_query": "Supercomputer server cluster",
                "broll_prompt": "Massive liquid-cooled AI supercomputer cluster pulsing with neon green light rays, 8k",
                "stat_badge": "200B TRANSISTORS"
            },
            {
                "layout": "pip_broll",
                "narration": "عشان كده الدولة أو الشركة اللي بتمتلك الشرائح دي النهاردة، هي اللي بتمتلك نفط القرن الواحد والعشرين وبتتحكم في اقتصاد المستقبل.",
                "caption": "الرقائق الذكية هي نفط القرن الحادي والعشرين",
                "broll_query": "Global network earth from space",
                "broll_prompt": "Planet Earth at night connected by glowing golden semiconductor supply chain beams, 8k",
                "stat_badge": "THE NEW OIL • $3T"
            },
            {
                "layout": "presenter_full",
                "narration": "في الجزء الرابع هكشفلك إزاي الحوسبة الكمية هتقلب الموازين تماماً. اضغط اشتراك دلوقتي واستنى الجزء الرابع!",
                "caption": "اشترك الآن لمتابعة الجزء الرابع!",
                "broll_query": "Quantum computer chandelier",
                "broll_prompt": "Golden quantum computer dilution refrigerator glowing in cryogenic lab, 8k",
                "stat_badge": "تابع الجزء 4"
            }
        ]
    },
    {
        "series_title": "أسرار إمبراطوريات الذكاء الاصطناعي",
        "part": "الجزء 4",
        "title": "الجزء 4 | الحاسوب الكمي: الآلة التي تحل في ٣ دقائق ما يستغرق ١٠ آلاف سنة! #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "تخيل جهاز كمبيوتر بيشتغل في درجة حرارة أبرد من الفضاء الخارجي، ويقدر يحل في تلات دقايق معادلة بتاخد عشرة آلاف سنة! ده الجزء الرابع من سلسلتنا.",
                "caption": "الجزء ٤: الحاسوب الكمي الأبرد من الفضاء!",
                "broll_query": "Quantum computer golden wires",
                "broll_prompt": "Golden chandelier quantum computer suspended in futuristic cryogenic laboratory, 8k",
                "stat_badge": "QUANTUM • PART 4"
            },
            {
                "layout": "split_screen",
                "narration": "الكمبيوتر العادي بيفكر بصفر أو واحد، لكن الكمبيوتر الكمي بيستخدم الكيوبيت اللي بيكون صفر وواحد في نفس اللحظة، وده بيخليه يجرب ملايين الاحتمالات في ثانية واحدة.",
                "caption": "تقنية الكيوبيت: ملايين الاحتمالات في ثانية واحدة",
                "broll_query": "Physics particle collision subatomic",
                "broll_prompt": "Glowing quantum qubit sphere in superposition with cyan and violet energy waves, 8k",
                "stat_badge": "QUBIT SUPERPOSITION"
            },
            {
                "layout": "pip_broll",
                "narration": "لما تندمج القوة دي مع الذكاء الاصطناعي، هنقدر نكتشف أدوية لأصعب الأمراض ونصمم بطاريات تعيش مية سنة في ساعات معدودة.",
                "caption": "اكتشاف أدوية جديدة وبطاريات تعيش ١٠٠ عام",
                "broll_query": "DNA helix medical research laboratory",
                "broll_prompt": "3D holographic DNA strand being repaired by quantum AI nanobots in medical lab, 8k",
                "stat_badge": "MEDICAL BREAKTHROUGH"
            },
            {
                "layout": "presenter_full",
                "narration": "في الجزء الخامس هنتكلم عن الروبوتات البشرية اللي بدأت تدخل المصانع فعلاً. اشترك في القناة عشان تشوف الجزء الخامس!",
                "caption": "اشترك الآن لمتابعة الجزء الخامس!",
                "broll_query": "Humanoid robot walking",
                "broll_prompt": "Sleek white humanoid robot standing in high-tech factory, 8k",
                "stat_badge": "تابع الجزء 5"
            }
        ]
    },
    {
        "series_title": "أسرار إمبراطوريات الذكاء الاصطناعي",
        "part": "الجزء 5",
        "title": "الجزء 5 | جيش الروبوتات البشرية: كيف ستعمل المصانع ٢٤ ساعة بتكلفة دولار واحد؟ #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "أول دفعة من الروبوتات البشرية استلمت شغلها فعلاً في المصانع الكبرى، وتكلفة تشغيل الروبوت في الساعة أقل من تمن فنجان قهوة! أهلاً بيك في الجزء الخامس.",
                "caption": "الجزء ٥: روبوتات بشرية بتكلفة أقل من فنجان قهوة!",
                "broll_query": "Industrial robot factory automotive",
                "broll_prompt": "Humanoid bipedal robots assembling electric vehicles on a gleaming futuristic factory floor, 8k",
                "stat_badge": "ROBOTICS • PART 5"
            },
            {
                "layout": "split_screen",
                "narration": "الروبوتات الجديدة مش متبرمجة بحركات ثابتة، دي بتتعلم بالنظر! بتتفرج على العامل البشري عشر دقايق وبعدين تقلد الحركة بدقة ملليمترية وبدون تعب.",
                "caption": "تتعلم بالمشاهدة في ١٠ دقائق وتعمل بلا توقف",
                "broll_query": "Robotic hand precision engineering",
                "broll_prompt": "Close-up of a bionic robotic hand with tactile sensors holding a delicate glass sphere, 8k",
                "stat_badge": "NEURAL VISION LEARNING"
            },
            {
                "layout": "pip_broll",
                "narration": "الخبراء بيتوقعوا وجود أكتر من مليار روبوت بشري على كوكب الأرض بحلول سنة ألفين وأربعين، وده هيغير شكل الاقتصاد العالمي للأبد.",
                "caption": "مليار روبوت بشري على الأرض بحلول عام ٢٠٤٠",
                "broll_query": "Futuristic city skyline technology",
                "broll_prompt": "Futuristic smart city where humanoid assistants and autonomous drones operate seamlessly, 8k",
                "stat_badge": "1 BILLION ROBOTS BY 2040"
            },
            {
                "layout": "presenter_full",
                "narration": "اكتبلي في التعليقات: هل ترحب بوجود روبوت مساعد في بيتك؟ واشترك دلوقتي عشان تتابع الجزء السادس!",
                "caption": "شاركنا رأيك في التعليقات واشترك للجزء ٦!",
                "broll_query": "Smart home technology future",
                "broll_prompt": "Friendly futuristic home assistant robot in a luxury modern living room, 8k",
                "stat_badge": "تابع الجزء 6"
            }
        ]
    },
    {
        "series_title": "أسرار إمبراطوريات الذكاء الاصطناعي",
        "part": "الجزء 6",
        "title": "الجزء 6 | استنساخ الصوت والفيديو: كيف تصنع الأفلام السينمائية من غرفة نومك؟ #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "دلوقتي تقدر تنتج مشهد سينمائي كامل بجودة هوليوود وإنت قاعد في أوضتك بموبايلك بس! في الجزء السادس هوريك الثورة اللي غيرت صناعة السينما.",
                "caption": "الجزء ٦: صناعة سينما هوليوود من غرفتك!",
                "broll_query": "Cinema camera film production studio",
                "broll_prompt": "Virtual LED volume film production stage rendering photorealistic sci-fi worlds in real time, 8k",
                "stat_badge": "AI CINEMA • PART 6"
            },
            {
                "layout": "split_screen",
                "narration": "محركات توليد الفيديو الجديدة بتفهم الفيزياء والضوء وحركة الكاميرا، وبتحول سطرين كتابة لمشهد سينمائي ناطق ومتزامن مع حركة الشفايف في ثواني.",
                "caption": "تحويل النص إلى مشهد سينمائي ناطق في ثوانٍ",
                "broll_query": "3D animation rendering software",
                "broll_prompt": "Split screen showing text prompt transforming into a photorealistic 8k movie character speaking, 8k",
                "stat_badge": "TEXT TO 8K CINEMA"
            },
            {
                "layout": "pip_broll",
                "narration": "استوديوهات كبرى وفرت ملايين الدولارات في المؤثرات البصرية، وصناع المحتوى المستقلين بقوا ينافسوا أكبر القنوات العالمية.",
                "caption": "صناع المحتوى المستقلون ينافسون القنوات الكبرى",
                "broll_query": "Video editing timeline workstation",
                "broll_prompt": "Creator studio desk with dual curved monitors displaying AI video generation timelines, 8k",
                "stat_badge": "INDIE CREATOR BOOM"
            },
            {
                "layout": "presenter_full",
                "narration": "في الجزء السابع هنكشف إزاي الذكاء الاصطناعي بيتوقع حركة الأسواق المالية قبل ما تحصل. اشترك دلوقتي عشان تشوف الجزء السابع!",
                "caption": "اشترك الآن لمتابعة الجزء السابع!",
                "broll_query": "Financial trading floor screens",
                "broll_prompt": "Futuristic AI algorithmic trading desk overlooking city lights, 8k",
                "stat_badge": "تابع الجزء 7"
            }
        ]
    }
]

EPISODE_BANK_EN = [
    {
        "series_title": "Billionaire Shadow Playbooks",
        "part": "Part 1",
        "title": "Part 1 | Why Billionaires Never Take a Salary (The $1 CEO Strategy Explained) #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "Why do the richest CEOs in the world pay themselves an official salary of just one single dollar a year? Welcome to Part 1 of Billionaire Shadow Playbooks.",
                "caption": "Why Billionaires Take a $1 Salary (Part 1)",
                "broll_query": "Manhattan skyscrapers aerial view",
                "broll_prompt": "Cinematic aerial view of Manhattan billionaire row skyscrapers at golden hour, 8k",
                "stat_badge": "SHADOW PLAYBOOK • PART 1"
            },
            {
                "layout": "split_screen",
                "narration": "Here is the math: regular salaries get taxed at up to thirty-seven percent immediately. Instead, founders take compensation in company stock, which pays zero tax until sold.",
                "caption": "Salary = 37% Tax vs. Unsold Stock = 0% Tax",
                "broll_query": "Stock market exchange trading board",
                "broll_prompt": "Holographic comparison chart showing 37 percent income tax vs 0 percent unrealized equity growth, 8k",
                "stat_badge": "37% TAX VS 0% TAX"
            },
            {
                "layout": "pip_broll",
                "narration": "When they need cash for a jet or a new company, they never sell shares. They pledge just five percent of their stock as collateral for an ultra-low-interest bank loan—and loans are completely tax-free!",
                "caption": "Borrowing Against Stock at 0% Income Tax",
                "broll_query": "Private jet luxury airport tarmac",
                "broll_prompt": "Sleek Gulfstream private jet parked on wet tarmac at dusk with luxury sedan waiting, 8k",
                "stat_badge": "BUY • BORROW • GROW"
            },
            {
                "layout": "presenter_full",
                "narration": "In Part 2, I will show you how everyday investors legally use this exact collateral blueprint with index funds. Hit subscribe right now so you do not miss Part 2!",
                "caption": "Subscribe Now for Part 2 Tomorrow!",
                "broll_query": "Wall street bull statue",
                "broll_prompt": "Wall Street financial district glowing at night, 8k",
                "stat_badge": "PART 2 NEXT"
            }
        ]
    },
    {
        "series_title": "Billionaire Shadow Playbooks",
        "part": "Part 2",
        "title": "Part 2 | How the Ultra-Wealthy Buy Commercial Empires Using Zero of Their Own Cash #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "In Part 1 we uncovered the one-dollar salary, but today in Part 2, watch how billionaires acquire hundred-million-dollar buildings without spending a dime of their own cash!",
                "caption": "Part 2: Buying Empires With $0 Down",
                "broll_query": "Luxury glass skyscraper architecture",
                "broll_prompt": "Towering modern glass commercial skyscraper in London financial district at sunset, 8k",
                "stat_badge": "SHADOW PLAYBOOK • PART 2"
            },
            {
                "layout": "split_screen",
                "narration": "They combine a pledged-asset credit line from their stock portfolio for the twenty percent down payment, while a commercial bank funds the remaining eighty percent.",
                "caption": "20% Asset Line + 80% Bank Debt = 100% Financed",
                "broll_query": "Architectural blueprint building model",
                "broll_prompt": "3D architectural glass skyscraper model glowing with financial leverage ratios on boardroom table, 8k",
                "stat_badge": "100% LEVERAGED ACQUISITION"
            },
            {
                "layout": "pip_broll",
                "narration": "Corporate tenants sign ten-year triple-net leases that pay off both loans automatically, while accelerated depreciation wipes out taxes on the rental cash flow!",
                "caption": "Tenants Pay the Debt While Depreciation Cuts Tax",
                "broll_query": "Modern corporate office lobby",
                "broll_prompt": "High-end marble corporate headquarters lobby with digital cash flow counters, 8k",
                "stat_badge": "TRIPLE-NET CASHFLOW"
            },
            {
                "layout": "presenter_full",
                "narration": "In Part 3, I am revealing the Dynasty Trust structure that protects this wealth for a hundred years. Subscribe now to catch Part 3!",
                "caption": "Subscribe Now so You Don't Miss Part 3!",
                "broll_query": "Gold vault bank door",
                "broll_prompt": "Massive stainless steel and gold private bank vault door open, 8k",
                "stat_badge": "PART 3 NEXT"
            }
        ]
    },
    {
        "series_title": "Billionaire Shadow Playbooks",
        "part": "Part 3",
        "title": "Part 3 | The 100-Year Dynasty Trust: Why Old Money Never Goes Broke #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "Why do seventy percent of lottery winners go broke in five years, while billionaire families stay rich for five generations? Welcome to Part 3 of Billionaire Shadow Playbooks!",
                "caption": "Part 3: The 100-Year Dynasty Trust Secret",
                "broll_query": "Historic estate mansion aerial",
                "broll_prompt": "Grand historic European stone estate surrounded by manicured gardens at sunrise, 8k",
                "stat_badge": "SHADOW PLAYBOOK • PART 3"
            },
            {
                "layout": "split_screen",
                "narration": "The secret is one rule: Own nothing personally, control everything through an irrevocable Dynasty Trust. The family members do not own the mansions or shares—the Trust does.",
                "caption": "Own Nothing Personally, Control Everything",
                "broll_query": "Legal contract fountain pen gold",
                "broll_prompt": "Luxury gold fountain pen resting on a leather-bound Dynasty Trust charter in mahogany library, 8k",
                "stat_badge": "DYNASTY TRUST SHIELD"
            },
            {
                "layout": "pip_broll",
                "narration": "Because the assets never officially change hands when a generation passes away, the portfolio compounds uninterrupted for a century without losing forty percent to estate taxes!",
                "caption": "100 Years of Uninterrupted Compounding",
                "broll_query": "Compound interest chart exponential",
                "broll_prompt": "Glowing golden exponential compound growth curve soaring across a century timeline, 8k",
                "stat_badge": "100-YR COMPOUNDING"
            },
            {
                "layout": "presenter_full",
                "narration": "In Part 4, we break down how sovereign wealth funds quietly buy up the world's biggest tech monopolies. Hit subscribe for Part 4!",
                "caption": "Subscribe Now for Part 4!",
                "broll_query": "Global financial hub skyline",
                "broll_prompt": "Futuristic financial capital skyline reflecting on water at twilight, 8k",
                "stat_badge": "PART 4 NEXT"
            }
        ]
    },
    {
        "series_title": "Billionaire Shadow Playbooks",
        "part": "Part 4",
        "title": "Part 4 | The Tollbooth Monopoly: How Warren Buffett Makes $24 Million a Day Passively #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "How does Warren Buffett collect over twenty-four million dollars every single day before he even finishes his morning coffee? Welcome to Part 4 of our wealth series!",
                "caption": "Part 4: Collecting $24 Million Every Single Day",
                "broll_query": "Freight train railway bridge",
                "broll_prompt": "Massive transcontinental freight train crossing a steel bridge at sunrise, 8k",
                "stat_badge": "SHADOW PLAYBOOK • PART 4"
            },
            {
                "layout": "split_screen",
                "narration": "He calls it the Economic Tollbooth strategy. Instead of gambling on hype stocks, he buys unavoidable infrastructure—payment networks, railways, and power grids that charge a tiny fee on every transaction.",
                "caption": "Economic Tollbooths: Collect a Fee on Every Sale",
                "broll_query": "Credit card payment terminal tap",
                "broll_prompt": "Close-up of a sleek contactless payment terminal glowing with micro-transaction beams, 8k",
                "stat_badge": "TOLLBOOTH MONOPOLY"
            },
            {
                "layout": "pip_broll",
                "narration": "Every time someone swipes a card, ships cargo, or flips a light switch, cash flows straight into Berkshire Hathaway's treasury—generating nearly nine billion dollars a year in pure dividends!",
                "caption": "$9 Billion a Year in Pure Passive Dividends",
                "broll_query": "Power grid city lights night",
                "broll_prompt": "High-voltage power grid illuminating a massive metropolis at night from above, 8k",
                "stat_badge": "$9B / YR DIVIDENDS"
            },
            {
                "layout": "presenter_full",
                "narration": "In Part 5, I will reveal the three tollbooth sectors growing fastest in the AI era. Subscribe right now so you never miss Part 5!",
                "caption": "Subscribe Now to Watch Part 5!",
                "broll_query": "Stock market ticker green",
                "broll_prompt": "Glowing green stock market ticker board in modern trading room, 8k",
                "stat_badge": "PART 5 NEXT"
            }
        ]
    },
    {
        "series_title": "Billionaire Shadow Playbooks",
        "part": "Part 5",
        "title": "Part 5 | Private Equity Roll-Ups: Turning Boring Local Businesses into $100M Exits #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "Why are Wall Street billionaires suddenly buying up local car washes, HVAC companies, and dental clinics? Welcome to Part 5 of Billionaire Shadow Playbooks!",
                "caption": "Part 5: Why Wall Street Buys Boring Businesses",
                "broll_query": "Private equity boardroom meeting",
                "broll_prompt": "Executive private equity deal room overlooking Manhattan skyline with acquisition maps, 8k",
                "stat_badge": "SHADOW PLAYBOOK • PART 5"
            },
            {
                "layout": "split_screen",
                "narration": "It is called a Multiple Arbitrage Roll-Up. A single local business sells for just three times its annual profit. But when you combine twenty of them into one regional brand, institutional funds pay twelve times profit!",
                "caption": "Buy at 3x Profit -> Combine -> Sell at 12x Profit",
                "broll_query": "Corporate merger handshake office",
                "broll_prompt": "3D financial diagram showing 20 small businesses merging into a 100 million dollar enterprise, 8k",
                "stat_badge": "3X TO 12X ARBITRAGE"
            },
            {
                "layout": "pip_broll",
                "narration": "By centralizing software, AI booking, and bulk purchasing, profit margins double overnight—turning ten million dollars of boring shops into a hundred-million-dollar exit!",
                "caption": "Centralized AI Operations Double Profit Margins",
                "broll_query": "Automated warehouse logistics",
                "broll_prompt": "Modern automated logistics command center tracking nationwide service fleets, 8k",
                "stat_badge": "$100M ROLL-UP EXIT"
            },
            {
                "layout": "presenter_full",
                "narration": "Comment 'PLAYBOOK' below if you want Part 6 on how micro-acquisitions work with zero employees, and hit subscribe right now!",
                "caption": "Subscribe Now for Part 6!",
                "broll_query": "Skyscraper glass reflection",
                "broll_prompt": "Golden sunset reflecting off Wall Street glass towers, 8k",
                "stat_badge": "PART 6 NEXT"
            }
        ]
    },
    {
        "series_title": "Billionaire Shadow Playbooks",
        "part": "Part 6",
        "title": "Part 6 | The Royalties Secret: Getting Paid 50 Years for Work You Did Once #Shorts",
        "segments": [
            {
                "layout": "presenter_full",
                "narration": "What if one single asset you acquired today kept depositing checks into your bank account for the next fifty years? Welcome to Part 6 of our wealth series!",
                "caption": "Part 6: Getting Paid 50 Years From One Asset",
                "broll_query": "Oil pump jack sunset",
                "broll_prompt": "Golden sunset over energy mineral royalty fields and digital patent vaults, 8k",
                "stat_badge": "SHADOW PLAYBOOK • PART 6"
            },
            {
                "layout": "split_screen",
                "narration": "Ultra-wealthy investors quietly buy Licensing and Royalty rights—from pharmaceutical patents and semiconductor designs to music catalogs and mineral rights.",
                "caption": "Owning Patents, Chip Licenses & Mineral Royalties",
                "broll_query": "Semiconductor wafer inspection",
                "broll_prompt": "Holographic patent blueprint of a smartphone microchip generating royalty streams, 8k",
                "stat_badge": "ROYALTY CASH STREAMS"
            },
            {
                "layout": "pip_broll",
                "narration": "Unlike a traditional business, a royalty owner has zero employees, zero inventory, and zero operating expenses—just a legal contract taking a percentage of gross global sales forever!",
                "caption": "0 Employees, 0 Inventory, Pure Gross Revenue Cut",
                "broll_query": "Global shipping container port",
                "broll_prompt": "Aerial view of a massive illuminated global container port moving billions in licensed goods, 8k",
                "stat_badge": "100% PASSIVE MARGIN"
            },
            {
                "layout": "presenter_full",
                "narration": "Make sure you are subscribed to the channel right now—Part 7 drops next with the Sovereign Debt Arbitrage strategy!",
                "caption": "Subscribe Now so You Never Miss Part 7!",
                "broll_query": "Financial district night lights",
                "broll_prompt": "Cinematic night skyline of global banking headquarters, 8k",
                "stat_badge": "PART 7 NEXT"
            }
        ]
    }
]


# ==============================================================================
# 2. ARABIC TEXT SHAPING & FONT UTILITIES
# ==============================================================================

def shape_text(text: str, lang: str = "ar") -> str:
    if not text:
        return ""
    if lang == "ar" and HAS_ARABIC_SHAPER:
        try:
            return get_display(arabic_reshaper.reshape(text))
        except Exception:
            return text
    return text


def get_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf",
        "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size=size)
            except Exception:
                continue
    return ImageFont.load_default()


# ==============================================================================
# 3. DYNAMIC MULTI-PART SCRIPT GENERATOR
# ==============================================================================

def get_episode_index(channel_key: str) -> int:
    run_num_str = os.environ.get("GITHUB_RUN_NUMBER", "").strip()
    attempt_str = os.environ.get("GITHUB_RUN_ATTEMPT", "1").strip()
    if run_num_str.isdigit():
        return int(run_num_str) + int(attempt_str if attempt_str.isdigit() else 1) - 1
    return int(time.time() // 3600)


def generate_dynamic_script(channel_key: str, cfg: dict) -> dict:
    lang = cfg["lang"]
    ep_idx = get_episode_index(channel_key)
    bank = EPISODE_BANK_AR if lang == "ar" else EPISODE_BANK_EN
    template_ep = bank[ep_idx % len(bank)]
    part_num = (ep_idx % 12) + 1
    part_label = f"الجزء {part_num}" if lang == "ar" else f"Part {part_num}"

    print(f"[{channel_key}] Selecting/Generating dynamic episode: {part_label} (Run index: {ep_idx})...")

    gemini_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if gemini_key:
        prompt = (
            f"You are an elite viral documentary scriptwriter for YouTube Shorts. "
            f"Create Episode '{part_label}' of an investigative series for channel '{cfg['name']}'. "
            f"Seed topic inspiration (create a FRESH angle for {part_label}): {template_ep['title']}. "
            f"Return STRICT JSON ONLY with keys: "
            f"'title' (must start with '{part_label} | ' and end with '#Shorts'), "
            f"'part' ('{part_label}'), "
            f"'series_title' ('{template_ep['series_title']}'), "
            f"'segments' (list of 4 segments, each having: "
            f"'layout' ['presenter_full', 'split_screen', 'pip_broll', 'presenter_full'], "
            f"'narration' [engaging spoken script in {'Arabic' if lang == 'ar' else 'English'}, 22-30 words], "
            f"'caption' [short punchy subtitle in {'Arabic' if lang == 'ar' else 'English'}, max 8 words], "
            f"'broll_query' [3-4 English keywords for real-world documentary footage search, e.g. 'AI server room' or 'Wall Street skyscraper'], "
            f"'broll_prompt' [detailed English FLUX image generation prompt for the visual being explained], "
            f"'stat_badge' [short upper-case badge text like 'AI EMPIRE • PART {part_num}'])."
        )
        for model_name in ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={gemini_key}"
                payload = json.dumps({
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.85, "responseMimeType": "application/json"}
                }).encode("utf-8")
                req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=25) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                raw_text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                if raw_text.startswith("```"):
                    raw_text = raw_text.split("```")[1]
                    if raw_text.startswith("json"):
                        raw_text = raw_text[4:]
                parsed = json.loads(raw_text.strip())
                if isinstance(parsed.get("segments"), list) and len(parsed["segments"]) >= 3:
                    print(f"[{channel_key}] Fresh script generated via {model_name}: {parsed.get('title')}")
                    return parsed
            except Exception as e:
                print(f"[{channel_key}] {model_name} script notice: {e}")

    ep_copy = json.loads(json.dumps(template_ep))
    print(f"[{channel_key}] Loaded episodic script: {ep_copy['title']}")
    return ep_copy


# ==============================================================================
# 4. NEURAL WAV2LIP ONNX ENGINE + REAL MOVING PRESENTER VIDEO FETCHER
# ==============================================================================

WAV2LIP_ONNX_URLS = [
    "https://huggingface.co/bluefoxcreation/Wav2lip-Onnx/resolve/main/wav2lip_gan.onnx",
    "https://huggingface.co/bluefoxcreation/Wav2lip-Onnx/resolve/main/wav2lip.onnx",
    "https://huggingface.co/numz/wav2lip_studio/resolve/main/Wav2lip/wav2lip_gan.onnx",
]

_WAV2LIP_SESSION = None
_WAV2LIP_CHECKED = False


def get_wav2lip_onnx_session(cache_dir: Path):
    """Downloads `wav2lip_gan.onnx` (145MB) once and initializes an ONNXRuntime CPU session."""
    global _WAV2LIP_SESSION, _WAV2LIP_CHECKED
    if _WAV2LIP_CHECKED:
        return _WAV2LIP_SESSION
    _WAV2LIP_CHECKED = True

    if os.environ.get("DISABLE_WAV2LIP_ONNX", "0") == "1":
        return None

    try:
        import onnxruntime as ort
    except Exception as e:
        print(f"  [Wav2Lip-ONNX] onnxruntime not installed ({e}); using 2D Facial Mesh Warper.")
        return None

    cache_dir.mkdir(parents=True, exist_ok=True)
    model_path = cache_dir / "wav2lip_gan.onnx"

    if not model_path.exists() or model_path.stat().st_size < 50_000_000:
        for url in WAV2LIP_ONNX_URLS:
            try:
                print(f"  [Wav2Lip-ONNX] Downloading neural lip-sync model from {url}...")
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=60) as resp, open(model_path, "wb") as out_f:
                    shutil.copyfileobj(resp, out_f)
                if model_path.exists() and model_path.stat().st_size > 50_000_000:
                    print(f"  [Wav2Lip-ONNX] Model downloaded ({model_path.stat().st_size // (1024*1024)} MB)")
                    break
            except Exception as e:
                print(f"  [Wav2Lip-ONNX] Download notice ({url}): {e}")

    if model_path.exists() and model_path.stat().st_size > 50_000_000:
        try:
            sess_opts = ort.SessionOptions()
            sess_opts.intra_op_num_threads = 4
            _WAV2LIP_SESSION = ort.InferenceSession(
                str(model_path), sess_options=sess_opts, providers=["CPUExecutionProvider"]
            )
            print("  [Wav2Lip-ONNX] Neural CPU Lip-Sync Session Ready!")
            return _WAV2LIP_SESSION
        except Exception as e:
            print(f"  [Wav2Lip-ONNX] Session init notice: {e}")
    return None


def build_mel_basis(sr: int = 16000, n_fft: int = 800, n_mels: int = 80, fmin: float = 55.0, fmax: float = 7600.0) -> np.ndarray:
    def hz_to_mel(f):
        return 2595.0 * np.log10(1.0 + f / 700.0)
    def mel_to_hz(m):
        return 700.0 * (10.0 ** (m / 2595.0) - 1.0)
    mels = np.linspace(hz_to_mel(fmin), hz_to_mel(fmax), n_mels + 2)
    hz = mel_to_hz(mels)
    bins = np.floor((n_fft + 1) * hz / sr).astype(int)
    fb = np.zeros((n_mels, n_fft // 2 + 1), dtype=np.float32)
    for m in range(1, n_mels + 1):
        f_m_minus, f_m, f_m_plus = bins[m - 1], bins[m], bins[m + 1]
        for k in range(f_m_minus, f_m):
            fb[m - 1, k] = (k - f_m_minus) / max(1, f_m - f_m_minus)
        for k in range(f_m, f_m_plus):
            fb[m - 1, k] = (f_m_plus - k) / max(1, f_m_plus - f_m)
    return fb


def wav_to_wav2lip_mel_chunks(wav_path: Path, fps: int = 30) -> list[np.ndarray]:
    """Converts a WAV file into standard Wav2Lip (80, 16) mel-spectrogram chunks aligned to `fps`."""
    tmp_16k = wav_path.parent / f"{wav_path.stem}_16k.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(wav_path), "-ac", "1", "-ar", "16000", str(tmp_16k)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    with wave.open(str(tmp_16k), "rb") as wf:
        raw = wf.readframes(wf.getnframes())
    wav_16k = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

    # Pre-emphasis (0.97)
    x = signal.lfilter([1.0, -0.97], [1.0], wav_16k).astype(np.float32)
    # STFT (n_fft=800, hop=200)
    _, _, Zxx = signal.stft(
        x, fs=16000, window="hann", nperseg=800, noverlap=600, nfft=800, boundary="zeros", padded=True
    )
    mag = np.abs(Zxx)
    mel_basis = build_mel_basis()
    mel = np.dot(mel_basis, mag)
    min_level = np.exp(-100.0 / 20.0 * np.log(10.0))
    S = 20.0 * np.log10(np.maximum(min_level, mel)) - 20.0
    mel_norm = np.clip((2.0 * 4.0) * ((S + 100.0) / 100.0) - 4.0, -4.0, 4.0)

    mel_chunks = []
    mel_idx_multiplier = 80.0 / float(fps)
    i = 0
    while True:
        start_idx = int(i * mel_idx_multiplier)
        if start_idx + 16 > mel_norm.shape[1]:
            mel_chunks.append(mel_norm[:, mel_norm.shape[1] - 16 :])
            break
        mel_chunks.append(mel_norm[:, start_idx : start_idx + 16])
        i += 1
    return mel_chunks


def detect_face_bbox(frame_rgb: np.ndarray) -> tuple[int, int, int, int]:
    """Detects the human presenter's face bounding box (x1, y1, x2, y2) on an RGB frame."""
    H, W, _ = frame_rgb.shape
    r = frame_rgb[:, :, 0].astype(np.float32)
    g = frame_rgb[:, :, 1].astype(np.float32)
    b = frame_rgb[:, :, 2].astype(np.float32)
    cr = 128.0 + 0.5 * r - 0.418688 * g - 0.081312 * b
    cb = 128.0 - 0.168736 * r - 0.331264 * g + 0.5 * b
    skin = (cr > 134) & (cr < 178) & (cb > 78) & (cb < 133)
    skin[: int(H * 0.08), :] = False
    skin[int(H * 0.82) :, :] = False
    skin[:, : int(W * 0.12)] = False
    skin[:, int(W * 0.88) :] = False
    ys, xs = np.where(skin)
    if len(xs) > 1200:
        x1, x2 = int(np.percentile(xs, 6)), int(np.percentile(xs, 94))
        y1, y2 = int(np.percentile(ys, 5)), int(np.percentile(ys, 94))
        # Ensure square-ish face box covering mouth and chin
        fw = max(160, x2 - x1)
        fh = max(180, y2 - y1)
        cx = (x1 + x2) // 2
        x1 = max(0, cx - int(fw * 0.55))
        x2 = min(W, cx + int(fw * 0.55))
        y1 = max(0, y1)
        y2 = min(H, y1 + int(fh * 1.05))
        return x1, y1, x2, y2
    # Fallback centered studio face box
    return int(W * 0.25), int(H * 0.16), int(W * 0.75), int(H * 0.68)


def apply_wav2lip_onnx_to_presenter_frames(
    presenter_frames: list[np.ndarray],
    wav_path: Path,
    cache_dir: Path,
    fps: int = 30,
) -> list[np.ndarray] | None:
    """
    Runs true Neural Lip-Sync (`wav2lip_gan.onnx`) on the moving human presenter video frames
    so the presenter's real lips, teeth, and jaw articulate the exact speech in `wav_path`.
    """
    session = get_wav2lip_onnx_session(cache_dir)
    if session is None or not presenter_frames:
        return None

    try:
        mel_chunks = wav_to_wav2lip_mel_chunks(wav_path, fps=fps)
        num_frames = len(presenter_frames)
        # Detect face bbox smoothly across presenter frames
        x1, y1, x2, y2 = detect_face_bbox(presenter_frames[0])
        fw, fh = max(32, x2 - x1), max(32, y2 - y1)

        # Feather blend mask for pasting the 96x96 neural mouth/face back seamlessly
        yy, xx = np.mgrid[0:fh, 0:fw].astype(np.float32)
        nx = (xx - fw * 0.5) / (fw * 0.48 + 1e-5)
        ny = (yy - fh * 0.55) / (fh * 0.44 + 1e-5)
        blend_mask = np.clip(1.0 - (nx ** 2 + ny ** 2), 0.0, 1.0) ** 1.5
        # Only blend the lower 62% of the face box (nose tip, lips, jaw) so eyes remain 100% ultra-sharp
        top_cut = np.clip((yy - fh * 0.36) / (fh * 0.15 + 1e-5), 0.0, 1.0)
        blend_mask = (blend_mask * top_cut)[:, :, None]

        in_names = [inp.name for inp in session.get_inputs()]
        mel_in_name = in_names[0]
        vid_in_name = in_names[1]

        out_frames = []
        batch_size = 16
        for b_start in range(0, num_frames, batch_size):
            b_end = min(num_frames, b_start + batch_size)
            img_batch = []
            mel_batch = []
            for idx in range(b_start, b_end):
                f_rgb = presenter_frames[idx]
                face_crop = f_rgb[y1:y2, x1:x2]
                face_96 = np.array(Image.fromarray(face_crop).resize((96, 96), Image.Resampling.BILINEAR))
                # Wav2Lip uses BGR normalized to [0..1], with lower half masked concatenated with full face -> (6, 96, 96)
                face_bgr = face_96[:, :, ::-1].astype(np.float32) / 255.0
                masked_bgr = face_bgr.copy()
                masked_bgr[48:, :, :] = 0.0
                concat_bgr = np.concatenate([masked_bgr, face_bgr], axis=2)  # (96, 96, 6)
                img_batch.append(np.transpose(concat_bgr, (2, 0, 1)))        # (6, 96, 96)

                m_chunk = mel_chunks[min(idx, len(mel_chunks) - 1)]
                mel_batch.append(m_chunk[None, :, :])                        # (1, 80, 16)

            img_tensor = np.array(img_batch, dtype=np.float32)
            mel_tensor = np.array(mel_batch, dtype=np.float32)

            preds = session.run(None, {mel_in_name: mel_tensor, vid_in_name: img_tensor})[0]
            # preds shape: (B, 3, 96, 96) in BGR [0..1]
            for bi, pred in enumerate(preds):
                pred_bgr = np.transpose(pred, (1, 2, 0))
                pred_rgb = np.clip(pred_bgr[:, :, ::-1] * 255.0, 0, 255).astype(np.uint8)
                pred_resized = np.array(
                    Image.fromarray(pred_rgb).resize((fw, fh), Image.Resampling.BILINEAR)
                ).astype(np.float32)

                orig_frame = presenter_frames[b_start + bi].copy()
                orig_patch = orig_frame[y1:y2, x1:x2].astype(np.float32)
                orig_frame[y1:y2, x1:x2] = (
                    orig_patch * (1.0 - blend_mask) + pred_resized * blend_mask
                ).astype(np.uint8)
                out_frames.append(orig_frame)

        print(f"  [Wav2Lip-ONNX] Successfully lip-synced {len(out_frames)} presenter frames!")
        return out_frames
    except Exception as e:
        print(f"  [Wav2Lip-ONNX] Inference notice ({e}); falling back to 2D Facial Mesh Animator.")
        return None


# ==============================================================================
# 5. REAL MOVING PRESENTER VIDEO FETCHER & 2D FACIAL MESH ANIMATOR
# ==============================================================================

def _create_gradio_client(space_id: str):
    from gradio_client import Client
    hf_token = os.environ.get("HF_TOKEN", "").strip()
    if hf_token:
        os.environ["HF_TOKEN"] = hf_token
    return Client(space_id)


def _extract_file_from_gradio_result(res):
    if isinstance(res, str) and os.path.exists(res):
        return res
    if isinstance(res, dict):
        for k in ("video", "path", "url", "image", "value"):
            v = res.get(k)
            if isinstance(v, str) and os.path.exists(v):
                return v
            if isinstance(v, dict) and isinstance(v.get("path"), str) and os.path.exists(v["path"]):
                return v["path"]
    if isinstance(res, (list, tuple)):
        for item in res:
            found = _extract_file_from_gradio_result(item)
            if found:
                return found
    return None


def generate_flux_image_zerogpu(prompt: str, out_path: Path, width: int = 768, height: int = 1024) -> bool:
    for space_id, api_name in [("black-forest-labs/FLUX.1-schnell", "/infer"), ("multimodalart/FLUX.1-merged", "/infer")]:
        try:
            client = _create_gradio_client(space_id)
            res = client.predict(prompt, random.randint(1, 999999), True, width, height, 4, api_name=api_name)
            fpath = _extract_file_from_gradio_result(res)
            if fpath and os.path.exists(fpath):
                Image.open(fpath).convert("RGB").save(out_path, quality=95)
                return True
        except Exception as e:
            print(f"  [FLUX ZeroGPU] {space_id} notice: {e}")
    return False


def fetch_pexels_video(query: str, out_mp4: Path, orientation: str = "portrait") -> bool:
    """Downloads a real HD video clip from Pexels Video API if `PEXELS_API_KEY` is set."""
    pexels_key = os.environ.get("PEXELS_API_KEY", "").strip()
    if not pexels_key:
        return False
    try:
        q_enc = urllib.parse.quote(query)
        url = f"https://api.pexels.com/videos/search?query={q_enc}&per_page=6&orientation={orientation}"
        req = urllib.request.Request(url, headers={"Authorization": pexels_key, "User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        videos = data.get("videos", [])
        for v in videos:
            for vf in v.get("video_files", []):
                link = vf.get("link", "")
                w = vf.get("width", 0)
                if link and w >= 540:
                    with urllib.request.urlopen(urllib.request.Request(link, headers={"User-Agent": "Mozilla/5.0"}), timeout=20) as r2:
                        raw = r2.read()
                    if len(raw) > 50_000:
                        out_mp4.write_bytes(raw)
                        return True
    except Exception as e:
        print(f"  [Pexels Video] Notice ({query}): {e}")
    return False


def fetch_wikimedia_visual(query: str, out_path: Path, prefer_video: bool = False) -> str | None:
    headers = {"User-Agent": "EmpireMediaBot/11.0 (https://github.com/yoyomado2312-byte/empire-cloud)"}
    try:
        ft = "video" if prefer_video else "bitmap"
        q_encoded = urllib.parse.quote(f"{query} filetype:{ft}")
        api_url = (
            f"https://commons.wikimedia.org/w/api.php?action=query&generator=search"
            f"&gsrsearch={q_encoded}&gsrnamespace=6&gsrlimit=8&prop=imageinfo&iiprop=url|size|mime&format=json"
        )
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        pages = data.get("query", {}).get("pages", {})
        candidates = []
        for _, p in pages.items():
            ii = (p.get("imageinfo") or [{}])[0]
            url = ii.get("url", "")
            mime = ii.get("mime", "")
            w = ii.get("width", 0)
            h = ii.get("height", 0)
            if not url:
                continue
            if prefer_video and ("video/" in mime or url.endswith((".webm", ".mp4", ".ogv"))):
                candidates.append(url)
            elif not prefer_video and ("image/jpeg" in mime or "image/png" in mime) and w >= 500 and h >= 400:
                candidates.append(url)
        if candidates:
            chosen = random.choice(candidates[:4])
            req2 = urllib.request.Request(chosen, headers=headers)
            with urllib.request.urlopen(req2, timeout=18) as r2:
                raw = r2.read()
            if len(raw) > 10_000:
                out_path.write_bytes(raw)
                return str(out_path)
    except Exception as e:
        print(f"  [Wikimedia] Search notice ({query}): {e}")
    return None


def get_moving_presenter_base_frames(
    cfg: dict,
    work_dir: Path,
    num_frames: int,
    target_w: int = 900,
    target_h: int = 1100,
) -> list[np.ndarray]:
    """
    Guarantees a sequence of `num_frames` REAL moving human presenter frames (`target_w x target_h`):
    1. Tries downloading a real driving/presenter video from Hugging Face CDN (`LivePortrait` / `Wav2Lip`)
       or Pexels Video API (`podcast host talking studio`) so the presenter's head, eyes, and expressions
       move naturally on every single frame.
    2. If a static AI portrait is generated/downloaded (via FLUX ZeroGPU or HuggingFace/Unsplash CDN),
       applies continuous 3D head-pose oscillation, natural eye blinking every 3.2 seconds, eyebrow
       expression lift, and shoulder breathing motion so the base frames are NEVER static!
    """
    vid_path = work_dir / "presenter_base_video.mp4"
    ep_idx = get_episode_index("presenter")

    # 1. Try Pexels real studio host video first if API key is present
    if not vid_path.exists():
        fetch_pexels_video("podcast host talking camera studio", vid_path, orientation="portrait")

    # 2. Try curated Hugging Face CDN real talking-head driving videos
    if not vid_path.exists() or vid_path.stat().st_size < 25_000:
        v_urls = cfg.get("presenter_video_urls", [])
        for i in range(len(v_urls)):
            u = v_urls[(ep_idx + i) % len(v_urls)]
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=15) as resp:
                    raw = resp.read()
                if len(raw) > 25_000:
                    vid_path.write_bytes(raw)
                    print(f"  [Presenter Video] Downloaded real moving human presenter video from HF CDN ({len(raw)//1024} KB)")
                    break
            except Exception as e:
                print(f"  [Presenter Video] HF CDN notice ({u}): {e}")

    # If we have a real video clip, extract 30fps frames and loop smoothly (ping-pong)
    if vid_path.exists() and vid_path.stat().st_size >= 25_000:
        frames_dir = work_dir / "pres_vid_frames"
        frames_dir.mkdir(exist_ok=True)
        try:
            subprocess.run(
                [
                    "ffmpeg", "-y", "-i", str(vid_path),
                    "-vf", f"scale={target_w}:{target_h}:force_original_aspect_ratio=increase,crop={target_w}:{target_h},fps=30",
                    "-frames:v", "180",
                    str(frames_dir / "pf_%04d.jpg"),
                ],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=25
            )
            extracted = sorted(frames_dir.glob("pf_*.jpg"))
            if len(extracted) >= 15:
                base_list = [np.array(Image.open(p).convert("RGB")) for p in extracted]
                # Ping-pong loop (forward + reverse) so head motion is 100% seamless with zero jump cuts
                ping_pong = base_list + base_list[-2:0:-1]
                out = []
                while len(out) < num_frames:
                    out.extend(ping_pong)
                return out[:num_frames]
        except Exception as e:
            print(f"  [Presenter Video] Decode notice: {e}")

    # 3. Otherwise obtain high-res AI studio presenter portrait and apply continuous facial/head motion
    portrait_path = work_dir / "presenter_portrait.jpg"
    if not portrait_path.exists() or portrait_path.stat().st_size < 12_000:
        if not generate_flux_image_zerogpu(cfg["presenter_prompt"], portrait_path, width=768, height=1024):
            urls = cfg.get("presenter_fallback_urls", [])
            for i in range(len(urls)):
                u = urls[(ep_idx + i) % len(urls)]
                try:
                    with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=12) as resp:
                        raw = resp.read()
                    if len(raw) > 12_000:
                        portrait_path.write_bytes(raw)
                        Image.open(portrait_path).convert("RGB").save(portrait_path, quality=95)
                        break
                except Exception:
                    pass

    if portrait_path.exists() and portrait_path.stat().st_size >= 12_000:
        im = Image.open(portrait_path).convert("RGB")
    else:
        # High-detail studio presenter illustration if completely offline
        im = Image.new("RGB", (target_w, target_h), (20, 26, 44))
        d = ImageDraw.Draw(im, "RGBA")
        d.ellipse([60, 80, 340, 360], fill=(0, 180, 220, 75))
        d.ellipse([580, 120, 860, 400], fill=(255, 160, 50, 75))
        d.polygon([(140, 1100), (260, 720), (640, 720), (760, 1100)], fill=(32, 38, 52, 255))
        d.rectangle([400, 590, 500, 745], fill=(210, 162, 130, 255))
        d.ellipse([295, 230, 605, 650], fill=(224, 176, 142, 255))
        d.pieslice([290, 210, 610, 480], start=180, end=360, fill=(28, 24, 22, 255))
        for ex in (385, 515):
            d.ellipse([ex - 28, 410, ex + 28, 438], fill=(250, 250, 252, 255))
            d.ellipse([ex - 12, 412, ex + 12, 436], fill=(42, 28, 18, 255))
        d.rounded_rectangle([405, 548, 495, 568], radius=9, fill=(175, 95, 92, 255))

    # Resize slightly larger to allow smooth natural head/camera motion + affine rotation
    over_w, over_h = int(target_w * 1.12), int(target_h * 1.12)
    im_over = im.resize((over_w, over_h), Image.Resampling.LANCZOS)
    arr_over = np.array(im_over)

    frames = []
    for f_idx in range(num_frames):
        t = f_idx / 30.0
        # Natural head tilt + nodding + breathing motion
        angle = 1.6 * math.sin(t * 2.1) + 0.7 * math.cos(t * 3.4)
        rot_im = im_over.rotate(angle, resample=Image.Resampling.BILINEAR, expand=False)
        dx = int((over_w - target_w) * 0.5 + 22 * math.sin(t * 1.8))
        dy = int((over_h - target_h) * 0.5 + 14 * math.cos(t * 2.6))
        dx = max(0, min(over_w - target_w, dx))
        dy = max(0, min(over_h - target_h, dy))
        cropped = np.array(rot_im)[dy : dy + target_h, dx : dx + target_w].copy()
        frames.append(cropped)
    return frames


def animate_presenter_mouth_and_eyes_2d(
    presenter_frames: list[np.ndarray],
    env: np.ndarray,
    fps: int = 30,
) -> list[np.ndarray]:
    """
    Animates the human presenter's jaw, upper/lower lips, inner oral cavity, teeth, eyebrow gestures,
    and natural eye blinks synchronized to the voice amplitude `env`.
    """
    if not presenter_frames:
        return []
    H, W, _ = presenter_frames[0].shape
    x1, y1, x2, y2 = detect_face_bbox(presenter_frames[0])
    fw, fh = max(160, x2 - x1), max(200, y2 - y1)
    mx = (x1 + x2) // 2
    my = int(y1 + fh * 0.74)
    mouth_w = int(fw * 0.38)
    jaw_h = int(fh * 0.28)
    eye_y = int(y1 + fh * 0.36)
    eye_lx = int(mx - fw * 0.20)
    eye_rx = int(mx + fw * 0.20)

    out = []
    for f_idx, base_f in enumerate(presenter_frames):
        t_sec = f_idx / float(fps)
        amp = float(env[min(f_idx, len(env) - 1)])
        frame = base_f.copy()

        # Multi-frequency syllable articulation (jaw + lip width modulation)
        syl_open = 0.60 + 0.40 * math.sin(t_sec * 26.0)
        syl_wide = 0.85 + 0.25 * math.cos(t_sec * 19.0)
        open_amt = float(np.clip(amp * syl_open * 1.25, 0.0, 1.0))
        jaw_shift = int(round(open_amt * max(16, int(jaw_h * 0.26))))

        if jaw_shift > 1:
            jx0 = max(0, mx - int(mouth_w * 0.95))
            jx1 = min(W, mx + int(mouth_w * 0.95))
            jy0 = max(0, my)
            jy1 = min(H - jaw_shift - 1, my + jaw_h)
            if jy1 > jy0 and jx1 > jx0:
                sub = base_f[jy0:jy1, jx0:jx1].astype(np.float32)
                shifted = base_f[jy0 - jaw_shift : jy1 - jaw_shift, jx0:jx1].astype(np.float32)
                sh, sw, _ = sub.shape
                yy, xx = np.mgrid[0:sh, 0:sw].astype(np.float32)
                nx = (xx - sw * 0.5) / (sw * 0.5 + 1e-5)
                ny = (yy - sh * 0.35) / (sh * 0.65 + 1e-5)
                mask = (np.clip(1.0 - (nx ** 2 + ny ** 2), 0.0, 1.0) ** 1.35)[:, :, None]
                frame[jy0:jy1, jx0:jx1] = (sub * (1.0 - mask) + shifted * mask).astype(np.uint8)

                # Inner mouth opening, upper teeth row, and lower tongue/oral shading
                lip_rx = max(16, int(mouth_w * 0.44 * syl_wide))
                lip_ry = max(4, int(jaw_shift * 0.82))
                ly0 = max(0, my - int(lip_ry * 0.45))
                ly1 = min(H, my + int(lip_ry * 1.15))
                lx0 = max(0, mx - lip_rx)
                lx1 = min(W, mx + lip_rx)
                if ly1 > ly0 and lx1 > lx0:
                    oy, ox = np.mgrid[ly0:ly1, lx0:lx1].astype(np.float32)
                    elli = ((ox - mx) / (lip_rx + 1e-5)) ** 2 + ((oy - (my + lip_ry * 0.25)) / (lip_ry + 1e-5)) ** 2
                    inside = elli <= 1.0
                    lip_border = (elli > 0.82) & (elli <= 1.18)
                    teeth_zone = (oy < (my + lip_ry * 0.05)) & (elli <= 0.78)
                    tongue_zone = (oy > (my + lip_ry * 0.42)) & (elli <= 0.68)

                    patch = frame[ly0:ly1, lx0:lx1].astype(np.float32)
                    patch[inside] = patch[inside] * 0.15 + np.array([32.0, 14.0, 18.0]) * 0.85
                    patch[tongue_zone] = patch[tongue_zone] * 0.25 + np.array([145.0, 58.0, 62.0]) * 0.75
                    patch[teeth_zone] = patch[teeth_zone] * 0.25 + np.array([238.0, 235.0, 228.0]) * 0.75
                    patch[lip_border] = patch[lip_border] * 0.45 + np.array([162.0, 78.0, 76.0]) * 0.55
                    frame[ly0:ly1, lx0:lx1] = patch.astype(np.uint8)

        # Natural periodic eye blink every ~3.1 seconds (lasts 0.13s)
        blink_phase = (t_sec % 3.1)
        if 1.45 <= blink_phase <= 1.58:
            ew, eh = int(fw * 0.11), max(4, int(fh * 0.025))
            for ex in (eye_lx, eye_rx):
                ex0, ex1 = max(0, ex - ew), min(W, ex + ew)
                ey0, ey1 = max(0, eye_y - eh), min(H, eye_y + eh)
                if ey1 > ey0 and ex1 > ex0 and ey0 >= eh * 2:
                    # Copy upper eyelid skin tone down over eye
                    frame[ey0:ey1, ex0:ex1] = frame[ey0 - eh * 2 : ey1 - eh * 2, ex0:ex1]

        out.append(frame)
    return out


# ==============================================================================
# 6. DYNAMIC B-ROLL VISUAL ENGINE (MOVING VIDEO CLIPS + 60FPS ANIMATED CHARTS)
# ==============================================================================

def render_animated_broll_frames(
    seg: dict,
    seg_idx: int,
    lang: str,
    work_dir: Path,
    num_frames: int,
    target_w: int,
    target_h: int,
) -> list[np.ndarray]:
    """
    Guarantees 100% moving B-roll frames (`target_w x target_h`):
    1. Tries Pexels Video API (`fetch_pexels_video`) and Wikimedia Commons Video Search (`prefer_video=True`).
    2. Tries FLUX.1-schnell ZeroGPU image generation or Wikimedia Commons photo search, then animates it with:
       - Dynamic camera zoom/pan across the image
       - Animated rising 3D bar charts & glowing data line that grow frame-by-frame (`prog = f_idx / num_frames`)
       - Floating light particles so the visual board is 100% alive!
    """
    broll_query = seg.get("broll_query", "Artificial intelligence technology")
    broll_prompt = seg.get("broll_prompt", broll_query)
    caption = seg.get("caption", "")
    badge = seg.get("stat_badge", f"PART {seg_idx + 1}")

    vid_candidate = work_dir / f"broll_vid_{seg_idx}.mp4"
    got_vid = fetch_pexels_video(broll_query, vid_candidate, orientation="portrait")
    if not got_vid:
        wm_v = fetch_wikimedia_visual(broll_query, vid_candidate, prefer_video=True)
        got_vid = bool(wm_v and vid_candidate.exists() and vid_candidate.stat().st_size > 20_000)

    if got_vid and vid_candidate.exists():
        raw_frames_dir = work_dir / f"broll_frames_{seg_idx}"
        raw_frames_dir.mkdir(exist_ok=True)
        try:
            subprocess.run(
                [
                    "ffmpeg", "-y", "-i", str(vid_candidate),
                    "-vf", f"scale={target_w}:{target_h}:force_original_aspect_ratio=increase,crop={target_w}:{target_h},fps=30",
                    "-frames:v", str(min(num_frames, 210)),
                    str(raw_frames_dir / "f_%04d.jpg"),
                ],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=25
            )
            extracted = sorted(raw_frames_dir.glob("f_*.jpg"))
            if len(extracted) >= 12:
                base_v = [np.array(Image.open(p).convert("RGB")) for p in extracted]
                ping_pong = base_v + base_v[-2:0:-1]
                frames = []
                while len(frames) < num_frames:
                    frames.extend(ping_pong)
                return frames[:num_frames]
        except Exception as e:
            print(f"  [B-Roll Video] Decode notice: {e}")

    # Load or generate high-res background image
    img_candidate = work_dir / f"broll_img_{seg_idx}.jpg"
    got_img = generate_flux_image_zerogpu(broll_prompt, img_candidate, width=768, height=768)
    if not got_img:
        wm_img = fetch_wikimedia_visual(broll_query, img_candidate, prefer_video=False)
        got_img = bool(wm_img and img_candidate.exists() and img_candidate.stat().st_size > 10_000)

    over_w, over_h = int(target_w * 1.25), int(target_h * 1.25)
    if got_img and img_candidate.exists():
        try:
            bg_im = Image.open(img_candidate).convert("RGB").resize((over_w, over_h), Image.Resampling.LANCZOS)
        except Exception:
            got_img = False

    if not got_img:
        # Rich cyber-studio backdrop
        y_grid, x_grid = np.mgrid[0:over_h, 0:over_w].astype(np.float32)
        palettes = [
            ((14, 32, 68), (0, 200, 235)),
            ((32, 16, 64), (185, 80, 255)),
            ((12, 46, 40), (16, 225, 145)),
            ((52, 18, 34), (255, 85, 125)),
        ]
        c_bg, c_pri = palettes[seg_idx % len(palettes)]
        dist = np.sqrt((x_grid - over_w * 0.5) ** 2 + (y_grid - over_h * 0.45) ** 2) / (over_w * 0.7)
        glow = np.clip(1.0 - dist, 0.0, 1.0) ** 1.5
        arr = np.zeros((over_h, over_w, 3), dtype=np.float32)
        for ch in range(3):
            arr[:, :, ch] = c_bg[ch] * (1.0 - 0.6 * glow) + c_pri[ch] * (0.6 * glow)
        bg_im = Image.fromarray(arr.astype(np.uint8), "RGB")

    bg_arr = np.array(bg_im)
    f_badge = get_font(32, bold=True)
    f_num = get_font(28, bold=True)
    bar_targets = [0.32, 0.48, 0.44, 0.68, 0.84, 0.96]

    frames = []
    for f_idx in range(num_frames):
        prog = f_idx / float(max(1, num_frames - 1))
        # Dynamic smooth camera pan & zoom
        smooth_p = 0.5 - 0.5 * math.cos(prog * math.pi)
        cw = int(target_w + (over_w - target_w) * (1.0 - 0.75 * smooth_p))
        ch_crop = int(target_h + (over_h - target_h) * (1.0 - 0.75 * smooth_p))
        x0 = int((over_w - cw) * (0.15 + 0.7 * smooth_p))
        y0 = int((over_h - ch_crop) * (0.15 + 0.7 * smooth_p))

        frame_im = Image.fromarray(bg_arr[y0 : y0 + ch_crop, x0 : x0 + cw]).resize(
            (target_w, target_h), Image.Resampling.BILINEAR
        )
        draw = ImageDraw.Draw(frame_im, "RGBA")

        # Animated growing HUD chart overlay so the viewer sees live data animation
        anim_growth = min(1.0, prog * 1.45)
        c_left = int(target_w * 0.12)
        c_bottom = int(target_h * 0.80)
        c_w = int(target_w * 0.76)
        c_h = int(target_h * 0.42)

        draw.rounded_rectangle(
            [c_left - 25, c_bottom - c_h - 45, c_left + c_w + 25, c_bottom + 35],
            radius=24,
            fill=(8, 14, 28, 175),
            outline=(0, 220, 255, 210),
            width=3,
        )

        nb = len(bar_targets)
        bw = max(36, int(c_w * 0.10))
        gap = (c_w - nb * bw) // (nb + 1)
        pts = []
        for i, bt in enumerate(bar_targets):
            # Each bar grows dynamically with a slight wave pulse
            pulse = 0.03 * math.sin(prog * 12.0 + i)
            cur_h = max(0.05, min(1.0, bt * anim_growth + pulse))
            bx = c_left + gap + i * (bw + gap)
            by = int(c_bottom - cur_h * c_h)
            col = (255, 200, 45, 235) if i == nb - 1 else (0, 215, 255, 215)
            draw.rounded_rectangle([bx, by, bx + bw, c_bottom], radius=10, fill=col)
            pts.append((bx + bw // 2, by - 14))

        if len(pts) > 1:
            draw.line(pts, fill=(255, 255, 255, 245), width=5)
            for px, py in pts:
                draw.ellipse([px - 9, py - 9, px + 9, py + 9], fill=(255, 205, 50, 255), outline=(255, 255, 255, 255), width=2)

        # Live counter badge in top of chart
        pct_val = int(round(anim_growth * 400))
        draw.text((c_left + c_w // 2, c_bottom - c_h - 18), f"{badge}  •  +{pct_val}%", font=f_badge, fill=(255, 215, 60, 255), anchor="mm")

        frames.append(np.array(frame_im))
    return frames


# ==============================================================================
# 7. AUDIO ENVELOPE, TTS & FULL SEGMENT RENDERER
# ==============================================================================

def compute_audio_envelope(wav_path: Path, fps: int = 30) -> tuple[np.ndarray, float]:
    with wave.open(str(wav_path), "rb") as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        raw = wf.readframes(n_frames)

    duration = max(1.5, n_frames / float(framerate))
    if sampwidth == 2:
        samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32)
        if n_channels > 1:
            samples = samples.reshape(-1, n_channels).mean(axis=1)
        samples /= 32768.0
    else:
        samples = np.zeros(int(duration * framerate), dtype=np.float32)

    total_video_frames = max(int(math.ceil(duration * fps)), 1)
    spc = max(1, len(samples) // total_video_frames)
    env = np.zeros(total_video_frames, dtype=np.float32)
    for i in range(total_video_frames):
        chunk = samples[i * spc : (i + 1) * spc]
        if len(chunk) > 0:
            env[i] = float(np.sqrt(np.mean(chunk ** 2)))

    p95 = float(np.percentile(env, 95)) if len(env) > 0 else 0.1
    if p95 > 1e-4:
        env = np.clip(env / p95, 0.0, 1.0)
    kernel = np.array([0.25, 0.5, 0.25], dtype=np.float32)
    env = np.convolve(env, kernel, mode="same")
    return env, duration


def synthesize_voiceover_segment(text: str, voice: str, out_mp3: Path, out_wav: Path) -> float:
    try:
        cmd = [
            sys.executable, "-m", "edge_tts",
            "--voice", voice,
            "--rate=+8%",
            "--text", text,
            "--write-media", str(out_mp3),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=35)
    except Exception as e:
        print(f"  [TTS] edge-tts fallback notice ({e}), using gTTS...")
        from gtts import gTTS
        lang_code = "ar" if voice.startswith("ar") else "en"
        gTTS(text=text, lang=lang_code, slow=False).save(str(out_mp3))

    subprocess.run(
        ["ffmpeg", "-y", "-i", str(out_mp3), "-ac", "1", "-ar", "24000", str(out_wav)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    _, dur = compute_audio_envelope(out_wav)
    return dur


def build_caption_overlay_rgba(
    W: int,
    H: int,
    part_label: str,
    series_title: str,
    caption_text: str,
    stat_badge: str,
    lang: str,
    layout_mode: str,
) -> tuple[np.ndarray, np.ndarray]:
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay, "RGBA")

    f_top = get_font(34, bold=True)
    f_badge = get_font(30, bold=True)
    f_cap = get_font(44, bold=True)

    header_raw = f"{part_label}  •  {series_title}"
    header_shaped = shape_text(header_raw, lang)
    draw.rounded_rectangle([65, 58, W - 65, 138], radius=40, fill=(10, 14, 26, 215), outline=(0, 215, 255, 230), width=3)
    draw.text((W // 2, 98), header_shaped, font=f_top, fill=(255, 255, 255, 255), anchor="mm")

    if layout_mode == "split_screen":
        draw.rectangle([0, 954, W, 966], fill=(0, 215, 255, 245))
        draw.rounded_rectangle([W // 2 - 210, 932, W // 2 + 210, 988], radius=28, fill=(12, 18, 34, 245), outline=(255, 195, 45, 255), width=3)
        draw.text((W // 2, 960), stat_badge, font=f_badge, fill=(255, 205, 55, 255), anchor="mm")

    cap_y0, cap_y1 = 1560, 1765
    draw.rounded_rectangle(
        [55, cap_y0, W - 55, cap_y1],
        radius=30,
        fill=(8, 12, 24, 228),
        outline=(255, 195, 45, 235),
        width=4,
    )

    words = caption_text.split()
    if len(words) > 5:
        mid = len(words) // 2
        line1 = shape_text(" ".join(words[:mid]), lang)
        line2 = shape_text(" ".join(words[mid:]), lang)
        draw.text((W // 2, cap_y0 + 68), line1, font=f_cap, fill=(255, 255, 255, 255), anchor="mm")
        draw.text((W // 2, cap_y0 + 135), line2, font=f_cap, fill=(255, 215, 65, 255), anchor="mm")
    else:
        line1 = shape_text(caption_text, lang)
        draw.text((W // 2, (cap_y0 + cap_y1) // 2), line1, font=f_cap, fill=(255, 215, 65, 255), anchor="mm")

    rgba = np.array(overlay)
    return rgba[:, :, :3].astype(np.float32), (rgba[:, :, 3:4].astype(np.float32)) / 255.0


def render_segment_video(
    seg: dict,
    seg_idx: int,
    total_segs: int,
    cfg: dict,
    part_label: str,
    series_title: str,
    work_dir: Path,
    cache_dir: Path,
) -> Path:
    W, H, FPS = 1080, 1920, 30
    lang = cfg["lang"]
    layout_mode = seg.get("layout", "split_screen")

    mp3_path = work_dir / f"seg_{seg_idx}.mp3"
    wav_path = work_dir / f"seg_{seg_idx}.wav"
    out_mp4 = work_dir / f"seg_{seg_idx}.mp4"

    # 1. Generate Voiceover & Envelope
    synthesize_voiceover_segment(seg["narration"], cfg["voice"], mp3_path, wav_path)
    env, duration = compute_audio_envelope(wav_path, fps=FPS)
    num_frames = len(env)

    # 2. Obtain moving human presenter base frames (real studio presenter video or animated head pose)
    raw_pres_frames = get_moving_presenter_base_frames(cfg, work_dir, num_frames, target_w=900, target_h=1100)

    # 3. Apply Neural Wav2Lip ONNX Lip-Sync (or 2D Facial Mesh + Jaw/Teeth/Blink Articulator)
    synced_pres_frames = apply_wav2lip_onnx_to_presenter_frames(raw_pres_frames, wav_path, cache_dir, fps=FPS)
    if synced_pres_frames is None:
        synced_pres_frames = animate_presenter_mouth_and_eyes_2d(raw_pres_frames, env, fps=FPS)

    # 4. Prepare Moving B-Roll Visual Frames (real video footage + animated live charts)
    if layout_mode == "split_screen":
        broll_frames = render_animated_broll_frames(seg, seg_idx, lang, work_dir, num_frames, W, 960)
    else:
        broll_frames = render_animated_broll_frames(seg, seg_idx, lang, work_dir, num_frames, W, H)

    # 5. Pre-render Broadcast Graphics & Subtitle Layer
    ov_rgb, ov_alpha = build_caption_overlay_rgba(
        W, H,
        part_label=part_label,
        series_title=series_title,
        caption_text=seg.get("caption", ""),
        stat_badge=seg.get("stat_badge", part_label),
        lang=lang,
        layout_mode=layout_mode,
    )

    pip_size = 440
    py_grid, px_grid = np.mgrid[0:pip_size, 0:pip_size].astype(np.float32)
    pip_dist = np.sqrt((px_grid - pip_size * 0.5) ** 2 + (py_grid - pip_size * 0.5) ** 2)
    pip_circle_mask = np.clip((pip_size * 0.48 - pip_dist) / 4.0, 0.0, 1.0)[:, :, None]
    pip_ring_mask = ((pip_dist >= pip_size * 0.455) & (pip_dist <= pip_size * 0.49)).astype(np.float32)[:, :, None]

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{W}x{H}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-i", str(wav_path),
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "21",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        str(out_mp4),
    ]
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for f_idx in range(num_frames):
        t_sec = f_idx / float(FPS)
        amp = float(env[f_idx])
        pres_frame = synced_pres_frames[f_idx]

        canvas = np.zeros((H, W, 3), dtype=np.uint8)

        if layout_mode == "presenter_full":
            # Full-screen talking human presenter + floating animated B-Roll monitor card
            pres_full = np.array(Image.fromarray(pres_frame).resize((W, H), Image.Resampling.BILINEAR))
            canvas[:, :, :] = pres_full
            inset_w, inset_h = 410, 410
            inset_im = Image.fromarray(broll_frames[f_idx]).resize((inset_w, inset_h), Image.Resampling.BILINEAR)
            ix0, iy0 = W - inset_w - 50, 170
            canvas[iy0 - 6 : iy0 + inset_h + 6, ix0 - 6 : ix0 + inset_w + 6] = (0, 220, 255)
            canvas[iy0 : iy0 + inset_h, ix0 : ix0 + inset_w] = np.array(inset_im)

        elif layout_mode == "split_screen":
            # Top 50%: Moving B-Roll Visuals being explained (1080x960)
            canvas[0:960, :, :] = broll_frames[f_idx]
            # Bottom 50%: Talking AI Human Presenter (1080x960)
            pres_half = np.array(Image.fromarray(pres_frame[:820, :]).resize((W, 960), Image.Resampling.BILINEAR))
            canvas[960:1920, :, :] = pres_half

        else:  # "pip_broll"
            # Full-screen moving B-Roll visuals + Circular Picture-in-Picture Talking Presenter
            canvas[:, :, :] = broll_frames[f_idx]
            pip_pres = np.array(Image.fromarray(pres_frame[:760, :]).resize((pip_size, pip_size), Image.Resampling.BILINEAR)).astype(np.float32)
            px0, py0 = 65, 1050
            bg_patch = canvas[py0 : py0 + pip_size, px0 : px0 + pip_size].astype(np.float32)
            blended_pip = bg_patch * (1.0 - pip_circle_mask) + pip_pres * pip_circle_mask
            blended_pip = blended_pip * (1.0 - pip_ring_mask) + np.array([255.0, 205.0, 45.0]) * pip_ring_mask
            canvas[py0 : py0 + pip_size, px0 : px0 + pip_size] = blended_pip.astype(np.uint8)

        # Multi-bar live audio equalizer above subtitle card
        eq_y = 1532
        num_eq_bars = 21
        eq_bw = 26
        eq_gap = 12
        total_eq_w = num_eq_bars * eq_bw + (num_eq_bars - 1) * eq_gap
        eq_x0 = (W - total_eq_w) // 2
        for bi in range(num_eq_bars):
            dist_center = abs(bi - num_eq_bars // 2) / float(num_eq_bars // 2)
            bar_h = int(6 + (1.0 - 0.65 * dist_center) * amp * 42 * (0.6 + 0.4 * abs(math.sin(t_sec * 18.0 + bi))))
            bx = eq_x0 + bi * (eq_bw + eq_gap)
            canvas[max(0, eq_y - bar_h) : min(H, eq_y + bar_h), bx : bx + eq_bw] = (0, 235, 255)

        # Composite RGBA broadcast graphics & subtitle overlay
        c_float = canvas.astype(np.float32) * (1.0 - ov_alpha) + ov_rgb * ov_alpha
        proc.stdin.write(c_float.astype(np.uint8).tobytes())

    proc.stdin.close()
    proc.wait()
    print(f"  [Render Seg {seg_idx + 1}/{total_segs}] Completed ({layout_mode}, {duration:.1f}s) -> {out_mp4.name}")
    return out_mp4


def produce_channel_episode(channel_key: str, cfg: dict, output_root: Path) -> tuple[Path, dict]:
    work_dir = output_root / f"work_{channel_key}"
    cache_dir = output_root / "models_cache"
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)

    script_data = generate_dynamic_script(channel_key, cfg)
    part_label = script_data.get("part", "Part 1")
    series_title = script_data.get("series_title", cfg["name"])
    segments = script_data["segments"]

    seg_files = []
    for idx, seg in enumerate(segments):
        seg_mp4 = render_segment_video(
            seg=seg,
            seg_idx=idx,
            total_segs=len(segments),
            cfg=cfg,
            part_label=part_label,
            series_title=series_title,
            work_dir=work_dir,
            cache_dir=cache_dir,
        )
        seg_files.append(seg_mp4)

    concat_list = work_dir / "concat.txt"
    concat_list.write_text("\n".join([f"file '{p.resolve()}'" for p in seg_files]), encoding="utf-8")

    final_mp4 = output_root / f"{channel_key}_latest.mp4"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(final_mp4)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    print(f"[{channel_key}] Final episode ready: {final_mp4} ({final_mp4.stat().st_size // 1024} KB)")
    return final_mp4, script_data


def upload_to_youtube(video_path: Path, script_data: dict, cfg: dict) -> str | None:
    secret_env = cfg["secret_env"]
    token_raw = os.environ.get(secret_env, "").strip()
    if not token_raw:
        print(f"  [YouTube Upload] {secret_env} is empty or not set in environment; skipping upload.")
        return None

    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload

        token_info = json.loads(token_raw)
        creds = Credentials.from_authorized_user_info(token_info)
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())

        youtube = build("youtube", "v3", credentials=creds)
        title = script_data.get("title", f"{cfg['name']} #Shorts")[:98]
        narration_full = "\n\n".join([s.get("narration", "") for s in script_data.get("segments", [])])
        desc = f"{title}\n\n{narration_full}\n\n#Shorts #AI #Wealth #Documentary"

        body = {
            "snippet": {
                "title": title,
                "description": desc,
                "tags": ["Shorts", "AI", "Technology", "Wealth", "Business", "Documentary"],
                "categoryId": "28" if cfg["lang"] == "ar" else "27",
            },
            "status": {
                "privacyStatus": "public",
                "selfDeclaredMadeForKids": False,
            },
        }
        media = MediaFileUpload(str(video_path), chunksize=-1, resumable=True, mimetype="video/mp4")
        req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
        resp = req.execute()
        vid_id = resp.get("id")
        print(f"  [YouTube Upload] SUCCESS! Video ID: https://youtu.be/{vid_id}")
        return vid_id
    except Exception as e:
        print(f"  [YouTube Upload] Error: {e}")
        return None


def main():
    output_root = Path("output_videos")
    output_root.mkdir(parents=True, exist_ok=True)
    target_filter = os.environ.get("TARGET_CHANNEL", "all").strip().lower()

    for ch_key, cfg in CHANNELS.items():
        if target_filter not in ("all", "", ch_key.lower()):
            continue
        print("=" * 72)
        print(f"STARTING NEURAL WAV2LIP + MOVING PRESENTER PIPELINE v11.0 FOR: {ch_key}")
        print("=" * 72)
        video_path, script_data = produce_channel_episode(ch_key, cfg, output_root)
        if os.environ.get("DRY_RUN", "0") != "1":
            upload_to_youtube(video_path, script_data, cfg)


if __name__ == "__main__":
    main()
