from django.db import models

# Create your models here.
class test(models.Model):
    botname = models.CharField(blank=True, max_length=128, default='', verbose_name='botname')
    testa = models.IntegerField(default=0, blank=True,help_text="这是一个测试", verbose_name="这是name")
    
    class Meta:
        verbose_name_plural = "测试表"

    def __str__(self):
        return self.botname

    