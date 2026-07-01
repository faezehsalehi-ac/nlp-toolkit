# NLP Toolkit

A lightweight Python library for learning and experimenting with Natural Language Processing (NLP) from scratch.

Instead of treating NLP as a black box, this project implements core NLP components step by step to better understand how they work internally. The project is designed with clean architecture, modularity, and extensibility in mind.

---

## Philosophy

The goal of this project is not to replace mature NLP libraries such as spaCy or NLTK.

Instead, it focuses on:

- Understanding NLP algorithms from first principles
- Writing clean, maintainable Python code
- Building reusable NLP components
- Following software engineering best practices
- Creating a foundation for future research projects

---

## Features

### Completed

- ✅ Text Cleaning

### In Progress

- 🚧 Tokenization

### Planned

- ⏳ Stopword Removal
- ⏳ Stemming
- ⏳ Lemmatization
- ⏳ Part-of-Speech (POS) Tagging
- ⏳ Named Entity Recognition (NER)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/faezehsalehi-ac/nlp-toolkit.git
cd nlp-toolkit
```

Create a virtual environment (recommended):

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install the package in editable mode:

```bash
pip install -e .
```

---

## Quick Start

```python
from nlp_toolkit.cleaner import TextCleaner

cleaner = TextCleaner()

text = "<h1>Hello, World! 123</h1>"

clean_text = cleaner.clean(text)

print(clean_text)
```

Output:

```text
hello world
```

---

## Project Structure

```
nlp-toolkit/
│
├── src/
│   └── nlp_toolkit/
│       ├── cleaner.py
│       ├── tokenizer.py
│       ├── stopwords.py
│       ├── stemmer.py
│       ├── lemmatizer.py
│       ├── pos_tagger.py
│       ├── ner.py
│       └── __init__.py
│
├── tests/
│
├── README.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

---

## Development Roadmap

### Phase 1 — NLP Foundations

- [x] Project setup
- [x] Packaging
- [x] Text Cleaner
- [ ] Tokenizer
- [ ] Stopword Removal
- [ ] Stemmer
- [ ] Lemmatizer

### Phase 2 — Advanced NLP

- [ ] POS Tagger
- [ ] Named Entity Recognition

### Phase 3 — Production Ready

- [ ] Full test coverage
- [ ] Documentation
- [ ] GitHub Actions
- [ ] Docker support
- [ ] Publish to PyPI

---

## Design Principles

This project follows several software engineering principles:

- Modular architecture
- Reusable components
- Type hints
- Comprehensive documentation
- Unit testing
- Clean Git history
- Extensible APIs

---

## Contributing

This project is currently under active development.

Suggestions, discussions, and improvements are always welcome.

---

## License

This project is licensed under the MIT License.

See the LICENSE file for more information.