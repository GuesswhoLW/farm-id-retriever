# Hive OS and mmpOS Farm ID Retriever

This Python project retrieves the Farm IDs from Hive OS and mmpOS using their respective APIs.

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/farm-id-retriever.git
    cd farm-id-retriever
    ```

2. Create a virtual environment and activate it (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your Hive OS API key and mmPOS API key:
    ```
    HIVE_OS_API_KEY=your_hive_os_api_key
    MMPOS_API_KEY=your_mmpos_api_key
    ```

## Usage

Run the scripts:
```sh
python showHiveFarmID.py
```

## Support
  If you find this small project helpful and would like to support my work and future projects, feel free to donate a cup of coffee to my Spectre wallet:
  ```sh
  spectre:qr7nl6z8nc8gmagarmzrnaw90xu2xxzzn8qtg2wql967njendf5eqeqdnmhuc
