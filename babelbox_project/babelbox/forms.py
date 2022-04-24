from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'message', 'message_language']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_method = 'post'
        self.helper.form_action = '/add'

        self.helper.add_input(Submit('submit', 'Submit'))