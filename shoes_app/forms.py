from django import forms
from shoes_app.models import Shoe


CATEGORY = [ ('Boots', 'Boots'), ('Sneakers', 'Sneakers'), 
('Sports', 'Sports'), ('Men','Men'), ('Women','Women') ]

GENDER = [ ('Unisex', 'Unisex'), ('Male', 'Male'), ('Female', 'Female') ]


class AddShoeForm(forms.ModelForm):
    name = forms.CharField(
        label="",
        help_text='name of the shoe. Field is required *',
        widget=forms.TextInput(attrs={
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'shoe name'}),
    )
    description = forms.CharField(
        label="",
        help_text='tell others more about this shoe. Field is required *',
        widget=forms.Textarea(attrs={
            'rows':7,
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'about this shoe product'}),
    )
    brand = forms.CharField(
        label="",
        required=False,
        help_text='brand of shoe e.g nike. Field is not required',
        widget=forms.TextInput(attrs={
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'shoe brand'}),
    )
    price = forms.FloatField(
        label="",
        required=False,
        help_text='how much you would sell this shoe. Field is not required',
        widget=forms.NumberInput(attrs={
            'class':'', 
            'align':'center', 
            'placeholder':'price'}),
    )
    shoe_size = forms.FloatField(
        label="",
        required=False,
        help_text='specify the size of this shoe. Field is not required',
        widget=forms.NumberInput(attrs={
            'class':'', 
            'align':'center',
            'maxlength': '500', 
            'placeholder':'shoe size'}),
    )
    category = forms.ChoiceField(
        choices= CATEGORY,
        label="",
        help_text='select the type of shoe. Field is required *',
        widget=forms.Select(attrs={
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'type of shoe'}),
    )
    gender = forms.ChoiceField(
        choices= GENDER,
        label="",
        help_text='who this shoe is most approriate for. Field is required *',
        widget=forms.Select(attrs={
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'type of shoe'}),
    )
    image1 = forms.ImageField(
        label="",
        help_text='this is the first image displayed. Field is required *',
    )
    image2 = forms.ImageField(
        label="",
        required=False,
        help_text='these are images displayed in the details page. Field is not required',
    )
    image3 = forms.ImageField(
        label="",
        required=False,
        help_text='these are images displayed in the details page. Field is not required',
    )
    image4 = forms.ImageField(
        label="",
        required=False,
        help_text='these are images displayed in the details page. Field is not required',

    )
    image5 = forms.ImageField(
        label="",
        required=False,
        help_text='these are images displayed in the details page. Field is not required',

    )

# class ShoeOwnerForm(forms.ModelForm):

    shop_name = forms.CharField(
        label="",
        required=False,
        help_text='your brand name. Field is not required',
        widget=forms.TextInput(attrs={
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'brand or shop name'}),
    )
    about_shop = forms.CharField(
        label="",
        required=False,
        help_text='about your shop or brand. Field is not required',
        widget=forms.Textarea(attrs={
            'rows':7,
            'class':'', 
            'type':'text', 
            'maxlength': '444',
            'align':'center', 
            'placeholder':'about shop or brand'}),
    )
    website = forms.URLField(
        label="",
        required=False,
        help_text='specify your brand or shop website. field must be in URL form. Field is not required',
        widget=forms.URLInput(attrs={
            'class':'', 
            'type':'url', 
            'align':'center', 
            'placeholder':'website'}),
    )
    instagram = forms.CharField(
        label="",
        required=False,
        help_text='your brand instagram name. Field is not required',
        widget=forms.TextInput(attrs={
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'instagram'}),
    )
    facebook = forms.CharField(
        label="",
        required=False,
        help_text='your brand facebook name. Field is not required',
        widget=forms.TextInput(attrs={
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'facebook'}),
    )
    twitter = forms.CharField(
        label="",
        required=False,
        help_text='your brand twitter name. Field is not required',
        widget=forms.TextInput(attrs={
            'class':'', 
            'type':'text', 
            'align':'center', 
            'placeholder':'twitter'}),
    )


    class Meta:
        model = Shoe
        fields = [
        'name','description','brand','price',
        'shoe_size','category','gender','image1',
        'image2','image3','image4','image5',
        'shop_name','about_shop',
        'website','instagram','facebook','twitter'
        ]
