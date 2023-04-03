from .models import MyUser, Shop, Product
from django.forms import ModelForm, TextInput, CharField, PasswordInput, EmailInput, TimeInput, Textarea, NumberInput
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password1 = CharField(widget = PasswordInput(attrs = {'placeholder' : 'Password (at least 8 characters)', 'id' : 'password1'}), min_length = 8)
    password2 = CharField(widget = PasswordInput(attrs = {'placeholder' : 'Confirm Password (at least 8 characters)', 'id' : 'password2'}), min_length = 8)

    class Meta:
        model = MyUser
        fields = ['username' ,'email', 'password1', 'password2']
        widgets = {
            'email' : EmailInput(attrs = {'id' : 'email', 'placeholder' : 'E-Mail'}),
            'username' : TextInput(attrs = {'id' : 'username', 'placeholder' : 'Username'}),
        }


class RegisterShop(ModelForm):
    class Meta:
        model = Shop 
        fields = ['name', 'category', 'opening_time', 'closing_time', 'address', 'state', 'city', 'pincode']
        widgets = {
            'name' : TextInput(attrs = {'id' : 'name', 'placeholder' : 'Shop Name'}),
            'opening_time' : TimeInput(attrs = {'id' : 'opening_time', 'placeholder' : 'Opening Time', 'type' : 'time'}),
            'closing_time' : TimeInput(attrs = {'id' : 'closing_time', 'placeholder' : 'Closing Time', 'type' : 'time'}),            
            'address' : Textarea(attrs = {'id' : 'address', 'placeholder' : 'Full Address'}),
            'state' : TextInput(attrs = {'id' : 'state', 'placeholder' : 'State'}),
            'city' : TextInput(attrs = {'id' : 'city', 'placeholder' : 'City'}),
            'pincode' : TextInput(attrs = {'id' : 'pincode', 'placeholder' : 'Pincode'}),
        }


class AddItemForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'price', 'description']
        widgets = {
            'name' : TextInput(attrs = {'id' : 'name', 'placeholder' : 'Product Name'}),
            'price' : NumberInput(attrs = {'id' : 'price', 'placeholder' : 'Product Price'}),
            'description' : Textarea(attrs = {'id' : 'description', 'placeholder' : 'Product Description'})
        }