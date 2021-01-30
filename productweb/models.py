from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    despation = models.CharField(max_length=500)
    year = models.IntegerField(default=0)
    image = models.ImageField(upload_to= None, height_field= None, width_field= None, max_length= 1000)
    category = models.CharField(max_length=100)

    def __str__(self):
        s = "Tên sản phẩm:" + str(self.name) + ", Giá sản phẩm:" + str(self.price) + ", Mô tả:" \
            + str(self.despation) + ", Năm sản xuất" + str(self.year) + ", Ảnh:" + str(self.image) + ",Thể loại:" + str(self.category)
        return s

