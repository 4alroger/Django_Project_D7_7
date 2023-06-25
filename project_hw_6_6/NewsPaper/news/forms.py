from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Заголовок'
        self.fields['category'].empty_label = None
        self.fields['category'].label = 'Категория'
        self.fields['author'].label = 'Автор'
        self.fields['author'].empty_label = 'Выберите автора'

    class Meta:
        model = Post

        fields = ['title',
                  'content',
                  'author',
                  'category']
