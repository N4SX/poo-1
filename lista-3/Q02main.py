from Q02 import Agenda

agenda = Agenda()
while 1:
   print('\nOpcoes: ')
   print('1 - Armazenar Pessoa')
   print('2 - Remover Pessoa')
   print('3 - Buscar Pessoa')
   print('4 - Imprimir Agenda')
   print('5 - Imprimir Pessoa')
   print('0 - Parar')
   op = input('Opcao: ')
   
   if(op == '0'):
      break
   
   elif(op == '1'):
      nome = input('\nDigite o nome: ')
      idade = input('Digite a idade: ')
      altura = input('Digite a altura: ')
      
      cad = agenda.armazenaPessoa(nome, idade, altura)
      if cad:
         print('Cadastro realizado com sucesso!!')
      else:
         print('não foi possivel cadastrar')
      input('\nDigite uma tecla para continuar!')
      
   elif(op == '2'):
      nome = input('\nDigite o nome: ')
      agenda.removePessoa(nome)
      print('Removido com sucesso !')
      input('\nDigite uma tecla para continuar!')
      
   elif(op == '3'):
      nome = input('\nDigite o nome: ')
      print('Essa pessoa se encontra no INDEX: ', agenda.buscaPessoa(nome))
      input('\nDigite uma tecla para continuar!')
      
   elif(op == '4'):
      agenda.imprimeAgenda()
      input('\nDigite uma tecla para continuar!')
      
   elif(op == '5'):
      nome = input('\nDigite o nome: ')
      agenda.imprimePessoa(nome)
      input('\nDigite uma tecla para continuar!')