def quiz_rita_lee():

    lista_perguntas = [
        {
            "pergunta": "1. Em qual distrito de São Paulo nasceu Rita Lee?",
            "opcoes": ["A - Vila Matilde", "B - Vila Mariana", "C - Jabaquara"],
            "resposta": ["A", "A - Vila Matilde"]
        },
        {
            "pergunta": "2. Qual é o filho mais velho de Rita Lee?",
            "opcoes": ["A - Beto Lee", "B - João Lee", "C - Antônio Lee"],
            "resposta": ["A", "A - Beto Lee"]
        },
        {
            "pergunta": "3. Qual o nome da 1ª banda que Rita Lee teve?",
            "opcoes": ["A - Teenage Singers", "B - Tutti Frutti", "C - Os Mutantes"],
            "resposta": ["A", "A - Teenage Singers"]
        },
        {
            "pergunta": "4. Rita Lee esteve entre as cantoras mais censuradas pela Ditadura Militar no Brasil. Verdadeiro ou falso?",
            "opcoes": ["A - Verdadeiro","B - Falso"],
            "resposta": ["A", "A - Verdadeiro"]
        },
        {
            "pergunta": "5. Quais idiomas Rita Lee sabia falar?",
            "opcoes": ["A - Inglês, francês, italiano, castelhano e português", "B - Inglês, francês, alemão, castelhano e português", "C - Inglês, italiano, japonês, castelhano e português"],
            "resposta": ["A", "A - Inglês, francês, italiano, castelhano e português"]
        },
        {
            "pergunta": "6. Para qual banda mundialmente conhecida Rita Lee fez o show de abertura?",
            "opcoes": ["A - David Bowie", "B - The Rolling Stones"],
            "resposta": ["B", "B - The Rolling Stones"]
        },
        {
            "pergunta": "7. Por qual motivo Rita Lee foi excomungada pela igreja católica?",
            "opcoes": ["A - Pelo lançamento do álbum ‘Santa Rita de Sampa’", "B - Por usar um figurino parecido ao de Nossa Senhora Aparecida em show", "C - Pelas críticas às interpretações bíblicas em entrevistas"],
            "resposta": ["B", "B - Por usar um figurino parecido ao de Nossa Senhora Aparecida em show"]
        },
        {
            "pergunta": "8. Qual desses clássicos mais encantou Rita Lee na infância?",
            "opcoes": ["A - Alice no País das Maravilhas", "B - Pinocchio", "C - Peter Pan"],
            "resposta": ["C", "C - Peter Pan"]
        },
        {
            "pergunta": "9. Qual figurino Rita Lee usou no icônico show no Maracanãzinho em 1968?",
            "opcoes": ["A - Vestido de Bruxa", "B - Vestido de Noiva", "C - Macacão estrelado"],
            "resposta": ["B", "B - Vestido de Noiva"]
        },
        {
            "pergunta": "10. Em 1975, Rita Lee desafiou o rock machista com um álbum cor-de-rosa e cheio de feminilidade. Esse álbum se chamava:",
            "opcoes": ["A - Babilônia", "B - Flerte Fatal", "C - Fruto Proibido"],
            "resposta": ["C", "C - Fruto Proibido"]
        },
    ]

    print("QUIZ SOBRE A RITA LEE\n")

    score = 0

    for questao in lista_perguntas:
        print(questao["pergunta"])
        
        for opcoes in questao["opcoes"]:
            print(opcoes)
        
        controle = True
        while controle:
            resposta = input("Resposta: ").lower()

            if resposta == questao["resposta"][0].lower():
                print("\n\033[32mResposta correta\033[m 😃\n")

                score += 1
                controle = False

            elif resposta != "a" and resposta != "b" and resposta != "c":
                print("\nOpção inválida! 🤨\n")

            else:
                print("\n\033[31mResposta errada\033[m 😭")
                print(f"\nResposta correta: \033[32m{questao['resposta'][1]}\033[m\n")
                controle = False


    errop = (10 - score) / 10 * 100
    print("\nResultados:")
    if score <= 3:
        print("Vish, não foi dessa vez...\nSeu erro percentual foi de {}%, mas esperamos que você tenha se divertido e descoberto mais sobre nossa Rita Lee!".format(errop))
    
    elif score <= 6:
        print("Uma ovelha negra na família?\nSeu erro percentual foi de {}%.\nEsperamos que você tenha aprendido coisas novas sobre nossa Rita Lee!".format(errop))
    
    elif score <= 9:
        print("Parabéns, você é um(a) superfã da Rita Lee!\nSeu erro percentual foi de apenas {}%!".format(errop))
    
    else:
        print("Parabéns, pelo visto seus conhecimentos sobre a Rita não deixam a desejar em nada!\nSeu erro percentual foi de {}%".format(errop))

    input("\nDigite qualquer tecla para voltar ao menu inicial...")
    
