from django.db import models
from django.db.models import Count
from project.settings import AUTH_USER_MODEL


class Theme(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Duel(models.Model):
    token = models.CharField(max_length=40, unique=True)
    theme = models.ForeignKey(Theme)
    creator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)

    def add_member(self, user, is_creator=False):
        return Member.objects.create(duel=self, user=user,
                                     is_creator=is_creator)

    def is_member(self, user):
        return Member.objects.filter(duel=self, user=user).exists()

    def is_creator(self, user):
        return user == self.creator

    def is_full(self):
        return Member.objects.filter(duel=self).count() >= 2


class Question(models.Model):
    SINGLE_CHOICE = 1
    NUMBER = 2
    TEXT = 3
    TYPE_CHOICES = (
        (SINGLE_CHOICE, 'Single choice'),
        (NUMBER, 'Number'),
        (TEXT, 'Text')
    )
    title = models.CharField(max_length=254)
    theme = models.ForeignKey(Theme)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)


class Answer(models.Model):
    content = models.CharField(max_length=254)
    question = models.ForeignKey(Question)

    created_at = models.DateTimeField(auto_now_add=True)


class UserAnswer(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)
    is_correct = models.BooleanField(default=False)

    sent_at = models.DateTimeField(auto_now_add=True)


class Member(models.Model):
    duel = models.ForeignKey(Duel, on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL)
    total_asserts = models.PositiveSmallIntegerField(null=True, blank=True)
    total_fails = models.PositiveSmallIntegerField(null=True, blank=True)
    is_creator = models.BooleanField(default=False)

    joined_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_active_duels(cls, user):
        return cls.objects.values(
            'duel__name', 'duel__token', 'duel__theme__name').filter(
            user=user,
            duel__is_active=True)
