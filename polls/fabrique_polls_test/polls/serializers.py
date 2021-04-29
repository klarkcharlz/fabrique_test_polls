from rest_framework import serializers
from .models import Polls, Questions, CompetedPoll


class AllPollsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = "__all__"


class AllQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"


class CompetedPollSerializers(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    question = serializers.SlugRelatedField(slug_field="text", read_only=True, many=True)

    class Meta:
        model = CompetedPoll
        fields = "__all__"


class CreateCompetedPollSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompetedPoll
        fields = "__all__"
