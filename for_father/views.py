from django.shortcuts import render
from django.http import HttpResponseRedirect

from users.models import search_user_with_domain, Table as ut
from paids.models import Money
from links.models import linked_accounts_table, Table as lt
from .models import show_dividents

# Create your views here.
def calculate(request):
    url = '%2Ffor_father'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        kassa = ut.objects.get(id = 7)
        tables = linked_accounts_table(kassa)
        account_bank = tables.get(id = 99)
        producters = tables.filter(linked__telegram_ids__telegram_id = 256710438)
        tables = tables.exclude(linked__telegram_ids__telegram_id = 256710438)
        dividents = show_dividents()
        dividents_table = lt.objects.none()
        for divident in dividents: 
            dividents_table = dividents_table  | tables.filter(id = divident).all()
            tables = tables.exclude(id = divident)
        residual_expenses = [4,5,17,20,21]
        residual_expenses_table = lt.objects.none()
        for residual_expenses in residual_expenses: 
            residual_expenses_table = residual_expenses_table  | tables.filter(id = residual_expenses).all()
            tables = tables.exclude(id = residual_expenses)
        notneed_expenses = [9,13,14,23,24,27,28,99]
        for notneed_expense in notneed_expenses:
            tables = tables.exclude(id = notneed_expense)
        not_providers = []
        providers = []
        currency = Money.objects.filter(user = kassa)
        result = [
            [
                {'name':'mijozlar','tables':producters, "right":False},
                {'name':'dividentchilar','tables':dividents_table, "right":False},
                {'name':'boshqalar','tables':residual_expenses_table, "right":False},
                {'name': 'hisoblar', 'tables':[{'account':'kassa', 'overall': currency[0].show_overall()},account_bank], 'right':True},
            ],
            [
                {'name':'taminotchilar','tables':tables, "right":False},
            ]
            
            
        ]
    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    
    data = {
                'rows': result,
                'kassa': currency,
                'columns':['kim','hisob', 'ko\'rish'],
                'user': kassa
            }
    return render(request, 'for_father.html', data)