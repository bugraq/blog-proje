from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Başlık alanı, en fazla 200 karakter
    content = models.TextField()  # İçerik alanı, uzun metinler için
    created_at = models.DateTimeField(auto_now_add=True)  # Gönderi oluşturulma tarihi
    updated_at = models.DateTimeField(auto_now=True)  # Gönderi güncellenme tarihi
    
    def __str__(self):
        return self.title  # Admin panelinde gösterilen başlık

    class Meta:
        ordering = ['-created_at']  # Gönderiler, oluşturulma tarihine göre azalan sıralanır
