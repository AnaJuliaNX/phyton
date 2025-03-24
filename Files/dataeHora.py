from datetime import datetime

today = datetime.today()

ultimoDia = datetime(today.year, 12, 31)

diasFaltando = (ultimoDia - today).days
print(f"Faltam {diasFaltando} para o fim do ano")