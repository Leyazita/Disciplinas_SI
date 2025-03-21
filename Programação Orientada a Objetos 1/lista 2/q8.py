from random import randint as rd

def generateTicket (lista):
    lista = [rd(1, 3) for i in range(13)]
    return lista

def win(ticket, winningTicket):
    hits = 0
    for i in range(0, 13):
        if ticket[i] == winningTicket[i]:
            hits += 1
    return hits


ticket1 = []
ticket2 = []
ticket3 = []
winningTicket = []

winningTicket = generateTicket(winningTicket)
ticket1 = generateTicket(ticket1)
ticket2 = generateTicket(ticket2)
ticket3 = generateTicket(ticket3)

print("Bilhete premiado:", winningTicket)

if win(ticket1, winningTicket) == 13:
    print("Apostador 1 - Ganhador!")
else:
    print("Apostador 1 | Acertos:", win(ticket1, winningTicket), "| Números:", ticket1)
    
if win(ticket2, winningTicket) == 13:
    print("Apostador 2 - Ganhador!")
else:
    print("Apostador 2 | Acertos:", win(ticket2, winningTicket), "| Números:", ticket2)

if win(ticket3, winningTicket) == 13:
    print("Apostador 3 - Ganhador!")    
else:
    print("Apostador 3 | Acertos:", win(ticket3, winningTicket), "| Números:", ticket3)   