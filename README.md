## Exercícios de fixação para Busca em espaço de estados


1. Dados uma bica d`agua, um jarro de capacidade 3 litros e um jarro de capacidade 4 litros (ambos vazios). Como obter 2 litros no jarro de 4?
    1. Formalizar o problema e apresentar espaço de estados;
    2. Desenhar busca em largura;
    3. Desenhar busca em profundidade;
    4. Desenhar busca com aprofundamento iterativo;
    5. Como a busca bidirecional funcionaria? 
2. Um caixeiro viajante deve visitar uma lista de cidades, exatamente uma vez cada uma delas. As cidades da lista são todas interconectadas (voo direto entre elas). O problema é encontrar o circuito mais curto que tem início e término em qualquer uma das cidades.”
    1. Formalizar o problema
    2. Escrever um algoritmo para o problema
    3. Implementar uma solução
    4. Dado o seguinte jogo: Quatro fileiras de palitos de dente com 1,3,5,7 palitos cada.

3. Formalize um jogo para ele da seguinte maneira
    1. Cada jogador pode retirar qualquer quantidade de palitos de uma das fileiras. 
    2. Perde quem fica com o último palito.
    3. Desenhe uma Busca MinMax para ele.
```
                    I
                   III
                  IIIII
                 IIIIIII
```

### Respostas
1.
    1. x = litros no jarro de 4 litros
    y = litros no jarro de 3 litros
    Espaço de estados = (x, y) tal que x está em {0, 1, 2, 3, 4}, y está em {1, 2, 3}