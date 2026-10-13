# Multi-Engine Oral Quiz (PA-34-200 Seneca I)

Offline multiple-choice quiz for the multi-engine practical test oral, for iPad (also iPhone and desktop). Same look as the PA-34-200 Checklists app: big tiles, Day / Night / Red modes.

**Install:** open https://douglasbrody.github.io/study-multiengine/ in Safari on the iPad → Share → **Add to Home Screen** → open it once from the icon while online. After that it works in airplane mode (Settings shows "Offline ready").

**What's in it:** two groups of topics. *Oral Exam Guide* covers every area of the ASA Multi-Engine Oral Exam Guide (documents and airworthiness, performance, weight and balance, every aircraft system, multi-engine aerodynamics and Vmc, engine-out procedures, and the chapter 4 maneuvers and ACS standards). *PA-34 Seneca* covers the airplane from its Pilot's Operating Manual (s/n 34-7350124): speeds and limits, weight and balance, performance charts, engines and props, fuel, gear, electrical and vacuum, airframe, normal and emergency procedures. Seneca speeds are MPH.

**How it works:** tap a tile to start a quiz. Practice quizzes show the answer, explanation and source after every question; the Mock Oral grades 50 mixed questions at the end. Questions you miss come back more often until you get them right. Flag any question to review it later (Settings › Copy flagged as text to send corrections). Study mode lists every question in a topic with its answer. Progress stays on the device.

**Updating questions:** edit `questions/*.json` (each item: `id`, `topic`, `q`, `a`, `d` = three wrong choices, `why`, `src`), run `python3 tools/build_questions.py` to check them and rebuild `questions.js`, then bump `VERSION` in `sw.js`. Keep ids unchanged; progress is stored by id. Add `"drop": true` to retire a question.

Questions are written in our own words from the ASA guide and the POH. If an answer disagrees with your POH or instructor, the POH wins.
