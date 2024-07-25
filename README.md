# LoCSID4SME

University project at THD supervised by Robert Aufschläger, authored by Martin Bischof, Marco Ludwig, Christian Werner and Richard Wittmann in collaboration with [ZVK GmbH](https://www.zvk-gmbh.de/). The goal of the project is to develop a Retrieval Augmented Generation (RAG) for answering questions about norms and standards.


## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

TODO !

## Features

TODO !

## Installation
> **Note:**
This project is run in Python 3.10.5

> **Clone Repository:**
Clone the locsid4sme repository. (e.g. with https: `git clone https://mygit.th-deg.de/ai-project-summer-24/locsid4sme1.git`)

> **Create Venv:**    
Create a virtual environment and install all neccesary pachages from `locsid4sme/requirements.txt`

> **Create Weaviate Docker:**  
Naviagte into the folder locsid4sme1\src\utils\vector_db and run `docker-compose up -d` to create the docker with basic settings.

> **Prepare OpenAi Key:**
Ensure that you have acces to a valid OpenAi-APIKey, else create a fresh one via the OpenAi webside and save it for now.

## Usage

> **Data:**  
Create a new folder `locsid4sme/data`.  
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

# License

## Preamble

This license governs the sharing, publishing, and usage of the project code. It is designed to ensure that the code can only be shared or published with the written consent of all contributors. This license is a legally binding agreement between you and the contributors listed below.

## License Grant

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, merge, and distribute copies of the Software, subject to the following conditions:

## Conditions

1. **Contributor Consent**: The Software or any substantial portion of it may only be shared, published, or distributed if written consent is obtained from all of the following contributors:
   - Martin Bischof
   - Marco Ludwig
   - Christian Werner
   - Richard Wittmann

2. **Written Allowance**: Written consent must be provided by all the contributors listed above. Consent must be explicit and documented, either digitally signed or physically signed and dated by each contributor.

3. **Attribution**: Any use, copying, modification, or distribution of the Software must include an attribution to the original contributors listed above.

4. **Modification of Terms**: Any modification of these terms must be agreed upon by all contributors listed above in writing.

5. **Non-Commercial Use**: The Software cannot be used for commercial purposes without prior written consent from all contributors listed above.

6. **Legal Compliance**: The use of the Software must be in compliance with all applicable laws and regulations.

## Termination

This license is automatically terminated if any of the above conditions are not met. Upon termination, any rights granted under this license will cease immediately, and the licensee must destroy all copies of the Software in their possession.

## Disclaimer of Warranty

The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the contributors be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software or the use or other dealings in the Software.

## Limitation of Liability

In no event shall any contributor be liable for any special, incidental, indirect, or consequential damages whatsoever arising out of the use of or inability to use the Software.

## Governing Law

This license shall be governed by and construed in accordance with the laws of the jurisdiction in which the primary contributor resides, excluding its conflicts of law principles.

## Acceptance

By using, copying, modifying, or distributing the Software, you accept and agree to be bound by the terms and conditions of this license.

---

**Contributors:**

Martin Bischof
Marco Ludwig
Christian Werner
Richard Wittmann

**Date:** 2024-07-02

