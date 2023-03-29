from django.db import models

# Create your models here.

class Post(models.Model): # пост в нашем блоге, класс дочерний от родителского класса Model
    """данные о посте"""
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изобранжение', upload_to='image/%Y')


    def __str__(self): # красиво вводим имя заголовка и имя автора
        return f'{self.title}, {self.author}'


    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи' # 13я минута 2го урока


