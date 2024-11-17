# Python-e-PowerBI

Usando Python dentro do Power BI para automatizar tarefas

Suponha que você tenha criado um dashboard com base em vários arquivos Excel e precise incorporar uma planilha com novos dados mensalmente. Além disso, esses novos dados precisam ser transformados para serem integrados ao seu relatório.

É possível incorporar um script do Python no Power BI, que será executado toda vez que você atualizar o dashboard, tornando processo manuais muito mais eficientes.

Para ilustrar, criei um dashboard utilizando 4 arquivos Excel mensais com dados de produção de uma indústria de calçados. 

Desenvolvi um programa no Python para concatenar todos os arquivos Excel e, em seguida, adicionar uma coluna UF, atribuindo valores com base nas cidades (São Paulo, Rio de Janeiro e Belo Horizonte), já presentes nas planilhas originais.

Para incorporar esse script no Power BI, basta colá-lo em:

Página Inicial -> Obert dados -> Mais... -> Script em Python

Após essas etapas, basta clicar em Atualizar no Power BI, e os novos dados serão automaticamente integrados aos visuais!
