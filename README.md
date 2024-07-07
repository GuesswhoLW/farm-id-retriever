# Hive OS Farm ID Retriever

This Python script retrieves the Farm ID from Hive OS using the Hive OS API.

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/GuesswhoLW/showHiveFarmID.py.git
    cd hive-os-farm-id-retriever
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

4. Create a `.env` file in the root directory of the project and add your Hive OS API key:
    ```
    HIVE_OS_API_KEY=your_hive_os_api_key
    ```

## Usage

Run the script:
```sh
python showHiveFarmID.py
