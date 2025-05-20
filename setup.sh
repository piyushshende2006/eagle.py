#!/bin/bash

echo "📦 Setting up EAGLE Toolkit..."

# Make sure pip is available
if ! command -v pip &> /dev/null; then
    echo "🔧 Installing pip..."
    sudo apt update && sudo apt install -y python3-pip
fi

# Install all required packages globally (safe for personal use)
pip install --break-system-packages --upgrade pip
pip install --break-system-packages -r requirements.txt

# Run the tool
echo "✅ Setup complete! Launching EAGLE..."
python3 eagle.py
