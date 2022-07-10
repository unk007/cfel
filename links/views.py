from django.shortcuts import render
from django.http import HttpResponseRedirect

from users.models import search_user_with_domain, Table as ut
from for_father.models import show_dividents
from .models import Table ,linked_accounts_table
from links.models import Table as lt
# Create your views here.

def calculate(request):
    url = '%2Flinks'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        tables = linked_accounts_table(user_info.users)
    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    
    data = {
                'tables': tables,
                'columns':['kim','hisob', 'ko\'rish'],
                'user': user_info.users
            }
    return render(request, 'links_table.html', data)

def calculate_events(request):
    url = '%2Flinks'
    try:
        unkid = request.COOKIES['unkid']  
    except:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    user_info = search_user_with_domain(unkid)
    if user_info:
        user_info = user_info.users
        dividents = []
        dividents = list(filter(lambda x: lt.objects.filter(linked__id = x).all()[0] == user_info, dividents))
        print(dividents)
        if dividents:
            user_info = ut.objects.get(id = 7)
        if request.GET:
            lnk = request.GET['lnk']
            linked_account = Table.objects.filter(id = lnk).all()
            linked_account = linked_account.filter(linked = user_info) | linked_account.filter(creator = user_info)
            if linked_account:
                sents_table = linked_account[0].show_producter() | linked_account[0].show_provider()
                paids_table = linked_account[0].show_payer() | linked_account[0].show_taker()
                sents_table = list(sents_table.order_by('date','id'))
                paids_table = list(paids_table.order_by('date', 'id'))                
                tables = []
                while sents_table:
                    while paids_table:
                        if sents_table:
                            if sents_table[0].date <= paids_table[0].date:
                                pop = sents_table.pop(0)
                                tables.append(pop)
                            else:
                                pop = paids_table.pop(0)
                                tables.append(pop)
                            continue
                        else:
                            break
                            
                            
                    tables += sents_table
                    sents_table = []
                    
                if paids_table:
                    tables += paids_table
                    paids_table = []
                     
            else:
                return HttpResponseRedirect(f'/')    
        else:
            return HttpResponseRedirect(f'/')
    else:
        return HttpResponseRedirect(f'/../users/login?url={url}')
    
    data = {
                'tables': tables,
                'linked_account': linked_account[0],
                'columns':['sana','kirim','chiqim','kimdan/ga','qo\'shimcha malumot'],
                'user': user_info.users
            }
    return render(request, 'calculate_events.html', data)