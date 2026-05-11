"""
app.py — Exam Study Timetable Tracker
Streamlit app with JSONBin.io backend for multi-user progress tracking.
Dark mode. Admin: hkay. 5 users total.
Features: Weekly grid, day cards, block checklist, per-user progress.
"""

import streamlit as st
import requests
from datetime import datetime

from timetable_data import (
    TIMETABLE, SUBJECTS, ADMIN_USER, get_blocks_by_date, get_subject_stats
)

# ─────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="Exam Study Tracker",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

JSONBIN_BASE = "https://api.jsonbin.io/v3"
try:
    API_KEY = st.secrets["jsonbin_api_key"]
    BIN_ID = st.secrets["jsonbin_bin_id"]
except Exception:
    import os
    API_KEY = os.environ.get("JSONBIN_API_KEY", "")
    BIN_ID = os.environ.get("JSONBIN_BIN_ID", "")

JSONBIN_URL = f"{JSONBIN_BASE}/b/{BIN_ID}" if BIN_ID else None

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def load_data():
    if not JSONBIN_URL or not API_KEY:
        return None
    try:
        r = requests.get(
            JSONBIN_URL,
            headers={"X-Master-Key": API_KEY},
            timeout=10,
        )
        r.raise_for_status()
        return r.json().get("record", {})
    except Exception:
        return None

def save_data(data):
    if not JSONBIN_URL or not API_KEY:
        return False
    try:
        requests.put(
            JSONBIN_URL,
            json=data,
            headers={"X-Master-Key": API_KEY},
            timeout=10,
        )
        return True
    except Exception:
        return False

def init_user(data, username):
    if username not in data.get("users", {}):
        data["users"][username] = {
            "role": "user",
            "name": username,
            "done": [],
            "last_seen": datetime.utcnow().isoformat(),
        }

def get_user_done(data, username):
    return data.get("users", {}).get(username, {}).get("done", [])

def update_user_done(data, username, done_list):
    if username in data.get("users", {}):
        data["users"][username]["done"] = done_list
        data["users"][username]["last_seen"] = datetime.utcnow().isoformat()
        data["metadata"]["last_updated"] = datetime.utcnow().isoformat()

def get_time_band(time_str):
    """Classify a block's start time into a time band for the grid."""
    start = time_str.split("–")[0].strip()
    if ":" in start:
        num = int(start.split(":")[0])
        meridiem = start.split()[-1]
    else:
        parts = start.split()
        num = int(parts[0])
        meridiem = parts[1] if len(parts) > 1 else ""
    if meridiem == "AM":
        if num == 12 or num <= 5:
            return "night"
        return "morning"
    if num == 12 or num <= 4:
        return "afternoon"
    if num <= 9:
        return "evening"
    return "night"

BAND_ORDER = ["morning", "afternoon", "evening", "night"]
BAND_LABELS = {
    "morning": "☀️ Morning",
    "afternoon": "🌤️ Afternoon",
    "evening": "🌙 Evening",
    "night": "⭐ Night",
}

DATE_ORDER = [
    "May 12", "May 13", "May 14", "May 15",
    "May 16", "May 17", "May 18", "May 19", "May 20",
]

def get_block_band_map():
    """Returns a dict: date -> band -> list of blocks for that band."""
    m = {}
    for d in DATE_ORDER:
        m[d] = {b: [] for b in BAND_ORDER}
    for block in TIMETABLE:
        band = get_time_band(block["time"])
        m[block["date"]][band].append(block)
    return m

def build_weekly_grid():
    """Build static HTML/CSS weekly overview grid."""
    band_map = get_block_band_map()

    subj_colors = {
        "forecasting": "#00C853",
        "dte": "#FFB300",
        "causal": "#2979FF",
    }
    bg_colors = {
        "forecasting": "rgba(0,200,83,0.15)",
        "dte": "rgba(255,179,0,0.15)",
        "causal": "rgba(41,121,255,0.15)",
    }
    exam_dates = {
        "May 16": ("📝 DTE", "#FFB300", "rgba(255,179,0,0.2)"),
        "May 18": ("📝 Forecasting", "#00C853", "rgba(0,200,83,0.2)"),
        "May 20": ("📝 Causal", "#2979FF", "rgba(41,121,255,0.2)"),
    }

    cols = '<col>'
    for _ in DATE_ORDER:
        cols += '<col>'

    head = '<tr><th style="position:sticky;left:0;z-index:2;background:#0E1117;min-width:55px;font-size:10px;color:#9BA4B4;text-align:center;padding:4px;">Band</th>'
    for d in DATE_ORDER:
        day_names = {"May 12": "Tue", "May 13": "Wed", "May 14": "Thu", "May 15": "Fri",
                     "May 16": "Sat", "May 17": "Sun", "May 18": "Mon", "May 19": "Tue", "May 20": "Wed"}
        dn = day_names[d]
        is_exam = d in exam_dates
        exam_label, _, _ = exam_dates.get(d, ("", "", ""))
        if is_exam:
            head += f'<th style="font-size:11px;padding:4px;text-align:center;color:#FAFAFA;font-weight:600;">{dn}<br><span style="font-size:9px;">{d.split()[1]}</span></th>'
        else:
            head += f'<th style="font-size:11px;padding:4px;text-align:center;color:#9BA4B4;">{dn}<br><span style="font-size:9px;">{d.split()[1]}</span></th>'

    thead = f'<thead>{head}</thead>'
    tbody = '<tbody>'

    for band in BAND_ORDER:
        lbl = BAND_LABELS[band]
        tbody += f'<tr><td style="font-size:9px;color:#9BA4B4;text-align:center;padding:4px;position:sticky;left:0;background:#0E1117;z-index:1;">{lbl}</td>'
        for d in DATE_ORDER:
            blocks = band_map[d][band]
            cell = ""
            is_exam = d in exam_dates
            exam_label, exam_color, exam_bg = exam_dates.get(d, ("", "", ""))

            if is_exam and band == "morning":
                cell += f'<div style="font-size:9px;font-weight:600;color:{exam_color};background:{exam_bg};padding:3px 5px;border-radius:4px;text-align:center;">{exam_label}</div>'
            if band == "morning" and d == "May 16":
                cell += '<div style="font-size:8px;color:#9BA4B4;padding:2px;text-align:center;">6-8AM review</div>'
            if band == "morning" and d == "May 18":
                cell += '<div style="font-size:8px;color:#9BA4B4;padding:2px;text-align:center;">6-8AM review</div>'
            if band == "morning" and d == "May 20":
                cell += '<div style="font-size:8px;color:#9BA4B4;padding:2px;text-align:center;">6-8AM review</div>'

            for b in blocks:
                s = b["subject"]
                sc = subj_colors[s]
                sbg = bg_colors[s]
                short = b["unit"].split()[0]
                tr = b["time"]
                dur = b.get("duration_hours", 0)
                cell += f'<div style="font-size:8px;color:{sc};background:{sbg};padding:2px 4px;border-radius:3px;margin:2px 0;line-height:1.3;"><b>{short}</b> {dur}h<br><span style="font-size:7px;color:#9BA4B4;">{tr}</span></div>'

            if not cell:
                cell = '<div style="height:6px;"></div>'

            bg = exam_bg if (is_exam and band == "morning") else "rgba(255,255,255,0.03)"
            tbody += f'<td style="background:{bg};vertical-align:top;padding:4px;border:1px solid rgba(255,255,255,0.06);border-radius:4px;">{cell}</td>'
        tbody += '</tr>'

    tbody += '</tbody>'

    html = f"""
    <style>
    .week-grid {{ width:100%; border-collapse:separate; border-spacing:3px; font-family:system-ui,sans-serif; }}
    .week-grid th {{ border-bottom:1px solid rgba(255,255,255,0.1); }}
    .week-grid td {{ min-width:72px; max-width:85px; }}
    .week-grid td:first-child {{ min-width:55px; max-width:55px; }}
    </style>
    <table class="week-grid">
      {thead}
      {tbody}
    </table>
    """
    return html

# ─────────────────────────────────────────────
# Session state init
# ─────────────────────────────────────────────

if "username" not in st.session_state:
    try:
        params = st.experimental_get_query_params()
        st.session_state.username = params.get("user", [""])[0]
    except Exception:
        st.session_state.username = ""

if "done" not in st.session_state:
    st.session_state.done = []
if "data" not in st.session_state:
    st.session_state.data = None
if "_first_load" not in st.session_state:
    st.session_state._first_load = True

# ─────────────────────────────────────────────
# Load data
# ─────────────────────────────────────────────

if st.session_state.data is None:
    st.session_state.data = load_data()

# ─────────────────────────────────────────────
# UI Starts
# ─────────────────────────────────────────────

st.title("📚 Exam Study Tracker")
st.caption("May 12–20, 2026 · Forecasting · DTE · Causal")

# ───── JSONBin guard ─────

if not JSONBIN_URL or not API_KEY:
    st.warning("⚠️ JSONBin not configured yet!")
    st.markdown("""
    **To enable progress tracking:**
    1. Sign up free at [jsonbin.io](https://jsonbin.io)
    2. Create a new bin and note the Bin ID + API Key
    3. Set in Streamlit Cloud: `Settings → Secrets`
       ```toml
       jsonbin_api_key = "your-master-key"
       jsonbin_bin_id = "your-bin-id"
       ```
    """)
    st.stop()

# ───── Sidebar ─────

with st.sidebar:
    st.subheader("👤 Your Profile")
    username_input = st.text_input(
        "Enter your name",
        value=st.session_state.username,
        placeholder="e.g. alice",
        help="Case-sensitive. Bookmark your URL after entering.",
    )

    if username_input:
        st.session_state.username = username_input
        try:
            st.experimental_set_query_params(user=username_input)
        except Exception:
            pass
        if st.session_state.data:
            init_user(st.session_state.data, username_input)
            st.session_state.done = get_user_done(st.session_state.data, username_input)

    st.divider()
    st.subheader("🔍 Filter")
    filter_choice = st.radio(
        "Show subject",
        options=["All", "Forecasting", "DTE", "Causal"],
        index=0,
        horizontal=True,
    )
    st.divider()
    if st.button("🗑️ Reset My Progress"):
        if st.session_state.username and st.session_state.data:
            st.session_state.done = []
            update_user_done(st.session_state.data, st.session_state.username, [])
            save_data(st.session_state.data)
            st.rerun()

# ─────────────────────────────────────────────
# 1. WEEKLY GRID
# ─────────────────────────────────────────────

if st.session_state.data is None:
    st.error("Could not load JSONBin data. Check your API key and Bin ID.")
    st.stop()

with st.container():
    st.markdown("### 📊 Week at a Glance")
    grid_html = build_weekly_grid()
    st.markdown(grid_html, unsafe_allow_html=True)
    st.caption("Hover over a block for details · 📝 = Exam day")

st.divider()

# ─────────────────────────────────────────────
# 2. PROGRESS BARS
# ─────────────────────────────────────────────

user_done = st.session_state.done
stats = get_subject_stats(user_done)

cols = st.columns(3)
for i, (subj, (done, total)) in enumerate(stats.items()):
    meta = SUBJECTS[subj]
    pct = int(100 * done / total) if total > 0 else 0
    with cols[i]:
        st.markdown(f"**{meta['emoji']} {meta['label']}**")
        st.progress(pct / 100, text=f"{done}/{total} blocks ({pct}%)")
        st.caption(f"Exam: {meta['exam_date']}")

# Share link
if st.session_state.username:
    st.caption(f"🔗 Your URL: `?user={st.session_state.username}` — bookmark this!")
else:
    st.info("Enter your name in the sidebar to get a shareable link.")

st.divider()

# ─────────────────────────────────────────────
# 3. ADMIN DASHBOARD
# ─────────────────────────────────────────────

if st.session_state.username == ADMIN_USER:
    st.markdown("### ⚙️ Admin Dashboard — All Users")
    users_data = st.session_state.data.get("users", {})
    admin_rows = []
    for u_name, u_info in users_data.items():
        u_done = u_info.get("done", [])
        u_stats = get_subject_stats(u_done)
        total_done = len(u_done)
        total_possible = len(TIMETABLE)
        overall_pct = int(100 * total_done / total_possible) if total_possible else 0
        last_seen = u_info.get("last_seen", "never")
        try:
            last_dt = datetime.fromisoformat(last_seen)
            diff = datetime.utcnow() - last_dt
            if diff.total_seconds() < 60:
                ago = "just now"
            elif diff.total_seconds() < 3600:
                ago = f"{int(diff.total_seconds()/60)}m ago"
            else:
                ago = f"{int(diff.total_seconds()/3600)}h ago"
        except Exception:
            ago = last_seen
        admin_rows.append({
            "user": u_name,
            "role": "👑" if u_info.get("role") == "admin" else "👤",
            "done": total_done,
            "pct": f"{overall_pct}%",
            "🟢": u_stats.get("forecasting", (0, 0))[0],
            "🟡": u_stats.get("dte", (0, 0))[0],
            "🔵": u_stats.get("causal", (0, 0))[0],
            "last_seen": ago,
        })
    admin_rows.sort(key=lambda x: x["done"], reverse=True)
    st.dataframe(admin_rows, use_container_width=True, hide_index=True)
    st.caption(f"Total blocks: {len(TIMETABLE)}")
    if st.button("🔄 Refresh"):
        st.session_state.data = load_data()
        st.rerun()
    st.divider()

# ─────────────────────────────────────────────
# 4. DAY CARDS WITH CHECKLIST
# ─────────────────────────────────────────────

st.markdown("### 📅 Study Schedule")

by_date = get_blocks_by_date()

filter_map = {
    "All": None,
    "Forecasting": "forecasting",
    "DTE": "dte",
    "Causal": "causal",
}
active_filter = filter_map[filter_choice]

exam_labels = {
    "May 16": "📝 DTE EXAM — 9:00 AM",
    "May 18": "📝 FORECASTING EXAM — 9:00 AM",
    "May 20": "📝 CAUSAL EXAM — 9:00 AM",
}

subj_badge_colors = {
    "forecasting": {"bg": "rgba(0,200,83,0.15)", "text": "#00C853", "emoji": "🟢"},
    "dte": {"bg": "rgba(255,179,0,0.15)", "text": "#FFB300", "emoji": "🟡"},
    "causal": {"bg": "rgba(41,121,255,0.15)", "text": "#2979FF", "emoji": "🔵"},
}

for d in DATE_ORDER:
    if d not in by_date:
        continue
    blocks = by_date[d]
    if active_filter:
        blocks = [b for b in blocks if b["subject"] == active_filter]
    if not blocks:
        continue

    first = blocks[0]
    day_name = first["day"]
    is_exam = d in exam_labels
    exam_label = exam_labels.get(d, "")

    # Day header
    header = f"**{d} ({day_name})**"
    if is_exam:
        header += f" — {exam_label}"
    else:
        # Show primary subject for the day
        subjects_today = set(b["subject"] for b in blocks)
        subj_names = []
        for s in ["forecasting", "dte", "causal"]:
            if s in subjects_today:
                subj_names.append(SUBJECTS[s]["emoji"] + " " + SUBJECTS[s]["label"])
        total_h = sum(b.get("duration_hours", 0) for b in blocks)
        header += f" — {', '.join(subj_names)} — {total_h}h of blocks"

    with st.expander(f"📅 {header}", expanded=False):
        for block in blocks:
            block_id = block["id"]
            is_done = block_id in user_done
            subj = block["subject"]
            badge = subj_badge_colors[subj]
            time_str = block["time"]
            unit_str = block["unit"]
            content_str = block["content"]
            dur = block.get("duration_hours", 0)

            rows = st.columns([0.4, 3.5, 0.6])

            with rows[0]:
                checked = st.checkbox(
                    "✅" if is_done else "",
                    value=is_done,
                    key=f"chk_{block_id}",
                    label_visibility="collapsed",
                )

            with rows[1]:
                if is_done:
                    st.markdown(
                        f"<span style='color:#4A5568;font-size:13px;'>"
                        f"<span style='background:{badge['bg']};color:{badge['text']};padding:1px 6px;border-radius:3px;font-size:11px;font-weight:600;'>{badge['emoji']} {unit_str}</span> "
                        f"<span style='text-decoration:line-through;'>[{time_str}] {content_str}</span>"
                        f"</span>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"<span style='font-size:13px;'>"
                        f"<span style='background:{badge['bg']};color:{badge['text']};padding:1px 6px;border-radius:3px;font-size:11px;font-weight:600;'>{badge['emoji']} {unit_str}</span> "
                        f"<span style='color:#FAFAFA;'>[{time_str}]</span> "
                        f"<span style='color:#E0E0E0;'>{content_str}</span>"
                        f"</span>",
                        unsafe_allow_html=True,
                    )

            with rows[2]:
                st.caption(f"{dur}h")

            # Handle checkbox change
            if checked != is_done:
                if checked:
                    if block_id not in st.session_state.done:
                        st.session_state.done.append(block_id)
                else:
                    st.session_state.done = [x for x in st.session_state.done if x != block_id]
                if st.session_state.username and st.session_state.data:
                    update_user_done(
                        st.session_state.data,
                        st.session_state.username,
                        st.session_state.done,
                    )
                    save_data(st.session_state.data)

            st.markdown(
                "<div style='height:1px;background:rgba(255,255,255,0.04);margin:4px 0;'></div>",
                unsafe_allow_html=True,
            )

# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────

st.markdown("---")
st.caption(
    "📚 Exam Study Tracker · May 12–20, 2026 · "
    f"Total: {len(TIMETABLE)} blocks · "
    "Built with Streamlit + JSONBin"
)