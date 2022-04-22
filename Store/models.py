from django.db import models
from uuslug import uuslug


class Product(models.Model):
    title = models.CharField(max_length=1000, null=False, unique=False, verbose_name='Название')
    description = models.TextField(max_length=5000, null=False, unique=False, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    slug = models.SlugField(max_length=1200, unique=True, db_index=True, allow_unicode=True, verbose_name="URL",
                            blank=True)
    parent = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, blank=True, related_name="products")

    def __str__(self):
        return f'Товар - {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.title, instance=self)
        super(Product, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=1000, null=False, unique=False, verbose_name='Название')
    description = models.TextField(max_length=5000, null=False, unique=False, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Созданa')
    slug = models.SlugField(max_length=1200, unique=True, db_index=True, allow_unicode=True, verbose_name="URL",
                            blank=True)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, related_name='categories')

    def __str__(self):
        return f'Категория - {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.title, instance=self)
        super(Category, self).save(*args, **kwargs)


class PropertyType(models.Model):
    title = models.CharField(max_length=1000, null=False, unique=False, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Созданa')

    def __str__(self):
        return f'Характеристика - {self.title}'


class PropertyValue(models.Model):
    value = models.CharField(max_length=1000, null=False, unique=False, verbose_name='Значение')
    property_type = models.ForeignKey("PropertyType", on_delete=models.PROTECT, related_name="values")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Созданa')
    parent = models.ForeignKey("Product", on_delete=models.PROTECT, related_name="properties")

    def __str__(self):
        return f'Значение - {self.value}'

    class Meta:
        unique_together = ('property_type', 'value')
