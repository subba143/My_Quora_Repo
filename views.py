from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('view_questions')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

@login_required
def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
    return redirect('view_questions')

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    if request.user not in answer.likes.all():
        answer.likes.add(request.user)
    return redirect('view_questions')

