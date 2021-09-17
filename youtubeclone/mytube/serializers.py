
from rest_framework import serializers
from .models import CommentSection
from .models import Reply

class CommentSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentSection
        fields = ['id','comment','video_id', 'like', 'dislike']

       
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['reply_text', 'comment_id']