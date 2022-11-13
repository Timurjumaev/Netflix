import rest_framework.views as APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


# class KinolarAPIView(APIView):
#     def get(self, request):
#         kinolar=Kino.objects.all()
#         serializer=KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         kino=request.data
#         serializer=KinoSerializer(data=kino)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success":"True", "data": serializer.data})
#         return Response({"success": "False"})
#
# class AktyorlarAPIView(APIView):
#     def get(self, request):
#         aktyorlar=Aktyor.objects.all()
#         serializer=AktyorSerializer(aktyorlar, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         aktyor=request.data
#         serializer=AktyorSerializer(data=aktyor)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"succes": "True", "data": serializer.data})
#         return Response({"succes": "False"})
#
# class AktyorAPIView(APIView):
#     def get(self, request, son):
#         aktyor=Aktyor.objects.get(id=son)
#         serializer=AktyorSerializer(aktyor)
#         return Response(serializer.data)
#     def put(self, request, son):
#         aktyor=Aktyor.objects.get(id=son)
#         serializer=AktyorSerializer(aktyor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Succes": "True", "Data":serializer.data})
#         return Response({"succes": "False"})
#     def delete(self, request, son):
#         aktyor=Aktyor.objects.get(id=son)
#         aktyor.delete()
#         return Response({"success": "True"})

# class KinoViewSet(ModelViewSet):
#     queryset=Kino.objects.all()
#     serializer_class = KinoSerializer
#     @action(methods=['GET'], detail=True)
#     def comments(self, request, pk):
#         comments=Comment.objects.filter(kino__id=pk)
#         serializer=CommentSerializer(comments, many=True)
#         return Response(serializer.data)
#
#
# class AktyorViewSet(ModelViewSet):
#     queryset=Aktyor.objects.all()
#     serializer_class = AktyorSerializer

class CommentsAPIView(APIView):
    def get(self, request):
        datas=Comment.objects.filter(user=request.user)
        serializer=CommentSerializer(datas, many=True)
        return Response(serializer.data)
    def post(self, request):
        data=request.data
        serializer=CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

