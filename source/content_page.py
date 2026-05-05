# topics_content.py
# Defines TOPICS list — one dict per topic.
# Each topic has: name, emoji, tag (folder name), images (fallback list).
# 'tag' is used by ContentPage to locate the snaps folder on disk.

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOPICS = [
    {
        "name": "What is a Computer",
        "emoji": "💻",
        "tag": "computer",
        
    },
    {
        "name": "Keyboard & Mouse",
        "emoji": "⌨️",
        "tag": "keyboard and mouse",
       
    },
    {
        "name": "Files & Folders",
        "emoji": "📁",
        "tag": "files and folders",
        
    },
    {
        "name": "Operating System",
        "emoji": "🖥️",
        "tag": "Operating System",
        
    },
    {
        "name": "Text Editors",
        "emoji": "📝",
        "tag": "Text Editors",
       
    },
    {
        "name": "Internet Safety",
        "emoji": "🛡️",
        "tag": "Internet Safety",
        
    },
    {
        "name": "Problem Solving",
        "emoji": "🧩",
        "tag": "Problem Solving",
        
    },
    {
        "name": "Numbers & Logic",
        "emoji": "🔢",
        "tag": "Numbers & Logic",
        
    },
]

