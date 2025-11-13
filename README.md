# PriceMyHome

**Simple web app to estimate your house price using Machine Learning**

Esta aplicação web permite que o usuário insira dados de imóveis e visualize uma estimativa de valor com base em um modelo de **Machine Learning**.

---

## Funcionalidades

* Inserção de múltiplos imóveis como parâmetros para treinar o modelo.
* Inserção de um imóvel alvo que o usuário deseja estimar o valor.
* Interface minimalista e fácil de usar.
* API REST no backend que recebe os dados em JSON e devolve a estimativa.
* Modelo de regressão simples com normalização de dados utilizando `StandardScaler`.

---

## Tecnologias usadas

* **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
* **Backend**: Python 3.x, Flask, Blueprints
* **Machine Learning**: scikit‑learn, Numpy
* **Comunicação**: JSON via API REST
* **Estrutura**: Projeto dividido entre servidor (`server/`), utilitários (`utils/`), arquivos estáticos (`static/`) e template HTML (`templates/`).

---

## Estrutura do Projeto

```
PriceMyHome/
│
├─ server/
│  ├─ app.py               # Arquivo principal do Flask
│  ├─ routes/
│  │  └─ get_data.py       # Rota para recebimento de dados e previsão
│  └─ utils/
│     └─ housesPrice.py    # Função de ML para estimar o valor do imóvel
│
├─ static/
│  ├─ css/
│  │   └─ index.css        # Estilização
│  └─ js/
│      └─ get_value.js     # Script JS para interações e envio de dados
│
├─ templates/
│  └─ index.html           # Página principal da aplicação
│
└─ README.md               # Documentação do projeto
```

---

## Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Whandger/PriceMyHome.git
cd PriceMyHome
```

### 2. Criar ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

pip install flask scikit-learn numpy
```

### 3. Iniciar a aplicação

**Clique duas vezes** no arquivo `run_app.bat` para iniciar o servidor.

Depois, abra seu navegador em:

```
http://127.0.0.1:5000
```

---

## Como Funciona

### Frontend

* O usuário preenche os campos para até 7 imóveis (rooms, square meters, distance to city center, value).
* Em seguida, preenche os campos para um imóvel alvo (rooms, square meters, distance to city center).
* Ao clicar em “Calculate”, o script JS coleta os valores e envia via `fetch` ao backend.

### Backend e Machine Learning

* A rota `/api/data` recebe um JSON com duas chaves:

  * `imoveis`: lista dos imóveis de exemplo usados para treinar o modelo.
  * `usuario`: objeto com os dados do imóvel que se quer prever.
* O servidor extrai os dados, transforma em matrizes:

  * `X`: características dos imóveis de exemplo
  * `Y`: valores dos imóveis de exemplo
  * `Z`: características do imóvel do usuário
* Os dados são normalizados (via `StandardScaler`) e alimentam um modelo de regressão para gerar a estimativa de valor.
* O resultado é retornado ao frontend como JSON `{ "previsao": valor_estimado }`.

---

## Exemplo de JSON enviado

```json
{
  "imoveis": [
    {"quartos": 2, "metros": 50, "distancia": 3, "valor": 250},
    {"quartos": 3, "metros": 70, "distancia": 5, "valor": 320},
    {"quartos": 1, "metros": 35, "distancia": 2, "valor": 180}
  ],
  "usuario": {"quartos": 3, "metros": 75, "distancia": 5}
}
```

Exemplo de resposta:

```json
{
  "previsao": 305.4
}
```

---

## Melhorias Futuras

* Adicionar mais características dos imóveis (ex: idade, bairro, número de banheiros).
* Persistência de dados (salvar imóveis em banco de dados para treinamento contínuo).
* Interface mais amigável com gráficos ou visualização dos dados.
* Implementar autenticação de usuários, podendo obter estimativas personalizadas e histórico de resultados.
* Migrar para produção com servidor WSGI, HTTPS, deploy em nuvem.

## Preview

<img src=".\images for preview\Formulario vazio.png"/>
<img src=".\images for preview\Primeira casa.png"/>

---

## Licença

Este projeto está licenciado sob a **MIT License**. Consulte o arquivo `LICENSE` para detalhes.

