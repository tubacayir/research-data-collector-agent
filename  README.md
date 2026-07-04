# Research Data Collector Agent

## Description

This project is a simple AI agent developed in Python.

The agent:
- Takes a research topic from the user.
- Searches the web using the Tavily API.
- Collects search results.
- Saves the results into an Excel file.

## Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

## API Key

Create a `.env` file and add your Tavily API key:

```env
TAVILY_API_KEY=your_api_key
```

## Run

```bash
python topicSearch.py
```

Enter a research topic when prompted. The program will generate an Excel file containing the search results.