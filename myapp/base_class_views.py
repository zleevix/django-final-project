import django
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from .models import Reporter, Article, Python2104

from .forms import ReporterForm

# List all data
class ReportListView(ListView):
    model = Reporter 
    # queryset = Reporter.objects.all()
    # Sử dụng ListView thì phải định nghĩa 1 trong 3 cái:
    # 1. model
    # 2. queryset
    # 3. Override method get_queryset()

    context_object_name = "all_reporters" # Đổi `object_list` thành giá trị của context_object_name cho dể nhớ
    # Template mặc định mà ListView này hiển thì là <tên appname>/<tên class model viết thường>_list.html
    # App myapp, tên model là reporter thì nó sẽ hiển thị template là `myapp/reporter_list.html`
    # Đổi template hiển thị
    template_name = "class_base/list_view.html" # Đổi tempalte qua `template_name`

    # thuộc tính dùng để phân trang trong ListView
    paginate_by = settings.PAGINATE_BY # Số lượng item muốn hiển thị 


    # Thêm context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['python2104'] = Python2104.objects.all()
        return context

    def get_queryset(self):
        # print(self.request.GET.get("search"))
        search = self.request.GET.get('search')
        all_reporters = Reporter.objects.all()
        if search:
            all_reporters = Reporter.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
        return all_reporters

@method_decorator(login_required(login_url="/login"), name="dispatch")
class ReporterDetailView(DetailView):
    model = Reporter
    template_name = "class_base/detail_view.html"

    # Thêm context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = "Hello from addtional context"
        return context

@method_decorator(login_required(login_url="/login"), name="dispatch")
class ReporterCreateView(CreateView):
    model = Reporter
    # fields = "__all__"
    form_class = ReporterForm
    template_name = "class_base/create_view.html"
    # success_url = reverse('all_reporters')

    def get_success_url(self):
        # return super().get_success_url()
        return reverse("all_reporters")

@method_decorator(login_required(login_url="/login"), name="dispatch")
class ReporterUpdateView(UpdateView):
    model = Reporter
    # fields = "__all__"
    form_class = ReporterForm
    template_name = "class_base/update_view.html"
    # success_url = reverse('all_reporters')
    def get_success_url(self):
        # return super().get_success_url()
        return reverse("all_reporters")

@method_decorator(login_required(login_url="/login"), name="dispatch")
class ReporterDeleteView(DeleteView):
    model = Reporter
    # success_url = reverse('all_reporters')
    template_name = "class_base/confirm_delete.html"
    def get_success_url(self):
        # return super().get_success_url()
        return reverse("all_reporters")


# ListView/DetailView   Read đọc dữ liệu
# CreateView            Create tạo mới dữ liệu
# UpdateView            Update cập nhật dữ liệu
# DetleteView           Delete xoá dữ liẹu