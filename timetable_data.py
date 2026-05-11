"""
timetable_data.py
All 8 days of study schedule as Python list of dicts.
Block IDs: {date_short}{unit_label} e.g. d12u1, d13u3pt2, d20u1
"""

TIMETABLE = [
    # ===== MAY 12 — FORECASTING DAY 1 =====
    {
        "id": "d12u1",
        "date": "May 12",
        "day": "Tue",
        "time": "12 PM – 2 PM",
        "subject": "forecasting",
        "unit": "U1",
        "content": "Six considerations, loss functions, forecast horizons",
        "duration_hours": 2,
    },
    {
        "id": "d12u2pt1",
        "date": "May 12",
        "day": "Tue",
        "time": "5 PM – 8 PM",
        "subject": "forecasting",
        "unit": "U2 Pt1",
        "content": "MA, SMA, WMA, exponential smoothing",
        "duration_hours": 3,
    },
    {
        "id": "d12u2pt2",
        "date": "May 12",
        "day": "Tue",
        "time": "9 PM – 12 AM",
        "subject": "forecasting",
        "unit": "U2 Pt2",
        "content": "Holt-Winters, decomposition, accuracy metrics",
        "duration_hours": 3,
    },
    {
        "id": "d12u2pt3",
        "date": "May 12",
        "day": "Tue",
        "time": "1 AM – 4 AM",
        "subject": "forecasting",
        "unit": "U2 Pt3",
        "content": "Numerical practice — MAE/MSE/MAPE/Theil's U",
        "duration_hours": 3,
    },

    # ===== MAY 13 — FORECASTING DAY 2 =====
    {
        "id": "d13u3pt1",
        "date": "May 13",
        "day": "Wed",
        "time": "12 PM – 3 PM",
        "subject": "forecasting",
        "unit": "U3 Pt1",
        "content": "Stationarity, AR(p), MA(q), ACF/PACF patterns",
        "duration_hours": 3,
    },
    {
        "id": "d13u3pt2",
        "date": "May 13",
        "day": "Wed",
        "time": "4 PM – 7 PM",
        "subject": "forecasting",
        "unit": "U3 Pt2",
        "content": "Box-Jenkins 4-step, ARIMA identification",
        "duration_hours": 3,
    },
    {
        "id": "d13u3pt3",
        "date": "May 13",
        "day": "Wed",
        "time": "8 PM – 11 PM",
        "subject": "forecasting",
        "unit": "U3 Pt3",
        "content": "Derivation drills — AR/MA mean/variance/ACF, Ljung-Box, AIC/SBC",
        "duration_hours": 3,
    },
    {
        "id": "d13u4",
        "date": "May 13",
        "day": "Wed",
        "time": "12 AM – 3 AM",
        "subject": "forecasting",
        "unit": "U4",
        "content": "Multiple regression inference, t-test, F-test, Chow test",
        "duration_hours": 3,
    },

    # ===== MAY 14 — DTE DAY 1 =====
    {
        "id": "d14u1pt1",
        "date": "May 14",
        "day": "Thu",
        "time": "12 PM – 3 PM",
        "subject": "dte",
        "unit": "U1 Pt1",
        "content": "Demographics, transition phases, age distributions",
        "duration_hours": 3,
    },
    {
        "id": "d14u1pt2",
        "date": "May 14",
        "day": "Thu",
        "time": "4 PM – 7 PM",
        "subject": "dte",
        "unit": "U1 Pt2",
        "content": "Missing markets, gender bias, externalities",
        "duration_hours": 3,
    },
    {
        "id": "d14u1pt3",
        "date": "May 14",
        "day": "Thu",
        "time": "8 PM – 11 PM",
        "subject": "dte",
        "unit": "U1 Pt3",
        "content": "Harrod-Domar, Solow, Boserup/Kremer — growth models",
        "duration_hours": 3,
    },
    {
        "id": "d14u2",
        "date": "May 14",
        "day": "Thu",
        "time": "12 AM – 3 AM",
        "subject": "dte",
        "unit": "U2",
        "content": "Harris-Todaro model, China case study",
        "duration_hours": 3,
    },

    # ===== MAY 15 — DTE DAY 2 (bed by 12 AM) =====
    {
        "id": "d15u3pt1",
        "date": "May 15",
        "day": "Fri",
        "time": "12 PM – 3 PM",
        "subject": "dte",
        "unit": "U3 Pt1",
        "content": "Land markets, tenancy contracts, Marshallian analysis",
        "duration_hours": 3,
    },
    {
        "id": "d15u3pt2",
        "date": "May 15",
        "day": "Fri",
        "time": "4 PM – 7 PM",
        "subject": "dte",
        "unit": "U3 Pt2",
        "content": "Sharecropping inefficiency, credit markets",
        "duration_hours": 3,
    },
    {
        "id": "d15u4",
        "date": "May 15",
        "day": "Fri",
        "time": "8 PM – 10 PM",
        "subject": "dte",
        "unit": "U4",
        "content": "Ostrom commons, Todaro institutions",
        "duration_hours": 2,
    },
    {
        "id": "d15formula",
        "date": "May 15",
        "day": "Fri",
        "time": "10:15 PM – 11:30 PM",
        "subject": "dte",
        "unit": "All Units",
        "content": "All-unit formula + arguments speed-run",
        "duration_hours": 1.25,
    },

    # ===== MAY 16 — DTE EXAM 9AM → FORECASTING (study starts 4 PM) =====
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
        "id": "d16u5pt1",
        "date": "May 16",
        "day": "Sat",
        "time": "4 PM – 7 PM",
        "subject": "forecasting",
        "unit": "U5 Pt1",
        "content": "Spurious regression, cointegration, DF tests",
        "duration_hours": 3,
    },
    {
        "id": "d16u5pt2",
        "date": "May 16",
        "day": "Sat",
        "time": "8 PM – 11 PM",
        "subject": "forecasting",
        "unit": "U5 Pt2",
        "content": "ECM derivation, Granger causality F-test",
        "duration_hours": 3,
    },
    {
        "id": "d16u6u5pt3",
        "date": "May 16",
        "day": "Sat",
        "time": "12 AM – 3 AM",
        "subject": "forecasting",
        "unit": "U6 + U5 Pt3",
        "content": "Delphi, groupthink, biases + Johansen test",
        "duration_hours": 3,
    },
    {
        "id": "d16u3drill",
        "date": "May 16",
        "day": "Sat",
        "time": "3 AM – 4 AM",
        "subject": "forecasting",
        "unit": "U3 Overflow",
        "content": "U3 derivation drills — ARIMA tables, write ECM from memory",
        "duration_hours": 1,
    },

    # ===== MAY 17 — FORECASTING REVISION (bed by 12 AM) =====
    {
        "id": "d17revu1u2",
        "date": "May 17",
        "day": "Sun",
        "time": "12 PM – 3 PM",
        "subject": "forecasting",
        "unit": "Revise U1+U2",
        "content": "Formula drill + numericals",
        "duration_hours": 3,
    },
    {
        "id": "d17revu3u4",
        "date": "May 17",
        "day": "Sun",
        "time": "4 PM – 7 PM",
        "subject": "forecasting",
        "unit": "Revise U3+U4",
        "content": "ARIMA steps + Chow/F-test problems",
        "duration_hours": 3,
    },
    {
        "id": "d17revu5",
        "date": "May 17",
        "day": "Sun",
        "time": "8 PM – 10 PM",
        "subject": "forecasting",
        "unit": "Revise U5",
        "content": "ECM flow, cointegration steps",
        "duration_hours": 2,
    },
    {
        "id": "d17final",
        "date": "May 17",
        "day": "Sun",
        "time": "10:15 PM – 11:30 PM",
        "subject": "forecasting",
        "unit": "Final Cram",
        "content": "U6 bullet points + full formula table",
        "duration_hours": 1.25,
    },

    # ===== MAY 18 — FORECASTING EXAM 9AM → CAUSAL (study starts 4 PM) =====
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
        "id": "d18u1",
        "date": "May 18",
        "day": "Mon",
        "time": "4 PM – 7 PM",
        "subject": "causal",
        "unit": "U1",
        "content": "Potential outcomes, ATE/ATT/ATU, SUTVA, CIA",
        "duration_hours": 3,
    },
    {
        "id": "d18u2",
        "date": "May 18",
        "day": "Mon",
        "time": "8 PM – 10 PM",
        "subject": "causal",
        "unit": "U2",
        "content": "Research design, RCTs, SDO, validity",
        "duration_hours": 2,
    },
    {
        "id": "d18u3pt1",
        "date": "May 18",
        "day": "Mon",
        "time": "11 PM – 2 AM",
        "subject": "causal",
        "unit": "U3 Pt1",
        "content": "Logit/probit, marginal effects, odds ratios",
        "duration_hours": 3,
    },
    {
        "id": "d18u3pt2",
        "date": "May 18",
        "day": "Mon",
        "time": "2:30 AM – 4 AM",
        "subject": "causal",
        "unit": "U3 Pt2",
        "content": "IV, Wald, 2SLS, LATE",
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
        "content": "Weak instruments, problem solving",
        "duration_hours": 3,
    },
    {
        "id": "d19u4pt1",
        "date": "May 19",
        "day": "Tue",
        "time": "4 PM – 7 PM",
        "subject": "causal",
        "unit": "U4 Pt1",
        "content": "Matching, PSM, DiD — parallel trends",
        "duration_hours": 3,
    },
    {
        "id": "d19u4pt2",
        "date": "May 19",
        "day": "Tue",
        "time": "8 PM – 10 PM",
        "subject": "causal",
        "unit": "U4 Pt2",
        "content": "RDD sharp/fuzzy, FE within, Hausman",
        "duration_hours": 2,
    },
    {
        "id": "d19final",
        "date": "May 19",
        "day": "Tue",
        "time": "10:15 PM – 11:30 PM",
        "subject": "causal",
        "unit": "All Units",
        "content": "Formulas + assumptions + pitfalls cram",
        "duration_hours": 1.25,
    },

    # ===== MAY 20 — CAUSAL EXAM 9AM =====
    {
        "id": "d20u1",
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

# Pre-defined user list (5 people)
DEFAULT_USERS = ["hkay", "alice", "bob", "charlie", "diana"]

# Admin username
ADMIN_USER = "hkay"

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