continueInsertData = "S";
dictDataInsertForUsers = [];
countInterationList = 1;
dictFiltered = [];
idadeLimite = 18;

while(continueInsertData.upper() == "S"):
  dictDataInsertForUsers.append(
      {"nome":input(f"Digite seu {countInterationList}º nome da lista: "), "idade":int(input(f"Digite a {countInterationList}º idade da lista: ")), 
       "cpf":input(f"Digite a {countInterationList}º cpf da lista: ")}
      );
  countInterationList += 1;
  continueInsertData = input("Deseja continuar digite (S/N): ")
for person in dictDataInsertForUsers:
  if(person["idade"] >= idadeLimite):
    dictFiltered.append(person);

print(f"Dicionario com todos as pessoas digitadas:  {dictDataInsertForUsers}")
print(f"Dicionario com somente as pessoal que possuem mais de 18 anos: {dictFiltered}")