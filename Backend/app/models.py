from pydantic import BaseModel
from typing import List, Dict

# Model for the request to recommend skills
class RecommendSkillsRequest(BaseModel):
    user_id: str
    similarity_threshold: float = 20.0

# Model for the response of recommended skills
class RecommendSkillsResponse(BaseModel):
    recommended_skills: List[str]
    user_scores: Dict[str, float]

# Model for adding a new user
class AddUserRequest(BaseModel):
    new_user_id: str
    current_skills: List[str]
    similarity_threshold: float = 90.0

# Model for the response after adding a new user
class AddUserResponse(BaseModel):
    recommended_skills: List[str]
    user_scores: Dict[str, float]
