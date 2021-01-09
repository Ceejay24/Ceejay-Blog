from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer



class BlogPostDetailView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'

class BlogPostListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'

class BlogPostFeaturedView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    
class BlogPostCategoriesView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['categories']
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=categories)
        serializer = BlogPostSerializer(queryset, many=True)
        list_per_page = 20

        return Response(serializer.data)
"""
class BlogWriteupView(APIView):
    def post (self, request, format=None):
        data = self.request.data

        title = data['title']
        author = data[]
        categories = data['categories']
        thumbnail = data['thumbnail']
        highlight = data['excerpts']
        date = data['date']
        content = data['content']
        post = User.objects.create_post(title=title, author=username, categories=categories, thumbnail=thumbnail, highlight=excerpt)
            user.save()
            return Response({'success': 'User created successfully'})
"""
