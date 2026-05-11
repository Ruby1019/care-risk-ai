#!/bin/bash

set -e

echo "======================================"
echo " CareRisk AI - Start Project"
echo "======================================"

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
FRONTEND_DIR="$PROJECT_ROOT/frontend"

echo ""
echo "Checking project files..."

if [ ! -f "$PROJECT_ROOT/run_pipeline.py" ]; then
    echo "Error: run_pipeline.py not found."
    exit 1
fi

if [ ! -d "$PROJECT_ROOT/backend" ]; then
    echo "Error: backend folder not found."
    exit 1
fi

if [ ! -d "$PROJECT_ROOT/data" ]; then
    echo "Error: data folder not found."
    exit 1
fi

if [ ! -d "$FRONTEND_DIR" ]; then
    echo "Error: frontend folder not found."
    exit 1
fi

if [ ! -f "$FRONTEND_DIR/package.json" ]; then
    echo "Error: frontend/package.json not found."
    exit 1
fi

echo "Project files are ready."

echo ""
echo "Step 1: Run automated data pipeline"
cd "$PROJECT_ROOT"

if command -v python3 >/dev/null 2>&1; then
    python3 run_pipeline.py
else
    python run_pipeline.py
fi

echo ""
echo "Step 2: Install frontend dependencies if needed"
cd "$FRONTEND_DIR"

if [ ! -d "node_modules" ]; then
    echo "node_modules not found. Installing frontend dependencies..."
    npm install
else
    echo "Frontend dependencies already installed."
fi

echo ""
echo "Step 3: Start React development server"
echo "After the server starts, open the Local URL shown below."
echo "Usually: http://localhost:5173/"
echo ""

npm run dev