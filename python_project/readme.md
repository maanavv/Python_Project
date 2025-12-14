# CyberSocial (Textual TUI App)

CyberSocial is a **terminal-based social media interface** built using **Python** and the **Textual** framework.  
It simulates a basic social platform layout (like Twitter/Reddit) entirely inside the terminal.

This project focuses on **UI layout, interaction, and state management in a TUI**, not networking or databases.

---

## Features

### Core UI
- Three-panel layout:
  - **Left panel**: Navigation (Home, Chats)
  - **Center panel**: Post feed / post view / chat view
  - **Right panel**: Widgets (clock, notifications)

### Social Features
- View a feed of posts
- Open a post in detail view
- Like a post
- Add comments to a post
- Simple chat interface (mock conversation)

### Interaction
- Buttons for navigation and actions
- `ESC` key to return from post view to feed
- Live clock widget

---

## Tech Stack

- **Python 3.9+**
- **Textual** (TUI framework)
- **Rich** (rendering backend)

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/cybersocial.git
cd cybersocial
