from django.forms import ModelForm
from .models import Group, Event


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'owner', 'desc']


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'title', 'desc', 'image_path']
        exclude = ['group']
