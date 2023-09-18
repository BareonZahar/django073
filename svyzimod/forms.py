from django import forms
from .models import Company

class FormaSok(forms.Form):
    all = Company.objects.all()
    # firma = forms.ModelChoiceField(all.filter(all.db.title))
    mas = []
    for a in all:
        mas.append((a.id,a.title))
    print(mas)
    # firma = forms.ModelChoiceField(Company.objects.all(),required=False)
    firma = forms.ChoiceField(choices=tuple(mas))
    # sok = forms.ModelChoiceField(Product.objects.all(),required=False)
# from .models import Product
# class ProductForm(forms.ModelForm):
#
#     class Meta:
#         model = Product()
#         fields = ['name','price','obym_upakov','vid_upakov','firma']
class Dobavity(forms.Form):
        name = forms.CharField(label='Название сока',max_length=20)
        price = forms.IntegerField(label='Цена сока')
        title = forms.CharField(label='Компания производитель')
        ob_upakov = forms.IntegerField(label='Объем упаковки',required=False)
        vid_upakov = forms.CharField(label='Вид упаковки',max_length=20,required=False)
        recomen = forms.BooleanField(label='Рекомендован',required=False)


# class FormaStudent(forms.Form):
#     imy = forms.ModelChoiceField(Student.objects.all(),required=False)
#     predmet = forms.ModelChoiceField(Course.objects.all(),required=False)
# class FormaUser(forms.Form):
