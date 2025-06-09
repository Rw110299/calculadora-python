#  Calculadora em Python
Este é um projeto simples de calculadora desenvolvido em Python.  
Ele permite realizar as quatro operações matemáticas básicas e inclui testes automatizados.

##  Funcionalidades
-  Soma de dois números
-  Subtração
-  Multiplicação
-  Divisão com tratamento de erro (divisão por zero)
-  Testes automatizados usando unittest

##  Tecnologias Utilizadas
- *Python *
- *unittest* (biblioteca padrão de testes do Python)
- *Git e GitHub* para versionamento e hospedagem do código

##  Como Rodar o Projeto
1. Clone este repositório:

git clone https://github.com/Rw110299/calculadora-python.git
cd calculadora-python# calculadora-python
 
 2.Execute o arquivo principal:
 
 python calculadora_completa.py
    Este script inclui as funcoes da calculadora e os testes. Ao rodar,os testes já serao executados automaticamente.

## Teste
Este projeto utiliza testes automatizados com a biblioteca unittest.
 python calculadora_completa.py
  Você vera uma saida como está:

  .....
  ran 5 test in 0.001s
  ok
  ## Autor
  RICHARD SOUZA
   * GitHub: @Rw110299

## Licença

Este projeto está licenciado sob a Licença MIT.
Você pode usar, modificar e distribuir livremente.
Para mais detalhes, veja o arquivo LICENSE.


## Estrutura Recomendada do Projeto

calculadora-python
│ 
├── src/                        # Código-fonte principal do projeto 
│   └── calculadora.py         # Módulo com as funções básicas da calculadora 
│ 
├── tests/                     # Testes automatizados do projeto 
│   └── test_calculadora.py    # Testes unitários usando unittest 
│ 
├── docs/                      # Documentação adicional do projeto 
│   └── ...                    # (Exemplos, manuais, diagramas, etc.) 
│ 
├── README.md                  # Documentação inicial com visão geral do projeto 
├── .gitignore                 # Arquivo para ignorar arquivos/pastas no Git 
├── LICENSE                    # Licença de uso (MIT, Apache, etc.) 
└── pyproject.toml             # (Opcional) Configuração de metadados e dependências do projeto 