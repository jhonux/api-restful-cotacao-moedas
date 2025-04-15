API de Cotação de Moedas
Esta é uma API simples desenvolvida com Flask que consulta cotações de moedas em tempo real e permite o registro de cotações manuais em cache. A API oferece endpoints para buscar cotações de moedas, registrar cotações manuais e visualizar um histórico de cotações.

Funcionalidades
A API oferece os seguintes endpoints:

1. GET /cotacao
Esse endpoint retorna a cotação atual de uma moeda em relação ao Real. Ele consulta uma API externa e retorna os valores para a moeda especificada.

URL: /cotacao

Método HTTP: GET

Parâmetros:

base: Moeda de origem (opcional, padrão: EUR)

symbols: Moeda de destino (opcional, padrão: BRL).
