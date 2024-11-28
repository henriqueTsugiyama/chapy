# Chatty
This is an implementation of a RAG using Pinecone Vector database and OpenAI API embedded model, in a custom chatbot that is able to chat using specific data from PDF and CSV files.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements
- Python 3.x
- NodeJS

## Installation
### Nodejs
cd client and:
```bash
npm install
```

Run development:
```bash
npm run dev
```

Run production:
```bash
npm start
```

Available on http://localhost:3000

### Python
cd server and activate virtual environment:
```bash
chatty_env\Scripts\activate
```

then:
```bash
pip install -r requirements.txt
```

## Usage:
### Flask server
On windows:
```bash
set FLASK_APP=server.py
```
```bash
set FLASK_ENV=development
```

On linux:
```bash
export FLASK_APP=server.py
```
```bash
export FLASK_ENV=development
```
Run:
```bash
flask run
```
Available on http://localhost:5000

<!-- 
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo -->
