from django import forms
from .models import Comment, PostRating, Recipe, RecipeComment, RecipeRating, Post,Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ['name', 'email', 'body']


class RatingForm(forms.ModelForm):
    class Meta:
        model = PostRating
        fields = ['name', 'email', 'rating']


class RecipeRatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['name', 'email', 'rating']


class SearchForm(forms.Form):
    query = forms.CharField()

class ImageCreateForm(forms.Form):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description','recipetype','cuisinetype']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.'
            )
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from the given URL
        response = requests.get(image_url)
        image.image.save(
            image_name,
            ContentFile(response.content),
            save=False
        )
        if commit:
            image.save()
        return image
