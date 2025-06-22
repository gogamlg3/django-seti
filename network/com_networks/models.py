from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()       # Текст темы
    video_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    topic = models.ForeignKey(Topic, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'✓' if self.is_correct else '✗'})"