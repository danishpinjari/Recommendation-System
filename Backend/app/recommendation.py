import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load data
data = pickle.load(open('current_skills.pkl', 'rb'))
similarity_percentage_df = pickle.load(open('similarity_scores.pkl', 'rb'))

def get_user_skills(user_id):
    assigned_skills = data.columns[data.loc[user_id] == 1].tolist()
    return assigned_skills

def get_unique_similar_users(user_id, threshold=20.0):
    """
    Get unique similar users for a specific user with a similarity score above the threshold.
    """
    similarity_percentages = similarity_percentage_df[user_id]
    similar_users = similarity_percentages[similarity_percentages >= threshold].to_dict()
    
    # Remove the user itself from the dictionary
    if user_id in similar_users:
        del similar_users[user_id]  
    
    return {user_id: similar_users}

def recommend_skills(user_id, similarity_threshold=20.0):
    similar_users_with_scores = get_unique_similar_users(user_id, similarity_threshold)
    user_skills = set(get_user_skills(user_id))

    recommended_skills = set()
    user_scores = {}

    for similar_user, scores in similar_users_with_scores[user_id].items():
        similar_user_skills = set(get_user_skills(similar_user))
        new_skills = similar_user_skills - user_skills
        recommended_skills.update(new_skills)
        user_scores[similar_user] = scores

    return recommended_skills, user_scores

def add_new_user(new_user_id, current_skills, similarity_threshold=90.0):
    # Create a row for the new user in the existing DataFrame with current skills
    new_user_row = pd.Series(0, index=data.columns)
    for skill in current_skills:
        if skill in new_user_row.index:
            new_user_row[skill] = 1
    data.loc[new_user_id] = new_user_row

    # Recompute cosine similarity with the new user added
    cosine_sim = cosine_similarity(data)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=data.index, columns=data.index)
    similarity_percentage_matrix = cosine_sim_df * 100
    similarity_percentage_df = pd.DataFrame(similarity_percentage_matrix, index=data.index, columns=data.index)

    # Save updated DataFrames to pickle files
    with open('current_skills.pkl', 'wb') as f:
        pickle.dump(data, f)

    with open('similarity_scores.pkl', 'wb') as f:
        pickle.dump(similarity_percentage_df, f)

    # Recommend skills for the new user
    recommended_skills, user_scores = recommend_skills(new_user_id, similarity_threshold)
    return recommended_skills, user_scores
