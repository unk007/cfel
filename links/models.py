from venv import create
from django.db import models

from users.models import Table as ut 
from sents.models import Table as st, Product
from paids.models import Table as pt
from django.db.models import Sum
from additional import put_comma
# Create your models here.
class Table(models.Model):
    #CREATE TABLE IF NOT EXISTS links(
    id = models.BigAutoField(primary_key=255) #BIGINT NOT NULL PRIMARY KEY,
    creator = models.ForeignKey(ut, on_delete=models.CASCADE, related_name='creator+') #BIGINT NOT NULL,
    linked = models.ForeignKey(ut, on_delete = models.CASCADE, related_name = 'linked+') #BIGINT NOT NULL,
    initial = models.BigIntegerField(null=True) #BIGINT,
    date = models.CharField(max_length=255) #VARCHAR(255) NOT NULL,
    sanction = models.BooleanField(null=True) #BOOLEAN,
    sanction_date = models.CharField(max_length=255, null=True) #VARCHAR(255),
    overall = models.BigIntegerField(null=True) #BIGINT

    def __str__(self):
        return f'(id:{self.id}) - (creator:{self.creator.account}) - (linked:{self.linked.account}) - (sanction:{self.sanction}) - (initial:{self.initial}) - (overall:{self.overall})'
    def show_producter(self):
        creator = st.objects.filter(producter = self.creator, provider = self.linked)
        return creator
    def show_provider(self):
        creator = st.objects.filter(provider = self.creator, producter = self.linked)
        return creator
    def show_taker(self):
        creator = pt.objects.filter(taker = self.creator, payer = self.linked)
        return creator
    def show_payer(self):
        creator = pt.objects.filter(payer = self.creator, taker = self.linked)
        return creator
    def show_overall(self):
        producter = 0 if not self.show_producter().filter(sanction = True).aggregate(Sum('overall'))['overall__sum'] else self.show_producter().filter(sanction = True).aggregate(Sum('overall'))['overall__sum']
        provider = 0 if not self.show_provider().filter(sanction = True).aggregate(Sum('overall'))['overall__sum'] else self.show_provider().filter(sanction = True).aggregate(Sum('overall'))['overall__sum']
        payer = 0 if not self.show_payer().filter(sanction = True).aggregate(Sum('cash'))['cash__sum'] else self.show_payer().filter(sanction = True).aggregate(Sum('cash'))['cash__sum']
        taker = 0 if not self.show_taker().filter(sanction = True).aggregate(Sum('cash'))['cash__sum'] else self.show_taker().filter(sanction = True).aggregate(Sum('cash'))['cash__sum']
        overall = self.initial + provider + payer - producter - taker
        return overall
    def show_creator_overall(self):
        overall = self.show_overall()
        return put_comma(overall)
    def show_linked_overall(self):
        creator_overall = self.show_overall()
        return put_comma(-creator_overall)



#to take info from sql
def linked_accounts(users):
    lnk_t = Table.objects.filter(creator = users).all()
    crt_t = Table.objects.filter(linked = users).all()
    all = []
    for lnk in lnk_t : all.append(lnk.linked)
    for crt in crt_t : all.append(crt.creator)
    return all
def search_linked_id( account, accounts ):
    result = []
    data = list(filter(lambda x: x.account == account, accounts ))
    if data : result = data[0]
    return result

def linked_accounts_table(users):
    lnk_t = Table.objects.filter(creator = users).all()
    crt_t = Table.objects.filter(linked = users).all()
    accounts = (lnk_t | crt_t).order_by('linked__account')
    return accounts