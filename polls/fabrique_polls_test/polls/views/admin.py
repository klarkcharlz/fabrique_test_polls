from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from ..models import Polls, Questions
from ..serializers import AllPollsSerializers, AllQuestionsSerializers


class CreatePolls(CreateAPIView):
    """Создание опроса"""
    serializer_class = AllPollsSerializers
    permission_classes = [IsAdminUser]


class CreateQuestions(CreateAPIView):
    """Создание вопроса"""
    serializer_class = AllQuestionsSerializers
    permission_classes = [IsAdminUser]


class UpdatePolls(RetrieveUpdateDestroyAPIView):
    """редактирование опроса"""
    queryset = Polls.objects.all()
    serializer_class = AllPollsSerializers
    permission_classes = [IsAdminUser]


class UpdateQuestions(RetrieveUpdateDestroyAPIView):
    """Редактирование вопроса"""
    queryset = Questions.objects.all()
    serializer_class = AllQuestionsSerializers
    permission_classes = [IsAdminUser]
