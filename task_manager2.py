#We are opening both user txt and task txt
users = open('user.txt', 'r')
tasks = open('tasks.txt', 'r+')

#We want to split the string to remove "," and add a space
for x in users:    
    words_in_line = x.split()

username = words_in_line[0].replace(",","")

#Whem login is false we want the user to give us the password is on the txt file
login = False
print("Welccome to Task Manager")
user_name1 = input("Please enter your user name: ")
password1 = input("Please enter your password: ")

#If the password is true it should take them to the next line of which is options
#If the username or the password does not match the txt file we want the user to keep trying
while login == False:
   if (user_name1 == username) and (password1 == words_in_line[1]):    
       login = True
       break
   if user_name1 != words_in_line[0]:
        print("The username name you have given is incorrect")
        input("Please re-enter the correct user name: ")
   if password1 != words_in_line[0]:
        print("The password that you have given is incorrect")
        input("Please re-enter the correct password: ")

if login==True:
    
# This should bring up the the options menu if the user added the correct password
# And than the option to choose from the menu

    print("please select ine of the following options:")
    print("r - register user" )
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my task")
    print("au - admin user")
    print("e - exit")      
    choice = input("please select a option: ")
    
#If choice is r  we want the options below to be chosen
while  choice == "r":
    username2 = input("Please enter a new username: ")
    new_password = input("Please enter a new password: ")   
    password2 = input("To confirm that you have access to change username and password please enter your password: ")
    if password1 ==password2 :
        confirm = open('user.txt', 'a+') 
        confirm.write("\n{}, {}".format(username2, new_password) )
        confirm.close()
    choice=""
    
#if the user chooses option a we want to give him this option
while choice == 'a':
    username2 = input("Please enter the name of the user that the task is assigned to: ")
    title = input("plese enter the title of the task: ")
    due_date = input("please enter the due date of the task: ")
    options = input("was the previous task completed?(yes/no): ")
    confirm = open('tasks.txt', 'a+')
    confirm.write("\n{}, {}, {}, {}".format(username2, title, due_date, options))
    confirm.close()
    choice = ""
 
#if the user chooses va we want the following options to be read.
while choice == "va":
    tasks = open('tasks.txt','r',)    
    for x in tasks:
    
        words_in_line = x.split(",")
        print("Task")
        print(words_in_line[2])
    
    choice = ''

#if the user choose vm we want the following options to be read.
while choice == "vm":
    tasks = open('tasks.txt','r',)    
    for x in tasks:
    
        words_in_line = x.split(",")
        if words_in_line[0] == username:
            print("Task")
            print(words_in_line[2])
    
    choice = ''
    
while  choice == "au":
    if username == "admin":
       tasks = open('tasks.txt','r',)
       count_tasks = 0
       for x in tasks:
           count_tasks += 1
           
       users = open('user.txt','r',)
       count_users = 0
       for x in users:
           count_users += 1
       print("This is staticts total tasks is {}, and total users is, {}".format(count_tasks, count_users))
    else:
        print("Sorry you are not the admin user.")
    choice = ""

tasks.close()