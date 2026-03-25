# utils.py
import logging
import os
import json
import pandas as pd
from datetime import datetime
from api_service.config import Config

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_environment_variable(key):
    """Get environment variable or raise ValueError if not set."""
    try:
        return os.environ[key]
    except KeyError:
        raise ValueError(f"Environment variable '{key}' not set")

def get_config():
    """Load application configuration from environment variables."""
    config = Config()
    config.api_key = get_environment_variable("API_KEY")
    config.api_url = get_environment_variable("API_URL")
    config.db_name = get_environment_variable("DB_NAME")
    config.db_user = get_environment_variable("DB_USER")
    config.db_password = get_environment_variable("DB_PASSWORD")
    return config

def convert_date(date_string):
    """Convert date string to datetime object."""
    return datetime.strptime(date_string, "%Y-%m-%d")

def load_data(file_path):
    """Load data from CSV file."""
    return pd.read_csv(file_path)

def save_data(data, file_path):
    """Save data to CSV file."""
    data.to_csv(file_path, index=False)

def load_json(file_path):
    """Load JSON data from file."""
    with open(file_path, "r") as file:
        return json.load(file)

def save_json(data, file_path):
    """Save JSON data to file."""
    with open(file_path, "w") as file:
        json.dump(data, file)