from django.contrib.auth.forms import UserCreationForm
from django import forms
from exp_app.models import User,ExpenseManager

class SignUpForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}),label="Enter Password")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}),label="Confirm Password")

    class Meta:

        model=User

        fields=["username","email","phone_number"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter E-Mail"}),
            "phone_number":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Phone Number"}),
        }


class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))


class ExpenseCreateForm(forms.ModelForm):

    class Meta:

        model=ExpenseManager

        fields=['title','category','amount','payment']

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Title"}),
            "category":forms.Select(choices=ExpenseManager.category_options,attrs={"class":"form-control form-select"}),
            "amount":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Amount"}),
            "payment":forms.Select(choices=ExpenseManager.payment_options,attrs={"class":"form-control"})
        }