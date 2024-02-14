from typing import Any
from django import forms


class Course(forms.Form):

    course_name=forms.CharField()
    course_fee=forms.IntegerField()
    course_description=forms.CharField()

    