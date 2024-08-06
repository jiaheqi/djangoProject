from django import forms
from .models import PersonInfo,Vocation


class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = '__all__'


class VocationForm(forms.ModelForm):
    class Meta:
        model = Vocation
        fields = '__all__'
    job = forms.CharField(max_length=20, label='职位')
    title = forms.CharField(max_length=20, label='职称')
    payment = forms.IntegerField(label='工资', initial=1000)
    value = PersonInfo.objects.values('name')
    choices = [(i + 1, v['name']) for i, v in enumerate(value)]
    name = forms.ChoiceField(choices=choices, label='选择人员', widget=forms.Select)
