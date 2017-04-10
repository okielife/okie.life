from django.forms import ModelForm

from .models import Blog


class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class BlogForm(BootstrapModelForm):
    class Meta:
        model = Blog
        exclude = ['posted', 'created_on']
