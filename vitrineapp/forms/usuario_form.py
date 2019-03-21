from django.forms import ModelForm
from django import forms

from vitrineapp.models import UsuarioModel


class UsuarioForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': True}
        )
    )

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()

    class Meta:
        model = UsuarioModel
        exclude = ('email', 'date_joined', 'is_staff', 'user_permissions', 'groups', 'is_active')
