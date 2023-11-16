from django import forms
from .models import Person


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "nickname",
                  "age", "gender", "address", "favorite_artist",
                  "birthday", "zodiac_sign", "profile_picture", "mbti",
                  "iq", "blood_type"]
        widgets = {
            "birthday": DateInput()
        }