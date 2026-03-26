<p align="center">
  <img src="https://ailaysa.com/logo512.png" alt="Ailaysa" width="200"/>
</p>

<h1 align="center">Ailaysa</h1>

<p align="center">
  <b>State-of-the-Art Natural Language Processing for Indic Languages</b><br>
  <i>Building the foundation for Tamil and Indic AI systems</i>
</p>

<p align="center">
  <a href="https://pypi.org/project/ailaysa/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/ailaysa?style=flat-square">
  </a>
  <a href="https://pypi.org/project/ailaysa/">
    <img alt="Python" src="https://img.shields.io/pypi/pyversions/ailaysa?style=flat-square">
  </a>
  <a href="https://github.com/Ailaysa-Technologies/Asai-Tokenizer/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/Ailaysa-Technologies/Asai-Tokenizer?style=flat-square">
  </a>
  <a href="https://github.com/Ailaysa-Technologies/Asai-Tokenizer/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Ailaysa-Technologies/Asai-Tokenizer?style=flat-square">
  </a>
  <a href="https://github.com/Ailaysa-Technologies/Asai-Tokenizer/network/members">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Ailaysa-Technologies/Asai-Tokenizer?style=flat-square">
  </a>
</p>

##  Overview

**Ailaysa** is an open-source research and engineering initiative focused on advancing **Natural Language Processing for Indic languages**, starting with Tamil.

It provides:

* Production-ready tools
* Research-oriented architecture
* Scalable AI infrastructure

###  Current Focus

Tamil NLP, with future expansion into broader Indic ecosystems.

---

##  The Story of Asai 🌿

**Asai (அசை)** — the fundamental unit of rhythm in Tamil prosody (*யாப்பிலக்கணம்*).
In classical Tamil literature, Asai represents the cadence formed by letters, classified into:

* **Ner (நேர்)** — short rhythmic unit
* **Nirai (நிரை)** — extended rhythmic unit

It is the pulse that gives poetry its movement, structure, and emotion.

Just as Asai forms the building blocks of Tamil verse, **Ailaysa** provides the foundational building blocks for Indic language AI.

> *“To build AI that understands Indic languages, one must first understand their soul.”*

---

##  Key Capabilities

*  **High-Performance Tokenization**
  Optimized subword tokenization tailored for Tamil script

*  **Research-Ready Design**
  Built for experimentation, extensibility, and academic workflows

*  **Production-Ready APIs**
  Clean interfaces designed for real-world deployment

*  **Modular Architecture**
  Plug-and-play components for future expansion

---

##  Installation

### Prerequisites

* Python 3.8+
* pip 20+

### Install via PyPI

```bash
pip install ailaysa
```

---

##  Quick Start

### Tamil Tokenization

```python
from ailaysa import tokenizer

# Load tokenizer
tok = tokenizer.load("asai-v1")

# Input text
text = "தமிழை உலகமெங்கும் கொண்டு சேர்ப்போம்."

# Encode
encoded = tok.encode(text)

print(encoded.ids)
print(encoded.tokens)
print(encoded.length)
```

---

## Architecture

Ailaysa is built with a modular and extensible design:

```
ailaysa/
│
├── tokenizer/      # Tokenization engine
├── embeddings/     # (Upcoming)
├── translation/    # (Upcoming)
├── ocr/            # (Upcoming)
├── models/         # Model storage
```

---

##  Model Catalog

| Model     | Description                     |
| --------- | ------------------------------- |
| `asai-v1` | General-purpose Tamil tokenizer |

---

## Research & Development

Ailaysa bridges **academic research** and **industrial applications**.

### Current Research Areas

* **Computational Linguistics**
  Morphological and syntactic analysis for Tamil

* **Low-Resource NLP**
  Training techniques with limited annotated data

* **Multilingual Transfer Learning**
  Cross-lingual learning across Indic languages

* **Cultural NLP**
  Preserving linguistic and cultural nuances in AI

---

##  Citation

If you use Ailaysa in your research:

```bibtex
@software{ailaysa2026,
  title = {Ailaysa: Indic Language NLP Toolkit},
  author = {Mukesh Anand G and Ailaysa Technologies},
  year = {2026},
  url = {https://github.com/ailaysa/ailaysa}
}
```

---

##  Community & Governance

Ailaysa is built by a growing community of:

* AI engineers
* Researchers
* Linguists
* Open-source contributors

### Ways to Contribute

*  Code (features, optimizations)
*  Data (datasets, corpora)
*  Research (papers, experiments)
*  Documentation (guides, tutorials)

---

## Author

**Mukesh Anand G**  
AI Research Engineer

---

## Organization

Developed and maintained by **Ailaysa Technologies**

---

## License

This project is licensed under the **MIT License**.

---

<p align="center">
  <b>Built with precision. Inspired by heritage. Open for the future.</b>
</p>

<p align="center">
  <a href="https://github.com/Ailaysa-Technologies/Asai-Tokenizer/">GitHub</a> •
  <a href="https://pypi.org/project/ailaysa/">PyPI</a> •
  <a href="https://ailaysa.com/">Website</a> 
</p>
