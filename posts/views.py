# from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['GET','POST'])
def PostList(request):
	"""
    List all products, or create a new product.
    """
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts,context={'request': request} ,many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def PostDetail(request, pk):
	"""
	Retrieve, update or delete a post instance.
	"""
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PostSerializer(post,context={'request': request})
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = PostSerializer(post, data=request.data,context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# class PostList(generics.ListCreateAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer