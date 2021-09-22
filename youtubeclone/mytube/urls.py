from django.urls import path
from . import views

urlpatterns= [
 path('mytube/', views.CommentAllList.as_view()),  
 path('mytube/video', views.Comments.as_view()),
 path('mytube/video/<str:video_id>', views.Comments.as_view()),
 path('mytube/<int:pk>', views.CommentDetail.as_view()),
 path('mytube/reply/video', views.ReplyList.as_view()),
 path('mytube/reply/<int:pk>/', views.ReplyDetail.as_view()),
 path('comments/<int:pk>/likes/', views.CommentLike.as_view()),
 path('comments/<int:pk>/dislikes/', views.CommentDislike.as_view()) 
]   

