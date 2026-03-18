from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from locations.models import SubCity, Woreda

class UserRegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('SUBCITY_ADMIN', 'SubCity Admin'),
        ('WOREDA_ADMIN', 'Woreda Admin'),
        ('WOREDA_STAFF', 'Woreda Staff'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES)
    sub_city = forms.ModelChoiceField(queryset=SubCity.objects.all())
    woreda = forms.ModelChoiceField(queryset=Woreda.objects.none(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'sub_city', 'woreda', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load Woredas when SubCity is selected
        if 'sub_city' in self.data:
            try:
                sub_city_id = int(self.data.get('sub_city'))
                self.fields['woreda'].queryset = Woreda.objects.filter(sub_city_id=sub_city_id)
            except:
                self.fields['woreda'].queryset = Woreda.objects.none()

        elif self.instance.pk and self.instance.sub_city:
            self.fields['woreda'].queryset = Woreda.objects.filter(sub_city=self.instance.sub_city)
