# Multi-Engine Oral Quiz (PA-34-200 Seneca I)

Offline multiple-choice quiz for the multi-engine practical test oral, for iPad (also iPhone and desktop). Same look as the PA-34-200 Checklists app: big tiles, Day / Night / Red modes.

**Install:** open https://douglasbrody.github.io/study-multiengine/ in Safari on the iPad → Share → **Add to Home Screen** → open it once from the icon while online. After that it works in airplane mode (Settings shows "Offline ready").

**What's in it:** two groups of topics. *Oral Exam Guide* covers every area of the ASA Multi-Engine Oral Exam Guide (documents and airworthiness, performance, weight and balance, every aircraft system, multi-engine aerodynamics and Vmc, engine-out procedures, and the chapter 4 maneuvers and ACS standards). *PA-34 Seneca* covers the airplane from its Pilot's Operating Manual, set up for N56307 (autopilot and electric pitch trim; no combustion heater or ice protection), with the school's procedures where they were chosen over the POH: speeds and limits, weight and balance, performance charts, engines and props, fuel, gear, electrical and vacuum, airframe, normal and emergency procedures. Seneca speeds are MPH.

**How it works:** tap a tile to start a quiz. Practice quizzes show the answer, explanation and source after every question; the Mock Oral grades 50 mixed questions at the end. Questions you miss come back more often until you get them right. Flag any question to review it later (Settings › Copy flagged as text to send corrections). Study mode lists every question in a topic with its answer. Progress stays on the device.

**Updating questions:** edit `questions/*.json` (each item: `id`, `topic`, `q`, `a`, `d` = three wrong choices, `why`, `src`), run `python3 tools/build_questions.py` to check them and rebuild `questions.js`, then bump `VERSION` in `sw.js`. Keep ids unchanged; progress is stored by id. Add `"drop": true` to retire a question.

**Writing questions:** every question must be answerable from memory, without the POH, AFM or charts in hand. Don't word a stem as if a page is open ("per POH 1-1", "on chart 8-2"); cite pages in `src` and `why` only. No chart reads or table lookups at given conditions. Calculation questions give every number they need (weights, arms, limits) in the stem.

Questions are written in our own words from the ASA guide and the POH. Where the school checklist and the POH differ, the quiz follows the choices listed under **Procedure choices** below.

## Procedure choices

Where the school checklist and the POH differ, the quiz uses:

- Engine failure / feathering airspeed: blue line, Vyse 105 MPH (school; AFM says above 90 MPH).
- Unfeathering: propeller control full forward (school; AFM says forward to cruise RPM).
- Two-engine go-around: flaps to 25°, gear up on a positive rate, then the rest of the flaps (school).
- Single-engine landing: don't extend the gear until certain of making the field (POH 3-13).
- One overvoltage light: alternator off, then on — if more than 50 amps, off (school).
- Normal start: electric fuel pump off after priming, before cranking (school).
- Short-field takeoff rotation, flaps 0°: 75 MPH (school briefing card); flaps 25°: 70 MPH.
- Gear may be lowered up to 150 MPH; 125 MPH is the retraction limit (POH).
- Stall speeds at 3,800 lb: about 65 MPH flaps 40°, 72 MPH flaps up (POH chart 8-11).
- Main tire pressure 53 psi (POH 9-8). Flap limit 125 MPH at every setting (AFM).
