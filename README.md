# FRH.365

This repository contains the **Time Capsule** app (⏳).

Write a message, pick an unlock time, and seal it. While sealed you can keep adding entries but cannot view them. When the time arrives, the capsule opens automatically.

> All file names in this repository are ASCII-only on purpose, to avoid filename encoding issues across Windows / browsers / GitHub. The file *contents* are still in Chinese.

## Structure

```
time-capsule/
├── index.html          # Front-end UI (open directly in a browser)
├── launcher.py         # Local-server launcher source
├── README.md           # Full usage guide (Chinese)
├── build.bat           # One-click rebuild script for Windows
└── dist/
    └── time-capsule.exe  # Standalone Windows executable
```

## Quick start

- **Easiest**: double-click `time-capsule/dist/time-capsule.exe`, your browser opens automatically.
- **With Python**: double-click `time-capsule/index.html`.
- **Rebuild**: double-click `time-capsule/build.bat`.

See [time-capsule/README.md](time-capsule/README.md) for the full Chinese guide.

## Features

1. Write content and freely choose the unlock time (with quick presets).
2. While sealed, keep adding entries but never view existing ones.
3. Auto-opens at the chosen time with all memories revealed.
4. Export / import `.capsule` files to move between computers, still encrypted.

Encryption uses browser-native AES-GCM 256-bit. The time lock is software-based and relies on the local system clock.
