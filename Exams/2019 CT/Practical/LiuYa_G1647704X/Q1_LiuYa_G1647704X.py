results = []

#Task 1.1
while True:
        line = input()
        if line == "end":
                break 
        line = line.split(",")
        temp = []
        flag = True
        try:
                name = str(line[0])
                temp.append(name)
        except:
                print("Invalid name entered, please enter again")
                flag = False
        for i in range(4):
                try:
                        mark = int(line[i+1])
                        if mark > 45 and mark % 5 > 2:
                                mark = (mark // 5 + 1) * 5
                        temp.append(mark)
                except:
                        print("Invalid marks entered, please enter again.")
                        flag = False
                        break
        if flag:
                results.append(temp)
                #print(results)

                #Task 1.2
                average = 0
                for i in range(4):
                        average += temp[i+1]
                average = int(round(average/4,0))
                print("Average mark for "+str(temp[0])+" is "+str(average))

#Task 1.3
subjects = ["English","MT","Math","Science"] 
for i in range(4):
        sumMark = 0
        for j in range(len(results)):
                sumMark += results[j][i+1]
        average = int(round(sumMark/len(results), 0))
        print("Average mark for "+subjects[i]+" is "+str(average))

#Task 1.4
for i in range(4):
        highest = 0
        lowest = 0
        for j in range(1, len(results)):
                if results[j][i+1] > results[highest][i+1]:
                        highest = j
                if results[j][i+1] < results[lowest][i+1]:
                        lowest = j
        print(subjects[i]+"(Highest,Lowest): "+results[highest][0]+", "+results[lowest][0]) 
