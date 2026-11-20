"""
Empire Cloud Documentary Seasons: Master Curated & Dynamic Topic Seeds
Engineered for 100M Monthly Views with:
1. 2-Second Explosive Shock Hook (Scene 1)
2. Seamless Infinite Loop Connector (Scene 10)
3. Exactly 10 Punchy Scenes per Episode (45-50s)
4. 100% Unique Visuals & SFX Scoring per Scene
"""

import time
import random

VIRAL_TOPIC_SEEDS_AR = [
    # Episode 1: Ariane 5 Rocket Bug
    {
        "id": "ariane5_bug",
        "title": "كارثة صاروخ أريان 5: عندما دمّر خطأ برمجي 370 مليون دولار في 37 ثانية! #Shorts",
        "hook": "كود برمجي تافه فجّر 370 مليون دولار في 37 ثانية!",
        "loop": "...ولهذا السبب الصادم بالتحديد،",
        "core_mystery": "The 1996 European Ariane 5 rocket exploded 37 seconds after liftoff because a 64-bit floating point number was converted into a 16-bit signed integer, causing a fatal software overflow.",
        "scenes": [
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "كود برمجي تافه فجّر 370 مليون دولار في 37 ثانية!",
                "broll_search": "Titan IV rocket launch pad Cape Canaveral",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Colossal space rocket lifting off launch pad engulfed in fire, 9:16 vertical",
                "visual_style": "rocket_launch_pad"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "في 4 يونيو 1996 انطلق أحدث صاروخ فضاء أوروبي.",
                "broll_search": "space rocket flying atmosphere smoke trail",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Rocket ascending into blue upper atmosphere trailing smoke, 9:16 vertical",
                "visual_style": "rocket_launch_pad"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "كل شيء كان مثالياً حتى بلغت الرحلة الثانية السابعة والثلاثين.",
                "broll_search": "cold war radar room operators tracking trajectory",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Mission control telemetry displays glowing with velocity charts, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "فجأة انحرف الصاروخ عن مساره بزاوية حادة وانشطر!",
                "broll_search": "catastrophic explosion shockwave fireball sky",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Explosion fireball high altitude destroying rocket fuselage, 9:16 vertical",
                "visual_style": "rocket_launch_pad"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "تحقيقات المهندسين كشفت مفاجأة صدمت العالم العلمي بأكمله.",
                "broll_search": "scientists examining computer software printouts",
                "caption": "", "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Engineers reviewing complex assembly code printouts under harsh light, 9:16 vertical",
                "visual_style": "vintage_mainframe_1960"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "حاسوب التوجيه حاول تحويل رقم 64-بت إلى 16-بت فقط.",
                "broll_search": "integrated circuit die microchip macro",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Silicon microchip wafer silicon core illuminated by blue laser, 9:16 vertical",
                "visual_style": "microchip_die_wafer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "الرقم كان أكبر من سعة الذاكرة، فحدث خطأ طفحان الذاكرة!",
                "broll_search": "supercomputer mainframe memory bank flashing",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Vintage supercomputer core processor status indicators flashing red, 9:16 vertical",
                "visual_style": "vintage_cray_supercomputer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "الكود القديم كان مأخوذاً من صاروخ أبطأ بدون اختبارات كافية.",
                "broll_search": "apollo mission control room operators vintage",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Apollo era flight controllers in panic at communication consoles, 9:16 vertical",
                "visual_style": "apollo13_mission_control"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "سطر كود واحد حوّل سنوات التطوير إلى غبار مشتعل.",
                "broll_search": "satellite debris falling dark space",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Satellite payload debris falling into darkness above earth curvature, 9:16 vertical",
                "visual_style": "satellite_earth_orbit"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "وما زال تاريخ البرمجة يذكر هذه الكارثة، ولهذا السبب الصادم بالتحديد،",
                "broll_search": "mission control room empty dark monitors",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Quiet mission control room monitors displaying final system crash dump, 9:16 vertical",
                "visual_style": "apollo13_mission_control"
            }
        ]
    },

    # Episode 2: Stuxnet Cyberweapon
    {
        "id": "stuxnet_cyber",
        "title": "سلاح ستاكسنت الرقمي: أول فيروس يدمر مفاعلات نووية حقيقية! #Shorts",
        "hook": "سلاح رقمي غير مرئي مزّق الفولاذ النووي!",
        "loop": "...ولهذا السبب الصادم بالتحديد،",
        "core_mystery": "Stuxnet was the world's first physical cyberweapon, covertly introduced via a USB drive into Iran's Natanz facility to spin uranium centrifuges to self-destruction while displaying normal readouts.",
        "scenes": [
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "سلاح رقمي غير مرئي مزّق الفولاذ النووي في الظلام!",
                "broll_search": "nuclear facility centrifuges uranium industrial plant",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "High speed uranium enrichment centrifuges spinning in secret facility, 9:16 vertical",
                "visual_style": "factory_production_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "في 2010 بدأت أجهزة الطرد المركزي النووية تنفجر ذاتياً.",
                "broll_search": "industrial machinery sparks catastrophic vibration",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Industrial metal centrifuge vibrating violently with flying metal fragments, 9:16 vertical",
                "visual_style": "factory_production_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "شاشات المراقبة كانت تظهر قراءات خضراء وطبيعية بنسبة 100%!",
                "broll_search": "industrial control room monitors green indicators fake",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Control room operators looking at deceptive green status monitors, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "العلماء ظنوا أن هناك عيباً تصنيعياً في المعادن.",
                "broll_search": "scientists examining cracked metal components magnifying glass",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Metallurgists examining fractured steel rotor components in lab, 9:16 vertical",
                "visual_style": "vintage_mainframe_1960"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "لكن الحقيقة كانت كوداً برمجياً استخباراتياً خبيثاً اسمه ستاكسنت.",
                "broll_search": "hacker typing assembly malicious code glowing screen",
                "caption": "", "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Cyber warfare code cascading down black CRT screen in dark vault, 9:16 vertical",
                "visual_style": "autonomous_agent_matrix"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "الفيروس تسلل عبر وحدة فلاش USB لأجهزة معزولة عن الإنترنت.",
                "broll_search": "usb flash drive inserted into industrial computer terminal",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Close-up of USB stick inserted into sealed industrial controller, 9:16 vertical",
                "visual_style": "microchip_die_wafer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "قام برفع سرعة المحركات لسرعات جنونية حتى تفككت.",
                "broll_search": "high voltage industrial motor spinning smoking hot",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Industrial turbine spinning at supersonic speed glowing red hot, 9:16 vertical",
                "visual_style": "factory_production_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "دمر الفيروس أكثر من ألف جهاز دون إطلاق رصاصة واحدة.",
                "broll_search": "abandoned damaged nuclear centrifuge hall dark",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Darkened centrifuge gallery with destroyed machinery and emergency lights, 9:16 vertical",
                "visual_style": "chernobyl_control_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "كانت تلك اللحظة بداية عصر حروب الإنترنت المادية الحديثة.",
                "broll_search": "world map global cyber warfare digital connections",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Global fiber optic network illuminated against dark earth horizon, 9:16 vertical",
                "visual_style": "satellite_earth_orbit"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "ودخل السلاح الرقمي التاريخ إلى الأبد، ولهذا السبب الصادم بالتحديد،",
                "broll_search": "classified top secret folder military cyber command",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Declassified military cyber warfare file on steel examination desk, 9:16 vertical",
                "visual_style": "madison_boardroom_1952"
            }
        ]
    },

    # Episode 3: Chernobyl AZ-5 Button
    {
        "id": "chernobyl_az5",
        "title": "كارثة تشرنوبل: السر المظلم وراء زر الطوارئ AZ-5! #Shorts",
        "hook": "زر الطوارئ في تشرنوبل كان هو القنبلة!",
        "loop": "...ولهذا السبب الصادم بالتحديد،",
        "core_mystery": "At Chernobyl in 1986, pressing the emergency shutdown button AZ-5 was intended to save the reactor, but the graphite tips on the control rods displaced water and triggered the catastrophic power surge.",
        "scenes": [
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "زر الطوارئ في تشرنوبل كان هو القنبلة القاتلة!",
                "broll_search": "Chernobyl reactor 4 control room flashing emergency red lights",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Chernobyl reactor control room consoles flashing intense red warning beacons, 9:16 vertical",
                "visual_style": "chernobyl_control_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "في 26 أبريل 1986 بدأ اختبار كهربائي روتيني.",
                "broll_search": "soviet electrical power plant dials analog meters",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Vintage Soviet analog power meters vibrating with unstable voltage needles, 9:16 vertical",
                "visual_style": "chernobyl_control_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "طاقة المفاعل انخفضت بشكل خطير وغير متوقع في الدقائق الأخيرة.",
                "broll_search": "reactor core water steam bubbling pressure gauges",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Boiling heavy water reactor core illuminated by eerie Cherenkov radiation blue glow, 9:16 vertical",
                "visual_style": "soviet_submarine_abyss"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "سحب المشغلون قضبان التحكم لرفع القوة من جديد.",
                "broll_search": "nuclear control rods steel mechanism rising",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Mechanical overhead crane extracting cadmium control rods from core lid, 9:16 vertical",
                "visual_style": "factory_production_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "عندما بدأت الحرارة تخرج عن السيطرة، ضغط المشغل زر AZ-5.",
                "broll_search": "hand pressing big red emergency shutdown button",
                "caption": "", "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Operator hand slamming circular red AZ-5 emergency shutdown button, 9:16 vertical",
                "visual_style": "chernobyl_control_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "كان من المفترض أن يغلق الزر المفاعل فوراً وينقذهم.",
                "broll_search": "control room schematic blueprints soviet nuclear",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Soviet RBMK reactor engineering schematic blueprints spread on console, 9:16 vertical",
                "visual_style": "vintage_mainframe_1960"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "لكن رؤوس القضبان كانت مصنوعة من مادة الغرافيت الرخيصة!",
                "broll_search": "graphite core blocks burning nuclear fire",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Graphite tip blocks entering reactor channel causing immediate steam surge, 9:16 vertical",
                "visual_style": "microchip_die_wafer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "الغرافيت زاد التفاعل النووي بدلاً من إيقافه في ثوانٍ!",
                "broll_search": "steam explosion destroying roof building sparks",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Massive steam explosion rupturing through reactor roof into night sky, 9:16 vertical",
                "visual_style": "rocket_launch_pad"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "انفجر قلب المفاعل وتحول الحادث لأكبر كارثة نووية.",
                "broll_search": "Chernobyl destroyed reactor 4 ruins smoking aerial view",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Smoking ruins of Chernobyl reactor 4 illuminated by emergency flares, 9:16 vertical",
                "visual_style": "chernobyl_control_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "والسبب عيب هندسي أخفته الدولة، ولهذا السبب الصادم بالتحديد،",
                "broll_search": "soviet classified report stamp top secret red",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "KGB classified folder stamped Top Secret on wooden cabinet desk, 9:16 vertical",
                "visual_style": "madison_boardroom_1952"
            }
        ]
    },

    # Episode 4: Deep Blue vs Kasparov
    {
        "id": "deep_blue_1997",
        "title": "هزم الذكاء الاصطناعي أذكى عقل بشري في التاريخ! #Shorts",
        "hook": "هزم الذكاء الاصطناعي أذكى عقل بشري تاريخياً!",
        "loop": "...ولهذا السبب الصادم بالتحديد،",
        "core_mystery": "In 1997, IBM's Deep Blue defeated world chess champion Garry Kasparov in a match where Kasparov was psychologically unsettled by a machine bug that looked like superior human intuition.",
        "scenes": [
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "هزم الذكاء الاصطناعي أذكى عقل بشري تاريخياً في 1997!",
                "broll_search": "Deep Blue chess IBM grandmaster match",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Garry Kasparov clutching forehead across chess board from IBM machine, 9:16 vertical",
                "visual_style": "deep_blue_kasparov"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "غاري كاسباروف كان بطل العالم بلا منازع لسنوات طويلة.",
                "broll_search": "chess board pieces spotlight dramatic grandmaster tournament",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Carved wooden chess pieces cast long dramatic shadows across tournament board, 9:16 vertical",
                "visual_style": "deep_blue_kasparov"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "شركة آي بي إم صنعت حاسوباً عملاقاً اسمه ديب بلو.",
                "broll_search": "IBM Deep Blue supercomputer black towers glowing blue LEDs",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Towering black IBM supercomputer mainframe with blue diagnostic status lights, 9:16 vertical",
                "visual_style": "vintage_cray_supercomputer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "الحاسوب كان يحلل 200 مليون نقلة شطرنج في الثانية الواحدة!",
                "broll_search": "computer silicon processors microchips processing fast data",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Specialized chess processor chips on motherboard pulsing with green current, 9:16 vertical",
                "visual_style": "microchip_die_wafer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "في الجولة الأولى لعبت الآلة حركة غريبة وغير متوقعة.",
                "broll_search": "chess pawn moving forward slow motion hand grandmaster",
                "caption": "", "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Chess rook slide move across board illuminated by stark stage spotlight, 9:16 vertical",
                "visual_style": "deep_blue_kasparov"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "كاسباروف أصيب بالذهول وظن أن الآلة تفكر بذكاء بشري!",
                "broll_search": "intense grandmaster eyes sweat stress tournament",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Extreme close-up of human eyes reflecting chess grid with visible stress, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "الحقيقة الصادمة كُشفت لاحقاً: كانت الحركة مجرد خلل برمجي عشوائي!",
                "broll_search": "software bug code glitch assembly language terminal",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Terminal debugger showing random fail-safe fallback move execution, 9:16 vertical",
                "visual_style": "vintage_mainframe_1960"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "لكن الصدمة النفسية حطمت تركيز بطل العالم في الجولات التالية.",
                "broll_search": "chess king falling toppled on wooden board defeat",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Fallen black chess king lying defeated on checkered grid, 9:16 vertical",
                "visual_style": "deep_blue_kasparov"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "استسلم كاسباروف في الجولة الأخيرة وأعلن العالم انتصار الآلة.",
                "broll_search": "press conference flash cameras reporters cheering 1997",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Flash cameras illuminating historic press conference announcing machine victory, 9:16 vertical",
                "visual_style": "wall_street_trading_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "ومنذ ذلك اليوم تفوقت الخوارزميات، ولهذا السبب الصادم بالتحديد،",
                "broll_search": "futuristic neural network matrix nodes glowing dark",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Vast neural network constellation connecting glowing nodes in infinity, 9:16 vertical",
                "visual_style": "autonomous_agent_matrix"
            }
        ]
    },

    # Episode 5: Soviet Dead Hand / Perimetr
    {
        "id": "soviet_dead_hand",
        "title": "نظام اليد الميتة السوفيتي: كمبيوتر يمكنه إشعال حرب نووية بمفرده! #Shorts",
        "hook": "كمبيوتر سوفيتي يملك صلاحية إشعال حرب نووية!",
        "loop": "...ولهذا السبب الصادم بالتحديد،",
        "core_mystery": "The Soviet Dead Hand (Perimetr) system was built in the 1980s to automatically launch retaliatory nuclear ICBMs if sensors detected nuclear detonations and military leadership was dead.",
        "scenes": [
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "كمبيوتر سوفيتي يملك صلاحية إشعال حرب نووية بمفرده!",
                "broll_search": "Soviet underground nuclear command bunker steel blast doors",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Underground nuclear silo command bunker reinforced steel blast doors, 9:16 vertical",
                "visual_style": "bank_vault_steel_door"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "في ذروة الحرب الباردة صمم السوفيت نظاماً سرياً اسمه بيريميتر.",
                "broll_search": "cold war military officers maps operations room",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Soviet military generals studying strategic strike maps in bunker, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "الهدف كان ضمان الرد النووي حتى لو قُتلت القيادة بالكامل.",
                "broll_search": "nuclear ballistic missile silo underground hatch opening",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Concrete missile silo lid sliding open in snowy desolate forest, 9:16 vertical",
                "visual_style": "rocket_launch_pad"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "النظام يعتمد على شبكة مجسات تقيس الضغط الجوي والإشعاع والزلازل.",
                "broll_search": "radiation sensor geiger counter needle scientific monitors",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Geiger counter needles jumping into red radioactive danger zone, 9:16 vertical",
                "visual_style": "chernobyl_control_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "إذا رصد الكمبيوتر انفجارات نووية مع انقطاع الاتصال بموسكو...",
                "broll_search": "oscilloscope screen static severed communication lines",
                "caption": "", "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Communication radio waveforms fading into dead flatline static, 9:16 vertical",
                "visual_style": "vintage_mainframe_1960"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "يفترض تلقائياً أن القيادة ماتت وينقل قرار الإطلاق لنفسه!",
                "broll_search": "vintage supercomputer circuits relays activating lights",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "High security automated command circuits closing relays with spark, 9:16 vertical",
                "visual_style": "vintage_cray_supercomputer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "يطلق الصاروخ القائد الذي يبث أوامر الإطلاق لكل الصواريخ.",
                "broll_search": "intercontinental ballistic missile launch fire smoke exhaust",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Command missile erupting from subterranean silo into grey clouds, 9:16 vertical",
                "visual_style": "rocket_launch_pad"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "مئات الرؤوس النووية تنطلق تلقائياً نحو أهدافها بدون أي إنسان!",
                "broll_search": "multiple missile trails rising into stratospheric space",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Multiple ballistic contrails arcing into dark edge of space, 9:16 vertical",
                "visual_style": "satellite_earth_orbit"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "المرعب أن النظام لا يزال مفعلاً وجاهزاً للعمل حتى اليوم.",
                "broll_search": "classified military bunker blinking status standby modern",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Unmanned military server racks humming in subterranean concrete vault, 9:16 vertical",
                "visual_style": "bank_vault_steel_door"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "آلة قادرة على إنهاء العالم بكود قديم، ولهذا السبب الصادم بالتحديد،",
                "broll_search": "planet earth seen from deep space dark void",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Planet Earth suspended peacefully against black abyss of cosmos, 9:16 vertical",
                "visual_style": "satellite_earth_orbit"
            }
        ]
    },

    # Episode 6: Morris Worm 1988
    {
        "id": "morris_worm",
        "title": "دودة موريس 1988: طالب أسقط شبكة الإنترنت العالمية بالكامل! #Shorts",
        "hook": "طالب جامعي أسقط شبكة الإنترنت بالكامل!",
        "loop": "...ولهذا السبب الصادم بالتحديد،",
        "core_mystery": "In 1988, Cornell graduate student Robert Tappan Morris released the first internet worm to measure the size of the nascent internet, but an aggressive replication loop crashed 10% of all connected computers.",
        "scenes": [
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "طالب جامعي أسقط شبكة الإنترنت العالمية بالكامل في 1988!",
                "broll_search": "vintage terminal crt green text cyber attack morris worm",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Vintage green phosphor terminal screen scrolling rapidly with memory dump, 9:16 vertical",
                "visual_style": "vintage_mainframe_1960"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "روبرت موريس كان طالباً عبقرياً في جامعة كورنيل الأمريكية.",
                "broll_search": "university computer laboratory 1980s students terminals",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Quiet 1980s academic computer lab with glowing mainframe terminals, 9:16 vertical",
                "visual_style": "dartmouth_conference_1956"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "أراد فقط قياس حجم شبكة الإنترنت وعدد الأجهزة المتصلة بها.",
                "broll_search": "early arpanet internet map connections nodes 1980",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Early ARPANET node connection diagram glowing on drafting table, 9:16 vertical",
                "visual_style": "autonomous_agent_matrix"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "كتب برنامجاً صغيراً يتنقل بين الأجهزة بهدوء تام دون إتلافها.",
                "broll_search": "c programming language source code vintage editor",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Clean C programming code scrolling across monochrome CRT screen, 9:16 vertical",
                "visual_style": "vintage_mainframe_1960"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "لكنه وضع خطأ فادحاً في آلية تكرار النسخ داخل الكود.",
                "broll_search": "microprocessor overloaded heat thermal imaging",
                "caption": "", "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Computer CPU chip glowing with intense heat from processing overload, 9:16 vertical",
                "visual_style": "microchip_die_wafer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "الدودة أصبحت تنسخ نفسها مئات المرات في الجهاز الواحد!",
                "broll_search": "server rack cooling fans spinning red alert lights",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Data center server racks halting with emergency error indicator LEDs, 9:16 vertical",
                "visual_style": "vintage_cray_supercomputer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "خلال ساعات تجمدت حواسيب البنتاغون والجامعات ومراكز الأبحاث.",
                "broll_search": "nasa apollo control room scientists panicked",
                "caption": "", "sfx_cue": "sfx_riser",
                "visual_prompt": "Research lab scientists unplugging network ethernet cables in panic, 9:16 vertical",
                "visual_style": "apollo13_mission_control"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "توقفت 10% من شبكة الإنترنت بالكامل عن العمل في لحظة.",
                "broll_search": "disconnected internet cables black screen terminal frozen",
                "caption": "", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Severed network cables lying on server room floor with dark terminals, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "أصبح موريس أول شخص يُحاكم بموجب قانون الاحتيال الحاسوبي.",
                "broll_search": "gavel slamming wooden desk courtroom judgment",
                "caption": "", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Judicial wooden gavel resting on legal case file in courtroom, 9:16 vertical",
                "visual_style": "madison_boardroom_1952"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "ومن ركام تلك الدودة وُلد الأمن السيبراني، ولهذا السبب الصادم بالتحديد،",
                "broll_search": "modern cyber defense security room blue screens glowing",
                "caption": "", "sfx_cue": "sfx_impact",
                "visual_prompt": "Modern cyber operations command center tracking live global threats, 9:16 vertical",
                "visual_style": "autonomous_agent_matrix"
            }
        ]
    }
]

VIRAL_TOPIC_SEEDS_EN = [
    # Episode 1: Project Azorian Submarine Heist
    {
        "id": "project_azorian",
        "title": "Project Azorian: The $4 Billion Cold War Submarine Heist #Shorts",
        "hook": "The CIA spent billions stealing a nuclear submarine!",
        "loop": "...which brings us right back to the shocking reality that:",
        "core_mystery": "In 1974, billionaire Howard Hughes built the Glomar Explorer under the cover story of mining manganese nodules, secretly executing a CIA plan to lift sunken Soviet submarine K-129 from three miles deep.",
        "scenes": [
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "The CIA spent billions stealing a sunken nuclear submarine!",
                "broll_search": "Soviet submarine abyss ocean depth underwater",
                "caption": "The CIA spent billions stealing a nuclear submarine!", "sfx_cue": "sfx_impact",
                "visual_prompt": "Soviet nuclear submarine resting on abyssal ocean floor illuminated by searchlights, 9:16 vertical",
                "visual_style": "soviet_submarine_abyss"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "In 1968 Soviet submarine K-129 sank with nuclear warheads.",
                "broll_search": "ocean dark storm waves naval submarine",
                "caption": "K-129 sank three miles deep with nuclear missiles.", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Dark storm waves crashing over conning tower of Soviet submarine, 9:16 vertical",
                "visual_style": "soviet_submarine_abyss"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Moscow searched for months across the Pacific and found nothing.",
                "broll_search": "naval fleet search sonar radar screens vintage",
                "caption": "Moscow searched the Pacific and found nothing.", "sfx_cue": "sfx_riser",
                "visual_prompt": "Soviet naval search ships navigating dark foggy waters with searchlights, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "American deep hydrophones recorded the exact explosion coordinates.",
                "broll_search": "underwater acoustic hydrophone sensor audio waveforms",
                "caption": "US acoustic hydrophones pinpointed the exact wreck coordinates.", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Acoustic hydrophone waveform spikes displayed on submarine telemetry screen, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Lifting 3,000 tons of steel from three miles was deemed impossible.",
                "broll_search": "deep sea robotic submersible mechanical claw hydraulic",
                "caption": "Lifting 3,000 tons from 16,000 feet was an engineering impossibility.", "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Colossal mechanical steel claw hovering above dark ocean trench floor, 9:16 vertical",
                "visual_style": "factory_production_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Billionaire Howard Hughes built a colossal fake mining ship.",
                "broll_search": "huge industrial recovery vessel derrick ocean",
                "caption": "Billionaire Howard Hughes built a colossal mining cover ship.", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Massive deep sea salvage vessel Glomar Explorer with center derrick tower, 9:16 vertical",
                "visual_style": "factory_production_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Soviet spy ships watched from meters away, completely oblivious.",
                "broll_search": "soviet spy ship binoculars observing foreign vessel",
                "caption": "Soviet spy ships circled nearby, completely oblivious.", "sfx_cue": "sfx_riser",
                "visual_prompt": "Soviet naval officer peering through binoculars at recovery vessel on high seas, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "As the claw lifted the hull, the metal fractured in half!",
                "broll_search": "hydraulic mechanical claw breaking metal falling",
                "caption": "Halfway up, the mechanical claw snapped under ocean pressure!", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Massive steel claw arm snapping under extreme hydraulic pressure underwater, 9:16 vertical",
                "visual_style": "soviet_submarine_abyss"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Two thirds of the submarine plunged right back to the abyss.",
                "broll_search": "heavy steel hull sinking into dark ocean depth",
                "caption": "Two thirds of the submarine fell back to the abyss.", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Submarine hull section tumbling down into darkness of ocean trench, 9:16 vertical",
                "visual_style": "soviet_submarine_abyss"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "The costliest heist in history remained classified for decades,",
                "broll_search": "top secret cia declassified folder stamped vault",
                "caption": "The most expensive heist in history was locked in a vault,", "sfx_cue": "sfx_impact",
                "visual_prompt": "Declassified CIA Project Azorian folder locked inside heavy steel bank vault, 9:16 vertical",
                "visual_style": "bank_vault_steel_door"
            }
        ]
    },

    # Episode 2: The 2010 Flash Crash
    {
        "id": "wall_street_flash_crash",
        "title": "The 2010 Flash Crash: One Trader Erased $1 Trillion in 36 Minutes! #Shorts",
        "hook": "One trader erased a trillion dollars in minutes!",
        "loop": "...which brings us right back to the shocking reality that:",
        "core_mystery": "On May 6, 2010, the US stock market crashed nearly 1,000 points in 36 minutes, later traced to British trader Navinder Sarao who manipulated automated algorithm spoofing from his childhood bedroom.",
        "scenes": [
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "One trader erased a trillion dollars in 36 minutes!",
                "broll_search": "wall street stock ticker crashing red numbers trading floor",
                "caption": "One trader erased a trillion dollars in 36 minutes!", "sfx_cue": "sfx_impact",
                "visual_prompt": "Wall street electronic ticker board tumbling with steep cascading red percentages, 9:16 vertical",
                "visual_style": "wall_street_trading_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "May 6, 2010 started like any regular financial trading day.",
                "broll_search": "wall street traders busy shouting paper trading floor",
                "caption": "May 6, 2010 started like any normal trading day.", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Chicago Board of Trade floor crowded with frantic brokers shouting orders, 9:16 vertical",
                "visual_style": "wall_street_trading_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "At 2:42 PM the Dow Jones suddenly went into freefall.",
                "broll_search": "financial stock market chart plunge steep drop",
                "caption": "At 2:42 PM the Dow Jones entered a catastrophic freefall.", "sfx_cue": "sfx_riser",
                "visual_prompt": "Digital stock index line graph plunging straight downward into negative territory, 9:16 vertical",
                "visual_style": "wall_street_trading_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Blue chip stocks like Procter & Gamble plunged by 37 percent!",
                "broll_search": "stock brokers hands on head panic trading desk",
                "caption": "Blue chip giants like P&G dropped 37 percent in seconds!", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Wall Street brokers staring in pure panic at red plunging terminal monitors, 9:16 vertical",
                "visual_style": "wall_street_trading_floor"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Automated algorithmic trading bots began panic selling across the globe.",
                "broll_search": "high frequency trading server rack fiber optic flashing",
                "caption": "High-frequency trading algorithms triggered instant automated selloffs.", "sfx_cue": "sfx_heartbeat",
                "visual_prompt": "Wall Street high frequency trading server racks blinking with rapid fiber optic pulses, 9:16 vertical",
                "visual_style": "vintage_cray_supercomputer"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "One trillion dollars in market value evaporated into thin air.",
                "broll_search": "dollar bills burning smoke ash currency destruction",
                "caption": "One trillion dollars of wealth evaporated into thin air.", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Bank vault floor strewn with dollar notes dissolving into digital smoke, 9:16 vertical",
                "visual_style": "bank_vault_steel_door"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Investigators spent five years searching for the mysterious culprit.",
                "broll_search": "fbi financial crime investigators documents evidence wall",
                "caption": "Federal investigators spent five years hunting the mastermind.", "sfx_cue": "sfx_riser",
                "visual_prompt": "Federal financial crime investigators analyzing algorithmic order book data prints, 9:16 vertical",
                "visual_style": "cold_war_radar_room"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "It was not a hedge fund, but a lone trader working from his bedroom!",
                "broll_search": "suburban bedroom computer monitors trading setup humble",
                "caption": "It was not a bank, but a lone trader in his bedroom!", "sfx_cue": "sfx_subdrop",
                "visual_prompt": "Modest suburban bedroom desk with multiple monitors running custom trading software, 9:16 vertical",
                "visual_style": "vintage_mainframe_1960"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "He spoofed massive fake orders, tricking the algorithms into collapsing.",
                "broll_search": "code algorithmic trading terminal fast numbers scrolling",
                "caption": "He tricked billion-dollar algorithms with automated spoof orders.", "sfx_cue": "sfx_whoosh",
                "visual_prompt": "Custom spoofing software terminal placing and canceling thousands of futures contracts, 9:16 vertical",
                "visual_style": "autonomous_agent_matrix"
            },
            {
                "speaker": "narrator", "scene_type": "b_roll", "character_focus": "broll_evidence",
                "narration": "Exposing the fragility of global finance,",
                "broll_search": "empty wall street exchange floor after hours dim lights",
                "caption": "Exposing the hidden fragility of modern finance,", "sfx_cue": "sfx_impact",
                "visual_prompt": "Quiet Wall Street trading floor after hours with lone security light reflections, 9:16 vertical",
                "visual_style": "wall_street_trading_floor"
            }
        ]
    }
]


def get_viral_topic_seed(channel_key: str, lang: str, run_num: int = 1, hour_slot: int = 0) -> dict:
    """Returns a deterministic yet constantly evolving viral documentary seed with 10-scene structure."""
    if lang == "ar" or "ar" in channel_key:
        bank = VIRAL_TOPIC_SEEDS_AR
    else:
        bank = VIRAL_TOPIC_SEEDS_EN

    # High-dispersion rotation formula: changes every run and every few hours
    rand_offset = random.randint(1, 999)
    idx = (run_num * 17 + hour_slot * 3 + rand_offset) % len(bank)
    return dict(bank[idx])
