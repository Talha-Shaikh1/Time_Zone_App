# Time Zone Converter App

This is a simple Streamlit app that allows users to:
- View the current time in multiple time zones.
- Convert time between different time zones.

## Features
- Select multiple time zones to display current time.
- Convert a user-input time from one time zone to another.
- Uses Python's `datetime` and `zoneinfo` modules for accurate time conversion.

## Installation

### 1. Clone the repository
```sh
git clone https://github.com/Talha-Shaikh1/Time_Zone_App.git
cd Time_Zone_App
```

### 2. Create and activate virtual environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

## Usage
Run the Streamlit app using:
```sh
streamlit run main.py
```

Replace `app.py` with the actual file name if different.

## Requirements
### Dependencies
The following dependencies are required:
```
streamlit
zoneinfo
```

All required dependencies are listed in `requirements.txt`.

## License
This project is open-source and available under the MIT License.
