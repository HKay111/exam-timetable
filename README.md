# Exam Study Tracker — Setup Guide

A live Streamlit app for tracking 5 friends' exam study progress over May 12-20, 2026.

---

## Quick Start (Local)

```bash
cd exam-timetable
pip install -r requirements.txt
export JSONBIN_API_KEY="your-jsonbin-master-key"
export JSONBIN_BIN_ID="your-jsonbin-bin-id"
streamlit run app.py
```

---

## JSONBin Setup (Required for multi-user persistence)

1. Go to [jsonbin.io](https://jsonbin.io) and sign up (free, 2 minutes)
2. Create a new bin with this initial content:

```json
{
  "metadata": {"created": "2026-05-12T00:00:00Z", "last_updated": "2026-05-12T00:00:00Z"},
  "users": {}
}
```

3. Copy your **Bin ID** from the bin URL (e.g., `https://api.jsonbin.io/v3/b/abc123...` → bin ID = `abc123...`)
4. Copy your **Master Key** from your jsonbin.io account settings

---

## Streamlit Cloud Deployment

1. Fork/push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Deploy — Streamlit auto-detects `app.py`
5. In Streamlit Cloud dashboard: **Settings → Secrets** add:
   ```toml
   jsonbin_api_key = "your-master-key"
   jsonbin_bin_id = "your-bin-id"
   ```
6. Your app is live at `https://your-repo-name.streamlit.app`

---

## Usage

| Action | How |
|:---|:---|
| Start tracking | Enter your name in the sidebar |
| Check a block done | Click the checkbox next to any study block |
| Share with friends | Give them your URL with `?user=yourname` appended |
| Admin dashboard | Log in as `hkay` to see all 5 users' progress |
| Reset your progress | Click "Reset My Progress" in sidebar |

---

## Users

| Username | Role |
|:---|:---|
| `hkay` | Admin (see everyone's progress) |

Any name auto-registers on first use. Enter your name to start tracking.

---

## Files

| File | Purpose |
|:---|:---|
| `app.py` | Main Streamlit app |
| `timetable_data.py` | All schedule data as Python |
| `TIMETABLE.md` | Human-readable timetable reference |
| `SPEC.md` | Technical specification |
| `requirements.txt` | Dependencies |
| `.streamlit/config.toml` | Dark theme config |

---

*Built May 12, 2026 · Streamlit + JSONBin.io*