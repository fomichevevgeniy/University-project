from django import forms
from .models import *


class MainForm(forms.Form):
    first_name = forms.CharField(label="Ismingiz", widget=forms.TextInput(attrs={
        'class': "form__inp",
        'placeholder': "Abdulla"
    }))
    last_name = forms.CharField(label="Familiyangiz", widget=forms.TextInput(attrs={
        'class': "form__inp",
        'placeholder': "Abdullayev"
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': "form__inp",
        'placeholder': "abdulla.abdullayev@gmail.com"
    }))
    phone_number = forms.CharField(label="Telefon raqam", widget=forms.TextInput(attrs={
        'class': "form__inp",
        'placeholder': "+998 (--) --- -- --"
    }))


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            'first_name', 'last_name', 'middle_name',
            'birth_date', 'gender', 'region',
            'district', 'address', 'phone_number',
            'extra_phone_number', 'passport_photo', 'passport_series',
            'passport_numbers', 'faculty', 'diploma_photo',
            'study_type', 'exam_lang'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={
                'id': "input_1",
                'class': "document-information-input",
                'placeholder': "Abdulla"
            }),
            'last_name': forms.TextInput(attrs={
                'id': "input_2",
                'class': "document-information-input",
                'placeholder': "Abdullayev"
            }),
            'middle_name': forms.TextInput(attrs={
                'id': "input_3",
                'class': "document-information-input",
                'placeholder': "Abdulla o‘g‘li"
            }),
            'birth_date': forms.DateInput(attrs={
                'class': "document-information-input",
                'placeholder': "kk/oo/yyyy",
                'type': 'date'
            }),
            'gender': forms.Select(attrs={
                'class': "document-information-input"
            }),
            'region': forms.Select(attrs={
                'class': "document-information-input"
            }),
            'district': forms.TextInput(attrs={
                'id': "input_4",
                'class': "document-information-input",
                'placeholder': "Toshkent tumani"
            }),
            'address': forms.TextInput(attrs={
                'id': "input_5",
                'class': "document-information-input",
                'placeholder': "Amir temur ko’chasi 35"
            }),
            'phone_number': forms.TextInput(attrs={
                'id': "input_6",
                'class': "document-information-input",
                'placeholder': "+998 (--) --- -- --"
            }),
            'extra_phone_number': forms.TextInput(attrs={
                'id': "input_7",
                'class': "document-information-input",
                'placeholder': "+998 (--) --- -- --"
            }),
            'passport_photo': forms.FileInput(attrs={
                'type': "file",
                'class': "document-img-upload",
                'value': "Fotosurat yuklash",
                'accept': "image/jpeg,image/png,image/gif",
                'id': "input_images_front"
            }),
            'passport_series': forms.TextInput(attrs={
                'id': "input_8",
                'class': "document-information-input",
                'placeholder': "AA"
            }),
            'passport_numbers': forms.NumberInput(attrs={
                'id': "input_9",
                'class': "document-information-input",
                'placeholder': "1234567"
            }),
            'faculty': forms.Select(attrs={
                'class': "document-information-input"
            }),
            'diploma_photo': forms.FileInput(attrs={
                'type': "file",
                'class': "document-img-upload",
                'value': "Fotosurat yuklash",
                'id': "input_images_back"
            }),
            'study_type': forms.Select(attrs={
                'class': "document-information-input"
            }),
            'exam_lang': forms.Select(attrs={
                'class': "document-information-input",
            })
        }
