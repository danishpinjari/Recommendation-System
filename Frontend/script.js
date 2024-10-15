// Function to handle skill recommendation for existing users
async function getSkillRecommendations() {
    const userIdInput = document.getElementById('user-id');
    const similarityThresholdInput = document.getElementById('similarity-threshold');
    
    const userId = userIdInput.value.trim();
    const similarityThreshold = similarityThresholdInput.value.trim();

    if (!userId || !similarityThreshold) {
        alert('Please enter both User ID and Similarity Threshold.');
        return;
    }

    try {
        const response = await fetch('/recommend-skills', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId, similarity_threshold: similarityThreshold })
        });

        if (response.ok) {
            const data = await response.json();
            displayRecommendations(data.recommended_skills, data.similar_users_scores);
        } else {
            alert('Error fetching recommendations.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching recommendations.');
    }
}

// Function to display the recommended skills and similar user scores
function displayRecommendations(recommendedSkills, similarUserScores) {
    const recommendationResults = document.getElementById('recommendation-results');
    recommendationResults.innerHTML = '';

    const skillList = document.createElement('ul');
    recommendedSkills.forEach(skill => {
        const listItem = document.createElement('li');
        listItem.textContent = skill;
        skillList.appendChild(listItem);
    });

    recommendationResults.appendChild(document.createElement('h3').textContent = 'Recommended Skills');
    recommendationResults.appendChild(skillList);

    const userScoresSection = document.createElement('div');
    userScoresSection.appendChild(document.createElement('h3').textContent = 'Similar Users & Scores');

    const scoreList = document.createElement('ul');
    Object.entries(similarUserScores).forEach(([user, score]) => {
        const listItem = document.createElement('li');
        listItem.textContent = `User: ${user}, Similarity: ${score}%`;
        scoreList.appendChild(listItem);
    });

    userScoresSection.appendChild(scoreList);
    recommendationResults.appendChild(userScoresSection);
}

// Function to handle adding a new user and recommending skills
async function addNewUser() {
    const newUserIdInput = document.getElementById('new-user-id');
    const newSkillsInput = document.getElementById('new-skills');
    const newSimilarityThresholdInput = document.getElementById('new-user-similarity-threshold');

    const newUserId = newUserIdInput.value.trim();
    const newSkills = newSkillsInput.value.trim().split(',').map(skill => skill.trim());
    const newSimilarityThreshold = newSimilarityThresholdInput.value.trim();

    if (!newUserId || !newSkills.length || !newSimilarityThreshold) {
        alert('Please fill out all fields.');
        return;
    }

    try {
        const response = await fetch('/add-new-user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id: newUserId,
                current_skills: newSkills,
                similarity_threshold: newSimilarityThreshold
            })
        });

        if (response.ok) {
            const data = await response.json();
            displayNewUserResults(data.recommended_skills, data.similar_users_scores);
        } else {
            alert('Error adding new user and fetching recommendations.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while adding the new user.');
    }
}

// Function to display the new user's recommended skills and similar user scores
function displayNewUserResults(recommendedSkills, similarUserScores) {
    const newUserResults = document.getElementById('new-user-results');
    newUserResults.innerHTML = '';

    const skillList = document.createElement('ul');
    recommendedSkills.forEach(skill => {
        const listItem = document.createElement('li');
        listItem.textContent = skill;
        skillList.appendChild(listItem);
    });

    newUserResults.appendChild(document.createElement('h3').textContent = 'Recommended Skills for New User');
    newUserResults.appendChild(skillList);

    const userScoresSection = document.createElement('div');
    userScoresSection.appendChild(document.createElement('h3').textContent = 'Similar Users & Scores');

    const scoreList = document.createElement('ul');
    Object.entries(similarUserScores).forEach(([user, score]) => {
        const listItem = document.createElement('li');
        listItem.textContent = `User: ${user}, Similarity: ${score}%`;
        scoreList.appendChild(listItem);
    });

    userScoresSection.appendChild(scoreList);
    newUserResults.appendChild(userScoresSection);
}
