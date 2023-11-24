from django.contrib import admin
from myfiles.models import *
# Register your models here.
# student start

class AdminDarajaType(admin.ModelAdmin):
    list_display = ['id', 'nomi']
admin.site.register(DarajaType,AdminDarajaType)
class AdminTolovQilganYokiQilmaganType(admin.ModelAdmin):
    list_display = ['nomi']

admin.site.register(TolovQilganYokiQilmaganType, AdminTolovQilganYokiQilmaganType)

class AdminTolovQilganYokiQilmaganType_5_10(admin.ModelAdmin):
    list_display = ['nomi']

admin.site.register(TolovQilganYokiQilmaganType_5_10, AdminTolovQilganYokiQilmaganType_5_10)


class AdminTolovQilganYokiQilmaganType_10_15(admin.ModelAdmin):
    list_display = ['nomi']

admin.site.register(TolovQilganYokiQilmaganType_10_15, AdminTolovQilganYokiQilmaganType_10_15)

class AdminTolovQilganYokiQilmaganType_20_25(admin.ModelAdmin):
    list_display = ['nomi']

admin.site.register(TolovQilganYokiQilmaganType_20_25, AdminTolovQilganYokiQilmaganType_20_25)

class AdminTolovQilganYokiQilmaganType_25_30(admin.ModelAdmin):
    list_display = ['nomi']

admin.site.register(TolovQilganYokiQilmaganType_25_30, AdminTolovQilganYokiQilmaganType_25_30)




class AdminTolovType(admin.ModelAdmin):
    list_display = ['id' , 'oy1' ]
admin.site.register(TolovType,AdminTolovType)

class AdminTaniganType(admin.ModelAdmin):
    list_display = ['id', 'nomi']
admin.site.register(QayerdanTaniganType,AdminTaniganType)

class AdminTeacherType(admin.ModelAdmin):
    list_display = ['id', 'nomi']
admin.site.register(TeacherType,AdminTeacherType)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'yosh', 'manzil', 'dars_soati','telefon','telefon2','darajasi', 'Oquv_tanigan' , 'qaysi_ustoz', 'date']


admin.site.register(Student,AdminStudent)
# student end
class AdminXarajatType(admin.ModelAdmin):
    list_display = ['nomi']
admin.site.register(XarajatType , AdminXarajatType)
class AdminXarajat(admin.ModelAdmin):
    list_display = ['id','description','qancha_pul_ketgan','XarajatTuri','date',]
admin.site.register(Xarajatlar , AdminXarajat)

# for student rus
class AdminStudentRus(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'yosh', 'manzil', 'dars_soati','telefon','telefon2','darajasi', 'Oquv_tanigan' , 'qaysi_ustoz', 'date']


admin.site.register(Student_rus,AdminStudentRus)

class AdminAllPeople(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'yosh', 'manzil', 'dars_soati','telefon','telefon2','darajasi', 'Oquv_tanigan' , 'qaysi_ustoz', 'qancha_tolov_qiladi','date']


admin.site.register(All_people,AdminAllPeople)



class AdminJuftKunlar(admin.ModelAdmin):
    list_display = ['id' , 'ism' , 'gurux_vaqti' , 'qaysi_ustoz' , 'qaysi_fan' , 'oquvchi1' , 'oquvchi2' , 'oquvchi3' , 'oquvchi4' , 'oquvchi5' , 'oquvchi6' , 'oquvchi7' , 'oquvchi8' , 'oquvchi9' , 'oquvchi10' , 'oquvchi11' , 'oquvchi12' , 'oquvchi13' , 'oquvchi14' ,  'oquvchi15' ]


admin.site.register(Juft_kunlari,AdminJuftKunlar)



class AdminToqKunlar(admin.ModelAdmin):
    list_display = ['id' , 'ism' , 'gurux_vaqti' , 'qaysi_ustoz' , 'qaysi_fan' , 'oquvchi1' , 'oquvchi2' , 'oquvchi3' , 'oquvchi4' , 'oquvchi5' , 'oquvchi6' , 'oquvchi7' , 'oquvchi8' , 'oquvchi9' , 'oquvchi10' , 'oquvchi11' , 'oquvchi12' , 'oquvchi13' , 'oquvchi14' ,  'oquvchi15' ]


admin.site.register(Toq_kunlari,AdminToqKunlar)



class AdminStudentMen(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'yosh', 'manzil', 'dars_soati','telefon','telefon2','darajasi', 'Oquv_tanigan', 'qaysi_ustoz','date']


admin.site.register(Student_mental,AdminStudentMen)





class AdminStudentMatem(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'yosh', 'manzil', 'dars_soati','telefon','telefon2','darajasi', 'Oquv_tanigan' , 'qaysi_ustoz', 'date']


admin.site.register(Student_matem,AdminStudentMatem)




class AdminStudentArab(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'yosh', 'manzil', 'dars_soati','telefon','telefon2','darajasi', 'Oquv_tanigan' , 'qaysi_ustoz', 'date']


admin.site.register(Student_arab,AdminStudentArab)

class AdminStudentVip(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'yosh', 'manzil', 'dars_soati','telefon','telefon2','darajasi', 'Oquv_tanigan' , 'qaysi_ustoz', 'date']


admin.site.register(Vip,AdminStudentVip)


class AdminTolov(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'qaysi_fan' ,'qaysi_ustoz', 'Qaysi_oy', 'tolov_filter', 'qaycha_tolov', 'qolgan_tolov', 'date']

admin.site.register(Tolov,AdminTolov)



class AdminTolov5_10(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'qaysi_fan' ,'qaysi_ustoz', 'Qaysi_oy', 'tolov_filter', 'qaycha_tolov', 'qolgan_tolov', 'date']

admin.site.register(Tolov5_10,AdminTolov5_10)


class AdminTolov10_15(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'qaysi_fan' ,'qaysi_ustoz', 'Qaysi_oy', 'tolov_filter', 'qaycha_tolov', 'qolgan_tolov', 'date']

admin.site.register(Tolov10_15,AdminTolov10_15)

class AdminTolov20_25(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'qaysi_fan' ,'qaysi_ustoz', 'Qaysi_oy', 'tolov_filter', 'qaycha_tolov', 'qolgan_tolov', 'date']

admin.site.register(Tolov20_25,AdminTolov20_25)

class AdminTolov25_30(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'qaysi_fan' ,'qaysi_ustoz', 'Qaysi_oy', 'tolov_filter', 'qaycha_tolov', 'qolgan_tolov', 'date']

admin.site.register(Tolov25_30,AdminTolov25_30)

class AdminQarzdorlar(admin.ModelAdmin):
    list_display = ['id' , 'ism', 'familya', 'qaysi_fan' ,'qaysi_ustoz', 'Qaysi_oy',  'qaycha_tolov', 'qolgan_tolov', 'date']

admin.site.register(Qarzdorlar,AdminQarzdorlar)

class AdminBor(admin.ModelAdmin):
    list_display = ["id" , 'ism', "oquvchi1_davomat" ,"oquvchi2_davomat" ,"oquvchi3_davomat" ,"oquvchi4_davomat" ,"oquvchi5_davomat" ,"oquvchi6_davomat" ,"oquvchi7_davomat" ,"oquvchi8_davomat" , "oquvchi9_davomat" ,"oquvchi10_davomat" ,"oquvchi11_davomat" ,"oquvchi12_davomat" ,"oquvchi13_davomat" ,"oquvchi14_davomat" ,"oquvchi15_davomat" ,"date"]
admin.site.register(Bor , AdminBor)



class AdminBorToq(admin.ModelAdmin):
    list_display = ["id" , 'ism', "oquvchi1_davomat" ,"oquvchi2_davomat" ,"oquvchi3_davomat" ,"oquvchi4_davomat" ,"oquvchi5_davomat" ,"oquvchi6_davomat" ,"oquvchi7_davomat" ,"oquvchi8_davomat" , "oquvchi9_davomat" ,"oquvchi10_davomat" ,"oquvchi11_davomat" ,"oquvchi12_davomat" ,"oquvchi13_davomat" ,"oquvchi14_davomat" ,"oquvchi15_davomat" ,"date"]
admin.site.register(BorToq , AdminBorToq)

class AdminKetgan(admin.ModelAdmin):
    list_display = ['id' , 'ism' , 'familya' , 'manzil' , 'telefon' , 'telefon2' , 'qaysi_ustoz' , 'date']
admin.site.register(Student_ketgan , AdminKetgan)


class AdminFanlar(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Fanlar , AdminFanlar)