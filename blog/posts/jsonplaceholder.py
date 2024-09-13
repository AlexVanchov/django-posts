import requests
from .models.post import Post
from .models.comment import Comment

def fetch_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts_data = response.json()

    # Convert API response into list of Post objects (unnecessary because we're not using Django ORM but i wanted to play with it :))
    posts = [Post(id=post['id'], user_id=post['userId'], title=post['title'], body=post['body']) for post in posts_data]
    return posts

def fetch_post_details(post_id):
    post_response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    post_data = post_response.json()

    # Fetch the comments for the post
    comments_response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    comments_data = comments_response.json()

    # Convert API response to list of objects
    comments = [Comment(id=comment['id'], post_id=comment['postId'], name=comment['name'], email=comment['email'], body=comment['body']) for comment in comments_data]
    post = Post(id=post_data['id'], user_id=post_data['userId'], title=post_data['title'], body=post_data['body'], comments=comments)

    return post

def paginate_data(data, page_number, per_page):
    # Assuming you're using Django's Paginator
    from django.core.paginator import Paginator
    paginator = Paginator(data, per_page)
    page_obj = paginator.get_page(page_number)
    return page_obj