dados_missao = [
[32, 55, 70, 98, 45],
[25, 80, 65, 70, 74],
[26, 95, 55, 99, 66],
[18, 22, 88, 85, 68],
[15, 10, 90, 99, 85],
[20, 79, 100, 100, 92]
]

areas_monitoradas = [
"Temperatura interna",
"Comunicação com a base",
"Sistema de energia",
"Suporte de oxigênio",
"Estabilidade operacional"
]
p_temp = 0
p_comun = 0
p_sis = 0
p_sup = 0
p_estab = 0

s_temp = ""
s_comun = ""
s_sis = ""
s_sup = ""
s_estab = ""

media_ciclo = 0

def monitor_temperatura(temp):
    if temp < 18:
        print(f"Temperatura interna: {temp}ºC | Alerta | Temperatura baixa")
        return "ALERTA", 1

    elif 18 <= temp < 31:
        print(f"Temperatura interna: {temp}ºC | Normal | Temperatura estável")
        return "NORMAL", 0

    elif 31 <= temp < 35:
        print(f"Temperatura interna: {temp}ºC | Alerta | Temperatura Alta")
        return "ALERTA", 1

    elif temp >= 35:
        print(f"Temperatura interna: {temp}ºC | Crítico | Risco de Superaquecimento")
        return "CRITICO", 2

    else:
        print(f"Algum erro foi encontrado")
        return "ERRO", -1

def monitor_comunicacao(comun):
    if comun < 30:
        print(f"Comunicação com a Base: {comun}% | Crítico | Perdendo comunicação")
        return "CRITICO", 2

    elif 30 <= comun <= 59:
        print(f"Comunicação com a Base: {comun}% | Alerta | Comunicação se deteriorando")
        return "ALERTA", 1


    elif comun >= 60:
        print(f"Comunicação com a Base: {comun}% | Normal | Comunicação Estável")
        return "Normal", 0

    else:
        print(f"Algum erro foi encontrado")
        return "ERRO", -1

def monitor_sis(sis):
    if sis < 20:
        print(f"Sistema de Energia: {sis}% | Crítico | Energia Crítica")
        return "CRITICO", 2

    elif 20 <= sis <= 49:
        print(f"Sistema de Energia: {sis}% | Alerta | Energia Baixa")
        return "ALERTA", 1


    elif sis >= 50:
        print(f"Sistema de Energia: {sis}% | Normal | Energia Esperada")
        return "Normal", 0

    else:
        print(f"Algum erro foi encontrado")
        return "ERRO", -1

def monitor_suporte(sup):
    if sup < 80:
        print(f"Suporte de Oxigênio: {sup}% | Crítico | Limiar Crítico de Oxigenação")
        return "CRITICO", 2

    elif 80 <= sup <= 89:
        print(f"Suporte de Oxigênio: {sup}% | Alerta | Oxigênio abaixo do esperado")
        return "ALERTA", 1


    elif sup >= 90:
        print(f"Suporte de Oxigênio: {sup}% | Normal | Oxigenação Estável")
        return "Normal", 0

    else:
        print(f"Algum erro foi encontrado")
        return "ERRO", -1

def monitor_estabilidade(estab):
    if estab < 40:
        print(f"Estabilidade Operacional: {estab}% | Crítico | Estabilidade Crítica")
        return "CRITICO", 2

    elif 40 <= estab <= 69:
        print(f"Estabilidade Operacional: {estab}% | Alerta | Estabilidade Deteriorada")
        return "ALERTA", 1


    elif estab >= 70:
        print(f"Estabilidade Operacional: {estab}% | Normal | Operação como esperado")
        return "Normal", 0

    else:
        print(f"Algum erro foi encontrado")
        return "ERRO", -1

def analise_ciclo():
    for ciclo in dados_missao:
        temp = ciclo[0]
        comun = ciclo[1]
        sis = ciclo[2]
        sup = ciclo[3]
        estab = ciclo[4]

        s_temp, p_temp = monitor_temperatura(temp)
        s_comun, p_comun = monitor_comunicacao(comun)
        s_sis, p_sis = monitor_sis(sis)
        s_sup, p_sup = monitor_suporte(sup)
        s_estab, p_estab = monitor_estabilidade(estab)

        media_ciclo = (
            p_temp +
            p_comun +
            p_sis +
            p_sup +
            p_estab
        )
        print(f"Pontuação de Risco do ciclo: {media_ciclo}\n\n")
        print("")


analise_ciclo()