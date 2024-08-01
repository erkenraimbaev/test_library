from django.contrib.auth.forms import UserCreationForm

from users.models import Reader


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = Reader
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        reader = super().save(commit=False)
        if commit:
            reader.save()
        return reader
