from django import forms

from . import models

class LiveVideoDetailForm(forms.Form):
    authentication_token = forms.CharField(max_length=250, label = "Facebook Authentication Token")
    live_stream_url = forms.URLField(label = "Live Stream URL")
    phone_numbers = forms.CharField(widget = forms.Textarea(), label = "Phone Numbers")
