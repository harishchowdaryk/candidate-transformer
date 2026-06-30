from pathlib import Path

folders = [
    "input",
    "output",
    "config",
    "src",
    "src/parsers",
    "tests"
]

files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "input/recruiter.csv",
    "input/resume.txt",
    "config/default.json",
    "config/custom.json",
    "src/main.py",
    "src/normalizer.py",
    "src/merger.py",
    "src/confidence.py",
    "src/projection.py",
    "src/validator.py",
    "src/utils.py",
    "src/parsers/csv_parser.py",
    "src/parsers/resume_parser.py"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).touch(exist_ok=True)

print("✅ Project structure created successfully!")