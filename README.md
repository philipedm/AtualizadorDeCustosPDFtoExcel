# AtualizadorDeCustosPDFtoExcel
Recentemente fui contatado para desenvolver uma breve automação de captura de dados em PDF e gravação em Excel.

Resumindo: 
A pessoa recebia um PDF, da Fábrica que trabalhava, com os preços de custo atualizados dos produtos à venda e tinha que alimentar uma tabela no Excel para realizar cálculos em cima desses preços de custo.
O problema é que eram 900 produtos a serem atualizados um a um e manualmente. Visto que os preços de custo estavam sendo alterados com mais frequência nesse período de pandemia, isso se tornava inviável e tomava muito tempo do colaborador.

Depois de analisar o padrão de como estavam colocadas as informações de produtos e preços nesse PDF, com apenas algumas horas e poucas linhas de código utilizando Python, consegui solucionar esse problema e automatizar o processo que durava dias, para alguns segundos e dois cliques no executável.

A automação consiste em ler o PDF inteiro, procurando pelos códigos dos produtos que estão numa tabela em Excel. Ao encontrar, faz uma busca na mesma linha pelo preço de custo, guarda essa informação e depois atualiza na tabela em Excel.
