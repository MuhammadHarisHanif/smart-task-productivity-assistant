
# Smart Task Productivity Assistant

An AI-powered task management assistant built with Python, Flask, LangChain, Groq, and SQLite.

## Features

- Create tasks with title, due date, and priority.
- View pending and completed tasks.
- Update task status.
- AI-powered interaction using a LangChain agent.
- Conversation history stored in SQLite.
- Session-based chat memory.
- Web-based chatbot interface.

## Technologies Used

- Python
- Flask
- LangChain
- Groq API
- SQLite
- HTML, CSS, JavaScript

## Project Structure

```text
End-to-End Agent/
├── app.py
├── agent.py
├── tools.py
├── database.py
├── memory.py
├── requirements.txt
├── .env
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project folder:

   ```bash
   cd "End-to-End Agent"
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate it on Windows:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Create a `.env` file and add your Groq API key:

   ```text
   GROQ_API_KEY=your_groq_api_key
   ```

7. Run the application:

   ```bash
   python app.py
   ```

8. Open the application:

   http://127.0.0.1:5000

## Security

- Never upload your `.env` file or API key.
- Keep your virtual environment out of Git.
- Do not upload private user data.

## Author

NIAI Course Project
