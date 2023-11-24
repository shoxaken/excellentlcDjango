from django.db import models




class TolovType(models.Model):
    oy1 = models.CharField(max_length=50)
    def __str__(self):
        return self.oy1

class TeacherType(models.Model):
    nomi = models.CharField(max_length=100)
    def __str__(self):
        return self.nomi

class DarajaType(models.Model):
    nomi = models.CharField(max_length=100)
    def __str__(self):
        return self.nomi

class QayerdanTaniganType(models.Model):
    nomi = models.CharField(max_length=100)
    def __str__(self):
        return self.nomi

class XarajatType(models.Model):
    nomi = models.CharField(max_length=100)
    def __str__(self):
        return self.nomi

class TolovQilganYokiQilmaganType(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class TolovQilganYokiQilmaganType_5_10(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class TolovQilganYokiQilmaganType_10_15(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class TolovQilganYokiQilmaganType_20_25(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi
class TolovQilganYokiQilmaganType_25_30(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class Fanlar(models.Model):
    nomi = models.CharField(max_length=100)

class Student(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField(max_length=100)
    dars_soati = models.PositiveIntegerField(max_length=100)
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    telefon2 = models.CharField(max_length=100)
    darajasi = models.ForeignKey(DarajaType,on_delete=models.CASCADE)
    Oquv_tanigan = models.ForeignKey(QayerdanTaniganType,on_delete=models.CASCADE)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)




class Student_rus(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField(max_length=100)
    dars_soati = models.PositiveIntegerField(max_length=100)
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    telefon2 = models.CharField(max_length=100)
    darajasi =  models.ForeignKey(DarajaType,on_delete=models.CASCADE)
    Oquv_tanigan = models.ForeignKey(QayerdanTaniganType,on_delete=models.CASCADE)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)



class Student_mental(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField(max_length=100)
    dars_soati = models.PositiveIntegerField(max_length=100)
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    telefon2 = models.CharField(max_length=100)
    darajasi =  models.ForeignKey(DarajaType,on_delete=models.CASCADE)
    Oquv_tanigan = models.ForeignKey(QayerdanTaniganType,on_delete=models.CASCADE)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class Student_ketgan(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    telefon2 = models.CharField(max_length=100)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)



class Student_matem(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField(max_length=100)
    dars_soati = models.PositiveIntegerField(max_length=100)
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    telefon2 = models.CharField(max_length=100)
    darajasi =  models.ForeignKey(DarajaType,on_delete=models.CASCADE)
    Oquv_tanigan = models.ForeignKey(QayerdanTaniganType,on_delete=models.CASCADE)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class All_people(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField(max_length=100)
    dars_soati = models.PositiveIntegerField(max_length=100)
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    telefon2 = models.CharField(max_length=100)
    darajasi =  models.ForeignKey(DarajaType,on_delete=models.CASCADE)
    Oquv_tanigan = models.ForeignKey(QayerdanTaniganType,on_delete=models.CASCADE)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    qancha_tolov_qiladi = models.PositiveIntegerField(max_length=100)
    date = models.DateTimeField(auto_now=True)
class Vip(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField(max_length=100)
    dars_soati = models.PositiveIntegerField(max_length=100)
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    telefon2 = models.CharField(max_length=100)
    darajasi =  models.ForeignKey(DarajaType,on_delete=models.CASCADE)
    Oquv_tanigan = models.ForeignKey(QayerdanTaniganType,on_delete=models.CASCADE)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)



class Student_arab(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField(max_length=100)
    dars_soati = models.PositiveIntegerField(max_length=100)
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    telefon2 = models.CharField(max_length=100)
    darajasi =  models.ForeignKey(DarajaType,on_delete=models.CASCADE)
    Oquv_tanigan = models.ForeignKey(QayerdanTaniganType,on_delete=models.CASCADE)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class Tolov(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    qaysi_fan = models.CharField(max_length=100)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    Qaysi_oy =  models.ForeignKey(TolovType,on_delete=models.CASCADE)
    tolov_filter = models.ForeignKey(TolovQilganYokiQilmaganType,on_delete=models.CASCADE)
    qaycha_tolov = models.PositiveIntegerField(max_length=100)
    qolgan_tolov = models.PositiveIntegerField(max_length=100)
    date = models.DateTimeField(auto_now=True)



class Tolov5_10(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    qaysi_fan = models.CharField(max_length=100)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    Qaysi_oy =  models.ForeignKey(TolovType,on_delete=models.CASCADE)
    tolov_filter = models.ForeignKey(TolovQilganYokiQilmaganType_5_10,on_delete=models.CASCADE)
    qaycha_tolov = models.PositiveIntegerField(max_length=100)
    qolgan_tolov = models.PositiveIntegerField(max_length=100)
    date = models.DateTimeField(auto_now=True)



class Tolov10_15(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    qaysi_fan = models.CharField(max_length=100)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    Qaysi_oy =  models.ForeignKey(TolovType,on_delete=models.CASCADE)
    tolov_filter = models.ForeignKey(TolovQilganYokiQilmaganType_10_15,on_delete=models.CASCADE)
    qaycha_tolov = models.PositiveIntegerField(max_length=100)
    qolgan_tolov = models.PositiveIntegerField(max_length=100)
    date = models.DateTimeField(auto_now=True)

class Tolov20_25(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    qaysi_fan = models.CharField(max_length=100)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    Qaysi_oy =  models.ForeignKey(TolovType,on_delete=models.CASCADE)
    tolov_filter = models.ForeignKey(TolovQilganYokiQilmaganType_20_25,on_delete=models.CASCADE)
    qaycha_tolov = models.PositiveIntegerField(max_length=100)
    qolgan_tolov = models.PositiveIntegerField(max_length=100)
    date = models.DateTimeField(auto_now=True)

class Xarajatlar(models.Model):
    description = models.TextField()
    qancha_pul_ketgan = models.PositiveIntegerField(max_length=100)
    XarajatTuri = models.ForeignKey(XarajatType, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class Qarzdorlar(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    qaysi_fan = models.CharField(max_length=100)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    Qaysi_oy =  models.ForeignKey(TolovType,on_delete=models.CASCADE)
    qaycha_tolov = models.PositiveIntegerField(max_length=100)
    qolgan_tolov = models.PositiveIntegerField(max_length=100)
    date = models.DateTimeField(auto_now=True)

class Tolov25_30(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    qaysi_fan = models.CharField(max_length=100)
    qaysi_ustoz = models.ForeignKey(TeacherType,on_delete=models.CASCADE)
    Qaysi_oy =  models.ForeignKey(TolovType,on_delete=models.CASCADE)
    tolov_filter = models.ForeignKey(TolovQilganYokiQilmaganType_25_30,on_delete=models.CASCADE)
    qaycha_tolov = models.PositiveIntegerField(max_length=100)
    qolgan_tolov = models.PositiveIntegerField(max_length=100)
    date = models.DateTimeField(auto_now=True)
class Juft_kunlari(models.Model):
    ism = models.CharField(max_length=50)
    gurux_vaqti = models.CharField(max_length=25)
    qaysi_ustoz = models.CharField(max_length=25)
    qaysi_fan = models.CharField(max_length=25)
    oquvchi1 = models.CharField(max_length=50)
    oquvchi2 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi3 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi4 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi5 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi6 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi7 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi8 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi9 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi10 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi11 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi12 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi13 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi14 = models.CharField(max_length=50,null=True,blank=True)
    oquvchi15 = models.CharField(max_length=50,null=True,blank=True)
class Toq_kunlari(models.Model):
    ism = models.CharField(max_length=50)
    gurux_vaqti = models.CharField(max_length=25)
    qaysi_ustoz = models.CharField(max_length=25)
    qaysi_fan = models.CharField(max_length=25)
    oquvchi1 = models.CharField(max_length=50)
    oquvchi2 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi3 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi4 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi5 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi6 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi7 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi8 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi9 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi10 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi11 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi12 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi13 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi14 = models.CharField(max_length=50, null=True, blank=True)
    oquvchi15 = models.CharField(max_length=50, null=True, blank=True)

class Bor(models.Model):
    ism = models.CharField(max_length=50)
    oquvchi1_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi2_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi3_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi4_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi5_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi6_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi7_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi8_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi9_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi10_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi11_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi12_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi13_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi14_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi15_davomat =  models.CharField(max_length=50,null=True,blank=True)
    date = models.DateTimeField(auto_now=True)


class BorToq(models.Model):
    ism = models.CharField(max_length=50)
    oquvchi1_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi2_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi3_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi4_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi5_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi6_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi7_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi8_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi9_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi10_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi11_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi12_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi13_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi14_davomat =  models.CharField(max_length=50,null=True,blank=True)
    oquvchi15_davomat =  models.CharField(max_length=50,null=True,blank=True)
    date = models.DateTimeField(auto_now=True)


