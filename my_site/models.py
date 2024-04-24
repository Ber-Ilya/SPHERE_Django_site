from django.db import models


class FormFooterContact(models.Model):
    name_under_footer = models.CharField(max_length=50)
    phone_under_footer = models.CharField(max_length=20)

    def __str__(self):
        return f'Имя клиента {self.name_under_footer}, номер телефона {self.phone_under_footer}'



class FormPopup(models.Model):
    name_popup = models.CharField(max_length=50)
    phone_popup = models.CharField(max_length=20)

    def __str__(self):
        return f'Имя клиента {self.name_popup}, номер телефона {self.phone_popup}'

