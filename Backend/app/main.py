from fastapi import FastAPI
from Backend.app.models import RecommendSkillsRequest, RecommendSkillsResponse, AddUserRequest, AddUserResponse
from Backend.app.recommendation import recommend_skills, add_new_user
from Backend.app.utils import load_dataframe_from_pickle

app = FastAPI()

# Load skills and similarity scores at startup
data = load_dataframe_from_pickle('current_skills.pkl')
similarity_scores = load_dataframe_from_pickle('similarity_scores.pkl')

@app.post("/recommend-skills", response_model=RecommendSkillsResponse)
async def recommend_skills_endpoint(request: RecommendSkillsRequest):
    recommended_skills, user_scores = recommend_skills(request.user_id, request.similarity_threshold)
    return RecommendSkillsResponse(recommended_skills=list(recommended_skills), user_scores=user_scores)

@app.post("/add-user", response_model=AddUserResponse)
async def add_user_endpoint(request: AddUserRequest):
    recommended_skills, user_scores = add_new_user(request.new_user_id, request.current_skills, request.similarity_threshold)
    return AddUserResponse(recommended_skills=list(recommended_skills), user_scores=user_scores)
