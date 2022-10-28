import requests
import time
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool

urls = ['http://www.ans.gov.br/component/legislacao/?view=legislacao&task=TextoLei&format=raw&id=NDAzMw==',
        'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf',
        'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx',
        'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf',
        'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf',
        'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf'
        ]

fns = [r'C:\User\vinic\Downloads\legislação',
       r'C:\User\vinic\Downloads\anexoI',
       r'C:\User\vinic\Downloads\anexoI_I',
       r'C:\User\vinic\Downloads\anexoII',
       r'C:\User\vinic\Downloads\anexoIII',
       r'C:\User\vinic\Downloads\anexoIV'
       ]

inputs = zip(urls, fns)


def download_url(args):
    t0 = time.time()
      url, fn = args[0], args[1]
       try:
            r = requests.get(url)
            with open(fn, 'wb') as f:
                f.write(r.content)
            return(url, time.time() - t0)
        except Exception as e:
            print('Exception in download_url():', e)
