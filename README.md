Aqui está o arquivo `README.md` formatado. Ele foi escrito sob a perspectiva de um desenvolvedor Python com domínio em físico-química, destacando tanto a estrutura do código quanto as fórmulas científicas implementadas (Nernst e Faraday).

---

# PROSIE - Programa para Cálculos de Processos Eletroquímicos

> **Versão:** 1.0
> **Autor:** Jenivaldo Lisboa

O **PROSIE** é uma ferramenta de linha de comando (CLI) desenvolvida em Python projetada para estudantes e profissionais de química. O software automatiza cálculos complexos de eletroquímica, variando desde a determinação de potenciais padrão em pilhas até a estequiometria de processos eletrolíticos e corrosão via Leis de Faraday.

## 📋 Funcionalidades

O sistema opera através de um menu interativo dividido em dois módulos principais:

### 1. Módulo Básico

Focado em condições padrão.

* **Simulação de Pilhas:**
    * Cálculo do Potencial Padrão da Célula.
    * Verificação automática de espontaneidade.


* **Simulação de Eletrólise:**
    * **Ígnea:** Cálculo de potenciais e voltagem necessária para forçar a reação não espontânea.
    * **Aquosa:** Algoritmo de decisão que verifica a **prioridade de descarga**. O programa analisa se quem descarrega é o íon do sal ou a água, baseando-se nos potenciais de redução cadastrados.


* **Variação de Massa (Corrosão e Deposição):**
    * Cálculo baseado na **1ª Lei de Faraday**.
    * Testes comparativos entre metais (Al, Fe, Zn) variando corrente, tempo ou massa.



### 2. Módulo Avançado

Focado em condições não-padrão.

* **Equação de Nernst:**
    * Permite input de **Temperatura (K)** e **Concentrações Molares**.
    * Cálculo automático do quociente reacional ajustado para estequiometrias de 1 ou 2 elétrons.



---

## 🛠️ Instalação e Requisitos

### Pré-requisitos

* Python 3.x instalado.

### Estrutura de Arquivos

Para o funcionamento correto, os dois arquivos abaixo devem estar no **mesmo diretório**:

1. `prosie.py`: Script principal contendo a lógica de interface, loops e cálculos.
2. `data.py`: Banco de dados contendo dicionários (`cations`, `anions`, `especies_quimicas`) com nomes, potenciais de redução e número de elétrons.

---

## 🚀 Como Executar

1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta onde salvou os arquivos.
3. Execute o comando:

```bash
python prosie.py

```

### Navegação

![](/imagens/prosie_tela_inicial.png)
O programa solicitará inputs numéricos para navegar nos menus:

* `[1] Básico` / `[2] Avançado`.
* Nas listas de espécies químicas, digite o número correspondente ao íon/metal desejado (ex: digite `2` para Zinco, conforme listado na tela).

---

## 🔬 Detalhes Científicos e Técnicos

### Banco de Dados (`data.py`)

O sistema utiliza um mapeamento de dicionários para buscar propriedades físico-químicas. Exemplo da estrutura:

```python
especies_quimicas = {
    2: {'especie': 'Zn2+/Zn', 'potencial': -0.76, 'eletrons': 2},
    # ...
}

```

Isso permite escalabilidade fácil: para adicionar novos elementos, basta editar o arquivo `data.py` sem alterar a lógica principal.

### Fórmulas Implementadas (`prosie.py`)

#### 1. Leis de Faraday (Corrosão/Eletrólise)

Implementado na função `massa(n, nox, MM)`:



Onde:

*  (Carga total)
*  (Constante de Faraday utilizada no código)

#### 2. Equação de Nernst (Módulo Avançado)

O código calcula o potencial real () ajustando o quociente  baseando-se na estequiometria ( e ):

O script lida automaticamente com os expoentes do quociente reacional dependendo se a reação transfere 1 ou 2 elétrons, ajustando as concentrações do ânodo e cátodo.

#### 3. Prioridade de Descarga (Eletrólise Aquosa)

O código possui lógica condicional (`if cation >= 8`) para determinar se ocorre a redução do cátion metálico ou a redução da água (), comparando os potenciais de metais alcalinos/alcalino-terrosos contra o hidrogênio.

---

## ⚠️ Tratamento de Erros

* O programa verifica se `potencial < 0` em pilhas, alertando o usuário para inverter ânodo/cátodo para obter um processo espontâneo.
* Menus possuem loops `while` para garantir que o usuário digite uma opção válida.