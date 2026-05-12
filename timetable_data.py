"""
timetable_data.py
All 8 days of study schedule as Python list of dicts.
Block IDs: {date_short}{unit_label} e.g. d12u1, d13u3pt2, d20u1
"""

TIMETABLE = [
    # ===== MAY 12 — FORECASTING DAY 1 (1 PM start) =====
    {
        "id": "d12u1",
        "date": "May 12",
        "day": "Tue",
        "time": "1 PM – 2:30 PM",
        "subject": "forecasting",
        "unit": "U1",
        "content": "Six considerations, loss functions, forecast horizons",
        "duration_hours": 1.5,
    },
    {
        "id": "d12u6",
        "date": "May 12",
        "day": "Tue",
        "time": "3 PM – 4:30 PM",
        "subject": "forecasting",
        "unit": "U6",
        "content": "Qualitative methods — Delphi, groupthink, biases, memory dump",
        "duration_hours": 1.5,
    },
    {
        "id": "d12u2pt1",
        "date": "May 12",
        "day": "Tue",
        "time": "5 PM – 7 PM",
        "subject": "forecasting",
        "unit": "U2 Pt1",
        "content": "MA, SMA, WMA, exponential smoothing, Holt-Winters",
        "duration_hours": 2,
    },
    {
        "id": "d12u2pt2",
        "date": "May 12",
        "day": "Tue",
        "time": "8 PM – 10 PM",
        "subject": "forecasting",
        "unit": "U2 Pt2",
        "content": "Decomposition, forecast accuracy metrics + numericals",
        "duration_hours": 2,
    },
    {
        "id": "d12u3pt1",
        "date": "May 12",
        "day": "Tue",
        "time": "11 PM – 2 AM",
        "subject": "forecasting",
        "unit": "U3 Pt1",
        "content": "Stationarity, AR(p), MA(q), ACF/PACF patterns",
        "duration_hours": 3,
    },
    {
        "id": "d12u3pt2",
        "date": "May 13",
        "day": "Wed",
        "time": "2 AM – 4 AM",
        "subject": "forecasting",
        "unit": "U3 Pt2",
        "content": "Box-Jenkins 4-step methodology start",
        "duration_hours": 2,
    },

    # ===== MAY 13 — FORECASTING DAY 2 =====
    {
        "id": "d13u3pt2finish",
        "date": "May 13",
        "day": "Wed",
        "time": "12 PM – 1 PM",
        "subject": "forecasting",
        "unit": "U3 Pt2 finish",
        "content": "Box-Jenkins 4-step, ARIMA identification tables",
        "duration_hours": 1,
    },
    {
        "id": "d13u4",
        "date": "May 13",
        "day": "Wed",
        "time": "2 PM – 4 PM",
        "subject": "forecasting",
        "unit": "U4",
        "content": "Multiple regression inference, t-test, F-test, Chow test",
        "duration_hours": 2,
    },
    {
        "id": "d13u5pt1",
        "date": "May 13",
        "day": "Wed",
        "time": "5 PM – 7 PM",
        "subject": "forecasting",
        "unit": "U5 Pt1",
        "content": "Spurious regression, cointegration, Dickey-Fuller tests",
        "duration_hours": 2,
    },
    {
        "id": "d13u5pt2",
        "date": "May 13",
        "day": "Wed",
        "time": "8 PM – 11 PM",
        "subject": "forecasting",
        "unit": "U5 Pt2",
        "content": "ECM derivation, Granger causality F-test, Johansen test",
        "duration_hours": 3,
    },
    {
        "id": "d13u3pt3",
        "date": "May 14",
        "day": "Thu",
        "time": "12 AM – 1 AM",
        "subject": "forecasting",
        "unit": "U3 Pt3",
        "content": "Derivation drills — AR/MA mean/variance/ACF, Ljung-Box, AIC/SBC",
        "duration_hours": 1,
    },

    # ===== MAY 14 — DTE DAY 1 =====
    {
        "id": "d14u1pt1",
        "date": "May 14",
        "day": "Thu",
        "time": "12 PM – 2:30 PM",
        "subject": "dte",
        "unit": "U1 Pt1",
        "content": "Demographics, transition phases, age distributions",
        "duration_hours": 2.5,
    },
    {
        "id": "d14u1pt2",
        "date": "May 14",
        "day": "Thu",
        "time": "3 PM – 5:30 PM",
        "subject": "dte",
        "unit": "U1 Pt2",
        "content": "Fertility choice, missing markets, gender bias, growth models",
        "duration_hours": 2.5,
    },
    {
        "id": "d14u2",
        "date": "May 14",
        "day": "Thu",
        "time": "6 PM – 8:30 PM",
        "subject": "dte",
        "unit": "U2",
        "content": "Harris-Todaro model, China case study",
        "duration_hours": 2.5,
    },
    {
        "id": "d14u3pt1",
        "date": "May 14",
        "day": "Thu",
        "time": "9 PM – 12 AM",
        "subject": "dte",
        "unit": "U3 Pt1",
        "content": "Land markets, tenancy contracts, Marshallian analysis",
        "duration_hours": 3,
    },

    # ===== MAY 15 — DTE DAY 2 (bed by 12 AM) =====
    {
        "id": "d15u3pt2",
        "date": "May 15",
        "day": "Fri",
        "time": "12 PM – 3 PM",
        "subject": "dte",
        "unit": "U3 Pt2",
        "content": "Sharecropping inefficiency, credit markets",
        "duration_hours": 3,
    },
    {
        "id": "d15u4",
        "date": "May 15",
        "day": "Fri",
        "time": "4 PM – 6 PM",
        "subject": "dte",
        "unit": "U4",
        "content": "Ostrom commons, Todaro institutions",
        "duration_hours": 2,
    },
    {
        "id": "d15rev12",
        "date": "May 15",
        "day": "Fri",
        "time": "7 PM – 9 PM",
        "subject": "dte",
        "unit": "Revise U1+U2",
        "content": "Formulas, key arguments, Harris-Todaro derivations",
        "duration_hours": 2,
    },
    {
        "id": "d15rev34",
        "date": "May 15",
        "day": "Fri",
        "time": "9:30 PM – 11 PM",
        "subject": "dte",
        "unit": "Revise U3+U4",
        "content": "Marshallian inefficiency, Ostrom, key concepts",
        "duration_hours": 1.5,
    },

    # ===== MAY 16 — DTE EXAM 9AM → FORECASTING REVISION (start 4 PM) =====
    {
        "id": "d16dte-pre",
        "date": "May 16",
        "day": "Sat",
        "time": "6 AM – 8 AM",
        "subject": "dte",
        "unit": "Pre-Exam",
        "content": "Light DTE formula review (pre-exam)",
        "duration_hours": 2,
    },
    {
        "id": "d16u5pt2",
        "date": "May 16",
        "day": "Sat",
        "time": "4 PM – 7 PM",
        "subject": "forecasting",
        "unit": "U5 Pt2 review",
        "content": "ECM derivation, Granger causality — write from memory",
        "duration_hours": 3,
    },
    {
        "id": "d16u6",
        "date": "May 16",
        "day": "Sat",
        "time": "8 PM – 9:30 PM",
        "subject": "forecasting",
        "unit": "U6 review",
        "content": "Qualitative methods — Delphi, groupthink, biases memory dump",
        "duration_hours": 1.5,
    },
    {
        "id": "d16rev12",
        "date": "May 16",
        "day": "Sat",
        "time": "10 PM – 1 AM",
        "subject": "forecasting",
        "unit": "Revise U1+U2",
        "content": "Formula drill + numerical problems",
        "duration_hours": 3,
    },
    {
        "id": "d16rev3",
        "date": "May 17",
        "day": "Sun",
        "time": "2 AM – 4 AM",
        "subject": "forecasting",
        "unit": "Revise U3",
        "content": "ARIMA identification tables, derivation drills",
        "duration_hours": 2,
    },

    # ===== MAY 17 — FORECASTING REVISION (bed by 12 AM) =====
    {
        "id": "d17rev45",
        "date": "May 17",
        "day": "Sun",
        "time": "12 PM – 3 PM",
        "subject": "forecasting",
        "unit": "Revise U4+U5",
        "content": "Chow/F-test problems, ECM flow, cointegration steps",
        "duration_hours": 3,
    },
    {
        "id": "d17num",
        "date": "May 17",
        "day": "Sun",
        "time": "4 PM – 7 PM",
        "subject": "forecasting",
        "unit": "Full formula drill",
        "content": "Write all formulas from memory, numericals",
        "duration_hours": 3,
    },
    {
        "id": "d17weak",
        "date": "May 17",
        "day": "Sun",
        "time": "8 PM – 9:30 PM",
        "subject": "forecasting",
        "unit": "Weak areas",
        "content": "Anything shaky + U6 memory verification",
        "duration_hours": 1.5,
    },
    {
        "id": "d17final",
        "date": "May 17",
        "day": "Sun",
        "time": "10 PM – 11:30 PM",
        "subject": "forecasting",
        "unit": "Final Cram",
        "content": "Formula table + Section strategy mental run-through",
        "duration_hours": 1.5,
    },

    # ===== MAY 18 — FORECASTING EXAM 9AM → CAUSAL (start 4 PM) =====
    {
        "id": "d18fore-pre",
        "date": "May 18",
        "day": "Mon",
        "time": "6 AM – 8 AM",
        "subject": "forecasting",
        "unit": "Pre-Exam",
        "content": "Light Forecasting formula review (pre-exam)",
        "duration_hours": 2,
    },
    {
        "id": "d18cau1",
        "date": "May 18",
        "day": "Mon",
        "time": "4 PM – 7 PM",
        "subject": "causal",
        "unit": "U1",
        "content": "Potential outcomes, ATE/ATT/ATU, SUTVA, CIA, selection bias",
        "duration_hours": 3,
    },
    {
        "id": "d18cau2",
        "date": "May 18",
        "day": "Mon",
        "time": "8 PM – 10 PM",
        "subject": "causal",
        "unit": "U2",
        "content": "Research design, RCTs, SDO decomposition, validity",
        "duration_hours": 2,
    },
    {
        "id": "d18cau3pt1",
        "date": "May 19",
        "day": "Tue",
        "time": "11 PM – 2 AM",
        "subject": "causal",
        "unit": "U3 Pt1",
        "content": "Logit/probit, marginal effects, odds ratios",
        "duration_hours": 3,
    },
    {
        "id": "d18cau3pt2",
        "date": "May 19",
        "day": "Tue",
        "time": "2:30 AM – 4 AM",
        "subject": "causal",
        "unit": "U3 Pt2",
        "content": "IV, Wald, 2SLS, LATE, weak instruments",
        "duration_hours": 1.5,
    },

    # ===== MAY 19 — CAUSAL DAY 2 (bed by 12 AM) =====
    {
        "id": "d19u3pt2cont",
        "date": "May 19",
        "day": "Tue",
        "time": "12 PM – 3 PM",
        "subject": "causal",
        "unit": "U3 Pt2 cont",
        "content": "Weak instruments deeper, 2SLS problems, LATE calculations",
        "duration_hours": 3,
    },
    {
        "id": "d19u4pt1",
        "date": "May 19",
        "day": "Tue",
        "time": "4 PM – 7 PM",
        "subject": "causal",
        "unit": "U4 Pt1",
        "content": "Matching, PSM, DiD — parallel trends, 2x2 tables",
        "duration_hours": 3,
    },
    {
        "id": "d19u4pt2",
        "date": "May 19",
        "day": "Tue",
        "time": "8 PM – 10 PM",
        "subject": "causal",
        "unit": "U4 Pt2",
        "content": "RDD sharp/fuzzy, FE within, Hausman test",
        "duration_hours": 2,
    },
    {
        "id": "d19final",
        "date": "May 19",
        "day": "Tue",
        "time": "10:30 PM – 11:30 PM",
        "subject": "causal",
        "unit": "All Units",
        "content": "Key formulas + assumptions + pitfalls cram",
        "duration_hours": 1,
    },

    # ===== MAY 20 — CAUSAL EXAM 9AM =====
    {
        "id": "d20cau-pre",
        "date": "May 20",
        "day": "Wed",
        "time": "6 AM – 8 AM",
        "subject": "causal",
        "unit": "Pre-Exam",
        "content": "Light formula + assumptions review (pre-exam)",
        "duration_hours": 2,
    },
]

# Total blocks
TOTAL_BLOCKS = len(TIMETABLE)

# Subject metadata
SUBJECTS = {
    "forecasting": {
        "label": "Forecasting",
        "color": "#00C853",
        "emoji": "🟢",
        "exam_date": "May 18, 9 AM",
        "exam_name": "ECON053",
    },
    "dte": {
        "label": "Development Theory",
        "color": "#FFB300",
        "emoji": "🟡",
        "exam_date": "May 16, 9 AM",
        "exam_name": "ECON017",
    },
    "causal": {
        "label": "Causal Inference",
        "color": "#2979FF",
        "emoji": "🔵",
        "exam_date": "May 20, 9 AM",
        "exam_name": "ECON056",
    },
}

# Exam structure for display in the app
EXAM_STRUCTURE = {
    "forecasting": {
        "label": "Forecasting (ECON053)",
        "emoji": "🟢",
        "total_marks": 90,
        "sections": [
            {"name": "Section 1", "marks": 10, "units": ["U1"], "type": "Compulsory"},
            {"name": "Section 2", "marks": 30, "units": ["U2", "U4"], "type": "Internal choice within each"},
            {"name": "Section 3", "marks": 40, "units": ["U3", "U5"], "type": "Internal choice within each"},
            {"name": "Section 4", "marks": 10, "units": ["U6"], "type": "Compulsory"},
        ],
    },
    "dte": {
        "label": "Development Theory (ECON017)",
        "emoji": "🟡",
        "total_marks": 100,
        "sections": [
            {"name": "Q1", "marks": 25, "units": ["U1"], "type": "Internal choice"},
            {"name": "Q2", "marks": 25, "units": ["U2"], "type": "Internal choice"},
            {"name": "Q3", "marks": 25, "units": ["U3"], "type": "Internal choice"},
            {"name": "Q4", "marks": 25, "units": ["U4"], "type": "Internal choice"},
        ],
    },
    "causal": {
        "label": "Causal Inference (ECON056)",
        "emoji": "🔵",
        "total_marks": 90,
        "sections": [
            {"name": "Compulsory", "marks": 18, "units": ["U1", "U2"], "type": "1 question, no choice"},
            {"name": "Choice", "marks": 72, "units": ["U3", "U4"], "type": "4 out of 5 questions (18 each)"},
        ],
    },
}

# Pre-defined user list
ADMIN_USER = "hkay"
DEFAULT_USERS = [ADMIN_USER, "mayank", "rishabh", "aniket", "ashi"]

# Display names mapping
USER_DISPLAY_NAMES = {
    "hkay": "HKay",
    "mayank": "Mayank",
    "rishabh": "Rishabh",
    "aniket": "Aniket",
    "ashi": "Ashi",
}

# Admin username

def get_blocks_by_date():
    """Returns dict of date -> list of blocks, sorted by time."""
    by_date = {}
    for block in TIMETABLE:
        date = block["date"]
        if date not in by_date:
            by_date[date] = []
        by_date[date].append(block)
    # Sort each date's blocks by time (daytime before nighttime)
    for date in by_date:
        by_date[date].sort(key=lambda b: (b["time"].split(" ")[0], b["time"]))
    return by_date

def get_blocks_by_subject(subject):
    """Returns list of blocks for a given subject."""
    return [b for b in TIMETABLE if b["subject"] == subject]

def get_subject_stats(user_done_list):
    """Returns dict of subject -> (done_count, total_count)"""
    stats = {}
    for subj in SUBJECTS:
        subj_blocks = [b["id"] for b in TIMETABLE if b["subject"] == subj]
        done = len(set(user_done_list) & set(subj_blocks))
        stats[subj] = (done, len(subj_blocks))
    return stats