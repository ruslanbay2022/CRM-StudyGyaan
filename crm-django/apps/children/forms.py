from django import forms
from apps.children.models import Child


# USER FORM
class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = [
            'gender',
            'name',
            'middlename',
            'surname',
            'birth_date',
            'avatar',
            'bio',
            'archived',
        ]