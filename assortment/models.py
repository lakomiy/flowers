from django.db import models

# Create your models here.
class Assortment(models.Model):
    name_product = models.CharField(max_length=100, verbose_name="Товар")
    description_product = models.TextField(null=True, blank=True, verbose_name="Описание товара")
    price_product = models.FloatField(null=True, blank=True, verbose_name="Цена товара")
    create_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата добавления")
    category = models.ForeignKey("Category", null=True, on_delete=models.PROTECT, verbose_name="Категория")
    photo_product = models.ImageField(null=True, blank=True, upload_to=f"img_flowers/%Y/%m/%d",
                                      verbose_name="Фото товара")

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
        ordering = ['-create_at']


class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name="Название категории")

    def __str__(self):
        return f"{self.name_category}"

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ["name_category"]