from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse


# def home(request):
#     context = {
#         "username": "Eman",
#         "age": 30,
#         "job": "programmer"

#     }
#     return render(request, "blog/home.html", context)
def home(request):
    context = {
        "articles": [
            {
                "title": "رونالدو گل برونو را به نام خودش ثبت کرد! (عکس)",
                "description": "کریستیانو رونالدو، ستاره پرتغالی، شب گذشته ابعاد جدیدی از غرور و خودبزرگ بینی‌اش را به نمایش گذاشت.",
                "img": "https://news-cdn.varzesh3.com/pictures/2022/11/29/B/nbxr114h.jpg?w=315",
            },
            {
                "title": "عصرانه و شام در اروگوئه با چاشنی علیرضا فغانی",
                "description": "فغانی در آخرین دقایق قضاوت بی‌دردسر خود، یک ضربه پنالتی اعلام کرد که حسابی جنجالی شد.",
                "img": "https://newsw-cdn.varzesh3.com/pictures/2022/11/29/B/ua1u2lij.jpg?w=315",
            },
            {
                "title": "ویژه: آخرین احتمالات صعود در گروه ایران",
                "description": "بیشتر از نصف احتمالات گروه ایران، حکم به صعود تیم‌ملی از مرحله گروهی جام جهانی می‌دهد.",
                "img": "https://news-cdn.varzesh3.com/pictures/2022/11/28/A/j2tmtgqw.jpg?w=315",
            }

        ]
    }
    return render(request, "blog/home.html", context)
