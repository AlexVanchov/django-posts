# Django Posts
## Demo

[Open link](https://alexvanchov.pythonanywhere.com/)

## Overview
This app interacts with the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)

## Main Features
- **List of Posts**: Displays titles and brief snippets. Clicking on a post navigates to its details.
- **Post Detail**: Shows the full content of a post and its comments.
- **Comment Details**: Displays the comment, author's name, and email formatted clearly.

## Setup

### Using Docker

1. Build the Docker image:
    ```bash
    docker build -t django-posts .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 django-posts
    ```

3. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the app.

### OR Local Instance

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
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