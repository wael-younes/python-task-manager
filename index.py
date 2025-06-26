# ///////////////////////////////////////////////////////extract/////////////////////////////////////////////
def extract (tasks : list):
    index=peek(tasks)
    return tasks.pop(index)
# ///////////////////////////////////////////////////////peek/////////////////////////////////////////////
        
def peek (tasks : list):
    if len(tasks)==0:
        return
  
    min_p_index=0
    high_p=tasks[0][0] 
    for i in range(1,len(tasks)):
        if tasks[i][0] < high_p:
            high_p= tasks[i][0]
            min_p_index=i
    return min_p_index
# ///////////////////////////////////////////////////////is empty /////////////////////////////////////////////

def is_empty(tasks:list):
    return len(tasks)==0   


def insert(tasks: list, priority: int, title: str, duration: int):
    task = (priority, title, duration)
    tasks.append(task)
    return tasks
# `complete_next_task`: first method
def comlete_next_task (queue:list):
    index=peek(queue)
    print("The highest priority task is :",queue[index])
    return extract(queue)
    
 #`search_for_task`: second method
def search_for_task(tasks, title):
    title_set = []
    sorted_tasks = sorted(tasks, key=lambda tasks: tasks[1])
    low = 0
    high = len(sorted_tasks) - 1
    found_index = -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_tasks[mid][1] == title:
            found_index = mid
            break
        elif sorted_tasks[mid][1] < title:
            low = mid + 1
        else:
            high = mid - 1
    if found_index != -1:
        i = found_index
        while i >= 0 and sorted_tasks[i][1] == title:
            i -= 1
        i += 1
        while i < len(sorted_tasks) and sorted_tasks[i][1] == title:
            title_set.append(sorted_tasks[i])
            i += 1
        return title_set
    else:
        return "There is no task with title: " + title

# 'sort_tasks' third method
def sort_tasks(tasks : list):
    ascending = sorted(tasks,key=lambda tasks:tasks[2],reverse=False)
    descending =sorted(tasks,key=lambda tasks:tasks[2],reverse=True)
    
    return ascending
 
    # for i in range (len(tasks)):
    #    if tasks[i][1] == title:
    #        set.append(tasks[i])
          
    # if len(set) ==0:
    #     return print("There is no tasks of this title")
    # else:
    #     print("the tasks of title ( "+title+" ) :")
    #     for element in set:
    #            print( element)
      
     


  
t_num=0
task_priority=0
task_title=""
duration=0
tasks=[]
t_num = input("What is the number of tasks? ")
while t_num == "0" or not t_num.isdigit():
    t_num = input("Number of tasks should be 1 or higher. Please enter the correct number of tasks: ")
t_num = int(t_num)

for i in range (t_num):
    task_priority= input(" the priority of task "+ str(i+1)+" is :")
    while not task_priority.isdigit():
        task_priority = input("Priority must be a non-negative integer. Please enter again: ")
    priority_int = int(task_priority)
    
    task_title= input(" the title of task "+str(i+1)+" is :")
    
    duration= input(" the duration of task "+str(i+1)+" is :")
    while not duration.isdigit():
        duration = input("duration must be a non-negative integer. Please enter again: ")
    duration = int(duration)
    tasks=insert(tasks,task_priority,task_title,duration)
    
#for task in tasks:
 #   print(task)    

comlete_next_task(tasks)    
#for task in tasks:
#    print(task) 
title_search=input("what is the task title that you want to search for ? ")
search=search_for_task(tasks,title_search)
for ele in search:
    print(ele)
sorted_tasks=sort_tasks(tasks)
print("the duration assending sort ")
for ele in sorted_tasks:
    print(ele)
