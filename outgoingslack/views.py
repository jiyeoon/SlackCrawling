from django.shortcuts import render
from django.utils import timezone
from .models import OutGoingSlack
from rest_framework import viewsets
from .serializers import SlackSerializer

# Create your views here.

def post_list(request):
    #posts = OutGoingSlack.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'outgoingslack/post_list.html', {})


#OutGoingSlack에 저장만 하는걸루~
def save_slack_msg(request):
    if request.method == "GET":
        print("잘못된 입력!")
        return




class SlackViewSet(viewsets.ModelViewSet):
    queryset = OutGoingSlack.objects.all()
    serializer_class = SlackSerializer
