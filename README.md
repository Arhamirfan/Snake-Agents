# 🐍 Snake Game – Autogen Multi-Agent AI Project

This project is a fully functional Snake game, automatically designed, developed, and tested by a team of autonomous agents using the Autogen framework. The AI agents involved include a Planner, Engineer, Quality Assurance (QA), and a Human-in-the-Loop (Admin).

---

## 🎮 Game Overview

- Classic Snake gameplay with arrow-key controls.
- Gain points by consuming food objects.
- The snake grows with each point.
- Win Condition: Collect 20 points within 60 seconds.
- Lose Condition: Fail to reach 20 points in time or collide with self.

---

## 🧠 Agent Roles

| Agent     | Role Description |
|-----------|------------------|
| Planner   | Drafts the game plan, assigns tasks to Engineer and QA. |
| Engineer  | Implements the game logic and UI in Python. |
| QA        | Tests the game, provides bug reports and enhancement suggestions. |
| Admin     | Approves plans and gives final input. |

---

## 📁 Project Structure

    project/
    ├── code/
    │   ├── snake_game.py               # Main game implementation
    │   ├── test_snake_game.py         # Auto-generated QA test scripts
    │   ├── run_game.ps1               # (Optional) PowerShell script to execute the game
    │   └── ...
    ├── README.md                      # Project overview
    ├── .env                           # API keys for LLM
    └── main.py                        # Entry point that initializes the Autogen agents

---

## 🚀 How to Run

### 1. Clone the Repository

    git clone <repo-url>
    cd project

### 2. Install Requirements

    pip install -r requirements.txt

Make sure you have a valid `.env` file with your OpenAI API key:

    OPENAI_API_KEY=your_openai_key

### 3. Run the Game

    python code/snake_game.py

On Windows with PowerShell:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
    .\code\run_game.ps1

---

## 🧪 Testing

To run automated tests:

    python code/test_snake_game.py

These tests were written by the QA agent to ensure:
- Win/lose logic works
- Timer constraints are enforced
- UI elements behave as expected

---

## 🛠️ Built With

- Python
- Autogen multi-agent AI framework
- Pygame for GUI rendering
- PowerShell (optional) for automation

---

## 🤖 AI Contributions

This project is 100% AI-generated, including:
- Game mechanics design
- Code implementation
- GUI layout
- Bug testing and correction
- Documentation and script setup

---

## 📌 Notes

- Execution policies on Windows may block scripts; see `about_Execution_Policies` for details.
- The `code/` folder is automatically populated by the Engineer agent.
- This project demonstrates agent collaboration for software development.

---

## 📞 Contact

If you'd like to learn more about Autogen multi-agent programming, connect with the maintainers of Autogen.
