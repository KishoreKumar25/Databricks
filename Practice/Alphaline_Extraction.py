# Databricks notebook source
import requests
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import json

# COMMAND ----------

# API Endpoint URL
api_url = 'https://webservicesv5.axsmarine.com/rest/liner/services/current/regions?token=AImhz38eS52MkpZbz431xH4I2zTsLrlX'

# COMMAND ----------

# Function to fetch data from API
def fetch_data_from_api():
    try:
        response = requests.get(api_url, verify= False)
        response.raise_for_status()  # Check for errors in the HTTP response
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
