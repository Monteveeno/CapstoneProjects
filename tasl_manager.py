file = open("user.txt",'r')

login = False

username = input("Please enter your username: ")
password = input("Please enter your password: ")

for line in file:
    split_line = line.split("\n")
    user_check = split_line[0].strip()
    pass_check = split_line[0].strip()
    if username == user_check and password == pass_check:
        login_success = True
        break

choice = ""    
admin_options =""
if username == "admin":
    print("r-    Register user")
    print("nds-  display statistics")
    print("ngr-  generate reports")
    input("choose your choice: ")
else:
    print("Either your password or username was incorrect")

if choice == "r":
    username2 = input("Please enter a new username: ")
    new_password = input("Please enter a new password: ")   
    password2 = input("To confirm that you have access to change username and password please enter your password: ")
    if password == password2 :
        confirm = open('user.txt', 'a+') 
        confirm.write("\n{}, {}".format(username2, new_password) )
        confirm.close()
    choice=""

if choice == "nds":
    tasks = open('tasks.txt','r',)    
    for x in tasks:
    
        words_in_line = x.split(",")
        print("Task")
        print(words_in_line[2])
    
    choice = ''
    
while choice == "ngr":
    tasks = open('tasks.txt','r',)    
    for x in tasks:
    
        words_in_line = x.split(",")
        if words_in_line[0] == username:
            print("Task")
            print(words_in_line[2])
    
    choice = ''
file.close()

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
            