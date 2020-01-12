from django.shortcuts import render
from django.utils import timezone
from .models import OutGoingSlack
from rest_framework import viewsets
from .serializers import SlackSerializer
from selenium import webdriver
from bs4 import BeautifulSoup

# Create your views here.

def post_list(request):
    #posts = OutGoingSlack.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'outgoingslack/post_list.html', {})


#OutGoingSlack에 저장만 하는걸루~
def save_slack_msg(request):
    if request.method == "GET":
        print("잘못된 입력!")





class SlackViewSet(viewsets.ModelViewSet):
    queryset = OutGoingSlack.objects.all()
    serializer_class = SlackSerializer


def getCommitList():
    driver = webdriver.Chrome(executable_path="../chromedriver")
    driver.get('https://app.slack.com/client/TS08LHC73/CSAFNFB4M')

    driver.find_element_by_id('domain').send_keys('githubfarm')
    driver.find_element_by_xpath('//*[@id="submit_team_domain"]').click()

    driver.find_element_by_name('email').send_keys('i3048i@yonsei.ac.kr')
    driver.find_element_by_xpath('//*[@id="signin_btn"]').click()


    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')

    message_list = soup.select('div.c-message_attachment__body')

    commit_list = []

    for i in range(len(message_list)):
        author_img = message_list[i].select('img.c-message_attachment__author_icon')
        author = message_list[i].select('span.c-message_attachment__author_name')
        msg = message_list[i].select('span.c-message_attachment__text')
        if "1 new commit" in msg[0].text:
            print(msg[0].text)
            commit_list.append(message_list[i])

    return commit_list


def saveCommitList():
    commit_list = getCommitList()

    for one_commit in commit_list:
        cd_author = one_commit.select_one('span.c-message_attachment__author_name').text
        cd_msg = one_commit.select_one('span.c-message_attachment__text > span') #html 코드
        cd_repository = one_commit.select_one('span.c-message_attachment__footer_text > span > a').text
        cd_respositoryUrl = one_commit.select_one('span.c-message_attachment__footer_text > span > a').get('href')
