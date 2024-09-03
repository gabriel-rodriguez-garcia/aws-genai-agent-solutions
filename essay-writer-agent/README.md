# DeepLearningAI - Agents with LangGraph

Hey there! This workshop contains 6 lessons that will help you understand the LangGraph framework and it's underlying concepts. Make sure to read and follow this README before you go through the lessons to ensure a smooth experience.

## Prerequisites
- Python >=3.10 (to install visit this link: https://www.python.org/downloads/)
- pipx (to install visit this link: https://pipx.pypa.io/stable/installation/)

## 1. Setup your virtual environment
Open a terminal in your IDE of choice and run the following commands:


### Install OS dependencies (Ubuntu/Debian)
```
sudo apt update

sudo apt-get install graphviz graphviz-dev python3-dev

pipx install poetry
```

Installation commands for other OS can be found here: https://pygraphviz.github.io/documentation/stable/install.html

### Create a virtual environemnt and install python dependencies

```
poetry shell

poetry install
```

## 2. Create and set your TAVILY API KEY
Head over to https://app.tavily.com/home and create an API KEY for free. Copy the key and add it to secrets manager in your aws account using plaintext format and use the name "TAVILY_API_KEY". Alternatively you can export the API KEY with the same name as environment variable in your terminal.

Your all set! Make sure to select 'agents-dev-env' as your kernel for each notebook