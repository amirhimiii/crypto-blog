from django import forms
from blog.models import User

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','last_name','first_name','email','special_user','is_author']


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileUserForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['username'].disabled =True
            self.fields['email'].disabled =True
            self.fields['special_user'].disabled =True
            self.fields['is_author'].disabled =True    

    


