from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)                        # название
    author = models.CharField(max_length=150)                       # автор
    genre = models.CharField(max_length=100)                        # жанр
    deposit = models.DecimalField(max_digits=8, decimal_places=2)   # залог
    rent_price = models.DecimalField(max_digits=8, decimal_places=2)  # стоимость проката

    def __str__(self):
        return "%s — %s" % (self.author, self.title)

    def get_excerpt(self):
        return "Жанр: %s. Залог: %s руб. Прокат: %s руб." % (
            self.genre, self.deposit, self.rent_price
        )