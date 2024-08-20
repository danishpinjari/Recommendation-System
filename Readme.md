# Skill-Based Recommendation System

This project is a skill-based recommendation system developed using Python. It utilizes a list of user IDs and their associated skills to recommend relevant skills based on the similarity of their skill sets. The project leverages the power of machine learning techniques, specifically cosine similarity, to achieve this.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Introduction

This project is designed to recommend skills to users based on the similarity of their existing skills with other users in the dataset. The core functionality is driven by the `cosine_similarity` metric, which measures the cosine of the angle between two non-zero vectors in a multi-dimensional space. This metric helps in identifying how similar the skill sets of different users are, and based on that, it recommends new skills to users.

## Features

- **User ID Generation**: Generates 1000 unique user IDs.
- **Skill Set Management**: Loads and processes a CSV file containing skills.
- **Skill Recommendation**: Recommends relevant skills to users based on similarity.
- **Data Cleaning**: Removes duplicate skills to ensure data consistency.

## Installation

To run this project, you'll need to have Python installed along with a few libraries. You can install the required libraries using pip:

```bash
pip install pandas numpy scikit-learn
```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/MustafaPinjari/Recommendation-System.git
    cd Recommendation-System
    ```

2. Prepare your environment by installing the necessary libraries.

3. Run the Jupyter Notebook `Recommend.ipynb`:

    ```bash
    jupyter notebook Recommend.ipynb
    ```

4. Follow the cells in the notebook to load the data, generate user IDs, and run the recommendation system.

## Data

The data used in this project is stored in a CSV file named `Skillset.csv`. This file should contain a list of skills that users possess. Make sure the CSV is in the same directory as the notebook for the code to run correctly.

### Sample Data Format

| skills               |
|----------------------|
| Python               |
| Machine Learning     |
| Data Analysis        |
| Statistical Modeling |
| Data Visualization   |

## Contributing

If you wish to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Make sure to document any new features or changes you introduce.

## Credits

This project was developed by [Mustafa Pinjari](https://github.com/MustafaPinjari).

- **GitHub**: [MustafaPinjari](https://github.com/MustafaPinjari)
- **LinkedIn**: [Mustafa Pinjari](https://www.linkedin.com/in/mustafa-pinjari-287625256/)
- **Instagram**: [its_ur_musuuu](https://www.instagram.com/its_ur_musuuu)
- **Email**: unlessuser99@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.

