from django.urls import path
from . import views

urlpatterns = [
    path('post_question/', views.post_question, name='post_question'),
    path('view_questions/', views.view_questions, name='view_questions'),
    path('answer_question/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),
]
