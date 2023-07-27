from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Question
from .serializers import QuestionSerializer


@api_view(['GET'])
def filter_questions(request):
    read_status = request.GET.get('read')
    favorite_status = request.GET.get('favorite')

    questions = Question.objects.all()

    if read_status == 'read':
        questions = questions.filter(readquestion__isnull=False)
    elif read_status == 'unread':
        questions = questions.filter(readquestion__isnull=True)

    if favorite_status == 'favorite':
        questions = questions.filter(favoritequestion__isnull=False)
    elif favorite_status == 'unfavorite':
        questions = questions.filter(favoritequestion__isnull=True)

    return Response(QuestionSerializer(questions, many=True).data)


def user_favorite_read_count():
    return None
