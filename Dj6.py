from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def get_info(self):
        return f"ID: {self.id} | Товар: {self.name}"

    def get_total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return self.name



from django.core.exceptions import ValidationError
from django.db import models

def validate_non_negative(value):
    if value < 0:
        raise ValidationError(
            f"Число {value} не может быть отрицательным. Допустимы значения от 0 и выше."
        )

class Order(models.Model):
    amount = models.IntegerField(validators=[validate_non_negative])
    description = models.TextField()

    def __str__(self):
        return f"Заказ №{self.id}"


