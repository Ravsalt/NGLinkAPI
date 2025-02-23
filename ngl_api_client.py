import requests
from config import NGL_API_URL
import logging

# Set up logging for the API client
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def submit_to_ngl(username, question, device_id, game_slug, referrer):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    data = {
        'username': username,
        'question': question,
        'deviceId': device_id,
        'gameSlug': game_slug,
        'referrer': referrer
    }

    try:
        logging.info(f"Sending data to NGL API: {data}")
        response = requests.post(NGL_API_URL, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Will raise HTTPError for bad responses
        
        logging.info(f"Received response: {response.status_code} - {response.text}")
        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"Error during API request: {e}")
        return {'error': f"Request failed: {str(e)}"}

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {'error': f"Unexpected error: {str(e)}"}
