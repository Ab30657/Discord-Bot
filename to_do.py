from replit import db

def add_todo(task):
  if "tasks" in db.keys():
    tasks= db["tasks"]
    tasks.append(task)
    db["tasks"]= tasks
  else:
    db["tasks"]=[task]


def del_todo(index):
  tasks= db["tasks"]
  if len(tasks)>index:
    del tasks[index]
    db["tasks"]=tasks

def get_tasks():
  task=''
  for t in db['tasks']:
      task+="{0}. {1}".format(db['tasks'].index(t)+1,t)+"\n"
  return task

def get_tasks_list():
  return db['tasks']