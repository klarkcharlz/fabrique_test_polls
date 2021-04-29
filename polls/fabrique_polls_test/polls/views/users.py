from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import AllPollsSerializers, CompetedPollSerializers, CreateCompetedPollSerializers
from ..models import Polls, CompetedPoll


class GetPolls(ListAPIView):
    """Получение пользователем всех опросов"""
    queryset = Polls.objects.all()
    serializer_class = AllPollsSerializers


class TryPoll(CreateAPIView):
    """Прохождение опроса"""
    serializer_class = CreateCompetedPollSerializers


class UserPolls(APIView):
    """Получение пользователем всех ответов пользователя"""

    def get(self, request, id):
        queryset = CompetedPoll.objects.filter(user_id=id)
        serializer = CompetedPollSerializers(queryset, many=True)
        return Response(serializer.data)

