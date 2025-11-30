from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Заголовок", help_text="Введите название заголовка"
    )

    content = models.TextField(
        verbose_name="Контент",
        help_text="Введите контент",
    )

    created_at = models.DateField(auto_now_add=True)

    photo = models.ImageField(verbose_name="Изображение", upload_to="blog/photo/")

    is_published = models.BooleanField(
        verbose_name="Подтверждение публикации",
        help_text="Подтвердите публикацию",
        default=False,
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="Колличество просмотров",
        help_text="Введите колличество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
