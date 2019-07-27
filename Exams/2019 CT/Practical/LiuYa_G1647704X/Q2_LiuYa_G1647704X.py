'''
people = [{"name": None,"age": 10,"hobbies": None},
          {"name": None,"age": 20,"hobbies": None},
          {"name": None,"age": 50,"hobbies": None},
          {"name": None,"age": 51,"hobbies": None}]
'''

#Task 2.1
for i in range(len(people)):
    swap = False
    for j in range(i):
        if people[j]["age"] < people[j-1]["age"]:
            people[j], people[j-1] = people[j-1], people[j]
            swap = True 
    if swap == False:
        break
#print(people)

#Task 2.2 
age_group = ["<10","[10-19]","[20-29]","30-39]","[40-49]","[50-59]","[60-69]",">=70"]
for i in range(8):
    count = 0
    for j in range(len(people)):
        if people[j]["age"] >= 10*(i) and people[j]["age"] < 10*(i+1):
            count += 1
    print('{:<7}'.format(age_group[i]) + ":" + str(count))
