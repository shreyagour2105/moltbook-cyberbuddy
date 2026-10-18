# 🛡️ Moltbook CyberBuddy

**An AI-powered cybersecurity agent for Moltbook, built with Python and Google Gemini.**

Moltbook CyberBuddy is a beginner-friendly AI agent designed to explore cybersecurity discussions, generate relevant responses, and publish useful contributions on Moltbook. It combines generative AI with rule-based safety checks and publishing limits to encourage responsible, controlled automation.

## ✨ Features

- **AI-Powered Responses:** Uses Google Gemini to generate context-aware comments on relevant posts.
- **Cybersecurity Focus:** Prioritizes topics such as cybersecurity, Python, AI safety, and secure software development.
- **Safety Validation:** Filters irrelevant or unsuitable drafts before attempting publication.
- **Controlled Automation:** Limits comments and original posts per day.
- **Scheduled Monitoring:** Periodically reviews recent posts.
- **Persistent State:** Uses SQLite to track processed posts and daily publishing counts.
- **Environment-Based Secrets:** Loads API credentials from environment variables instead of hardcoding them.
- **Automated Tests:** Includes tests for safety-related functionality.

## 🧰 Tech Stack

- **Language:** Python
- **AI Model:** Google Gemini
- **API Integration:** Moltbook API
- **Libraries:** `google-genai`, `python-dotenv`, `requests`
- **Database:** SQLite
- **Testing:** pytest

## 📁 Project Structure

```text
moltbook-cyberbuddy/
├── agent.py              # AI response generation
├── moltbook_client.py    # Moltbook API integration
├── safety.py             # Relevance and safety checks
├── scheduler.py          # Scheduled agent execution
├── tests/
│   └── test_safety.py    # Safety validation tests
├── .env.example          # Example environment variables
├── .gitignore            # Excludes secrets and generated files
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shreyagour2105/moltbook-cyberbuddy.git
cd moltbook-cyberbuddy
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file using `.env.example` as a template.

```env
GEMINI_API_KEY=your_gemini_api_key_here
MOLTBOOK_API_KEY=your_moltbook_api_key_here
```

Replace the placeholders with your own credentials. Never commit `.env` or share API keys publicly.

### 5. Run the safety tests

```bash
pytest -q
```

### 6. Run CyberBuddy

```bash
python scheduler.py
```

**Note:** The scheduler may publish comments or posts when publishing is enabled. Review the configuration in `scheduler.py` before running it. Start with controlled testing, and stop execution with `Ctrl+C` when needed.

## 🔐 Safety and Responsible Automation

CyberBuddy includes safeguards intended to make automated interactions more controlled:

- Topic relevance checks before generating or publishing responses.
- Validation of generated text.
- Daily limits for comments and original posts.
- Tracking of previously processed posts.
- API credentials stored in environment variables.

These checks reduce risk but do not guarantee that every generated response is correct or appropriate. API acceptance also does not guarantee that a comment is publicly visible. Any platform verification requirements must be handled through Moltbook's supported process.

## 🚧 Current Limitations

- AI-generated content can be inaccurate or require editing.
- Safety checks are rule-based and cannot detect every possible issue.
- Publishing behavior depends on Moltbook API responses and platform requirements.
- The project is an educational prototype, not a production-grade autonomous security system.

## 🎯 Learning Objectives

This project explores practical applications of:

- Python programming and modular design
- Generative AI and API integration
- Environment variables and credential management
- Input validation and safety checks
- Scheduled automation
- SQLite persistence
- Unit testing and responsible AI development

## 🔮 Future Improvements

- Add structured API response handling and clearer publication-status reporting.
- Introduce a dry-run mode for reviewing drafts without publishing.
- Add stronger prompt-injection defenses and adversarial tests.
- Implement retry handling with safe backoff and duplicate prevention.
- Build a dashboard for reviewing drafts, activity, and safety decisions.
- Add configurable topic filters and human approval before publication.

## 👩‍💻 Author

**Shreya S Gour**  
First-Year Information Science and Engineering Student

Interested in cybersecurity, artificial intelligence, and software development.

---
**Moltbook Profile:** [feheart](https://www.moltbook.com/u/feheart)

*Built as a learning project to explore responsible AI agents and cybersecurity-focused automation.*
