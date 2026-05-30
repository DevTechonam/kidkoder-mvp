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
        "tag": "T1",
        
    },
    {
        "name": "Keyboard & Mouse",
        "emoji": "⌨️",
        "tag": "T2",
       
    },
    {
        "name": "Files & Folders",
        "emoji": "📁",
        "tag": "T3",
        
    },
    {
        "name": "Operating System",
        "emoji": "🖥️",
        "tag": "T4",
        
    },
    {
        "name": "Text Editors",
        "emoji": "📝",
        "tag": "T5",
       
    },
    {
        "name": "Internet Safety",
        "emoji": "🛡️",
        "tag": "T6",
        
    },
    {
        "name": "Problem Solving",
        "emoji": "🧩",
        "tag": "T7",
        
    },
    {
        "name": "Numbers & Logic",
        "emoji": "🔢",
        "tag": "T8",
        
    },
]

