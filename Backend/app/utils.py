import pandas as pd

def load_skills_from_csv(file_path: str) -> pd.DataFrame:
    """
    Load skills from a CSV file and return as a DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing skills.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading skills from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def save_dataframe_to_pickle(df: pd.DataFrame, file_path: str):
    """
    Save a DataFrame to a pickle file.
    
    Args:
        df (pd.DataFrame): DataFrame to save.
        file_path (str): Path to the pickle file.
    """
    try:
        df.to_pickle(file_path)
    except Exception as e:
        print(f"Error saving DataFrame to {file_path}: {e}")

def load_dataframe_from_pickle(file_path: str) -> pd.DataFrame:
    """
    Load a DataFrame from a pickle file.
    
    Args:
        file_path (str): Path to the pickle file.
    
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        return pd.read_pickle(file_path)
    except Exception as e:
        print(f"Error loading DataFrame from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
