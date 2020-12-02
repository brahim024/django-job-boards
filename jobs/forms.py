from django import forms
from .models import Apply,Post
from ckeditor.widgets import CKEditorWidget
class ApplyForm(forms.ModelForm):
	#Coverletter=forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=Apply
        fields='__all__'
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        exclude=('user','slug')
