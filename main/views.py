from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import TemplateView, FormView
from django.views import View

from . import forms

# Create your views here.

class Index(TemplateView):
    template_name = 'main/index.html'

class Stream(FormView):
    template_name = 'main/stream.html'
    post_template_name = 'main/streamPreview.html'
    form_class = forms.LiveVideoDetailForm

    def extract_details(self):
        form = self.get_form()

        if form.is_valid():

            subscribers = form.cleaned_data['phone_numbers']

            access_token = form.cleaned_data['authentication_token']

            stream_url = form.cleaned_data['live_stream_url']

            # https://www.facebook.com/manan.negi.142/videos/102297264039426/

            stripped_stream_url = stream_url if stream_url[-1] != '/' else stream_url[:-1]

            stream_id = stripped_stream_url.split('/')[-1]

            return subscribers, access_token, stream_id
        
        raise Exception()

    def get_video_iframe(self, access_token, stream_id):
        import requests
        import json
        print(stream_id)
        url = "https://graph.facebook.com/{}".format(stream_id)

        data = {
            "access_token": access_token,
            "fields": "embed_html"
        }

        r = requests.get(url, params = data)
        resp = r.content.decode('UTF-8')
        print(resp)
        return str(json.loads(resp)['embed_html'])

    def post(self, request):
        try:
            subscribers, access_token, stream_id = self.extract_details()

            iframe = self.get_video_iframe(access_token, stream_id)

            context = {
                'subscribers': subscribers,
                'iframe': iframe
            }
            return render(request, self.post_template_name, context)

        except Exception as e:
            print(e)
            return HttpResponse("Error")
            # return super().post(request)