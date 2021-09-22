
from .models import CommentSection
from .models import Reply

from django.http.response import Http404

from .serializers import CommentSectionSerializer
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class CommentAllList(APIView):
    def get(self, request):
        comment= CommentSection.objects.all()
        serializer= CommentSectionSerializer(comment, many=True)
        return Response(serializer.data)

class Comments(APIView):
   def get(self, request):
        comment = CommentSection.objects.all()
        serializer = CommentSectionSerializer(comment, many=True)
        return Response(serializer.data)

   def post(self,request):
        serializer = CommentSectionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 


class CommentDetail(APIView):

    def get_object(self, video_id):
        try:
            return CommentSection.objects.get(video_id = video_id)
        except CommentSection.DoesNotExist:
            raise Http404
        
    def get(self, request, video_id):
        comment = CommentSection.objects.filter(video_id = video_id)
        serializer = CommentSectionSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        comment = CommentSection.objects.filter(pk = pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReplyList(APIView):
    def get(self,request,):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer= ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class ReplyDetail(APIView):
    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    def get(self, request, video_id):
        reply = self.get_object(video_id)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
   
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentLike(APIView):
        def get_object(self, pk):
            try:
                return CommentSection.objects.get(pk = pk)
            except CommentSection.DoesNotExist:
                raise Http404

        def get(self, request, pk):
            comment = self.get_object(pk)
            serializer = CommentSectionSerializer(comment, data=request.data)
            return Response(serializer.data)

        def patch(self, request, pk):
            comment = self.get_object(pk)
            data = {"likes": comment.likes + int(1)}
            serializer = CommentSectionSerializer(comment, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDislike(APIView):
        def get_object(self, pk):
            try:
                return CommentSection.objects.get(pk = pk)
            except CommentSection.DoesNotExist:
                raise Http404

        def get(self, request, pk):
            comment = self.get_object(pk)
            serializer = CommentSectionSerializer(comment, data=request.data)
            return Response(serializer.data)

        def patch(self, request, pk):
            comment = self.get_object(pk)
            data = {"dislikes": comment.dislikes + int(1)}
            serializer = CommentSectionSerializer(comment, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











