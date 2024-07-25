# Chatbot for Norms

University project at [Deggendorf Institute of Technology](https://www.th-deg.de/en) authored by Martin Bischof, Marco Ludwig, Christian Werner and Richard Wittmann in collaboration with [ZVK GmbH](https://www.zvk-gmbh.de/). The goal of the project is to develop a Retrieval Augmented Generation (RAG) for answering questions about norms and standards.


## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)

## Introduction

This project is a Proof of Concept to show that RAG can be used to answer questions about norms and standardts based on internal documents. Therfore its only a prototype and needs further development to leverage its capabilitys for daily usage.

## Features

This PoC includes the following Features:
- **ETL-Pipeline:**  
This Feature extracts the text from pdf documents, loads it and transforms it into chunks. Those chunks are embedded and stored in a vector database.
- **Answer Generation:**  
Thid Function allows the user to querry the vector database, retrieve context and generate an answer based on it.
- **UI:**  
For interaction a basic UI was implemented as an alternative to console interaction.

## Installation
> **Note:**
This project is run in Python 3.10.5

> **Clone Repository:**  
Clone the repository.
> **Create Venv:**    
Create a virtual environment and install all neccesary pachages from `chatbot_for_norms/requirements.txt`

> **Create Weaviate Docker:**  
Naviagte into the folder chatbot_for_norms\src\utils\vector_db and run `docker-compose up -d` to create the docker with basic settings.

> **Prepare OpenAi Key:**
Ensure that you have acces to a valid OpenAi-APIKey, else create a fresh one via the OpenAi webside and save it for now.

## Usage

> **Data:**  
Create a new folder `chatbot_for_norms/data`.  
Put all neccessary files in this folder (only pdf).


> **Start VectorDB:**  
Before running the code, start the Docker Daemon and ensure that the Weaviate Docker container is running.

> **Run ETL-Pipeline:**  
```python
from dotenv import load_dotenv
import os

load_dotenv("locsid4sme1/env.env")
os.environ['OPENAI_KEY'] = 'YOUR_API_KEY'

from locsid4sme1 import run_etl_pipeline

run_etl_pipeline()
```

> **Run Answer Generation with UI:**
```python
from dotenv import load_dotenv
import os
load_dotenv("locsid4sme1/env.env")
os.environ['OPENAI_KEY'] = 'YOUR_API_KEY'

from locsid4sme1 import ChatUI

app = ChatUI()
app.run()
```

> **Run only Answer Genration:**  
```python
from dotenv import load_dotenv
import os
load_dotenv("locsid4sme1/env.env")
os.environ['OPENAI_KEY'] = 'YOUR_API_KEY'

from locsid4sme1 import run_answer_pipeline
question = "Must the WWW-Authenticate be included in a 401?"
print(run_answer_pipeline(question))
```

## contributing
This project was part of a lecture at [Deggendorf Institute of Technology](https://www.th-deg.de/en) in collaboration with [ZVK GmbH](https://www.zvk-gmbh.de/). 
It was authored by:
- Martin Bischof
- Marco Ludwig
- Christian Werner
- Richard Wittmann 

 