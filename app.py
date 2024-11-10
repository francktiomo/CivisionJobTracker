from flask import Flask, jsonify
import requests
import pandas as pd
from datetime import datetime, timedelta
from logger import setup_logger

app = Flask(__name__)
LOGGER = setup_logger(name=__name__)

API_BASE_URL = 'https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search'

HEADERS = {
    'Authorization': 'Bearer sUUZNpUiFdo5VNuqceJiTYgq7uE',
    'Accept': 'application/json'
}

@app.route('/fetch_today_jobs', methods=['GET'])
def fetch_jobs():
    """
    Fetch jobs postings for the current day
    """
    try:
        params = {
            "publieeDepuis": "1",
            "sort": "1"
        }
        response = requests.get(API_BASE_URL, headers=HEADERS, params=params)
        LOGGER.info(f"Fetched {len(response.json()['resultats'])} jobs")
        return response.json()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/job_stats', methods=['GET'])
def job_stats():
    """
    Generate statistics from a sample job dataset
    """
    try:
        params = {
            'minCreationDate': (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%dT%H:%M:%SZ"),
            'maxCreationDate': (datetime.now()).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        response = requests.get(API_BASE_URL, headers=HEADERS, params=params)
        LOGGER.info(f"Fetched {len(response.json()['resultats'])} jobs")
        offers = response.json().get('resultats', [])
        df_offers = pd.DataFrame(offers)

        # Compute stats
        if not df_offers.empty:
            df_offers['departement'] = df_offers['lieuTravail'].apply(lambda x: x.get('commune', '')[:2])
            stats_par_departement = df_offers['departement'].value_counts().to_dict()

            LOGGER.info("Job statistics by department:")
            LOGGER.info(stats_par_departement)

        return response.json()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
