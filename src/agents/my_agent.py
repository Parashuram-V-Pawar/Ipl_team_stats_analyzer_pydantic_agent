from pydantic_ai import Agent
from src.schema.schema import TeamAnalysis
from config.config import MODEL

ipl_agent = Agent(
    MODEL,
    output_type=TeamAnalysis,
    system_prompt="""
You are an IPL team analyzer.

STRICT RULES:
- Return ONLY valid JSON
- No explanations outside JSON

Format:
{
    "team": "RCB | CSK | MI | KKR | Other",
    "summary": "
        - Team players
        - Probable playing 11 (based on recent form in 2026)
        - Strategy analysis
        - Batting first vs second comparison
        - Performance on different pitch conditions
    "
}
"""
)