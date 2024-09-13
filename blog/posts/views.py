from django.shortcuts import render
from django.http import HttpResponseServerError
from .jsonplaceholder import fetch_posts, fetch_post_details, paginate_data  # Import from services
import logging

logger = logging.getLogger(__name__)

def post_list(request):
    try:
        # Get posts
        posts = fetch_posts()
        page_number = request.GET.get('page')
        # paginate comments
        page_obj = paginate_data(posts, page_number, 10)

        return render(request, 'post_list.html', {'page_obj': page_obj})
    except Exception as e:
        logger.error(f"Error for post_list view: {e}")
        return render(request, 'error.html', {'message': str(e)})

def post_detail(request, post_id):
    try:
        # Get post details
        post = fetch_post_details(post_id)
        page_number = request.GET.get('page')
        # paginate comments
        page_obj = paginate_data(post.comments, page_number, 3)

        return render(request, 'post_detail.html', {
            'post': post,
            'page_obj': page_obj
        })
    except Exception as e:
        logger.error(f"Error for post_detail view: {e}")
        return render(request, 'error.html', {'message': str(e)})