include .env
export

.PHONY: init run test build clean

init:
    @echo "Installing dependencies..."
    pip install -r requirements.txt

run:
    @echo "Running Flask app on port ${FLASK_RUN_PORT}..."
    python app.py

test:
    @echo "Running unit tests..."
    python -m unittest test.py

build:
    @echo "Building Docker image..."
    docker build -t health-calculator:latest .

clean:
    @echo "Cleaning cache..."
    find . -type d -name "__pycache__" -exec rm -rf {} +
