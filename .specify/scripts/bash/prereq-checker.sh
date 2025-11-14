#!/usr/bin/env bash

# Proactive prerequisite checker for AI-native repository setup
# Usage: ./prereq-checker.sh [--json]

set -e

JSON_MODE=false
if [ "$1" == "--json" ]; then
  JSON_MODE=true
fi

# Function to check command existence
check_command() {
  if command -v "$1" &> /dev/null; then
    echo "true"
  else
    echo "false"
  fi
}

# Check Python version
python_version=$(python3 --version 2>&1 | cut -d " " -f 2 | cut -d "." -f 1,2)
if [[ "$python_version" < "3.12" ]]; then
  python_ok=false
else
  python_ok=true
fi

# Check Node.js version
node_version=$(node --version 2>&1 | cut -d "v" -f 2 | cut -d "." -f 1)
if [[ "$node_version" -lt 20 ]]; then
  node_ok=false
else
  node_ok=true
fi

# Check other commands
npm_ok=$(check_command npm)
uv_ok=$(check_command uv)
git_ok=$(check_command git)

# Check mem0ai (requires venv active, but check globally for simplicity)
mem0_ok=$(python3 -c "import mem0" 2>/dev/null && echo "true" || echo "false")

# Check disk space (500MB = 500000 kB)
disk_space=$(df . | tail -1 | awk '{print $4}')
if [[ "$disk_space" -lt 500000 ]]; then
  disk_ok=false
else
  disk_ok=true
fi

if [ "$JSON_MODE" = true ]; then
  jq -n --arg python "$python_ok" --arg node "$node_ok" --arg npm "$npm_ok" --arg uv "$uv_ok" --arg git "$git_ok" --arg mem0 "$mem0_ok" --arg disk "$disk_ok" \
    '{python: $python == "true", node: $node == "true", npm: $npm == "true", uv: $uv == "true", git: $git == "true", mem0ai: $mem0 == "true", disk_space: $disk == "true"}'
else
  echo "Python 3.12+: $python_ok"
  echo "Node.js 20+: $node_ok"
  echo "NPM: $npm_ok"
  echo "uv: $uv_ok"
  echo "Git: $git_ok"
  echo "mem0ai: $mem0_ok"
  echo "Disk Space (500MB+): $disk_ok"
fi

if [ "$python_ok" = false ] || [ "$node_ok" = false ] || [ "$npm_ok" = false ] || [ "$uv_ok" = false ] || [ "$git_ok" = false ] || [ "$mem0_ok" = false ] || [ "$disk_ok" = false ]; then
  exit 1
fi