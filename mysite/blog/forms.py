from django import forms
from .models import Comment, PostRating, Recipe, RecipeComment, RecipeRating, Post


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
