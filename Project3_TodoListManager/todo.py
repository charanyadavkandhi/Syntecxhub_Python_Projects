import json,os
F='tasks.json'
def load():
    return json.load(open(F)) if os.path.exists(F) else []
def save(t): json.dump(t,open(F,'w'),indent=2)
tasks=load()
while True:
    print("\n1.Add 2.View 3.Done 4.Delete 5.Exit")
    c=input("Choice: ")
    if c=='1':
        tasks.append({'task':input('Task: '),'done':False}); save(tasks)
    elif c=='2':
        [print(i+1,'[✓]' if x['done'] else '[ ]',x['task']) for i,x in enumerate(tasks)]
    elif c=='3':
        i=int(input('No: '))-1
        if 0<=i<len(tasks): tasks[i]['done']=True; save(tasks)
    elif c=='4':
        i=int(input('No: '))-1
        if 0<=i<len(tasks): tasks.pop(i); save(tasks)
    else: break
