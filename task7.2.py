todo=["eat","sleep","play"]
task=(input("enter task"))

def view():
   print(todo)
view()

def add(task):
    todo.append(task)
add(task)
print(todo)

def check(task):
    o=todo.index(task)
check(task)
print(f"{task} is completed")

def rem(task):
    j=todo.index(task)
    todo.remove(task)
rem(task)
print(todo)


