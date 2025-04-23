# SNPClassifier - MVP (Sprint de Transição -> Ciência de Dados -> PUC-Rio)

**SNPClassifier** é um sistema para classificar variantes genéticas (SNPs) em dados VCF de pacientes. Ele integra Flask, SQLite e a API do Ensembl para enriquecer os dados com anotações e informações relevantes.

## Funcionalidades

- **Upload de VCF**: Envio de arquivos VCF contendo variantes genéticas.
- **Consulta à API Ensembl**: Cada variante é enriquecida com dados sobre genes, consequências, impacto, SIFT, PolyPhen, e frequência.
- **Classificação de Variantes**: Variantes são classificadas em base de regras definidas.
- **Armazenamento em Banco de Dados SQLite**: Pacientes e variantes são armazenados de forma persistente.
- **Interface Web**: Interface interativa para upload e visualização das variantes.

## Estrutura do Projeto

```bash
SNPClassifier/
│
├── app/
│   ├── __init__.py          # Inicializa o aplicativo Flask
│   ├── models.py            # Modelos de banco de dados
│   ├── routes.py            # Lógica de rotas
│   ├── templates/
│   │   └── index.html       # Página principal
│   └── utils.py             # Funções auxiliares
│
├── uploads/                 # Arquivos VCF enviados
├── requirements.txt         # Dependências
└── run.py                   # Inicialização da aplicação
```

## Instalação e Execução Passo a Passo

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/SNPClassifier.git
   cd SNPClassifier
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie a estrutura de pastas (se ainda não existirem):

   ```bash
   mkdir -p uploads
   ```

5. Execute a aplicação:

   ```bash
   python run.py
   ```

6. Abra o navegador e acesse:

   ```
   http://127.0.0.1:5000/
   ```

7. Na interface:
   - Preencha o nome do paciente.
   - Faça upload do arquivo `.vcf` desejado.
   - Veja a tabela com as variantes enriquecidas pela API do Ensembl.

## Como Usar

1. **Upload de Arquivo VCF**: No formulário da página inicial, insira o nome do paciente e envie o arquivo VCF.
2. **Visualizar Variantes**: Após o upload, as variantes serão exibidas com informações enriquecidas da Ensembl (gene, consequência, impacto, etc.).

## Estrutura do Banco de Dados

### Tabela `patients`

| Campo        | Tipo    | Descrição |
|--------------|---------|----------|
| id           | INTEGER | ID único do paciente |
| name         | TEXT    | Nome do paciente |
| vcf_filename | TEXT    | Nome do arquivo VCF |
| upload_date  | DATETIME | Data do upload |

### Tabela `variants`

| Campo         | Tipo    | Descrição |
|---------------|---------|----------|
| id            | INTEGER | ID único da variante |
| patient_id    | INTEGER | Referência para paciente (FK) |
| chromosome    | TEXT    | Cromossomo da variante |
| position      | INTEGER | Posição da variante |
| ref           | TEXT    | Alelo de referência |
| alt           | TEXT    | Alelo alternativo |
| gene          | TEXT    | Gene afetado |
| consequence   | TEXT    | Consequência da variante |
| impact        | TEXT    | Impacto da variante |
| sift          | TEXT    | Previsão SIFT |
| polyphen      | TEXT    | Previsão PolyPhen |
| af            | REAL    | Frequência alélica |
| classification| TEXT    | Classificação da variante |

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
