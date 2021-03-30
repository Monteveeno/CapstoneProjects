
# I want to open the file in user text
file = open("user.txt",'r')

# I want to assign the login as false
login = False

# I want the user tp enter the username and password and it should match the txt file
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# I want to the code to find the username and password
for line in file:
    split_line = line.split("\n")
    user_check = split_line[0].strip()
    pass_check = split_line[0].strip()
    if username == user_check and password == pass_check:
        login_success = True
        break

# I want the menu to show
# If the user name and passowrd does not match i want it to say it is incorrect
valid_option= ""
admin_options =""
if username == 'admin':
    admin_options = "r - register user\nds- display statistics\ngr- register user"
else:
    print("username or password maybe incorrect")
file.close()

# If login is successful as a admin user
# we want the following  options to appear
while login_success:
    valid_option == False
    option = input('\n' + admin_options + "a - add task\nva view all tasks\nvm-view my tasks\ne exit")
    
    if option == "r" and username == "admin":
        valid_option = True
        username2 = input("Please enter a new username: ")
    new_password = input("Please enter a new password: ")   
    password2 = input("To confirm that you have access to change username and password please enter your password: ")
    if password2 == password :
        confirm = open('user.txt', 'a+') 
        confirm.write("\n{}, {}".format(username2, new_password) )
        confirm.close()
    
    if option == "a" and username == "admin":
        valid_option = True
        username2 = input("Please enter the name of the user that the task is assigned to: ")
    title = input("plese enter the title of the task: ")
    due_date = input("please enter the due date of the task: ")
    options = input("was the previous task completed?(yes/no): ")
    confirm = open('tasks.txt', 'a+')
    confirm.write("\n{}, {}, {}, {}".format(username2, title, due_date, options))
    confirm.close()
    
    if option == "va" and username == "admin":
        valid_option = True
        tasks = open('tasks.txt','r',)    
    for x in tasks:
    
        words_in_line = x.split(",")
        print("Task")
        print(words_in_line[2])
    
    if option == "a" and username == "admin":
        valid_option = True
        tasks = open('tasks.txt','r',)    
    for x in tasks:
    
        words_in_line = x.split(",")
        if words_in_line[0] == username:
            print("Task")
            print(words_in_line[2])
    
# We going to def a few options to register a user add task and etc
# I will be modifying register user to also let the user know that the username is taken
# We will also modify all code to what the user needs
while login:
    valid_option = False
    option = input("\n" + admin_options + "a- add task\nva- view all tasks\nvm view all my tasks\ne - exit\nplease select one of the following options: ")
 
task_number = ""
def get_task_line(tasknumber):
    task_file = open("tasks.txt",'r')
    for task_line in task_file:
        task_list = task_line.strip().split(",")
        if int(task_list[6]) == task_number:
            task_file.close()
            return task_line
    
    task_file.close()
    return ""

def register_user():
    new_user = input("please enter your username: ")
    file = open("user.txt","r+")
    for line in file:
        split_line = line.split(",")
        user_check = split_line[0].strip()
        if new_user == user_check:
            print ("The user name is already in use")
    if new_user != user_check:        
        new_password = input("Please enter your password: ")
        new_password == input("confirm password: ")
        file.write("\n" + new_user)
        file.write(new_password)
        file.close()
    else:
        print("Password does not match")
        
def add_task():
    assigned_person = input("Please enter who the task is assigned to: ")
    task_title = input("Please enter the title of task: ")
    task_detail = input("Please enter details of the tasks: ")        
    date_assigned = input("Please input todays date: ")
    task_due = input("Please enter the date the task is due: ")
    complete = input("Is the task comple (yes or no?)")
    file = open("tasks.txt","a")
    file.write("\n",assigned_person,+",",task_title,+",",task_detail,+",",date_assigned,+",",task_due,+",",complete)
    file.close()

def view_all():
    file = open("tasks.txt")
    for line in file:
        task = line.split(",")
        print("Task manager: " + task[0] +"\n" +"Task Subject: "+task[1]+"\n"+"Task details: "+ task[2]+"\n"+"Date issued: "+task[3]+"\n"+"Deadline: "+task[4]+"\n"+"Completed: "+task[5])

def view_mine():
    task_count = 0
    file = open("tasks.txt","r+")
    print("")
    for line in file:
        task = line.split(",")
        if task[0] == username:
            task_count += 1
            print("Task manager: " + task[0] +"\n" +"Task Subject: "+task[1]+"\n"+"Task details: "+ task[2]+"\n"+"Date issued: "+task[3]+"\n"+"Deadline: "+task[4]+"\n"+"Completed: "+task[5])
    
    if task_count == 0:
        print("you have no active tasks.")
        file.close()
    
    if task_count != 0:
        ammend = int(input("Select a task to ammend or press '-1 to return" ))
    
    if ammend == -1:
        print("Thank you have a great day")
        
    line == get_task_line(ammend)
    line_list = line.strip().split(",")
    update_task_line = ""
    
    if line != "":
        choice = input("Would you like yo either:\n(a) mark the task as complete\n(b) mark the task as incomplete\n(c) edit the deadline\n(d) edit the task manager\n: ")
        if choice == 'a':
            update_task_line(ammend,5,"yes")
        if choice == 'b':
            update_task_line(ammend,5,"no")
        if choice == 'c':
            if line_list[5] == 'no':
                new_deadline = input("Please enter a new deadline date: ")
                update_task_line(ammend,4,new_deadline)
            