from django import forms
from django.forms import ModelForm
# Task modelinizin import edildiğini varsayıyoruz
from .models import Task 

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_done']
        
        # --- Widget'lar Bölümü ---
        widgets = {
            # 1. 'title' Alanı İçin Widget
            # CharField'lar için yaygın olarak TextInput kullanılır.
            # 'class' niteliği ile Bootstrap/CSS sınıfı ekledik.
            # 'placeholder' ile alan içinde bir ipucu gösterdik.
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Görevin başlığını buraya girin'
            }),
            
            # 2. 'description' Alanı İçin Widget
            # TextField'lar için varsayılan olarak Textarea kullanılır.
            # Yine bir CSS sınıfı ekledik ve satır sayısını belirttik.
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,  # Textarea'nın varsayılan yüksekliğini artırır
                'placeholder': 'Görevin detaylı açıklamasını girin'
            }),
            
            # 3. 'is_done' Alanı İçin Widget
            # BooleanField'lar için varsayılan CheckboxInput'tur.
            # Widget'ı özelleştirerek özel bir form sınıfı verdik.
            # Not: Checkbox'lar için 'form-check-input' gibi özel sınıflar yaygındır.
            'is_done': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }