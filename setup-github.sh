#!/bin/bash
# Create GitHub repo and push code

cd ~/.openclaw/workspace/music-player-web

# Initialize git if not already
git init 2>/dev/null

# Add all files
git add .

# Commit
git commit -m "Initial commit for GitHub Pages" 2>/dev/null || echo "Already committed"

# Create repo using gh CLI
echo "Creating GitHub repo..."
gh repo create moose-music-player --public --source=. --remote=origin --push

echo ""
echo "✅ Repo created!"
echo ""
echo "Now enable GitHub Pages:"
echo "1. Go to: https://github.com/moosetheaxie/moose-music-player/settings/pages"
echo "2. Under 'Source', select 'Deploy from a branch'"
echo "3. Select 'main' branch and '/ (root)' folder"
echo "4. Click Save"
echo ""
echo "Your site will be at: https://moosetheaxie.github.io/moose-music-player"
