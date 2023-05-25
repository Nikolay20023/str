from django import forms
from django.contrib.auth import get_user_model
from .models import Course, Comment, Follow


User = get_user_model()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            'name',
            'on_list',
            'on_list_fact',
            'sport',
            'komandirovka',
            'bolinoy',
            'otpusk',
            'praktika',
            'raport'
        )
        help_text = {
            'name': 'Курс',
            'on_list': 'По списку',
            'on_list_fact': 'На лицо',
            'sport': 'Спорт',
            'komandirovka': 'Командировка',
            'bolinoy': 'Больной',
            'otpusk': 'Отпуск',
            'praktika': 'Практика',
            'raport': 'Рапорт'
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if data.lower() == '':
            raise forms.ValidationError('Вы должны заполнить поля текста ')
        return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        help_text = {
            'text': 'Текст нового комментария'
        }


class FollowForm(forms.ModelForm):
    model = Follow
    fields = ('user', 'author',)

    def clean_text(self):
        data = self.cleaned_data['text']
        if data.lower() == '':
            raise forms.ValidationError('Вы должны заполнить поля текста ')
        return data
    '''def clean_slug(self):
        """Обрабатывает случай, если slug не уникален."""
        cleaned_data = super().clean()
        slug = cleaned_data.get('slug')
        if not slug:
            title = cleaned_data.get('title')
            slug = slugify(title)[:100]
        if Post.objects.filter(slug=slug).exists():
            raise forms.ValidationError(
                f'Адрес "{slug}" уже существует, '
                'придумайте уникальное значение'
            )
        return slug'''
