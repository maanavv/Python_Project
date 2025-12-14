# CyberSocial — Terminal Social Media UI (Textual)

CyberSocial is a **terminal-based social media interface** built using **Python** and the **Textual** framework.  
It demonstrates how modern, content-driven application layouts (feeds, posts, chats, widgets) can be implemented entirely inside a terminal.

This project focuses on **UI architecture, interaction design, and state management** in a Textual TUI environment.

---

## ✨ Features

### Interface
- Three-panel layout:
  - **Left panel** — Navigation (Home, Chats)
  - **Center panel** — Post feed, post detail view, and chat view
  - **Right panel** — Widgets (clock, notifications)

### Social Interactions
- View a feed of posts
- Open posts in a detailed view
- Like posts
- Add comments to posts
- Simple chat interface (mock conversation)

### Usability
- Scrollable feed
- Keyboard support (`ESC` to return from post view)
- Real-time clock widget
- Clean black-and-white UI for clarity

---

## 🧠 Design Goals

CyberSocial was designed to:

- Explore how **GUI-style layouts** translate to terminal UIs
- Practice **event-driven UI programming** in Textual
- Build a **non-trivial TUI** beyond menus or dashboards
- Maintain a **single-file, readable architecture**

The project intentionally avoids backend complexity to stay focused on UI behavior and interaction.

---

## 🛠 Tech Stack

- **Python 3.9+**
- **Textual** — TUI framework
- **Rich** — Terminal rendering engine

---

## 🚀 Getting Started

### Installation

```bash
pip install textual rich
