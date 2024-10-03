def quiz_biblico():

    lista_perguntas = [
        {
            "pergunta": "1. Qual livro da Bíblia narra a história do Dilúvio?",
            "opcoes": ["A - Gênesis", "B - Êxodo", "C - Levítico"],
            "resposta": ["A", "A - Gênesis"]
        },
        {
            "pergunta": "2. Quem foi o primeiro homem criado por Deus, segundo a Bíblia?",
            "opcoes": ["A - Adão", "B - Abel", "C - Noé"],
            "resposta": ["A", "A - Adão"]
        },
        {
            "pergunta": "3. Qual o nome do mar que se abriu para que o povo de Israel pudesse passar?",
            "opcoes": ["A - Mar Vermelho", "B - Mar Morto", "C - Mar Mediterrâneo"],
            "resposta": ["A", "A - Mar Vermelho"]
        },
        {
            "pergunta": "4. Qual o nome da lei que Deus deu a Moisés no Monte Sinai?",
            "opcoes": ["A - Lei de Moisés", "B - Dez Mandamentos", "C - Lei Talmúdica"],
            "resposta": ["B", "B - Dez Mandamentos"]
        },
        {
            "pergunta": "5. Quem foi o profeta que foi engolido por um grande peixe?",
            "opcoes": ["A - Jonas", "B - Daniel", "C - Jeremias"],
            "resposta": ["A", "A - Jonas"]
        },
        {
            "pergunta": "6. Qual foi a montanha onde Moisés recebeu os Dez Mandamentos?",
            "opcoes": ["A - Monte Sinai", "B - Monte Sião", "C - Monte Carmelo"],
            "resposta": ["A", "A - Monte Sinai"]
        },
        {
            "pergunta": "7. Em qual cidade Jesus nasceu?",
            "opcoes": ["A - Jerusalém", "B - Belém", "C - Nazaré"],
            "resposta": ["B", "B - Belém"]
        },
        {
            "pergunta": "8. Qual dos livros da Bíblia abaixo narra a vida de Jesus?",
            "opcoes": ["A - Atos dos Apóstolos", "B - Romanos", "C - Evangelho de João"],
            "resposta": ["C", "C - Evangelho de João"]
        },
        {
            "pergunta": "9. Qual o nome da mãe de Jesus?",
            "opcoes": ["A - Maria", "B - Marta", "C - Ana"],
            "resposta": ["A", "A - Maria"]
        },
        {
            "pergunta": "10. Qual o nome do discípulo que negou Jesus três vezes?",
            "opcoes": ["A - Pedro", "B - Judas", "C - Tomé"],
            "resposta": ["A", "A - Pedro"]
        },
    ]

    print("QUIZ BÍBLICO\n")

    score = 0

    for questao in lista_perguntas: # laço que percorre todas as perguntas
        print(questao["pergunta"])
        
        for opcoes in questao["opcoes"]: # laço interno que percorre todas as opções
            print(opcoes)
        
        controle = True
        while controle:
            resposta = input("Resposta: ").lower()

            if resposta == questao["resposta"][0].lower(): # se resposta é igual a letra da resposta correta | questao["resposta"][0]
                print("\n\033[32mResposta correta\033[m 😃\n")

                score += 1
                controle = False

            elif resposta != "a" and resposta != "b" and resposta != "c": # se resposta for diferente de a, b ou c
                print("\nOpção inválida! 🤨\n")

            else: # caso contrário, resposta errada
                print("\n\033[31mResposta errada\033[m 😭")
                print(f"\nResposta correta: \033[32m{questao['resposta'][1]}\033[m\n")
                controle = False


    errop = (10 - score) / 10 * 100
    print("\nResultados:")
    if score <= 3:
        print("Vish, não foi dessa vez...\nSeu erro percentual foi de {}%, mas esperamos que você tenha se divertido e descoberto mais sobre a Bíblia!".format(errop))
    
    elif score <= 6:
        print("Um(a) novo(a) convertido(a) na família?\nSeu erro percentual foi de {}%.\nEsperamos que você tenha aprendido coisas novas sobre a Bíblia!".format(errop))
    
    elif score <= 9:
        print("Parabéns, você é um(a) superfã da Bíblia!\nSeu erro percentual foi de apenas {}%!".format(errop))
    
    else:
        print("Parabéns, pelo visto seus conhecimentos sobre a Bíblia não deixam a desejar em nada!\nSeu erro percentual foi de {}%".format(errop))

    input("\nDigite qualquer tecla para voltar ao menu inicial...")
