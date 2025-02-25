#!/bin/bash

echo "🚀 Starting Build Process..."

# Step 1: Activate Virtual Environment (if exists, otherwise create)
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate  # For Linux/macOS
# source venv/Scripts/activate  # For Windows (Git Bash)

# Step 2: Install Dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 3: Apply Migrations
echo "📦 Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# Step 4: Collect Static Files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Step 5: Run Server
echo "🚀 Starting Django server..."
python manage.py runserver

echo "✅ Build process complete!"
