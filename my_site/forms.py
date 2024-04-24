from django import forms
from .models import FormFooterContact, FormPopup

class FormFooterData(forms.ModelForm):
    name_under_footer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form'}))
    phone_under_footer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+7 (---) --- -- --', 'class': 'form',  'requirements': 'requirements',}))

    class Meta:
        model = FormFooterContact
        fields = ('name_under_footer', 'phone_under_footer')




class FormPopupForm(forms.ModelForm):
    class Meta:
        model = FormPopup
        fields = ['name_popup', 'phone_popup']

    def __init__(self, *args, **kwargs):
        super(FormPopupForm, self).__init__(*args, **kwargs)
        self.fields['name_popup'].widget.attrs.update({
            'id': 'id_name_popup',
            'class': 'form__input',
            'placeholder': 'Ваше имя'
        })
        self.fields['phone_popup'].widget.attrs.update({
            'id': 'id_phone_popup',
            'class': 'form__input phone',
            'placeholder': '+7 (---) --- -- --',
            'requirements': 'requirements',
        })

    def clean_phone(self):
        phone = self.cleaned_data.get('phone_popup')
        # Добавьте здесь логику проверки номера телефона, если это необходимо
        return phone
