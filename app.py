"""
app.py — Exam Study Timetable Tracker
Streamlit app with JSONBin.io backend for multi-user progress tracking.
Dark mode. Admin: hkay. 5 users total.
"""

import streamlit as st
import requests
from datetime import datetime
from urllib.parse import parse_qs

from timetable_data import (
    TIMETABLE, SUBJECTS, ADMIN_USER, DEFAULT_USERS,
    get_blocks_by_date, get_subject_stats
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

# JSONBin config (set via Streamlit secrets or env vars)
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
    """Load full JSONBin record."""
    if not JSONBIN_URL or not API_KEY:
        return None
    try:
        r = requests.get(JSONBIN_URL, headers={"X-Master-Key": API_KEY}, timeout=10)
        r.raise_for_status()
        return r.json().get("record", {})
    except Exception:
        return None

def save_data(data):
    """Write full record back to JSONBin."""
    if not JSONBIN_URL or not API_KEY:
        return False
    try:
        requests.put(
            JSONBIN_URL,
            json=data,
            headers={"X-Master-Key": API_KEY},
            timeout=10
        )
        return True
    except Exception:
        return False

def init_user(data, username):
    """Ensure user exists in data."""
    if username not in data.get("users", {}):
        data["users"][username] = {
            "role": "user",
            "name": username,
            "done": [],
            "last_seen": datetime.utcnow().isoformat(),
        }

def get_user_done(data, username):
    """Get this user's done list."""
    return data.get("users", {}).get(username, {}).get("done", [])

def update_user_done(data, username, done_list):
    """Update user's done list and last_seen."""
    if username in data.get("users", {}):
        data["users"][username]["done"] = done_list
        data["users"][username]["last_seen"] = datetime.utcnow().isoformat()
        data["metadata"]["last_updated"] = datetime.utcnow().isoformat()

def get_shareable_url(username):
    """Returns the current page URL with user param."""
    try:
        return f"?user={username}"
    except Exception:
        return f"?user={username}"

# ─────────────────────────────────────────────
# Session state init
# ─────────────────────────────────────────────

if "username" not in st.session_state:
    # Try to get from query params
    try:
        params = st.experimental_get_query_params()
        st.session_state.username = params.get("user", [""])[0]
    except Exception:
        st.session_state.username = ""

if "done" not in st.session_state:
    st.session_state.done = []

if "data" not in st.session_state:
    st.session_state.data = None

# ─────────────────────────────────────────────
# Load data on start
# ─────────────────────────────────────────────

if st.session_state.data is None:
    st.session_state.data = load_data()

# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────

st.title("📚 Exam Study Tracker")
st.caption("May 12–20, 2026 · Forecasting · DTE · Causal")

# ─────────────────────────────────────────────
# JSONBin Setup (if not configured)
# ─────────────────────────────────────────────

if not JSONBIN_URL or not API_KEY:
    st.warning("⚠️ JSONBin not configured yet!")
    st.markdown("""
    **To enable progress tracking:**
    1. Sign up free at [jsonbin.io](https://jsonbin.io)
    2. Create a new bin and note the Bin ID + API Key
    3. Set these in Streamlit Cloud: `Settings → Secrets`
       ```toml
       jsonbin_api_key = "your-master-key"
       jsonbin_bin_id = "your-bin-id"
       ```
    4. Or export as env vars locally:
       ```bash
       export JSONBIN_API_KEY="..."
       export JSONBIN_BIN_ID="..."
       ```
    """)
    st.stop()

# ─────────────────────────────────────────────
# User login
# ─────────────────────────────────────────────

with st.sidebar:
    st.subheader("👤 Your Profile")

    username_input = st.text_input(
        "Enter your name",
        value=st.session_state.username,
        placeholder="e.g. alice",
        help="Case-sensitive. Enter your name to load your progress.",
    )

    if username_input:
        st.session_state.username = username_input
        try:
            st.experimental_set_query_params(user=username_input)
        except Exception:
            pass

        # Ensure user exists in data
        if st.session_state.data:
            init_user(st.session_state.data, username_input)
            st.session_state.done = get_user_done(st.session_state.data, username_input)

    st.divider()

    # Subject filter
    st.subheader("🔍 Filter")
    filter_choice = st.radio(
        "Show subject",
        options=["All", "Forecasting", "DTE", "Causal"],
        index=0,
        horizontal=True,
    )

    st.divider()

    # Reset button
    if st.button("🗑️ Reset My Progress"):
        if st.session_state.username and st.session_state.data:
            st.session_state.done = []
            update_user_done(st.session_state.data, st.session_state.username, [])
            save_data(st.session_state.data)
            st.rerun()
        st.warning("Reset! Refresh to confirm.")

# ─────────────────────────────────────────────
# Progress summary bars
# ─────────────────────────────────────────────

st.markdown("### 📊 Progress")

if st.session_state.data is None:
    st.error("Could not load JSONBin data. Check your API key and Bin ID.")
    st.stop()

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
st.divider()
st.markdown("### 🔗 Share Your Progress")
current_user = st.session_state.username
if current_user:
    share_url = f"?user={current_user}"
    st.code(share_url, language=None)
    st.caption("Bookmark this URL to save your progress!")
else:
    st.info("Enter your name above to get a shareable link.")

st.divider()

# ─────────────────────────────────────────────
# Admin dashboard (only for hkay)
# ─────────────────────────────────────────────

if st.session_state.username == ADMIN_USER:
    st.markdown("### ⚙️ Admin Dashboard — All Users")

    users_data = st.session_state.data.get("users", {})
    all_users = list(users_data.keys())

    admin_data = []
    for u_name, u_info in users_data.items():
        u_done = u_info.get("done", [])
        u_stats = get_subject_stats(u_done)
        total_done = len(u_done)
        total_possible = len(TIMETABLE)
        overall_pct = int(100 * total_done / total_possible) if total_possible else 0
        last_seen = u_info.get("last_seen", "never")
        try:
            last_dt = datetime.fromisoformat(last_seen)
            ago = str(datetime.utcnow() - last_dt).split(".")[0] + " ago"
        except Exception:
            ago = last_seen

        # Per-subject
        subj_pcts = {
            s: f"{d}/{t} ({int(100*d/t)}%)"
            for s, (d, t) in u_stats.items()
        }

        admin_data.append({
            "user": u_name,
            "role": u_info.get("role", "user"),
            "total_done": total_done,
            "pct": overall_pct,
            "fore": subj_pcts.get("forecasting", "0/0 (0%)"),
            "dte": subj_pcts.get("dte", "0/0 (0%)"),
            "causal": subj_pcts.get("causal", "0/0 (0%)"),
            "last_seen": ago,
        })

    # Sort by total done desc
    admin_data.sort(key=lambda x: x["total_done"], reverse=True)

    st.dataframe(
        admin_data,
        use_container_width=True,
        hide_index=True,
    )

    st.caption(f"Total blocks in timetable: {len(TIMETABLE)}")

    if st.button("🔄 Refresh from JSONBin"):
        st.session_state.data = load_data()
        st.rerun()

    st.divider()

# ─────────────────────────────────────────────
# Main timetable
# ─────────────────────────────────────────────

st.markdown("### 📅 Study Schedule")

by_date = get_blocks_by_date()
date_order = ["May 12", "May 13", "May 14", "May 15",
               "May 16", "May 17", "May 18", "May 19", "May 20"]

filter_map = {
    "All": None,
    "Forecasting": "forecasting",
    "DTE": "dte",
    "Causal": "causal",
}
active_filter = filter_map[filter_choice]

for date in date_order:
    if date not in by_date:
        continue

    blocks = by_date[date]
    day_blocks = blocks

    # Apply filter
    if active_filter:
        day_blocks = [b for b in day_blocks if b["subject"] == active_filter]
    if not day_blocks:
        continue

    first_block = day_blocks[0]
    day_label = f"{date} ({first_block['day']})"

    with st.expander(f"📆 {day_label} — {len(day_blocks)} blocks", expanded=(date in ["May 12", "May 13"])):
        for block in day_blocks:
            block_id = block["id"]
            subj_meta = SUBJECTS[block["subject"]]

            # Checkbox state
            is_done = block_id in user_done

            col1, col2, col3 = st.columns([1, 4, 1])

            with col1:
                checked = st.checkbox(
                    "✅" if is_done else "☐",
                    value=is_done,
                    key=f"chk_{block_id}",
                )
            with col2:
                # Color badge + unit label + content
                color = subj_meta["color"]
                badge = f":[{color}][{subj_meta['emoji']} {block['unit']}]"
                st.markdown(
                    f":[{color}][**{block['time']}**]{' ~~' if is_done else ''} "
                    f"**{block['content']}**"
                )
                if is_done:
                    st.caption(f"✅ {subj_meta['emoji']} {subj_meta['label']} — {block['unit']}")
                else:
                    st.caption(f"{subj_meta['emoji']} {subj_meta['label']} · {block['unit']}")
            with col3:
                duration_h = block.get("duration_hours", 0)
                st.caption(f"{duration_h}h")

            # Handle checkbox change
            if checked != is_done:
                if checked:
                    if block_id not in st.session_state.done:
                        st.session_state.done.append(block_id)
                else:
                    st.session_state.done = [d for d in st.session_state.done if d != block_id]

                # Persist to JSONBin
                if st.session_state.username and st.session_state.data:
                    update_user_done(
                        st.session_state.data,
                        st.session_state.username,
                        st.session_state.done
                    )
                    saved = save_data(st.session_state.data)
                    if not saved:
                        st.warning("⚠️ Save failed — check your JSONBin connection.")

            st.divider()

# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────

st.markdown("---")
st.caption(
    "📚 Exam Study Tracker · May 12–20, 2026 · "
    f"Total: {len(TIMETABLE)} blocks · "
    "Built with Streamlit + JSONBin"
)