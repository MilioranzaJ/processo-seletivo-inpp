Análise de Dados Ambientais - Pantanal
Este projeto foi desenvolvido com o objetivo de realizar a análise de dados ambientais fictícios do Pantanal durante o mês de janeiro de 2025. A base utilizada contém informações de temperatura, nível do rio e índice NDVI, permitindo explorar etapas de limpeza, tratamento, análise estatística e visualização de dados.
Tecnologias Utilizadas


Python 3.x


Pandas: utilizado para manipulação e tratamento dos dados.


Matplotlib: utilizado para geração dos gráficos e visualizações.


Como Executar o Projeto
1. Organize os arquivos
Certifique-se de que os arquivos abaixo estejam na mesma pasta:


dados_pantanal.csv


analise_pantanal.py


2. Instale as dependências
Caso ainda não tenha as bibliotecas instaladas, execute no terminal:
pip install pandas matplotlib
3. Execute o script
No terminal, rode o comando:
python analise_pantanal.py
Resultados Gerados
Ao executar o programa:


Os dados originais e os dados tratados serão exibidos no console.


As estatísticas calculadas também serão apresentadas.


Os gráficos serão exibidos em uma janela.


Uma imagem chamada visualizacao_pantanal.png será salva automaticamente na pasta do projeto.


Decisões Técnicas
Tratamento de Valores Ausentes
Durante a análise foi identificado que algumas colunas possuíam valores ausentes, principalmente nas variáveis relacionadas ao nível do rio e ao NDVI.
Para resolver isso, foi utilizada interpolação linear temporal:
df.interpolate(method='time')
Essa abordagem foi escolhida porque os dados representam uma série temporal ambiental, onde as mudanças costumam ocorrer de forma gradual entre dias consecutivos. Assim, a interpolação permite preencher os valores faltantes de maneira mais coerente, sem remover registros importantes ou distorcer os dados utilizando médias gerais.
Estatísticas Obtidas
Após o tratamento dos dados, foram obtidas as seguintes médias:


Temperatura média: 33.95 °C


Nível médio do rio: 4.49 m


NDVI médio: 0.6815


Visualizações
Foram gerados dois gráficos principais:
Evolução da Temperatura
O primeiro gráfico mostra a variação diária da temperatura ao longo do mês, permitindo visualizar tendências e dias com temperaturas mais elevadas.
Nível do Rio e NDVI
O segundo gráfico utiliza dois eixos para representar simultaneamente o nível do rio e o NDVI. Essa escolha foi feita porque as variáveis possuem escalas diferentes, e o uso de eixo duplo facilita a comparação visual entre elas sem comprometer a leitura do gráfico.