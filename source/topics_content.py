import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOPICS = [
    {
        "name": "What is a Computer", "emoji": "💻",
        "tag": "T1",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "compu.jpg"),
             "content": "📚 What is a Computer?\n\nA computer is an electronic device that processes information and helps us solve problems, create things, and connect with others around the world!"},
            {"path": os.path.join(BASE_DIR, "images", "cpu.jpg"),
             "content": "⚙️ Inside the Computer\n\nThis is the CPU (Central Processing Unit) - it's like the brain of the computer! It makes all the decisions and does all the calculations."},
            {"path": os.path.join(BASE_DIR, "images", "monitor.jpeg"),
             "content": "🖥️ Monitor\n\nThe monitor shows us pictures, videos, and everything we do on the computer."},
        ]
    },
    {
        "name": "Keyboard & Mouse", "emoji": "⌨️",
        "tag": "T2",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "keyboard.jpg"),
             "content": "⌨️ Keyboard\n\nThe keyboard is how we type information into the computer. Each key has a letter, number, or special character on it!"},
            {"path": os.path.join(BASE_DIR, "images", "keyboard2.jpg.jpeg"),
             "content": "⌨️ Keyboard\n\nThe keyboard is how we type information into the computer. Each key has a letter, number, or special character on it!"},
            {"path": os.path.join(BASE_DIR, "images", "mouse.jpeg"),
             "content": "🖱️ Mouse\n\nThe mouse helps us move the pointer on the screen and click to open, select, and move things on the computer."},
        ]
    },
{
        "name": "Files & Folders", "emoji": "📁",
        "tag": "T3",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "file.png"),
             "content": "📁 Files & Folders\n\nFiles are like documents and pictures. Folders are like containers that hold multiple files organized together!"},
            {"path": os.path.join(BASE_DIR, "images", "folder.png"),
             "content": "📁 Files & Folders\n\nFiles are like documents and pictures. Folders are like containers that hold multiple files organized together!"},
        ]
    },    {
        "name": "Operating System", "emoji": "🖥️",
        "tag": "T4",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "Osystem.jpg"),
             "content": "🖥️ Operating System\n\nThe Operating System is like a manager! It controls all the programs and makes sure everything works smoothly together."},
            {"path": os.path.join(BASE_DIR, "images", "Osystem2.jpg"),
             "content": "🖥️ Operating System\n\nThe Operating System is like a manager! It controls all the programs and makes sure everything works smoothly together."},
        ]
    },
    {
        "name": "Text Editors", "emoji": "📝",
        "tag": "T5",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "text_editor.jpg"),
             "content": "📝 Text Editors\n\nText editors are programs where you can write and edit text. They're simple tools for creating documents!"},
        ]
    },
    {
        "name": "Internet Safety", "emoji": "🛡️",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "internet.jpg"),
             "content": "🛡️ Internet Safety\n\nStay safe online! Never share personal information, use strong passwords, and always ask an adult before visiting websites."},
            {"path": os.path.join(BASE_DIR, "images", "internet2.jpg"),
             "content": "🛡️ Internet Safety\n\nStay safe online! Never share personal information, use strong passwords, and always ask an adult before visiting websites."},
        ]
    },
    {
        "name": "Problem Solving", "emoji": "🧩",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "problem_solve.jpg"),
             "content": "🧩 Problem Solving\n\nProblem solving means breaking down big problems into smaller steps and finding solutions. This is what computers do!"},
        ]
    },
    {
        "name": "Numbers & Logic", "emoji": "🔢",
        "images": [
            {"path": os.path.join(BASE_DIR, "images", "number.png"),
             "content": "🔢 Numbers & Logic\n\nComputers work with numbers and logic. They use patterns and rules to process information very quickly!"},
        ]
    },
]
