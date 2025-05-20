#!/bin/bash

echo "📦 Setting up EAGLE Toolkit..."

# Step 1: Install python3-venv if not available
if ! dpkg -s python3-venv >/dev/null 2>&1; then
    echo "🔧 Installing python3-venv..."
    sudo apt update && sudo apt install -y python3-venv
fi

# Step 2: Create virtual environment
python3 -m venv venv

# Step 3: Activate virtual environment
source venv/bin/activate

# Step 4: Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Setup complete!"
echo "👉 Run the tool with: source venv/bin/activate && python eagle.py"
