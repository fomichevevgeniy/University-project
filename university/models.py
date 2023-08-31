from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=255, verbose_name="Jins")

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = "Jins"
        verbose_name_plural = "Jinslar"


class Region(models.Model):
    region = models.CharField(max_length=255, verbose_name="Viloyat")

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"


class Faculty(models.Model):
    faculty = models.CharField(max_length=255,
                               verbose_name="Ta'lim yo‘nalishi")
    description = models.TextField(verbose_name="Batafsil ta‘lim yo‘nalishi haqida",
                                   null=True, blank=True)
    image = models.ImageField(upload_to='photos/directions_study',
                              verbose_name='Ta‘lim yo‘nalishi foto',
                              null=True, blank=True)

    def get_photo(self):
        if self.image:
            return self.image.url


    def __str__(self):
        return self.faculty

    class Meta:
        verbose_name = "Yo‘nalish"
        verbose_name_plural = "Yo‘nalishlar"


class StudyType(models.Model):
    type = models.CharField(max_length=255,
                            verbose_name="Ta‘lim shakli")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Ta'lim shakli"
        verbose_name_plural = "Ta'lim shakllari"


class ExamLang(models.Model):
    lang = models.CharField(max_length=255,
                            verbose_name="Imtixon tili")

    def __str__(self):
        return self.lang

    class Meta:
        verbose_name = "Imtixon tili"
        verbose_name_plural = "Imtixon tillari"


class Document(models.Model):
    first_name = models.CharField(max_length=255,
                                  verbose_name="Ism")
    last_name = models.CharField(max_length=255,
                                 verbose_name="Familiya")
    middle_name = models.CharField(max_length=255,
                                   verbose_name="Otasining ismi")
    birth_date = models.DateField(verbose_name="Tug'ilgan sanangiz")

    gender = models.ForeignKey(to=Gender, on_delete=models.SET_NULL, null=True,
                               verbose_name="Jins")
    region = models.ForeignKey(to=Region, on_delete=models.SET_NULL, null=True,
                               verbose_name="Viloyat")
    district = models.CharField(max_length=255,
                                verbose_name="Tuman")
    address = models.CharField(max_length=255,
                               verbose_name="Manzil")
    phone_number = models.CharField(max_length=255,
                                    verbose_name="Telefon raqam")
    extra_phone_number = models.CharField(max_length=255,
                                          verbose_name="Telefon raqam")
    passport_photo = models.ImageField(upload_to='photos/passports',
                                       verbose_name="Passport rangli nusxasi")
    passport_series = models.CharField(max_length=2,
                                       verbose_name="Passport Seriya")
    passport_numbers = models.IntegerField(verbose_name="Passport raqami")

    diploma_photo = models.ImageField(upload_to='photos/diplomas',
                                      verbose_name="Diplom rangli nusxasi")
    faculty = models.ForeignKey(to=Faculty, on_delete=models.SET_NULL, null=True,
                                verbose_name="Ta'lim yo‘nalishi")
    study_type = models.ForeignKey(to=StudyType, on_delete=models.SET_NULL, null=True,
                                   verbose_name="Ta‘lim shakli")
    exam_lang = models.ForeignKey(to=ExamLang, on_delete=models.SET_NULL, null=True,
                                  verbose_name="Imtixon tili")

    application_data = models.DateTimeField(auto_now=True,
                                            verbose_name="Dokument topshirilgan sana")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ----- {self.application_data}"

    class Meta:
        verbose_name = "Ariza, Xujjat"
        verbose_name_plural = "Arizalar, Xujjatlar"


# ---------------------------------------------------------------------------------------------------------------------
# Blog
class NewsCategory(models.Model):
    category_title = models.CharField(max_length=255,
                                      verbose_name="Yangiliklar kategoriyasi")

    def count_products(self, id):
        return NewsCategory.objects.filter(pk=id).count()

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = "Yangiliklar kategoriyasi"
        verbose_name_plural = "Yangiliklar kategoriyalari"


class News(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="Yangiliklar nomi")

    min_to_read = models.IntegerField(verbose_name="O‘qishga ketadigan vaqt")

    created_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Yangilik qo‘shilgan sana")
    updated_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Yangilik yangilangan sana")
    status = models.BooleanField(default=True,
                                 verbose_name="Yangilik statusi")
    category = models.ForeignKey(to=NewsCategory, on_delete=models.CASCADE,
                                 verbose_name="Yangilik kategoriyasi")

    def get_first_photo(self):
        if self.image:
            try:
                return self.image.first().image.url
            except:
                return ''

    def get_first_desc(self):
        if self.description:
            try:
                return self.description.first().description
            except:
                return ''


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


class NewsImage(models.Model):
    image = models.ImageField(upload_to="photos/news")
    news = models.ForeignKey(to=News, on_delete=models.CASCADE,
                             verbose_name="Yangilik",
                             related_name="image")


    class Meta:
        verbose_name = "Yangilik rasmi"
        verbose_name_plural = "Yangilik rasmlari"


class NewsDesc(models.Model):
    description = models.TextField(verbose_name="Yangilik batafsil")
    news = models.ForeignKey(to=News, on_delete=models.CASCADE,
                             verbose_name="Yangilik",
                             related_name="description")


    class Meta:
        verbose_name = "Yangilik batafsil ma'lumoti"
        verbose_name_plural = "Yangilik batafsil ma'lumotlari"


# ------------------------------------------------------------------------------------------
# For student
class Article(models.Model):
    image = models.ImageField(upload_to='photos/articles',
                              verbose_name="Foto")
    title = models.CharField(max_length=255,
                             verbose_name="Nomi")
    description = models.TextField(verbose_name="Batafsil")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"


# -----------------------------------------------------------------------------------------------------
class SliderPhoto(models.Model):
    photo = models.ImageField(upload_to='photos/slider_photos',
                              verbose_name="O‘quv jarayonidan lavha")


    def get_photo(self):
        if self.photo:
            return self.photo.url

    def __str__(self):
        return f"Foto"

    class Meta:
        verbose_name = "Lavha"
        verbose_name_plural = "Lavhalar"

