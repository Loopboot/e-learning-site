from django import forms
from .models import Course, Lesson, Material

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'difficulty', 'thumbnail', 'is_published')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'content', 'order')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('title', 'file', 'material_type', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
