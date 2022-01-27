from django import forms

my_default_errors = {
    'required': 'This attribute is required',
    'invalid': 'The requested date and/or time have an '
               'incorrect format. The correct format '
               'should be YYYY-MM-DDTHH:MM:SS'
}


class DateTimeForm(forms.Form):
    start_time = forms.DateTimeField(required=True, error_messages=my_default_errors)
    end_time = forms.DateTimeField(required=True, error_messages=my_default_errors)

    def clean_start_time(self):
        start_time = self.cleaned_data['start_time']
        return start_time

    def clean_end_time(self):
        end_time = self.cleaned_data['end_time']
        return end_time
