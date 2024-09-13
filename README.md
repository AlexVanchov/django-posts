# Django Posts

## Overview
This app interacts with the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)

## Main Features
- **List of Posts**: Displays titles and brief snippets. Clicking on a post navigates to its details.
- **Post Detail**: Shows the full content of a post and its comments.
- **Comment Details**: Displays the comment, author's name, and email formatted clearly.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
    ```bash
    python manage.py runserver
    ```
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the app.

## Tests
To run tests for the "posts" app:

```bash
python manage.py test posts
```

```bash
python manage.py runserver
```