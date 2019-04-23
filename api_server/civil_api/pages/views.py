# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.paginator import Paginator
from django.http import JsonResponse


def loadContent():
    with open("../../data_fetch/reversed_tweets.json") as tweets:
        all_tweets = json.loads(tweets.read())
        return all_tweets


def homePageView(request):
    # TODO: Need to move this to some global initialization place
    tweets = loadContent()
    page_index = int(request.GET['page']) # need to do this right. parse number, check max etc.
    page_size = int(request.GET['size']) # need a default

    p = Paginator(tweets, page_size)
    page = p.page(page_index)
    response = JsonResponse(page.object_list, safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response
