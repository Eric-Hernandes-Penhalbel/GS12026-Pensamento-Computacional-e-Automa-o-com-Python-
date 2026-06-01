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

media_ciclo = 0


def introducao_missao():
    print("== == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==")
    print("                                 MISSION CONTROL AI  ")
    print("== == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==")
    print("Missão: Edgar Pollo. Beta 1")
    print("Equipe: Mend Menar Team (8: - Integrantes - )")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")






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
        return "NORMAL", 0

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
        return "NORMAL", 0

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
        return "NORMAL", 0

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
        return "NORMAL", 0

    else:
        print(f"Algum erro foi encontrado")
        return "ERRO", -1


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"

    elif 3 <= pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(pontuacao):
    if pontuacao <= 2:
        return "Operação como esperado, continuar monitoramento."

    elif 3 <= pontuacao <= 5:
        return "Monitoramento necessário, preparar plano de contingência."

    else:
        return "Ativar modo de segurança do setor, priorizar suporte à vida, energia e comunicação."


def analisar_tendencia(historico_risco):
    primeiro = historico_risco[0]
    ultimo = historico_risco[-1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."

    elif ultimo < primeiro:
        return "A missão apresentou tendência de recuperação."

    else:
        return "A missão permaneceu estável."


def classificacao_final(risco_medio):

    if risco_medio <= 2:
        return "MISSÃO ESTÁVEL"

    elif 2 < risco_medio <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"


def gerar_conclusao(classificacao):

    if classificacao == "MISSÃO ESTÁVEL":

        return (
            "Durante a operação da Missão, tudo se manteve estável. \n"
            "O comportamento dos sistemas estão todos dentro ou próximo do esperado."
        )

    elif classificacao == "MISSÃO EM ATENÇÃO":

        return (
            "Instabilidade na missão foi detectada durante a operação.\n "
            "Houveram momentos estáveis dentro da missão, mas com os \n"
            "sistemas em atenção a equipe deve manter o plano de contingência ativo."
        )

    else:

        return (
            "Estado crítico da missão foi atingido durante a operação. \n"
            "Múltiplos sistemas mostraram comportamentos nocivos para \n"
            "o estado da missão. É necessário ação e intervenção pelo bem\n"
            "da integridade da missão."
        )


def analise_ciclo():
    p_temp_total = 0
    p_comun_total = 0
    p_sis_total = 0
    p_sup_total = 0
    p_estab_total = 0

    temp_total = 0
    comun_total = 0
    sis_total = 0
    sup_total = 0
    estab_total = 0

    risco_total = 0
    maior_pontuacao = 0
    ciclo_mais_critico = 0
    qtd_ciclos_criticos = 0
    historico_risco = []

    total_ciclos = len(dados_missao)

    for i, ciclo in enumerate(dados_missao):

        print(f"\nCICLO {i + 1} ------------------------------------------------------------")

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

        pontuacao_total = (
            p_temp +
            p_comun +
            p_sis +
            p_sup +
            p_estab
        )

        classificacao = classificar_ciclo(pontuacao_total)
        recomendacao = gerar_recomendacao(pontuacao_total)

        p_temp_total += p_temp
        p_comun_total += p_comun
        p_sis_total += p_sis
        p_sup_total += p_sup
        p_estab_total += p_estab

        temp_total += temp
        comun_total += comun
        sis_total += sis
        sup_total += sup
        estab_total += estab

        risco_total += pontuacao_total

        historico_risco.append(pontuacao_total)

        if pontuacao_total > maior_pontuacao:
            maior_pontuacao = pontuacao_total
            ciclo_mais_critico = i + 1

        if pontuacao_total >= 6:
            qtd_ciclos_criticos += 1

        print(f"\nPontuação de risco do ciclo: {pontuacao_total}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    risco_medio = round(risco_total / total_ciclos, 2)

    areas = {
        "Temperatura interna": p_temp_total,
        "Comunicação com a base": p_comun_total,
        "Sistema de energia": p_sis_total,
        "Suporte de oxigênio": p_sup_total,
        "Estabilidade operacional": p_estab_total
    }

    area_mais_afetada = max(areas, key=areas.get)

    return {

        "dados_reais": (
            temp_total,
            comun_total,
            sis_total,
            sup_total,
            estab_total
        ),

        "criticidade": (
            p_temp_total,
            p_comun_total,
            p_sis_total,
            p_sup_total,
            p_estab_total
        ),

        "estatisticas": (
            risco_total,
            maior_pontuacao,
            ciclo_mais_critico,
            qtd_ciclos_criticos,
            area_mais_afetada,
            risco_medio
        ),

        "total_ciclos": total_ciclos,

        "historico_risco": historico_risco
    }


def calcular_medias(
    temp_total,
    comun_total,
    sis_total,
    sup_total,
    estab_total,
    p_temp_total,
    p_comun_total,
    p_sis_total,
    p_sup_total,
    p_estab_total,
    total_ciclos
):

    media_temp_real = temp_total / total_ciclos
    media_comun_real = comun_total / total_ciclos
    media_sis_real = sis_total / total_ciclos
    media_sup_real = sup_total / total_ciclos
    media_estab_real = estab_total / total_ciclos

    media_temp_crit = p_temp_total
    media_comun_crit = p_comun_total
    media_sis_crit = p_sis_total
    media_sup_crit = p_sup_total
    media_estab_crit = p_estab_total

    return {

        "temperatura_real": round(media_temp_real, 2),
        "temperatura_crit": round(media_temp_crit, 2),

        "comunicacao_real": round(media_comun_real, 2),
        "comunicacao_crit": round(media_comun_crit, 2),

        "sistema_real": round(media_sis_real, 2),
        "sistema_crit": round(media_sis_crit, 2),

        "suporte_real": round(media_sup_real, 2),
        "suporte_crit": round(media_sup_crit, 2),

        "estabilidade_real": round(media_estab_real, 2),
        "estabilidade_crit": round(media_estab_crit, 2)
    }




def gerar_relatorio(
    medias,
    estatisticas,
    tendencia,
    classificacao_missao,
    conclusao,
    total_ciclos
):

    risco_total, maior_pontuacao, ciclo_mais_critico, qtd_ciclos_criticos, area_mais_afetada, risco_medio = estatisticas

    print("\n============================================================")
    print("RELATÓRIO FINAL DA MISSÃO")
    print("============================================================")

    print(f"Quantidade de ciclos analisados: {total_ciclos}")

    print(f"\nMédia de temperatura: {medias['temperatura_real']} °C")
    print(f"Média de comunicação: {medias['comunicacao_real']}%")
    print(f"Média de bateria: {medias['sistema_real']}%")
    print(f"Média de oxigênio: {medias['suporte_real']}%")
    print(f"Média de estabilidade: {medias['estabilidade_real']}%")

    print(f"\nCiclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_pontuacao}")
    print(f"Risco médio da missão: {risco_medio}")
    print(f"Quantidade de ciclos críticos: {qtd_ciclos_criticos}")

    print(f"\nTendência da missão:")
    print(tendencia)

    print(f"\nPontuação acumulada por área:")
    print(f"Temperatura interna: {medias['temperatura_crit']} pontos")
    print(f"Comunicação com a base: {medias['comunicacao_crit']} pontos")
    print(f"Sistema de energia: {medias['sistema_crit']} pontos")
    print(f"Suporte de oxigênio: {medias['suporte_crit']} pontos")
    print(f"Estabilidade operacional: {medias['estabilidade_crit']} pontos")

    print(f"\nÁrea mais afetada:")
    print(area_mais_afetada)
    print(f"\nClassificação final da missão:")
    print(classificacao_missao)

    print(f"\nConclusão:")
    print(conclusao)
    print("== == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==")



introducao_missao()

dados = analise_ciclo()

medias = calcular_medias(

    *dados["dados_reais"],

    *dados["criticidade"],

    dados["total_ciclos"]
)

estatisticas = dados["estatisticas"]

tendencia = analisar_tendencia(dados["historico_risco"])
classificacao_missao = classificacao_final(
    dados["estatisticas"][5]
)

conclusao = gerar_conclusao(classificacao_missao)


gerar_relatorio(
    medias,
    estatisticas,
    tendencia,
    classificacao_missao,
    conclusao,
    dados["total_ciclos"]
)
