from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic

# Главная
def index(request):
    return render(request, 'index.html')

# Список разделов курса
def course_list(request):
    topics = Topic.objects.all()
    return render(request, 'course_list.html', {'topics': topics})

# Страница изучения конкретной темы
def learning(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    questions = topic.questions.all()
    if request.method == 'POST':
        # Обработка ответов теста (простейший вариант)
        score = 0
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected and q.choices.get(pk=int(selected)).is_correct:
                score += 1
        return render(request, 'learning.html', {
            'topic': topic,
            'questions': questions,
            'score': score,
            'completed': True,
        })
    return render(request, 'learning.html', {'topic': topic, 'questions': questions})