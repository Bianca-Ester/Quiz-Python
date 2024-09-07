def quiz_versace():

    # lista com todas as perguntas, opções e respostas
    lista_perguntas = [
        {
            "pergunta": "1. Em que ano a Versace foi lançada?",
            "opcoes": ["A - 1987", "B - 1978", "C - 1975"],
            "resposta": ["B", "B - 1978"]
        },
        {
            "pergunta": "2. Qual a modelo mais famosa que já desfilou pela Versace?",
            "opcoes": ["A - Kylie Jenner", "B - Gigi Hadid", "C - Adriana Lima"],
            "resposta": ["B", "B - Gigi Hadid"]
        },
        {
            "pergunta": "3. Qual o símbolo da Versace?",
            "opcoes": ["A - Cobra", "B - Medusa", "C - Escorpião"],
            "resposta": ["B", "B - Medusa"]
        },
        {
            "pergunta": "4. A Versace tem um resort na Australia. Verdadeiro ou falso?",
            "opcoes": ["A - Verdadeiro", "B - Falso"],
            "resposta": ["A", "A - Verdadeiro"]
        },
        {
            "pergunta": "5. Em que data Gianne Versace morreu?",
            "opcoes": ["A - 2003", "B - 1999", "C - 1997"],
            "resposta": ["C", "C - 1997"]
        },
        {
            "pergunta": "6. Qual o nome da irmã de Gianne Versace?",
            "opcoes": ["A - Linda Versace", "B - Donatella Versace", "C - Emilly Versace"],
            "resposta": ["B", "B - Donatella Versace"]
        },
        {
            "pergunta": "7. O que a Versace representa hoje na moda?",
            "opcoes": ["A - Breguice", "B - Luxo e sexualidade", "C - Conforto e beleza"],
            "resposta": ["B", "B - Luxo e sexualidade"]
        },
        {
            "pergunta": "8. Atualmente, (setembro de 2024) a marca Versace desfila em que país?",
            "opcoes": ["A - Milão", "B - França", "C - Brasil"],
            "resposta": ["A", "A - Milão"]
        },
        {
            "pergunta": "9. Onde fica a principal fábrica da Versace?",
            "opcoes": ["A - Itália", "B - China", "C - Estados Unidos"],
            "resposta": ["A", "A - Itália"]
        },
        {
            "pergunta": "10. Qual a data de nascimento de Gianne Versace (fundador da marca)?",
            "opcoes": ["A - 1949", "B - 1952", "C - 1946"],
            "resposta": ["C", "C - 1946"]
        },
    ]

    print("QUIZ SOBRE A VERSACE\n")

    score = 0

    for questao in lista_perguntas: # laço que percorre todas as perguntas
        print(questao["pergunta"])
        
        for opcoes in questao["opcoes"]: # laço interno que percorre todas as opções de resposta daquela pergunta
            print(opcoes)
        
        controle = True
        while controle:
            resposta = input("Resposta: ").lower()

            if resposta == questao["resposta"][0].lower(): # se resposta é igual a letra da resposta correta | questao["resposta"][0]
                print("\n\033[32mResposta correta 😃\033[m\n")

                score += 1
                controle = False

            elif resposta != "a" and resposta != "b" and resposta != "c": # se resposta for diferente de a, b ou c
                print("\nOpção inválida! 🤨\n")

            else: # caso contrário, resposta errada
                print("\nResposta errada 😭")
                print(f"\n\033[31mResposta correta: {questao['resposta'][1]}\033[m\n")
                controle = False

    # Resultados

    errop = (10 - score) / 10 * 100  
    print("\nResultados:")
    if score <= 3: 
        print("Vish, não foi dessa vez...\nSeu erro percentual foi de {}%, mas esperamos que você tenha se divertido e descoberto mais sobre a Versace!".format(errop))

    elif score <= 6:
        print("Um(a) novo(a) especialista em moda?\nSeu erro percentual foi de {}%. Esperamos que você tenha aprendido coisas novas sobre a grande marca Versace!".format(errop))

    elif score <= 9:
        print("Parabéns, você é um(a) superfã de moda!\nSeu erro percentual foi de apenas {}%!".format(errop))

    else:
        print("Parabéns, pelo visto seus conhecimentos sobre moda não deixam a desejar em nada!\nSeu erro percentual foi de {}%".format(errop))
    
    input("\nDigite qualquer tecla para voltar ao menu inicial...") # prende o terminal para poder exibir o resultado
