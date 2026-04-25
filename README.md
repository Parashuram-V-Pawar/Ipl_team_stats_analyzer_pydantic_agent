# IPL Team Stats Analyzer (Pydantic AI)
A simple AI-powered CLI application that analyzes IPL teams using a single-agent architecture built with Pydantic AI and Groq (LLaMA model).

## Features
- Analyze IPL teams (MI, CSK, RCB, KKR, etc.)
- AI-generated insights:
    - Team players overview
    - Probable Playing XI
    - Strategy analysis
    - Batting first vs second comparison
    - Pitch condition performance
- Structured output using Pydantic
- Powered by Groq’s ultra-fast LLaMA models
- Simple CLI interface

## Tech Stack
- Python 3.10+
- Pydantic AI
- python-dotenv
- Groq API (OpenAI-compatible)

## Project Structure
```
Ipl_team_stats_analyzer_pydantic_agent/
|
|-- src/
|   |-- main.py
│   |-- agents/
|   |   |-- __init__.py
|   |   |-- my_agent.py
|   |
│   |-- schema/
|   |   |-- __init__.py
|   |   |-- schema.py
|   |           
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Installation
```
Clone the repository
-> git clone https://github.com/Parashuram-V-Pawar/Ipl_team_stats_analyzer_pydantic_agent.git

Move to project folder
-> cd Ipl_team_stats_analyzer_pydantic_agent

Create Virtual Environment
-> python -m venv venv
-> source venv/bin/activate   # Mac/Linux
-> venv\Scripts\activate      # Windows

Install Dependencies
-> pip install -r requirements.txt

Run project
-> python3 -m src.main.py
```

## Author
```
Parashuram V Pawar
GitHub username: Parashuram-V-Pawar
```
