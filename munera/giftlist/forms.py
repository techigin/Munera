from django import forms
from . import models

class AddGift(forms.ModelForm):
    class Meta:
        model = models.Gift
        fields = ['name', 'price', 'link', 'user']

class AddGroupMember(forms.ModelForm):
    class Meta:
        model = models.GroupMember
        fields = ['member','group']
