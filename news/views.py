from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from .embedding_utils import VectorStore
import json

# In-memory vector index for simplicity
vector_store = VectorStore()

@csrf_exempt
def upload_article(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            article = Article.objects.create(
                title=data.get('title'),
                content=data.get('content')
            )
            vector_store.add_articles([article])
            return JsonResponse({"message": "Article uploaded", "id": article.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)

@csrf_exempt
def search_articles(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            query = data.get('query')
            article_ids = vector_store.search(query)
            articles = Article.objects.filter(id__in=article_ids)
            results = [{"title": a.title, "content": a.content} for a in articles]
            return JsonResponse({"results": results})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)
