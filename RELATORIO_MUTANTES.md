# Relatório de Testes de Software
## Projeto Calculadora GCS

## 1. Introdução

Este relatório apresenta os resultados dos testes de software realizados no projeto Calculadora GCS, desenvolvido em Python. O objetivo foi avaliar a qualidade dos testes implementados por meio de duas técnicas: cobertura de código e teste de mutação.

Foram utilizadas as ferramentas Pytest, Pytest-Cov e Mutmut para verificar o funcionamento dos testes, a cobertura das instruções e a capacidade dos testes de identificar alterações no código-fonte.

## 2. Ferramentas utilizadas

- **Pytest:** execução e validação dos testes automatizados.
- **Pytest-Cov:** análise da cobertura de código.
- **Mutmut:** geração e execução de mutações artificiais no código para avaliar a eficiência dos testes.

## 3. Testes de cobertura

A cobertura foi calculada considerando exclusivamente os módulos responsáveis pelas operações da calculadora. Os arquivos `main.py`, `test_calc.py` e `test_mutante.py` foram excluídos do cálculo, pois não fazem parte do código de produção avaliado.

### 3.1. Resultados

| Módulo | Instruções | Não cobertas | Cobertura |
|---|---:|---:|---:|
| calculadora_basico.py | 20 | 0 | 100% |
| calculadora_conversao.py | 25 | 4 | 84% |
| calculadora_estatistica.py | 28 | 0 | 100% |
| calculadora_percentual.py | 15 | 0 | 100% |
| calculadora_potencia.py | 19 | 0 | 100% |
| **Total** | **107** | **4** | **96,26%** |

A cobertura geral dos módulos avaliados foi de aproximadamente **96,26%**.

O módulo `calculadora_conversao.py` apresentou a menor cobertura, com 84%. As linhas 66–67 e 82–83 não foram executadas durante os testes, indicando a possibilidade de criação de novos casos de teste.

Os demais módulos alcançaram 100% de cobertura de instruções.

## 4. Testes de mutação

Os testes de mutação foram realizados com a ferramenta Mutmut, responsável por modificar artificialmente trechos do código-fonte para verificar se os testes automatizados conseguem identificar essas alterações.

Entre as alterações avaliadas estão modificações em operadores, condições, valores e validações.

### 4.1. Resultados quantitativos

Na execução mais recente, foram apresentados os seguintes resultados:

| Indicador | Resultado |
|---|---:|
| Mutantes gerados | 166 |
| Mutantes mortos | 165 |
| Mutantes sobreviventes | 0 |
| Mutantes equivalentes | 1 |
| Mutantes com timeout | 0 |
| **Mutation Score bruto** | **99,40%** |

O Mutation Score bruto foi calculado utilizando a quantidade de mutantes mortos dividida pelo total de mutantes:

$$
Mutation\ Score = \frac{165}{166} \times 100 = 99,40\%
$$

Esse resultado demonstra que os testes automatizados conseguiram identificar praticamente todas as alterações introduzidas pelo Mutmut.

### 4.2. Mutante equivalente identificado

Durante a análise da função `_validate_operandos()`, do módulo `calculadora_potencia.py`, foi identificada uma mutação que alterava o valor padrão do parâmetro `expoente` de `0` para `1`.

Essa alteração não modificava o comportamento observável da aplicação, pois o parâmetro era utilizado apenas para verificar se o valor recebido era numérico. Como ambos os valores são números válidos, a validação continuava funcionando da mesma maneira.

Por esse motivo, essa mutação foi considerada equivalente, não sendo necessário modificar a implementação apenas para eliminá-la.


## 5. Análise dos resultados

Os resultados demonstram que a suíte de testes apresenta boa cobertura de código, alcançando aproximadamente 96,26% nos módulos de produção avaliados.

Além disso, o Mutation Score bruto de 99,40% demonstra uma alta capacidade dos testes de identificar alterações artificiais no código.

A combinação dessas duas métricas permite uma avaliação mais abrangente: enquanto a cobertura verifica quais instruções foram executadas, o teste de mutação avalia se os testes conseguem identificar alterações no comportamento do programa.

## 6. Conclusão

A realização dos testes de cobertura e mutação permitiu avaliar diferentes aspectos da qualidade da suíte de testes do projeto Calculadora GCS.

A cobertura de aproximadamente 96,26% demonstra que a maior parte das instruções dos módulos avaliados foi executada durante os testes.

Os testes de mutação alcançaram um resultado de 99,40%, com 165 mutantes mortos de um total de 166.

Conclui-se que a combinação entre cobertura de código e teste de mutação proporciona uma avaliação mais abrangente da qualidade dos testes automatizados, contribuindo para aumentar a confiabilidade e a manutenção do software.