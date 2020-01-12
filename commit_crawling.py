# commit crawling.py

import time
import requests
from bs4 import BeautifulSoup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "slack.settings")

import django
django.setup()

from .outgoingslack.models import OutGoingSlack
from collections import namedtuple


from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")

def getCommitList():
    driver.get('https://app.slack.com/client/TS08LHC73/CSAFNFB4M')

    driver.find_element_by_id('domain').send_keys('githubfarm')
    driver.find_element_by_xpath('//*[@id="submit_team_domain"]').click()

    driver.find_element_by_name('email').send_keys('i3048i@yonsei.ac.kr')

    driver.find_element_by_xpath('//*[@id="signin_btn"]').click()

    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')
    message_list = soup.select('div.c-message_kit__gutter')

    commit_list = []
    for i in range(len(message_list)):
        temp = message_list[i].select('a.c-message__sender_link')
        if temp:
            if(temp[0].text == "GitHub"):
                commit_list.append(message_list[i])

    return commit_list
