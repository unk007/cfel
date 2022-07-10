from django.db import models

# Create your models here.
class Table(models.Model):
    #CREATE TABLE IF NOT EXISTS kreteria(
    id = models.BigAutoField(primary_key=255) #BIGINT NOT NULL PRIMARY KEY,
    name = models.CharField(max_length=255) #VARCHAR(255) NOT NULL,
    user_id = models.BigIntegerField() #BIGINT NOT NULL

    def __str__(self):
        return f'(id:{self.id}) - (name:{self.name}) - (user-id:{self.user_id})'