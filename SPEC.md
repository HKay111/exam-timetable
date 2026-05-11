# Exam Timetable App — Technical Specification

## Overview

A live, shareable exam study timetable for 5 users (1 admin + 4 friends) tracking progress across 3 exams over 8 days (May 12-20, 2026).

**Stack:** Python 3 + Streamlit + JSONBin.io (free tier)  
**Design:** Dark mode only  
**URL:** TBD after Streamlit Cloud deployment

---

## Architecture

### Data Flow

```
User checks a block
        ↓
Streamlit app reads JSONBin → updates session state
        ↓
User unchecks → app writes new state to JSONBin
        ↓
All users see their own checked blocks (persisted across sessions)
Admin (hkay) sees all users' progress via dashboard
```

### Storage: JSONBin.io

Free JSON storage API. No SQL needed.

- **1 bin** stores all data
- App reads/writes via `requests` library
- No authentication required for reads (public bin)
- API key required for writes

**Initial JSONBin structure:**

```json
{
  "metadata": {
    "created": "2026-05-12T00:00:00Z",
    "last_updated": "2026-05-12T00:00:00Z"
  },
  "users": {
    "hkay": {
      "role": "admin",
      "name": "Hkay",
      "done": [],
      "last_seen": "2026-05-12T00:00:00Z"
    }
  }
}
```

**Done field format:** Array of block IDs, e.g. `["d12u1", "d12u2pt1", "d13u3pt1"]`

### File Structure

```
exam-timetable/
├── app.py                 # Main Streamlit application (~250 lines)
├── timetable_data.py     # All 8 days of schedule as Python list of dicts
├── requirements.txt       # Dependencies
├── README.md             # Setup + usage guide
├── SPEC.md               # This file
└── .streamlit/
    └── config.toml       # Dark theme + app config
```

---

## Features

### 1. User Login (Dropdown selection)

- Dropdown selection from predefined user list (HKay, Mayank, Rishabh, Aniket, Ashi)
- No password required, case-insensitive
- Admin username = `hkay` (hardcoded)
- URL updates to `?user=yourname` — bookmark this to persist
- Each user auto-initializes in JSONBin on first load (no manual setup)
- If username exists, their progress loads from JSONBin

### 2. Main Timetable View

- Grouped by date (May 12 → May 20)
- Each day shows all study blocks with:
  - Subject color badge (🟢 Forecasting / 🟡 DTE / 🔵 Causal)
  - Time block (e.g., "12 PM – 3 PM")
  - Unit label (e.g., "U1", "U2 Pt1")
  - Content description
  - Checkbox (checked = done)
- Completed blocks shown with strikethrough text + muted color
- Subject filter: "All" / "Forecasting" / "DTE" / "Causal"
- "Reset my progress" button (clears only this user's checks in JSONBin)

### 3. Progress Summary (Top of page)

Per subject, shown as:
```
🟢 Forecasting:  8 / 22 blocks done (36%)
🟡 DTE:          5 / 14 blocks done (36%)
🔵 Causal:       0 / 12 blocks done (0%)
```

### 4. Admin Dashboard (only visible to user=`hkay`)

- Table of all users
- For each user: name, role, total blocks done, % per subject, last seen timestamp
- "Refresh" button to pull latest from JSONBin
- "View All" expands to show which specific blocks each user has checked

### 5. Sharing

- User selects their name from the dropdown. URL updates to `?user=yourname`.
- Copy button next to the shareable URL
- Friends open URL, see their name auto-selected in dropdown, track their own progress

---

## Block ID Schema

Each block has a unique ID: `{date_short}{unit_label}`

| ID | Date | Unit | Content |
|:---|:---|:---|:---|
| `d12u1` | May 12 | U1 | Six considerations... |
| `d12u2pt1` | May 12 | U2 Pt1 | MA, SMA, WMA... |
| `d12u2pt2` | May 12 | U2 Pt2 | Holt-Winters... |
| `d12u2pt3` | May 12 | U2 Pt3 | Numerical practice... |
| `d13u3pt1` | May 13 | U3 Pt1 | Stationarity, AR(p)... |
| ... | ... | ... | ... |
| `d20-u1` | May 20 | U1 | Pre-exam review |

Date short format: `d12` = May 12, `d13` = May 13, ..., `d20` = May 20

---

## UI Design (Dark Mode)

### Color Palette

| Element | Color | Hex |
|:---|:---|:---|
| Background | Near black | `#0E1117` |
| Card/surface | Dark grey | `#1E2530` |
| Forecasting | Green | `#00C853` |
| DTE | Yellow/Orange | `#FFB300` |
| Causal | Blue | `#2979FF` |
| Text primary | White | `#FAFAFA` |
| Text secondary | Grey | `#9BA4B4` |
| Checked/muted | Dim grey | `#4A5568` |
| Admin badge | Purple | `#9C27B0` |

### Typography

- Streamlit default (Roboto family)
- Headers: Bold, larger size
- Body: Regular weight

### Layout

```
┌──────────────────────────────────────────┐
│  📚 Exam Study Tracker    [hkay] [⚙️]   │
│  ──────────────────────────────────────  │
│  [Your name: ____________] [→]          │
│  Share: https://.../?user=yourname          │
├──────────────────────────────────────────┤
│  🟢 Forecasting   8/22  ████░░░░░ 36%     │
│  🟡 DTE          5/14  ████░░░░░ 36%     │
│  🔵 Causal       0/12  ░░░░░░░░░  0%     │
├──────────────────────────────────────────┤
│  [Filter: All ▼]  [Reset Mine]  [Share] │
├──────────────────────────────────────────┤
│  ▼ May 12 (Tue) — Forecasting            │
│    ☑ 12–2 PM  [U1] Six considerations... │
│    ☐  5–8 PM  [U2 Pt1] MA, SMA...        │
│    ☐  9–12 AM [U2 Pt2] Holt-Winters...  │
│    ☐  1–4 AM  [U2 Pt3] Numerical...      │
│  ▶ May 13 (Wed) — Forecasting            │
│  ...                                     │
├──────────────────────────────────────────┤
│  [Admin Dashboard] (only if user=hkay)   │
│  ┌────────────────────────────────────┐  │
│  │ User     | Done | %    | Last seen   │  │
│  │ hkay     | 13   | 27%  | 2 min ago  │  │
│  └────────────────────────────────────┘  │
└──────────────────────────────────────────┘
```

---

## API Integration

### JSONBin.io Endpoints

- **Read:** `GET https://api.jsonbin.io/v3/b/{BIN_ID}`
- **Write:** `PUT https://api.jsonbin.io/v3/b/{BIN_ID}`
  - Headers: `X-Master-Key: {API_KEY}`

### App reads on load:
```python
response = requests.get(f"{BASE_URL}/{BIN_ID}", headers={"X-Master-Key": API_KEY})
data = response.json()["record"]
```

### App writes on checkbox change:
```python
# Update user's done list in data
data["users"][username]["done"] = user_done_list
data["users"][username]["last_seen"] = datetime.utcnow().isoformat()

# Write back
requests.put(f"{BASE_URL}/{BIN_ID}",
             json=data,
             headers={"X-Master-Key": API_KEY})
```

---

## Configuration

### Streamlit Secrets (for deployment)

File: `.streamlit/secrets.toml`
```toml
jsonbin_api_key = "your-jsonbin-master-key"
jsonbin_bin_id = "your-jsonbin-bin-id"
```

In Streamlit Cloud, these are set via the web UI (Settings → Secrets).

### Environment Variables (local development)

```bash
export JSONBIN_API_KEY="your-key"
export JSONBIN_BIN_ID="your-bin-id"
```

Or use `.env` file with `python-dotenv`.

---

## Update Workflow

1. User messages HKay: "done with U3 of Forecasting, shift X to Y"
2. HKay edits `timetable_data.py` (the Python schedule)
3. HKay commits + pushes to GitHub
4. Streamlit Cloud auto-redeploys in ~30 seconds

---

## Tech Decisions

| Decision | Choice | Reason |
|:---|:---|:---|
| Backend DB | JSONBin.io (free) | No SQL, no backend, free tier enough for 5 users |
| Auth | Free-text username | No passwords, no OAuth complexity |
| Persistence | URL params + JSONBin | Bookmarkable, shareable, persistent |
| State management | Streamlit session_state | Built-in, works across reruns |
| Deployment | Streamlit Community Cloud | Free, easy, auto-deploys from GitHub |
| Theme | Dark mode only | User requested dark mode |

---

## User Stories

1. **Friend opens the app for the first time**
   - Selects their name from the dropdown → sees empty timetable with all boxes unchecked
   - Checks "d12u1" → JSONBin updates, box gets strikethrough
   - They bookmark the URL or copies share link

2. **Friend returns to their progress from yesterday**
   - Pastes URL with `?user=theirname` → their checks from yesterday are restored, their name auto-selected in dropdown
   - They uncheck a block they didn't actually finish → JSONBin updates

3. **HKay (admin) checks everyone's progress**
   - Selects "HKay" from dropdown → admin dashboard visible
   - Sees each user's blocks done and last_seen timestamps

---

*Spec version: 1.0 — Created May 12, 2026*