from django import forms
from .models import employee
class FeedbackForm(forms.Form):

    email_id=forms.EmailField(label="enter your mail",max_length=100)
    name=forms.CharField(label="enter your name",max_length=50)
    feedback=forms.CharField(label="your feedback",widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields=['name','employee_id','phone_no','address','Working']