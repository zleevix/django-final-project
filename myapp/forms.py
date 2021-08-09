from django.forms import ModelForm, Form
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import Reporter, Article

class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
        # Thuộc tính `fields` quan trọng, mình muốn cái property/thuộc tính của class được hiển thị HTML.
        # Lấy tất cả luôn: fields = "__all__"
    # Validation client/browser: Kiễm tra được bắt buộc phải nhập tên, họ và email. emal phải đúng format

    # Mình muốn validate ở phía server thì viết form và muốn validate field nào thì tạo hàm tên `clean_<field>`
    #  Các hàm clean_field sẽ đc gọi khi form.is_valid()
    def clean_email(self): # Validation cho thuộc tính email của Reporter
        input_email = self.cleaned_data['email']
        try:
            Reporter.objects.get(email=input_email) # Lấy Reporter theo email
        except Reporter.DoesNotExist:
            # Reporter lấy không được
            # Chứng tỏ input_email này chưa có trong database
            return input_email
        except BaseException as e:
            print("")
        # input_email đã tồn tại trong dabase
        # raise error cho client biết
        raise ValidationError(f"{input_email} đã tồn tại. Vui lòng chọn email khác !")

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'report': forms.Select(attrs={'class': 'form-control'})
        }

class RegisterForm(Form):
    username = forms.CharField(
        label="Tên Đăng Nhâp", 
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "id": "username"
            }
        )
    )
    password = forms.CharField(
        label="Mật Khẩu", 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 
                "id": "password"
            }
        )
    )
    confirm_password = forms.CharField(
        label="Nhập Lại Mật Khẩu", 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 
                "id": "confirm_password"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control", 
                "id": "email"
            }
        )
    )
    first_name = forms.CharField(
        label="Tên",
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "id": "first_name"
            }
        )
    )
    last_name = forms.CharField(
        label="Họ",
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "id": "last_name"
            }
        )
    )
    # avarta = forms.ImageField()
    

    # Validation: username và email không được trùng với data trong database.
    #             password và confirm_password là phải giống nhau (Kiểm tra ở phía client, javascript)

    def clean_username(self):
        inputed_username = self.cleaned_data['username']
        try:
            User.objects.get(username=inputed_username)
            raise ValidationError(f"Tên đăng nhập '{inputed_username}' đã tổn tại. Vui lòng chọn tên đăng nhập khác")
        except User.DoesNotExist:
            return inputed_username

    def clean_email(self):
        inputed_email = self.cleaned_data['email']
        try:
            User.objects.get(email=inputed_email)
            raise ValidationError(f"Email '{inputed_email}' đã tổn tại. Vui lòng chọn tên email khác")
        except User.DoesNotExist:
            return inputed_email

    def clean_confirm_password(self):
        inputed_password = self.cleaned_data['password']
        inputed_confirm_password = self.cleaned_data['confirm_password']
        if inputed_password != inputed_confirm_password:
            raise ValidationError(f"Mật khẩu không trùng nhau")
        return inputed_confirm_password

    def save_user(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return User.objects.get(username = self.cleaned_data['username'])


class LoginForm(Form):
    username = forms.CharField(
        label="Tên Đăng Nhâp", 
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "id": "username"
            }
        )
    )
    password = forms.CharField(
        label="Mật Khẩu", 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 
                "id": "password"
            }
        )
    )
    # remember = forms.ChoiceField()
