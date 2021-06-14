def take_name():
      try:
          f = open("names.txt", "r+")
          name = f.read()
          f.close()

      except:
          f = open("names.txt", "x")
          f.close()
          print("I forgot to ask for your name!........ .. ; Can I have your name ?")
          name = input("Enter your name: ")
          while(name == "" or name == None):
            name = input("Can I have your name: ")
          g = open("names.txt", "w")
          g.write(name)
          g.close()
          print("Thank you")
      return name

      
def change_name(new_name):
      while(new_name == "" or new_name == None):
            new_name = input("Can I have your name: ")
      f = open("names.txt","r+")
      f.write(f"{new_name}")
      print("Sucessfully changed")
      f.close()
      return new_name



=======
>>>>>>> 3dec995785cf7dcfb56c9a733ec098064e9684ca
take_name()
