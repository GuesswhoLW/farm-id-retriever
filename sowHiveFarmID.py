import requests
import os
from dotenv import load_dotenv

load_dotenv()

hive_os_api_url = "https://api2.hiveos.farm/api/v2"
hive_os_api_key = os.getenv("HIVE_OS_API_KEY")

print(f"HIVE_OS_API_KEY: {hive_os_api_key[:4]}********")

def get_farm_id():
    headers = {
        "Authorization": f"Bearer {hive_os_api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{hive_os_api_url}/farms", headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            return data["data"][0]["id"]
        else:
            print("No farms found.")
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
