from django.shortcuts import render,redirect
from django.views.generic import View
from exp_app.forms import SignUpForm,SignInForm,ExpenseCreateForm
from exp_app.models import ExpenseManager

from django.contrib.auth import authenticate,login,logout
from exp_app.decorators import signin_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from django.db.models import Sum,Avg

# Create your views here.

decs=[signin_required,never_cache]


class SignUpView(View):
    template_name="register.html"
    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("signup")
        
        return render(request,self.template_name,{"form":form_instance})
    
class SignInView(View):
    template_name='login.html'
    form_class=SignInForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_obj=authenticate(request,username=uname,password=pwd)

            if user_obj:

                login(request,user_obj)

                print("logged in")

                return redirect("expense-create")

            print("Failed")

            return render(request,self.template_name,{"form":form_instance})

@method_decorator(decs,name="dispatch")
class SignOutView(View):
    
    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

@method_decorator(decs,name="dispatch")
class ExpenseCreateView(View):

    template_name="expense_create.html"

    form_class=ExpenseCreateForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        exp_obj=None

        if id:

            exp_obj=ExpenseManager.objects.get(id=id)


        form_instance = self.form_class(instance=exp_obj)

        qs=ExpenseManager.objects.filter(owner=request.user)

        total_amount=qs.aggregate(Sum('amount'))['amount__sum']

        average=qs.aggregate(Avg('amount'))['amount__avg']

        print(average)

        return render(request,self.template_name,{"form":form_instance,"data":qs,"total":total_amount,"average":average})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST                    
        
        # Update View Start

        id=kwargs.get("pk")

        exp_obj=None

        if id:
            exp_obj=ExpenseManager.objects.get(id=id)

        
        # # Update View End

        form_instance=self.form_class(form_data,instance=exp_obj)

        if form_instance.is_valid():

            form_instance.instance.owner=request.user

            form_instance.save()

            return redirect("expense-create")
        
        return render(request,self.template_name,{"form":form_instance})


class ExpenseDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        ExpenseManager.objects.get(id=id).delete()

        return redirect("expense-create")
    

class ExpenseSummaryView(View):
    template_name="expense_summary.html"

    def get(self,request,*args,**kwargs):

        qs=ExpenseManager.objects.filter(owner=request.user)

        return render(request,self.template_name,{"data":qs})