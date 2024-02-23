from django.db import models

# Create your models here.


class BaseModel(models.Model):
    ...

    class Meta:
        abstract = True


class Menu(BaseModel):
    title = models.CharField('title', max_length=25)
    slug = models.SlugField('slug', max_length=25)
    order_number = models.IntegerField(
        'order number', unique=True, blank=False, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'


class SubMenu(BaseModel):
    title = models.CharField('submenu', max_length=40)
    slug = models.SlugField('slug', max_length=40)
    order_number = models.IntegerField('order number', blank=False, null=True)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE,
                             related_name='submenu', related_query_name='submenu')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'submenu'
        verbose_name_plural = 'submenus'
        unique_together = ('menu', 'order_number')
