from django.urls import path
from . import views
#Bengü:Bu sayfada değiştirdiğim şeyler var.

#Evertime you add a new page, add its path to urls.py. 
#Then add its view to views.py

urlpatterns=[
	#views.home'daki home views.py'daki home functionı
	#'' içerisine home.html yazsaydık localhost:8000 yazdığımızda homePage'e direkt ulaşamazdık. 
	#Böyle yapınca localhost:8000 yazınca direkt olarak homePage'e gidiyoruz.
	path('',views.home,name="home"),
	path('about.html',views.about,name="about"),
	path('add_stock.html',views.add_stock,name="add_stock"),
	path('delete/<stock_id>',views.delete,name="delete"),
	path('delete_stock.html',views.delete_stock,name="delete_stock")
]