from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from shoes_app.forms import AddShoeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from shoes_app.models import Shoe
from django.contrib.auth.decorators import login_required


def index_page(request):
    
    sneakers = Shoe.objects.filter(category='Sneakers').order_by('-time_posted')
    women_shoes = Shoe.objects.filter(category='Women').order_by('-time_posted')
    men_shoes = Shoe.objects.filter(category='Men').order_by('-time_posted')
    boots = Shoe.objects.filter(category='Boots').order_by('-time_posted')
                       
    return render(request,'index.html',
    {
    'sneakers':sneakers,
    'women_shoes':women_shoes,
    'men_shoes':men_shoes,
    'boots':boots,

    })
    
def search(request):
    if request.method == 'GET':
        return redirect('index')
    
    if request.method == 'POST':
        search = request.POST['search']
        shoes = Shoe.objects.filter(name__contains=search)
        users = User.objects.filter(username__contains=search)
        
               
    return render(request,'search.html',{
        'search':search,'shoes':shoes,'users':users})  
    

        
def about_us(request):
    return render(request,'about_us.html',{})

def men_shoes_page(request):
    
    men_shoes = Shoe.objects.filter(category='Men')   
    return render(request,'shoes_app/men_shoes.html',{'men_shoes':men_shoes})

def women_shoes_page(request):  
    
    women_shoes = Shoe.objects.filter(category='Women')
    return render(request,'shoes_app/women_shoes.html',{'women_shoes':women_shoes})

def boots_page(request):
    
    boots = Shoe.objects.filter(category='Boots')
    return render(request,'shoes_app/boots.html',{'boots':boots})

def sneakers_shoe_page(request):
    
    sneakers = Shoe.objects.filter(category='Sneakers')
    return render(request,'shoes_app/sneakers_shoes.html',{'sneakers':sneakers})

def sports_shoe_page(request): 
    sports_shoe = Shoe.objects.filter(category='Sports')
    return render(request,'shoes_app/sports_shoes.html',{'sports_shoe':sports_shoe})

class AddShoe(LoginRequiredMixin,CreateView):
    model = Shoe
    form_class = AddShoeForm    
    template_name = "shoes_app/add_shoe.html"
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        
        if self.request.user != form.instance.user:
            return redirect('index')
        
        return super().form_valid(form)
    
    
def shoe_detail(request,slug):
    shoe =  Shoe.objects.get(slug=slug)
    return render(request,'shoes_app/shoe_detail.html',
    {'shoe':shoe})

@login_required
def edit_shoe(request,slug):
    shoe = Shoe.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = AddShoeForm(request.POST,request.FILES,instance=shoe)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Shoe model updated successfully')
            return redirect('index')
          
    else:
        form = AddShoeForm(instance=shoe)
    
    
    if request.user != shoe.user:
        return redirect('index')
    
    
    return render(request,'shoes_app/edit_shoe.html',{'shoe':shoe,'form':form})        


@login_required
def delete_shoe(request,slug):
    shoe = Shoe.objects.get(slug=slug)
      
    if request.method == 'POST':
        shoe.delete()
        messages.success(request,'Shoe deleted successfully')
        return redirect('index')
    
    if request.user != shoe.user:
        return redirect('index')

    return render(request,'shoes_app/delete_shoe.html',{'shoe':shoe})