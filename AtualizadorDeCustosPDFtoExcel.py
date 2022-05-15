import pandas as pd
from pdfminer.high_level import extract_text
from datetime import datetime

arquivo = input("Digite o nome do arquivo PDF sem a extensão: ") 

try:
    texto = extract_text(arquivo + '.pdf')  # extraindo o texto do arquivo em pdf

    tabela = pd.read_excel("codigos_original.xlsx")  # lendo o arquivo em excel e armazenando em tabela

    # conta quantas linhas temos na coluna código para saber a quantidade de repetição do laço
    qtde_linhas = tabela["Código"].count()
    
    i = 0  # variavel para inicialização do laço while

    while i < qtde_linhas:  # percorrer todos os códigos
        codigo = str(tabela.loc[i, "Código"])  # localizar o código [linha,coluna]
        codigo = codigo.replace(" ", ".")  # substituir "espaço" por "." (particularidade da empresa)
        
        # para cada código da tabela, faz uma busca no pdf
        # se o codigo for encontrado no pdf, percorre a linha até encontrar os caracteres numericos
        # armazena na string custo até achar o caractere | que é a condição de parada
        
        if codigo in texto:
            posicao_codigo = texto.find(codigo) + 20  # percorrendo pro campo que está 20 caracteres após
            custo = ""
            while texto[posicao_codigo] != "|":  # condicao de parada
                if texto[posicao_codigo] != " ":  # encontra o caractere numerico
                    custo = custo + texto[posicao_codigo]  # preenche a variavel custo com os caracteres numericos encontrados
                posicao_codigo = posicao_codigo + 1  # pula pro proximo caractere
            custo = custo.replace(".", "")  # onde for '.' vai retirar
            custo_float = float(custo.replace(",", "."))  # onde for vírgula vai ser ponto
            tabela.loc[i, "Custo"] = custo_float  # atribui o valor do custo na tabela
        else:  # se não encontrou o código no pdf
            print("Código " + codigo + " não foi encontrado no PDF")
        i = i + 1  # pula pro codigo seguinte e retoma o laço

    dataHora = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')  # captura data e hora atual
    
    tabela.to_excel("codigo_e_custo_" + dataHora + ".xlsx", index=False)  # cria novo arquivo excel renomeado com data e hora
    
except FileNotFoundError as error:
    print(error)
except:
    print("Erro. Entrar em contato com o desenvolvedor.")
