# Multi-Source Candidate Data Transformer

> Eightfold Engineering Intern Assignment (Jul–Dec 2026)

A Python-based data transformation pipeline that collects candidate information from multiple sources, normalizes the data, merges it into a single canonical profile, calculates confidence scores, tracks data provenance, and generates configurable JSON output.

---

## 📌 Project Overview

Recruitment systems often receive candidate information from different sources such as recruiter spreadsheets and resumes. These sources may contain duplicate, missing, or inconsistent information.

This project transforms those multiple inputs into **one clean and standardized candidate profile** by:

- Parsing candidate data from multiple sources
- Normalizing emails, phone numbers, and skills
- Merging duplicate information
- Calculating confidence scores
- Recording the source (provenance) of each field
- Producing configurable JSON output using runtime configuration

---

## ✨ Features

- ✅ Parse structured recruiter CSV files
- ✅ Parse unstructured resume (TXT)
- ✅ Normalize email addresses
- ✅ Convert phone numbers to E.164 format
- ✅ Remove duplicate values
- ✅ Merge multiple data sources
- ✅ Generate confidence scores
- ✅ Track provenance (source of each field)
- ✅ Configurable output using JSON config
- ✅ Validate candidate data before output
- ✅ Command Line Interface (CLI)

---

## 📁 Project Structure

```
candidate-transformer/
│
├── config/
│   ├── default.json
│   └── custom.json
│
├── input/
│   ├── recruiter.csv
│   └── resume.txt
│
├── output/
│   └── profile.json
│
├── src/
│   ├── parsers/
│   │   ├── csv_parser.py
│   │   └── resume_parser.py
│   │
│   ├── confidence.py
│   ├── merger.py
│   ├── normalizer.py
│   ├── projection.py
│   ├── provenance.py
│   ├── validator.py
│   ├── utils.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

- Python 3.10+
- Pandas
- Phonenumbers
- JSON
- Regular Expressions (Regex)
- VS Code

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
 git clone https://github.com/harishchowdaryk/candidate-transformer.git
cd candidate-transformer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Default Output

```bash
python src/main.py
```

### Custom Configurable Output

```bash
python src/main.py --config config/custom.json
```

---

## 📥 Sample Input

### recruiter.csv

| full_name | email | phone | location |
|------------|-------|--------|----------|
| Harish Chowdary | Harish@gmail.com | 9876543210 | Bangalore |

---

### resume.txt

```
Harish Chowdary

Email:
HARISH@gmail.com

Phone:
+91 9876543210

Skills:
Java
Python
Spring Boot
Docker

Education:
B.E Computer Science

Experience:
Fresher
```

---

## 📤 Sample Output

```json
{
  "candidate": {
    "full_name": "Harish Chowdary",
    "emails": [
      "harish@gmail.com"
    ],
    "phones": [
      "+919876543210"
    ],
    "location": "Bangalore",
    "skills": [
      "Java",
      "Python",
      "Spring Boot",
      "Docker"
    ],
    "education": "B.E",
    "experience": "Fresher"
  },
  "confidence": {
    "full_name": 1.0,
    "emails": 1.0,
    "phones": 1.0,
    "location": 1.0,
    "skills": 1.0,
    "education": 1.0,
    "experience": 1.0
  },
  "overall_confidence": 1.0,
  "provenance": {
    "full_name": [
      "Recruiter CSV"
    ],
    "emails": [
      "Recruiter CSV",
      "Resume"
    ],
    "phones": [
      "Recruiter CSV",
      "Resume"
    ],
    "location": [
      "Recruiter CSV"
    ],
    "skills": [
      "Resume"
    ],
    "education": [
      "Resume"
    ],
    "experience": [
      "Resume"
    ]
  }
}
```

---

## 🔄 Project Workflow

```
Recruiter CSV
        │
        ▼
   CSV Parser
        │

Resume.txt
        │
        ▼
 Resume Parser
        │
        ▼
Data Normalization
        │
        ▼
Merge Engine
        │
        ▼
Confidence Calculation
        │
        ▼
Provenance Tracking
        │
        ▼
Projection Layer
        │
        ▼
Validation
        │
        ▼
JSON Output
```

---

## ⚠️ Assumptions

- Recruiter CSV and Resume belong to the same candidate.
- Resume is provided in TXT format.
- Phone numbers are normalized to E.164 format.
- Missing values are returned as `null` (or omitted depending on configuration).
- Invalid values are ignored instead of causing the program to fail.

---

## 🚧 Future Enhancements

- Support PDF and DOCX resume parsing
- LinkedIn profile integration
- GitHub profile integration
- AI-based skill extraction
- Database integration
- REST API support
- Web-based user interface
- Improved confidence scoring using machine learning

---

## 👨‍💻 Author

**Harish Chowdary K**

B.E. Computer Science and Engineering

GitHub: github.com/harishchowdaryk

Email: harishchowdary132@gmail.com

---

## 📄 License

This project was developed as part of the **Eightfold Engineering Intern Assignment (Jul–Dec 2026)** for educational and evaluation purposes.
