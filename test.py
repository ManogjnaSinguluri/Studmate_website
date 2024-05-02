import sys
import copy
dailyv=[]
def validate(slots,tasks,times,completed_tasks):
  check=0
  for l in tasks:
    check=check+sum(l)
  if check==0:
    for i in range(len(times)):
      for j in range(len(times[i])):
        if times[i][j]<=completed_tasks[i][j]:
          return False
    return True
  return False
def arrange(slots_c,task_names,tasks,times,completed_tasks,d,curr_d,curr_s):
  global dailyv
  slots = copy.deepcopy(slots_c)
  if curr_d>=3:
    if validate(slots,tasks,times,completed_tasks):
      dailyv.append([slots,d])
  elif curr_s>=3:
    arrange(slots,task_names,tasks,times,completed_tasks,d,curr_d+1,0)
  else:
    if slots[curr_d][curr_s]=="":
      for i in range(len(tasks)):
        for j in range(len(tasks[i])):
          c=1
          if curr_s==1 and tasks[i][j]<2:
              c=0
          if c==1 and tasks[i][j]>0:
            slots_1 = []
            for row in slots:
              slots_1.append(copy.deepcopy(row))
            tasks_c = []
            for row in tasks:
              tasks_c.append(copy.deepcopy(row))
            completed_tasks_c = []
            for row in completed_tasks:
              completed_tasks_c.append(copy.deepcopy(row))
            tasks_c[i][j]=tasks_c[i][j]-1
            if curr_s==1:
                tasks_c[i][j]=tasks_c[i][j]-1
            slots_1[curr_d][curr_s]=task_names[i][j]
            if tasks_c[i][j]==0:
              completed_tasks_c[i][j]=curr_d
            arrange(slots_1,task_names,tasks_c,times,completed_tasks_c,d,curr_d,curr_s+1)
    arrange(slots,task_names,tasks,times,completed_tasks,d,curr_d,curr_s+1)
def daily(slots_c,task_names,tasks,times,completed_tasks,daily_t,i,d):
  slots = copy.deepcopy(slots_c)
  if i==3:
    arrange(slots,task_names,tasks,times,completed_tasks,d,0,0)
  if i<3:
    daily(slots,task_names,tasks,times,completed_tasks,daily_t,i+1,d)
    slots1=[]
    for k in range(len(slots)):
      sl=[]
      for j in range(len(slots[k])):
        sl.append(slots[k][j])
      slots1.append(sl)
    slots1[i][2]=daily_t
    daily(slots1,task_names,tasks,times,completed_tasks,daily_t,i+1,d+1)
  return
def divide(s):
    r=[]
    a=""
    for i in range(len(s)):
        if s[i]==",":
            if len(a)==1:
              r.append(int(a))
            else:
              r.append(a)
            a=""
        else:
            a=a+s[i]
    if len(a)==1:
      r.append(int(a))
    else:
      r.append(a)
    return r
slots=[["","",""]]*3
tasks_names=[divide(sys.argv[1])]
tasks=[divide(sys.argv[2])]
times=[divide(sys.argv[3])]
tasks_names.append(divide(sys.argv[4]))
tasks.append(divide(sys.argv[5]))
times.append(divide(sys.argv[6]))
completed=[["5"]*len(times[0])]
completed.append((["5"]*len(times[1])))
daily_t=sys.argv[7]
daily(slots,tasks_names,tasks,times,completed,daily_t,0,0)
dailyv.sort(key=lambda x:x[1])
sl=dailyv[-1][0]
print("Today"+" :")
if(sl[0][0]!=""):
  print("6:30-7:30 PM :"+sl[0][0])
else:
  print("6:30-7:30 PM :"+"complete other works")
if(sl[0][1]!=""):
  print("7:30-8:30 PM :"+sl[0][1])
else:
  print("7:30-8:30 PM :"+"complete other works")

if(sl[0][2]!=""):
  print("9:30-10:30 PM:"+sl[0][2])
else:
  print("9:30-10:30 PM:"+"complete other works")
if(sl[0][1]!=""):
  print("6:30-7:30 AM:"+sl[0][1])
else:
  print("6:30-7:30 AM:"+"complete other works")
print()
print()
print("Tomorrow"+" :")
if(sl[1][0]!=""):
  print("6:30-7:30 PM :"+sl[1][0])
else:
  print("6:30-7:30 PM :"+"complete other works")
if(sl[1][1]!=""):
  print("7:30-8:30 PM :"+sl[1][1])
else:
  print("7:30-8:30 PM :"+"complete other works")

if(sl[1][2]!=""):
  print("9:30-10:30 PM:"+sl[1][2])
else:
  print("9:30-10:30 PM:"+"complete other works")
if(sl[1][1]!=""):
  print("6:30-7:30 AM:"+sl[1][1])
else:
  print("6:30-7:30 AM:"+"complete other works")
print()
print()
print("Day after tomorrow"+" :")
if(sl[2][0]!=""):
  print("6:30-7:30 PM :"+sl[2][0])
else:
  print("6:30-7:30 PM :"+"complete other works")
if(sl[2][1]!=""):
  print("7:30-8:30 PM :"+sl[2][1])
else:
  print("7:30-8:30 PM :"+"complete other works")

if(sl[2][2]!=""):
  print("9:30-10:30 PM:"+sl[2][2])
else:
  print("9:30-10:30 PM:"+"complete other works")
if(sl[2][1]!=""):
  print("6:30-7:30 AM:"+sl[2][1])
else:
  print("6:30-7:30 AM:"+"complete other works")