num = num2 = contador_soma = contador_produto = soma_produto = soma_total = 0
while True:
	# Opção do usuario:
	opção = int(input('[1] Soma\n[2] Multiplicação\n[3] Divisão\n[4] Subtração\n\nEscolha: '))
	print('-=' * 20)
	print('\n')
	#Se a opção do usuario for 1 (Soma):
	if opção == 1:
		while True: # Enquanto não digitar 0 (breakpoint) pergunte o número e calcule no final
			contador_soma += 1 # Gambiarra 
			num = int(input(f'Digite o {contador_soma}º número: ')) # Pergunta ao usuario um numº
			soma_total += num # Soma todos os números digitados
			if num == 0: # Se número receber 0 saia do loop e calcule a soma
				break
		print(f'A soma total foi: {soma_total}') # Mostra o resultado da soma
	# Se a opção do usuario for 2 (Multiplicação):
	if opção == 2:
		while True: # Enquanto não digitar 0 (breakpoint) pergunte o número e calcule no final
			contador_produto += 1 # Gambiarra
			num = int(input(f'Digite o {contador_produto}º número: ')) # Pergunte ao usuario um numº
			soma_produto += num 
			if num == 0:
				break