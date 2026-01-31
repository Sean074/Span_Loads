#!/bin/bash

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages from requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Launch main.py
python main.py