from django.db import models

# Create your models here.

class CommentSection(models.Model):
    comment= models.TextField(max_length=200)   
    video_id= models.TextField(blank=True, null=True, max_length=500)
    like= models.IntegerField(default= None, blank=True, null=True)
    dislike= models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.comment

class Reply(models.Model):
    reply_text = models.TextField(max_length=500)
    repliedcomment = models.ForeignKey(CommentSection ,blank=True, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.reply_text


