from django.db import models

# Create your models here.
class Categories(models.Model):
    name =  models.CharField(max_length=150, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='Url')

    class Meta:
        db_table: str = 'category'
        verbose_name: str = 'Категорию'
        verbose_name_plural: str = 'Категории'
        

    def __str__(self):
        return self.name
    



class Products(models.Model):

    name =  models.CharField(max_length=150, unique=True, verbose_name='Название продукта')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='Url')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to= Categories, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        db_table: str = 'product'
        verbose_name: str = 'Продукт'
        verbose_name_plural: str = 'Продукты'
        ordering = ('id',)
    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}' 
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100 , 2)               

        return self.price                                                                 