def idade(idade):
    
    ano = idade / 365
    restoAno = idade % 365
    mes = restoAno / 30
    restoMes = restoAno % 30
    dia = restoMes
    
    print(f"ano = {ano} mes = {mes} dia = {dia}")
    
    
idade(500)