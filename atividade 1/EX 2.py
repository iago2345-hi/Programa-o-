segundos = int(input("Segundos: "))




dias = segundos // 86400
segundos_restante = segundos % 86400
horas = segundos_restante // 3600
segundos_rest = segundos_restante % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60




print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")
