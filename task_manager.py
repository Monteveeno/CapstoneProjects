#We are opening both user txt and task txt
users = open('user.txt', 'r')
tasks = open('tasks.txt', 'r+')

user_creds = []

#We want to split the string to remove "," and add a space
for x in users:   
    user_creds.append(x) 

#Whem login is false we want the user to give us the password is on the txt file
login = False
print("Welccome to Task Manager")
input_username = input("Please enter your user name: ")
input_password = input("Please enter your password: ")

#If the password is true it should take them to the next line of which is options
#If the file_username or the password does not match the txt file we want the user to keep trying
while login == False:
   for user_cred in user_creds:
       words_in_line = user_cred.split(",")
       file_username = words_in_line[0]
       file_password = words_in_line[1]
       file_password = file_password.replace(" ", "")
       file_password = file_password.replace("\n", "")
       if (input_username == file_username) and (input_password == file_password): 
           login = True
   if login == False:
        print("The file_username or password you have given is incorrect")
        input_username = input("Please re-enter the correct user name: ")
        input_password = input("Please re-enter the correct password: ")

choice = ""
while choice != "e":
    print("please select one of the following options:")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my task")
    if input_username == "admin":
        print("r - register user" )    
        print("s - stats" ) 
    print("e - exit") 
    choice = input("please select a option: ")

# This should bring up the the options menu if the user added the correct password
# And than the option to choose from the menu
  
    
#If choice is r  we want the options below to be chosen
# I have also modified the option so that if the user is admin than they should get the full menu
    password2 = ""
    if  choice == "r":
        username_to_add = input("Please enter a new file_username: ")
        password_to_add = input("Please enter a new password: ")   
        password2 = input("To prove that you have access to change the username and password please enter your password: ")
    if "adm1n" == password2 :
        user_file = open('user.txt', 'a+') 
        user_file.write("\n{}, {}".format(username_to_add, password_to_add) )
        user_file.close()
        choice=""
    
#if the user chooses option a we want to give him this option
    if choice == 'a':
        username_to_add = input("Please enter the name of the user that the task is assigned to: ")
        title = input("plese enter the title of the task: ")
        due_date = input("please enter the due date of the task: ")
        options = input("was the previous task completed?(yes/no): ")
        user_file = open('tasks.txt', 'a+')
        user_file.write("\n{}, {}, {}, {}".format(username_to_add, title, due_date, options))
        user_file.close()
        choice = ""
 
#if the user chooses va we want the following options to be read.
    if choice == "va":
        tasks = open('tasks.txt','r',)    
        for x in tasks:
    
            words_in_line = x.split(",")
            print("Task")
            print(words_in_line[2])
    
        choice = ''

#if the user choose vm we want the following options to be read.
    if choice == "vm":
        tasks = open('tasks.txt','r',)    
        for x in tasks:
    
            words_in_line = x.split(",")
            if words_in_line[0] == file_username:
                print("Task")
                print(words_in_line[2])
    
        choice = ''

    if choice == "e":
        print("Thank you for using the program, hope to see you soon")

tasks.close()