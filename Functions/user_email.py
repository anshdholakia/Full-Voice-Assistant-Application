#Email Function
#Purpose: Also the user to send an email through two different gmail accounts
#Version: Python 3.9
#02-23-2021
#Shravya Bingi, Ansh Dholakia 
#Dependencies: yagmail, keyring, and getpass modules, main.py


#This needs to be gmail emails 

#See if the user's email is already stored, if not prompt the user to enter their email
def ask_email():
      try:
          f = open("email.txt", "r+")
          email = f.read()
          f.close()

      except:
          print("I don't have your email, can I have it? Please make sure that it is a gmail")
          email = input("Enter your email: ")
          while((email == "") or (email == None) or (not email.endswith("@gmail.com")) or (email.i.salnum) ): 
            email = input("Please enter your gmail in the proper format (username@gmail.com): ")
            email = email.strip       
            f = open("email.txt", "x")
            f.close()
            g = open("email.txt", "w")
            g.write(email)
            g.close()
            print("Thank you")
      return email

#Function to change the email
def change_email(new_email):
      while(new_email == "" or new_email == None):
            new_email = input("Can I have your email: ")
      f = open("email.txt","r+")
      f.write(f"{new_email}")
      print("Sucessfully changed")
      f.close()
      return new_email

#Gather input from user
def send_email():
      import yagmail, keyring, getpass
      receiver_email = input("Enter the email you want to send it to:")
      body = input("Enter the body that you want to send:")
      subject_user = input("Enter the subject for your email:")

      e = open("email.txt", "r")
      yag = yagmail.SMTP(e.read())

      #send the email 
      try:
            password = getpass.getpass("Enter your password:")
            keyring.set_password("system", f"{e.read()}", f"{password}")
            yag.send(
                  to = receiver_email,
                  subject = subject_user,
                  content = body )

      except Exception as f:
            print(f"Please allow less secure apps to ON by changing your gmail settings. Error{f}")
            
      e.close()
            

ask_email()
