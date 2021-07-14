value = (14,99,2000,25,65)

def menu():
  global value 
  option = ''
  while(option !=4):
    print('***Tuple Example***')
    print('1.Print Tuple ***')
    print('2.Loop over taple')
    print('3.Copy tuple')
    print('4.Conver tuple to a list')
    print('5.Sort tuple ')
    print('6. Exit ')
    option= int(input('please enter option: '))

    if(option == 1):
      print(value)

    elif(option == 2):
      continue
      
    elif(option == 3):
      start = int(input('Enter start of range: '))
      end = int(input('enter end of range: '))

      newtuple = value[start:end]
      print(newtuple)
    elif(option == 4):
      templist = list(value)
      templist.append(100)
      list(value).append("100")
      print(value)

    elif(option == 5):
      templist = list(value)
      templist.