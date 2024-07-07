import requests
import os
from dotenv import load_dotenv

load_dotenv()

mmpos_api_url = "https://api.mmpos.eu/api/v1"
mmpos_api_key = os.getenv("MMPOS_API_KEY")

print(f"MMPOS_API_KEY: {mmpos_api_key[:4]}********")

def get_farm_id():
    headers = {
        "X-API-Key": mmpos_api_key,
        "Content-Type": "application/json"
    }
    response = requests.get(f"{mmpos_api_url}/farms", headers=headers)
    
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")
    
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return data[0]["id"]
            else:
                print("No farms found.")
                return None
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON response")
            return None
    else:
        print("Failed to fetch farms data:", response.status_code, response.text)
        return None

def main():
    farm_id = get_farm_id()
    if farm_id:
        print(f"Farm ID: {farm_id}")
    else:
        print("Failed to retrieve the Farm ID.")

if __name__ == "__main__":
    main()
