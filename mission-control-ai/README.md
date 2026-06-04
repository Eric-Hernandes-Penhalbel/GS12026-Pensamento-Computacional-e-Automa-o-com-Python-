# Mission Control AI

Sistema de monitoramento e análise de risco para missões espaciais desenvolvido em Python.

## Sobre o Projeto

O Mission Control AI foi desenvolvido com o objetivo de simular o monitoramento de sistemas críticos de uma missão espacial. A aplicação analisa dados operacionais coletados em ciclos sucessivos e gera avaliações de risco, recomendações operacionais e um relatório consolidado da missão.

O projeto foi desenvolvido como atividade acadêmica, aplicando conceitos de programação estruturada, funções, listas, matrizes, análise de dados e geração de relatórios automatizados.

---

## Funcionalidades

* Monitoramento de temperatura interna.
* Monitoramento da comunicação com a base.
* Monitoramento do sistema de energia.
* Monitoramento do suporte de oxigênio.
* Monitoramento da estabilidade operacional.
* Classificação automática de risco por ciclo.
* Geração de recomendações operacionais.
* Cálculo de médias dos sistemas monitorados.
* Identificação do ciclo mais crítico.
* Análise da tendência da missão.
* Identificação da área mais afetada.
* Classificação final da missão.
* Geração de relatório consolidado.

---

## Estrutura dos Dados

Os dados da missão são armazenados em uma matriz onde cada linha representa um ciclo operacional.

Exemplo:

```python
dados_missao = [
    [32, 55, 70, 98, 45],
    [25, 80, 65, 70, 74],
    [26, 95, 55, 99, 66]
]
```

Cada posição representa:

| Índice | Variável                     |
| ------ | ---------------------------- |
| 0      | Temperatura Interna (°C)     |
| 1      | Comunicação com a Base (%)   |
| 2      | Sistema de Energia (%)       |
| 3      | Suporte de Oxigênio (%)      |
| 4      | Estabilidade Operacional (%) |

---

## Critérios de Avaliação

### Temperatura Interna

| Faixa       | Status  |
| ----------- | ------- |
| < 18°C      | Alerta  |
| 18°C a 30°C | Normal  |
| 31°C a 34°C | Alerta  |
| ≥ 35°C      | Crítico |

### Comunicação com a Base

| Faixa     | Status  |
| --------- | ------- |
| < 30%     | Crítico |
| 30% a 59% | Alerta  |
| ≥ 60%     | Normal  |

### Sistema de Energia

| Faixa     | Status  |
| --------- | ------- |
| < 20%     | Crítico |
| 20% a 49% | Alerta  |
| ≥ 50%     | Normal  |

### Suporte de Oxigênio

| Faixa     | Status  |
| --------- | ------- |
| < 80%     | Crítico |
| 80% a 89% | Alerta  |
| ≥ 90%     | Normal  |

### Estabilidade Operacional

| Faixa     | Status  |
| --------- | ------- |
| < 40%     | Crítico |
| 40% a 69% | Alerta  |
| ≥ 70%     | Normal  |

---

## Classificação da Missão

A pontuação acumulada de cada ciclo é utilizada para determinar o estado operacional da missão.

| Pontuação | Classificação     |
| --------- | ----------------- |
| 0 a 2     | MISSÃO ESTÁVEL    |
| 3 a 5     | MISSÃO EM ATENÇÃO |
| 6 ou mais | MISSÃO CRÍTICA    |

---

## Exemplo de Saída

```text
CICLO 4
Temperatura interna: 18ºC | Normal
Comunicação com a Base: 22% | Crítico
Sistema de Energia: 88% | Normal
Suporte de Oxigênio: 85% | Alerta
Estabilidade Operacional: 68% | Alerta

Pontuação de risco do ciclo: 4
Classificação do ciclo: MISSÃO EM ATENÇÃO
Recomendação: Monitoramento necessário, preparar plano de contingência.
```

---

## Tecnologias Utilizadas

* Python 3
* Programação Estruturada
* Matrizes e Listas
* Funções
* Análise de Dados
* Relatórios em Terminal

---

## Possíveis Evoluções

* Leitura de dados por arquivos CSV.
* Interface gráfica.
* Dashboard de monitoramento em tempo real.
* Persistência em banco de dados.
* Integração com APIs de telemetria.
* Visualização gráfica de tendências.

---

## Autor

Projeto acadêmico desenvolvido por:
* Enzo Ricardo Silva            - RM: 571333
* Eric Hernandes Penhalbel      - RM 570237
* João Guilherme Figuereido     - RM: 572697
