# NLP Toolkit

I built this library from scratch to learn how NLP works under the hood.
Instead of just using libraries like spaCy or NLTK directly,
I implemented the core concepts myself.

## Requirements

- Python 3.14.6
- Git 2.54.0
- pip 26.1.2

## Dependencies

- spaCy 3.8.13 — used for POS Tagging and NER
- NLTK 3.9.4 — used for Tokenization and Stemming
- pytest 9.1.1 — for unit testing

## What it does

- Cleans raw text (removes HTML, numbers, special characters)
- Tokenizes text into words and sentences
- Removes stopwords
- Stems and lemmatizes words
- Tags parts of speech (POS)
- Detects named entities (NER)

## Installation

git clone https://github.com/faezehsalehi-ac/nlp-toolkit.git
cd nlp-toolkit
pip install -r requirements.txt

## Progress

- [x] Project setup
- [x] Text Cleaning
- [ ] Tokenization
- [ ] Stopwords
- [ ] Stemming & Lemmatization
- [ ] POS Tagging
- [ ] NER

## Project Structure

```
nlp-toolkit/
├── nlp_toolkit/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── tokenizer.py
│   ├── stopwords.py
│   ├── stemmer.py
│   ├── lemmatizer.py
│   ├── pos_tagger.py
│   └── ner.py
├── tests/
│   └── test_cleaner.py
├── requirements.txt
├── setup.py
└── README.md
```