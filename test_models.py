import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")
django.setup()

from myapp.models import Python2104, Restaurant, Place, Article, Reporter, Publication, BaiBao

# # a = Python2104(ten="Messi", tuoi = 34, diachi= "Barcelona")
# # a.save()
# a = Python2104.objects.filter(tuoi=20)
# for i in a:
#     print(i.ten)
# all_data = Python2104.objects.all()
# for item in all_data:
#     print(item.ten, item.tuoi)


# p1 = Place(name="Quận 1", address = "Hồ Chí Minh")
# p1.save()

# rest1 = Restaurant(place_id = 1, serves_hot_dogs=True, serves_pizza=False) # place_id là tên chính xác column trong
# rest1.save()

# p2 = Place.objects.create(name="Quận 2", address="Hồ Chí Minh") # 
# p2 = Place.objects.get(name="Quận 2")
# rest2 = Restaurant(place=p2, serves_hot_dogs=True, serves_pizza=False) # p2 là đối tượng
# rest2.save()

# p3 = Place.objects.create(name="Quận 3", address="Hồ Chí Minh")
# p3.


# place = Place.objects.get(name="Quận 1") # Nhìn vô là biết biến place là khởi tạo từ Place#
# a = Place.objects.get(name="Quận 1")
# restaurant = Place.objects.get(name="Quận 1")
# Note: tên biến khởi tạo thì tên class viết thường
# print(place.restaurant.serves_hot_dogs, place.restaurant.serves_pizza)
# # Truy suất tới restaurant
# print(place.restaurant) # restaurant là tên class quan hệ 1-1 thằng Place viết thường

# restaurants = Restaurant.objects.all()
# Class Person -> số ít person, số ít people
# for rest in restaurants:
#     print(rest.place.name)
# Quan hệ 1-1: Thông qua field: OneToOneField
# Truy cập vào cái đối tượng class liên kết thì truy cập qua thuộc tính <tên class viết thường>
# Place 1-1 Restaurant
# Biến đc khởi tạo từ Place tên place. Truy cập qua Restaurant thì gọi place.restaurant.
# Và ngược lại    

# Quan hệ 1-n
# 1 Reporter sẽ có nhiều Articles
# reporter = Reporter.objects.create(first_name = "Cristiano", last_name = "Ronaldo", email="ronaldo@ gmail.com")
# Cách 1: truyền chính xác tên được định nghĩa trong table 
# import datetime
# reporter1 = Reporter.objects.get(pk=1) # id = pk
# article1 = Article(headline = "Ronaldo ghi cú đúp Penalty trong trận Pháp-Bồ", pub_date=datetime.datetime.now(), reporter_id=reporter1.id)
# article1.save()
# Cách 2: truyền tên với các tên được định nghĩa trong models
# reporter1 = Reporter.objects.get(pk=1) # id = pk
# article3 = Article(headline = "Ronaldo ghi cú đúp Penalty trong trận Pháp-Bồ", pub_date=datetime.datetime.now(), reporter=reporter1)
# article3.save()
# Cách 3: <số nhiều>_set
# reporter1 = Reporter.objects.get(pk=1)
# reporter1.article_set.all() = Article.object.filter(reporter= reporter)
# reporter1.article_set.create(headline = "Benzama ghi cú đúp trong trận Pháp-Bồ", pub_date=datetime.datetime.now())

# Lấy thông tin ra
# reporter1 = Reporter.objects.get(pk=1) # 
# print(reporter1.first_name, reporter1.last_name)
# article1 =  Article.objects.get(pk=1)
# print(article1.reporter.first_name) # reporter class số 1 viết thường
# print(reporter1.article_set.all()) # <tên class số nhiều>_set
# articles = Article.objects.filter(reporter=reporter1) # 
# for item in reporter1.article_set.all():
#     print(item.headline)

# Quan hệ 1-n: thông qua fields ForeignKey
# 1 SoMot - n SoNhieu
# 1 biến từ class SoMot tên là somot. Truy cập qua các data liên quan tới nó
# thông qua somot.sonhieu_set.all() 
#  1 biến từ class SoNhieu tên sonhieu. Truy cập qua data class kia
# thông quan sonhieu.somot

# Publication.objects.create(title="Title 1")
# Publication.objects.create(title="Title 2")
# BaiBao.objects.create(headline = "Headline 1")
# BaiBao.objects.create(headline = "Headline 2")

# pub1 = Publication.objects.get(title="Title 1")
# pub2 = Publication.objects.create(title="Title 2")
# b1 = BaiBao.objects.get(headline = "Headline 1")
# b2 = BaiBao.objects.get(headline = "Headline 2")
# b1.publications.add(pub1, pub2)
# pub1.baibao_set.add(b1,b2)

# Quan hệ nhiều-nhiều: ManyToManyField
# Truy cập qua lại:
# Class nào có chưa field ManyToManyField thì lấy field đó ra dùng hàm add thêm vào
# Class kia thì <tên class kia>_set.add()

# all() -> Trả về 1 list
for reporter in Reporter.objects.all():
    print(reporter.first_name)

