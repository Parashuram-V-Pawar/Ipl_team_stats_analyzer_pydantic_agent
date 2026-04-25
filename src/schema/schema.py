from pydantic import BaseModel

class TeamAnalysis(BaseModel):
    team: str
    summary: str