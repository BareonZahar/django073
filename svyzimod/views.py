from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(req):
    return render(req,'index.html')
    # fima = Dobavity()
    # bd = Product.objects.all()
    # data = {'fima': fima, 'database': bd}
    # return render(req, 'index.html', context=data)

def add(req):
    # Company.objects.create(title= 'J7')
    # Company.objects.create(title='Добрый')
    # Company.objects.create(title='Сады Придонии')
    # p1 = Product(name='orange',price=170,obym_upakov=3,vid_upakov='Стекло',recomen=True)
    # p2 = Product(name='apple', price=150,obym_upakov=2,vid_upakov='Пласмас',recomen=True)
    # p3 = Product(name='tomat', price=160,obym_upakov=1,vid_upakov='Бумажный покет',recomen=False)
    # c1 = Company.objects.get(title='J7')
    # c2 = Company.objects.get(title='Добрый')
    # c3 = Company.objects.get(title='Сады Придонии')
    # c1.product_set.add(p1, bulk=False)
    # c2.product_set.add(p2, bulk=False)
    # c3.product_set.add(p3, bulk=False)
    # print(c1.product_set.values_list())
    # print(c2.product_set.values_list())
    # print(c3.product_set.values_list())
    return redirect('home')

def table1(req):
    baza = Product.objects.all()
    anketa = FormaSok()
    bd = []
    if req.POST:
        a = req.POST['firma']
        baza = Product.objects.filter(firma_id=a)
    for i in baza:
        bd.append([i.name,i.price,i.firma.title,i.obym_upakov,i.vid_upakov,i.recomen])
    print(bd)
    title = ['Назв.сока','','Цена','','Фирма','','Обьем.упак','','Вид.упак','','Рекомендации','']
    data = {'table':bd,'title':title,'forma':anketa}
    return render(req,'tablisa.html',context=data)

    pass
def table2(req):
    return render(req,'tablisa.html')
    pass
# from .forms import ProductForm
def dobav(req):
    # if req.method == 'POST':
    #     forma = ProductForm(req.POST)
    #     if forma.is_valid():
    #         forma.save()
    #         return render(req,'tablisa.html')
    # else:
    #     forma = ProductForm()
    # return render(req,'tablisa.html',{'fina':forma})

    fima = Dobavity()
    bd = Product.objects.all()
    if req.POST:
        man = Company()
        man.name = req.POST.get('name')
        man.price = req.POST.get('price')
        man.firma = req.POST.get('filma')
        man.ob_upakov = req.POST.get('ob_upakov')
        man.vid_upakov = req.POST.get('vid_upakov')
        man.recomen = req.POST.get('recomen')
        man.save()
        # return render(req,'tablisa.html')
    data = {'fima': fima, 'database': bd}
    return render(req, 'tablisa.html', context=data)

'''
--------------------------------------update_or_create() ===================================
Метод update_or_create (и его асинхронная версия aupdate_or_create())
 обновляет запись, а если ее нет, то добавляет ее в таблицу:

1 : values_for_update={"name":"Bob", "age": 31}
2 : bob, created = Person.objects.update_or_create(id=2, defaults = values_for_update)
        Метод    ------update_or_create()--------   принимает два параметра.
        Первый параметрпредставляет критерий выборки объектов,
        которые будут обновляться.Второй параметр представляет объект со значениями, 
        которые получат выбранные объекты. Если критерию не соответствует
        никаких объектов, то в таблицу добавляется новый объект,
        а переменная created будет равна True.
'''
'''
------------------------------------bulk_update()=====================================
Метод bulk_update() (и его асинхронная версия abulk_update())
 позволяет обновить за один раз набор объектов.

1 : bulk_update(objs, fields, batch_size=None)
        
        Первый параметр - obj указывает на обновляемые объекты,
        а второй параметр - fields представляет обновляемые поля с 
        новыми значениями. Последний параметр - batch_size указывает, 
        сколько объектов обновляется в одном запросе (по умолчанию 
        обновляются все объекты)
        
from .models import Person
  
first_person = Person.objects.get(id=1)
first_person.name = "Tomas"
 
second_person = Person.objects.get(id=2)
second_person.age = 29
 
number = Person.objects.bulk_update([first_person, second_person], ["name", "age"])
print(number)   # 2

        В данном случае у первого объекта обновляется
        значение поля "name", а у второго - значение поля "age".
        Поэтому в качестве второго параметра передается список 
        с данными полями. Результатом метода является количество 
        обновленных объектов.
        Данный метод имеет некоторые ограничения. В частности, 
        мы не можем обновить значение первичного ключа. 
        Также если в обновляемом наборе есть дубли, 
        то только первое вхождение объекта будет 
        использоваться для обновления
        
--------------------- Удаление =======  delete()  ===================
        
        Для удаления мы можем вызвать метод delete()
        (либо его асинхронную версию adelete()) у удаляемого объекта:

1 : person = Person.objects.get(id=2)
2 : person.delete()
        Если не требуется получение отдельного объекта из базы данных,
        тогда можно удалить объект с помощью комбинации методов filter() и delete():

1 : Person.objects.filter(id=4).delete()

        Удаление всех данных из таблицы:

1 : Person.objects.all().delete()


'''
def table3(req):
    baza = User.objects.all()
    anketa = FormaUser()
    if req.POST:
        anketa = FormaUser()
        a = req.POST['user']
        baza = User.objects.all()
