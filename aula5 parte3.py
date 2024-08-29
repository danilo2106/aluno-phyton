nome_ususario = input("enter username:")
print("olá,"+ nome_ususario + "como voce esta")
print("SENAC ARSENAL...")
print("vamos jogar um jogo?")
while True:
    resposta=input("voce quer continuar?(sim/nao)").strip().lower()
    if resposta =="sim":
        print("voce escolheu continuar")
        break
    elif resposta == "nao":
        print('quer continuar')
        
print("qual e o nome da namorada do mikey mouse?")
print("pateta mouse\n minie mouse\n ana mouse\n")
mone = input("resposta/")
if mone == ("minie mouse"):
 print("voce acertou")
if mone == ("pateta mouse"):
     print("voce errou")
if mone == ("ana mouse"):
    print("voce errou")