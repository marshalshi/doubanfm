from django.shortcuts import render

from django.http import HttpResponse


import urllib2
import json

# Create your views here.
def test(request):

    
    
    return render(request, 'fm.html')

def get_play_list(request):
    response = urllib2.urlopen('http://www.douban.com/j/app/radio/people?app_name=radio_desktop_mac&version=100&type=n&user_id=52285926&token=e511658c0c&expire=1405063931&channel=0')
    data = json.load(response)

    return HttpResponse(content=json.dumps(data), content_type='application/json')
