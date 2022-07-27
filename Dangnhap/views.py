from django.shortcuts import render
from Dangky.models import NguoiDung

# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')


def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')
    dulieu = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau=mk)
    if (dulieu.exists()):
        return render(request,'themnhanvien.html')
    else:
        return render(request,'thatbai.html')