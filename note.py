from myapp.models import Python2104
a = Python2104(ten="Nguyễn Văn A", tuoi = 12, diachi = "Hồ Chí Minh")
a
# <Python2104: Python2104 object (None)>
a.save()
b = Python2104(ten="Trần B", tuoi=20, diachi = "HÀ Nội")
b.save()
Python2104.objects.all() # SELECT * FROM Python2104
# <QuerySet [<Python2104: Python2104 object (1)>, <Python2104: Python2104 object (2)>]>
for item in Python2104.objects.all():
    print(item.ten, item.tuoi)
# Nguyễn Văn A 12
# Trần B 20
Python2104.objects.get(ten="Nguyễn Văn A") # SELECT * FROM Python2104 WHERE ten = "Nguyễn Văn A"
# <Python2104: Python2104 object (1)>
a1 = Python2104.objects.get(ten="Nguyễn Văn A") # SELECT * FROM Python2104 WHERE ten = "Nguyễn Văn A"
# a1.ten
# 'Nguyễn Văn A'
# a.tuoi
# 12
# a.diachi
# 'Hồ Chí Minh'
# a1.tuoi
# 12
# a1
# <Python2104: Python2104 object (1)>
# a1.tuoi
# 12
a1.tuoi = 30
a1.save()
c = Python2104(ten="Alice", tuoi = 20, diachi="Việt Nam")
c.save() # Khi khởi tạo 1 biến từ class Model thì phải gọi thêm <bien>.save()
# Cách 1: Khởi tạo từ class Model

Python2104.objects.create(ten="Ronaldo", tuoi = 36, diachi = "Juventus")
# <Python2104: Python2104 object (4)>
