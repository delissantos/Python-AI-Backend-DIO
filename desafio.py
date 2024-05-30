
saldo = 0.0
saque = 0.0
deposito = 0.0
extrato = ""

limite_depositos = 3
limite_saques = 3

print("    Bem-vindo!\n")
menu_inicial = """Selecione a operação a ser realizada a seguir:\n
    [a] Deposito
    [b] Saque
    [c] Extrato
    [d] Sair
    \n"""

while True:
    
    opcao = input(menu_inicial)

# deposito 

    if opcao == "a" :
        valor_deposito = float(input("\nInsira o valor que deseja depositar:\n"))

        if valor_deposito > 0 and limite_depositos > 0:

            saldo += valor_deposito
            limite_depositos -= 1 
            extrato += f"Deposito R$ {valor_deposito: .2f}\n"
            
            print ("\nDeposito realizado com sucesso!")
            continue

        elif limite_depositos == 0:
             print("Erro na operação: limite de depósitos execido.")

        else: 
             print("Valor invalido.")
            
#saque

    elif opcao == "b": 
        valor_saque = float(input("Insira o valor que deseja sacar:\n"))

        if valor_saque <= 500 and valor_saque <= saldo and limite_saques > 0: 
            
            saldo -= valor_saque
            limite_saques -= 1 
            extrato += f"Saque R$ {valor_saque:.2f}\n"
            
            print ("Saque bem sucedido!")
            
        elif valor_saque > saldo:
                print ("Erro na operação: saldo insuficiente.")
        
        elif valor_saque >= 500:
                print ("Erro na operação: o valor do saque solicitado excede ao limite permitido.")
        
        elif limite_saques == 0:
                print("Erro na operação: limite de saques excedido.")

        else: 
             print("O valor informado é invalido.")
 
 #extrato

    elif opcao == "c": 
        print (f"""  
                            *** EXTRATO ***
            """)
        print (extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        print("**************************************************************")
        
    
    elif opcao == "d":
         print("\nVolte sempre!\n\n")
         break
    
    else:
         print("Opção invalida.\n")
    