# RELATÓRIO COMPARATIVO DE REFACTORAÇÃO DE CÓDIGO-FONTE

- Disciplina: Manutenção de Software
- Tema: Código Limpo (Capítulo 2)
- Aplicação: Calculadora GCS
- Autor: João Eliézer

## 1. Introdução

Este relatório apresenta a análise comparativa entre a versão original e a versão refatorada da aplicação Calculadora GCS. O processo de manutenção do código-fonte foi guiado pelas diretrizes do Capítulo 2 do livro "Fundamentos de Manutenção de Software", cujo objetivo central é elevar a legibilidade, clareza e consistência do sistema, reduzindo o esforço cognitivo na compreensão da lógica do programa.

A solução é composta por cinco módulos de cálculo (`calculadora_basico.py`, `calculadora_potencia.py`, `calculadora_percentual.py`, `calculadora_estatistica.py` e `calculadora_conversao.py`), um módulo de interface/execução principal (`main.py`) e um módulo de testes unitários automatizados (`test_calc.py`).

## 2. Análise Comparativa com Base nas 6 Premissas

### 2.1. Premissa 1: Use Verificadores de Estilo e Formatadores

- Código Original: o código apresentava inconsistências de espaçamento, ausência de anotações de tipo (Type Hints), docstrings com formatação mista e presença de caracteres ocultos não imprimíveis (`\xa0`) herdados da cópia de texto.
- Código Limpo: ajustado estritamente em conformidade com as diretrizes da PEP 8 (guia de estilo para Python), PEP 257 (docstrings no padrão Google) e PEP 484 (Type Hints). Todas as funções receberam assinaturas de tipo explícitas (`int | float`, `list[int | float]`) preparadas para validação por ferramentas de análise estática como `mypy`, além da automação de testes com a biblioteca `pytest`.

### 2.2. Premissa 2: Escolha Nomes Legíveis

- Código Original: utilização pontual de variáveis de nomeação menos descritiva e ocorrência de erros de ortografia
- Código Limpo: todas as variáveis e argumentos foram renomeados para termos autoexplicativos que revelam o seu real propósito no sistema (por exemplo: `operando1`, `operando2`, `percentual_valor`, `lista_ordenada`, `tamanho_lista`).

### 2.3. Premissa 3: Evite Números Mágicos

- Código Original: presença de literais numéricos diretamente no corpo dos cálculos sem contextualização clara, como `0.5`, `1/3`, `9/5` e `32`.
- Código Limpo: substituição de todos os valores literais por constantes nomeadas em maiúsculas (UPPER_CASE) no topo dos ficheiros:
  - `CELSIUS_PARA_FAHRENHEIT_FATOR = 9 / 5` e `FAHRENHEIT_OFFSET = 32` em `calculadora_conversao.py`.
  - `EXPOENTE_RAIZ_QUADRADA = 0.5` em `calculadora_estatistica.py`.

### 2.4. Premissa 4: Adote uma Linguagem Ubíqua

- Código Original: conflito de terminologia técnica ao nomear entradas numéricas como "operadores" nas assinaturas das funções de cálculo.
- Código Limpo: padronização vocabular de acordo com o domínio da matemática e do cálculo estatístico. Símbolos aritméticos (`+`, `-`, `*`, `/`) são designados como operadores, enquanto os valores numéricos fornecidos passaram a ser estritamente nomeados como operandos (`operando1`, `operando2`). A terminologia foi estendida às docstrings e mensagens de exceção.

### 2.5. Premissa 5: Implemente Funções Coesas e Desacopladas

- Código Original: repetição de blocos de tratamento de exceção (`try...except TypeError`) dentro de cada função de cálculo, duplicidade integral das funções `km_para_milhas` e `kg_para_libras` no ficheiro `calculadora_conversao.py`, além de imprecisão matemática em `raiz_cubica` para valores negativos.
- Código Limpo: aplicação rigorosa do princípio DRY (Don't Repeat Yourself). A validação de tipo e a rejeição de tipos booleanos foram centralizadas em funções auxiliares privadas (`_validar_operandos`, `_validar_lista`, `_validar_valor`). As funções duplicadas foram eliminadas e a função `raiz_cubica` passou a delegar o cálculo à função nativa `math.cbrt` para garantir suporte correto a números negativos.

### 2.6. Premissa 6: Separe os Fluxos de Execução

- Código Original: mistura pontual de validações de estado diretamente na lógica de cálculo e verificação manual de exceções nos testes unitários utilizando estruturas `try/except`.
- Código Limpo: arquitetura organizada em três fluxos perfeitamente desacoplados:
  1. Camada de Regras de Negócio/Domínio: módulos `calculadora_*.py` encarregados exclusivamente de validar e executar operações matemáticas.
  2. Camada de Interface e Execução: ficheiro `main.py` dedicado unicamente ao carregamento dinâmico dos módulos e exibição dos resultados ao utilizador.
  3. Camada de Testes: suíte `test_calc.py` utilizando o gerenciador de contexto `with pytest.raises(...)` para validar o disparo de exceções sem poluir o fluxo do teste.

## 3. Tabela Comparativa de Resumo

| Premissa | Código Original | Código Limpo (Refatorado) |
| --- | --- | --- |
| 1. Verificadores e Formatadores | Sem anotações de tipo; formatação mista; presença de caracteres não imprimíveis. | Conformidade integral com PEP 8, PEP 257 e PEP 484 (Type Hints). |
| 2. Nomes Legíveis | Erros de digitação em constantes (`FAHRENHEITR...`). | Nomes descritivos e autoexplicativos (`CELSIUS_PARA_FAHRENHEIT_FATOR`). |
| 3. Números Mágicos | Literais numéricos espalhados pelo código (`0.5`, `1/3`, `9/5`, `32`). | Constantes nomeadas em maiúsculas (`EXPOENTE_RAIZ_QUADRADA`, `FAHRENHEIT_OFFSET`). |
| 4. Linguagem Ubíqua | Confusão conceptual entre o termo operador e operando. | Vocabulário preciso do domínio matemático (`operando1`, `operando2`, `mediana`). |
| 5. Coesão e Desacoplamento | Blocos de tratamento repetidos; funções duplicadas no mesmo módulo. | Centralização das validações em funções privadas (`_validar_*`); código DRY. |
| 6. Fluxos de Execução | Captura manual de exceções nos testes com `try/except`. | Separação entre Regras de Negócio, Interface (`main.py`) e Testes (`pytest`). |

## 4. Conclusão

A refatoração realizada na Calculadora GCS permitiu transformar o código inicial num sistema modular, legível e robusto. A aplicação das seis premissas do Capítulo 2 da literatura de Manutenção de Software garantiu que o código-fonte se tornasse imune a bugs de conversão implícita (como a aceitação de valores booleanos como inteiros), além de facilitar a adição de novas funcionalidades e a manutenção por outros programadores.
