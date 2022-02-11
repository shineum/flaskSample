# Init virtual environment
python3 -m venv venv

# Activate virtual environment
### Windows
venv\Scripts\activate

### MacOS or Linux
source venv/bin/activate

# Install package
(venv) pip3 install flask

# Set environment variable
### Windows
(venv) set FLASK_APP=app

### MacOS or Linux
(venv) export FLASK_APP=app

# Run flask app (with port option)
(venv) flask run -p 5000