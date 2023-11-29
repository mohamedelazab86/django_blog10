# functions
from .models import Post
from .serializers import PostSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_post_api(request):
    posts=Post.objects.all()
    data=PostSerializers(posts,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def detail_post_api(request,pk):
    post=Post.objects.get(id=pk)
    data=PostSerializers(post).data
    return Response({'data':data})



#======================= api by class
from rest_framework import generics

class List_api(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers

class List_new_api(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers
class List_api_test(generics.RetrieveUpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers

