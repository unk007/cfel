from django.db import models

# Create your models here.
class Table(models.Model):
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    date = models.CharField(max_length=255) #VARCHAR(255) NOT NULL,
    producter_id = models.BigIntegerField() #BIGINT NOT NULL,
    provider_id = models.BigIntegerField() #BIGINT NOT NULL,
    comment = models.CharField(max_length=255, null=True) #VARCHAR(255),
    sanction = models.BooleanField(null=True) #BOOLEAN,
    sanction_date = models.CharField(null=True, max_length=255) #VARCHAR(255)

    def __str__(self):
        return f'(id:{self.id}) - (date:{self.date}) - (producter-id:{self.producter_id}) - (provider-id:{self.provider_id}) - (sanction:{self.sanction})'

class Product(models.Model):
    #CREATE TABLE IF NOT EXISTS product(
    id = models.BigAutoField(primary_key=True) #BIGINT NOT NULL PRIMARY KEY,
    product_id = models.BigIntegerField() #BIGINT NOT NULL,
    product_value = models.BigIntegerField() #BIGINT NOT NULL,
    production_id = models.BigIntegerField() #BIGINT NOT NULL

    def __str__(self):
        return f'(id:{self.id}) - (product-id:{self.product_id}) - (product-value:{self.product_value}) - (orders-id:{self.production_id})'