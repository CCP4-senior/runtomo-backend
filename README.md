# Runtomo

Welcome to Runtomo!

## Introduction

Runtomo is a social running app curated for users in the Tokyo area of Japan. Users will easily be able to find and particpate in local running events with other users at the touch of a button.

## Installation/Running the App

To use the application locally, please follow the steps below.

**1: Create a virtual environment**

Run this command in the root directory of the project to enable virtual environment:

```
source venv/bin/activate
```

**2: Install dependencies**

Install all dependencies by running:

```
pip install -r requirements.txt
```

**3: Migrate Database**

Migrate the database by running:

```
python3 manage.py migrate
```

**4: Start server**

Start the server by running:

```
python3 manage.py runserver
```
