from django.urls import path
from .views import Company,add_emp,delete_emp,update_emp,do_update,Testimonials,feedback
urlpatterns= [
    path("home/",Company),
    path("add-emp/",add_emp),
    path("update-emp/<int:employee_id>",update_emp),
    path("del-emp/<int:employee_id>",delete_emp),
    path("do-update/<int:employee_id>",do_update),
    path("testimonials/",Testimonials),
    path("feedback/",feedback),
]