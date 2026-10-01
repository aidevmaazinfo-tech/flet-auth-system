# 💎 LUXE - Luxury Mobile App

A stylish and luxury-themed mobile application built with **Python** and **Flet**, featuring a complete authentication system (Register / Login) and a premium welcome dashboard.

---

## ✨ Features

- 🔐 **User Authentication**
  - Secure Registration with username, email & password
  - Login with validation
  - Local JSON-based user storage (`users.json`)

- 🎨 **Luxury UI Design**
  - Deep black & gold color theme
  - Elegant gradients and glass-morphism cards
  - Responsive mobile-first layout
  - Premium typography and icons

- 📱 **Screens**
  - **Login Screen** — Dark elegant login with gold accents
  - **Register Screen** — Clean signup form with validation
  - **Welcome Screen** — Luxury dashboard with stats & feature cards

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Backend logic |
| Flet | Cross-platform UI framework |
| JSON | Local data storage |
| Material Icons | UI icons |

---

## 📁 Project Structure

```
task4/
│
├── main.py                  # App entry point & routing
├── auth.py                  # Authentication logic
├── requirements.txt         # Python dependencies
├── users.json               # Auto-generated user database
│
└── screens/
    ├── __init__.py
    ├── login_screen.py      # Login UI
    ├── register_screen.py   # Registration UI
    └── welcome_screen.py    # Welcome Dashboard UI
```

---

## 🚀 Getting Started

### 1. Clone / Setup Project

```bash
cd C:\Hassan\task4
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv mainvenv
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**
```bash
mainvenv\Scripts\activate
```

**Windows (CMD):**
```bash
mainvenv\Scripts\activate.bat
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the App

```bash
python main.py
```

Or using Flet CLI:
```bash
flet run main.py
```

---

## 📱 Mobile Preview

To run in mobile-like window size:

```bash
flet run main.py --android
```

Or simply run `main.py` — the app window is pre-configured to **400×750** pixels for a mobile experience.

---

## 🎨 Color Palette

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Deep Black | `#0A0A0A` | Background |
| Dark Surface | `#1A1A1A` | Cards & inputs |
| Gold | `#D4AF37` | Primary buttons, accents |
| Light Gold | `#FFD700` | Focus states |
| White | `#FFFFFF` | Headings |
| Gray | `#888888` | Subtitles |

---

## 🔐 Default Flow

1. Open app → **Login Screen**
2. New user? → Click **Register** → Create account
3. Existing user? → Enter credentials → **Welcome Screen**
4. Click **Logout** icon → Back to Login

---

## 📝 Notes

- User data is stored locally in `users.json` (no external database needed)
- Passwords are stored in plain text for demo purposes — **DO NOT use in production**
- For production, integrate a proper database (SQLite/PostgreSQL) and hash passwords with `bcrypt`

---

## 🧑‍💻 Author

**Hassan** — Built with ❤️ using Python & Flet

---

## 📄 License

This project is for educational/demo purposes.
