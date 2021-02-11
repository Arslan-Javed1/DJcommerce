from django.db import models

from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name + ' | ' + self.category.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    available = models.BooleanField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    img1 = models.ImageField(upload_to='prod_imgs/')
    img2 = models.ImageField(upload_to='prod_imgs/')
    img3 = models.ImageField(upload_to='prod_imgs/')

    def get_all_products():
        return Product.objects.all()

    def get_products_by_cat(cat_id):
        if cat_id:
            return Product.objects.filter(category = cat_id)
        else:
            return Product.objects.all()

    class Meta:
        ordering = ['-timeStamp']
        
    def __str__(self):
        return self.name + ' | ' + self.category.name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return str(self.product) + ' | ' + str(self.quantity) + ' | ' + str(self.price)

    def get_total():
        
        return OrderItem.product.price*OrderItem.quantity

class Order(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    zip_code = models.IntegerField()
    total_charges = models.FloatField()

    def __str__(self):
        return self.first_name + ' | ' + self.last_name + ' | ' + self.total_charges


    

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Category.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_reciever, sender = Category)

pre_save.connect(pre_save_reciever, sender = SubCategory)

pre_save.connect(pre_save_reciever, sender = Product)



# def create_subcat_slug(instance, new_slug=None):
#     slug = slugify(instance.subcat_name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Category.objects.filter(subcat_slug=slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_subcat_slug(instance, new_slug=new_slug)
#     return slug

# def pre_save_subcat_reciever(sender, instance, *args, **kwargs):
#     if not instance.subcat_slug:
#         instance.subcat_slug = create_subcat_slug(instance)

# pre_save.connect(pre_save_subcat_reciever, sender = SubCategory)



# def create_pro_slug(instance, new_slug=None):
#     slug = slugify(instance.pro_name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Category.objects.filter(pro_slug=slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_pro_slug(instance, new_slug=new_slug)
#     return slug

# def pre_save_pro_reciever(sender, instance, *args, **kwargs):
#     if not instance.pro_slug:
#         instance.pro_slug = create_pro_slug(instance)

# pre_save.connect(pre_save_pro_reciever, sender = Product)