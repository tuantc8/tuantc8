from django.shortcuts import render

# Create your views here.


# Create your views here.
def nhanvien(request):
    return render(request,'themnhanvien.html')


# def xuly_dangnhap(request):
#     ten = request.GET.get('ten')
#     mk = request.GET.get('matkhau')
#     dulieu = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau=mk)
#     if (dulieu.exists()):
#         return render(request,'themnhanvien.html')
#     else:
#         return render(request,'thatbai.html')