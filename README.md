## LISA - Leading Indicators Scraping and Analysis
A program to extract, transform, store, analyse and visualize various leading economic indicators and stock market data from online sources.
<br></br>
**Motiation for project:** 
- to learn development best practices and programming design patterns via building something concrete
- to document my learning journey and demonstrate current level of competence
<br></br>
## Usage
See example usage of code in [this notebook](https://github.com/haroon-altaf/lisp/blob/main/notebook.ipynb).
<br></br>
## Setup
**Python version >= 3.12**
<br></br>
1. Clone the repository
   ```cmd
   git clone https://github.com/haroon-altaf/LISA
   cd LISA
2. Install uv from [here](https://docs.astral.sh/uv/), then run the following to setup venv and install dependencies
   ```cmd
   uv sync
   ```
<br></br>
## Project File Structure
   ```text
   LISA/
   |
   ├─ src/
   |  └─lisa/
   |    |
   |    ├─ common/
   |    │  ├─ __init__.py
   |    │  ├─ db_connection.py             # Creates SQLAlchemy engine and database methods
   |    |  ├─ web_session.py               # Provides context manager for requests sessions
   |    |  └─ template_logger.py           # Provides template logger class for use throughout code
   |    |
   |    ├─ scrapers/
   |    │  ├─ __init__.py
   |    │  ├─ ism_report.py                # extracts, transforms and loads data from ISM business reports
   |    │  ├─ html_dictionary.py           # contains information on navigating ISM reports' HTML
   |    │  ├─ consumer_survey.py           # extracts, transforms and loads UoM Consumer Survey data
   |    │  ├─ construction_survey.py       # extracts, transforms and loads US Buildings Survey data
   |    │  ├─ euro_survey.py               # extracts, transforms and loads EU economic sentiment data
   |    │  ├─ caixin_pmi.py                # extracts, transforms and loads Caixin PMI data
   |    │  ├─ finviz.py                    # extracts, transforms and loads stocks data from Finviz
   |    │  └─ trading_economics.py         # extracts, transforms and loads data from Trading Economics
   |    |
   |    ├─ utils/
   |    │  ├─ __init__.py
   |    │  └─ utils.py                     # Contains miscellaneous utility functions
   |    | 
   |    ├─ database_models/                # Contains SQLAlchemy ORM classes for each database table
   |       ├─ __init__.py
   |       └─ ...
   |
   ├─ data/
   |  └─Leading Indicators and Stocks.db   # SQLite database containing scraped data
   |
   ├─ notebook.ipynb                       # Jupyter notebook containing example code 
   ├─ pyproject.toml
   ├─ uv.lock
   ├─ README.md
   └─ .gitignore
   ```
