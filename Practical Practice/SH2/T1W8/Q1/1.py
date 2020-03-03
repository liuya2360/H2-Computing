import csv

#Task 1.1
check_1 = False 
while True: 
    print("1. Read file data")
    print("2. Enter additional data")
    print("3. Rank students")
    print("4. Quit program")
    user_input = input()

    #Task 1.2 
    if user_input == "1":
        if check_1: 
            print("Option 1 is not available")
            continue 
        with open("RESULTS.TXT") as f:
            reader = csv.reader(f)
            results = [row for row in reader]
        check_1 = True 

    else:
        if not check_1:
            print("User must choose Option 1 before any other operations")
            continue 
        if user_input == "2":
            while True: 
                nric = input("Please input the Student NRIC: ")
                quiz1 = input("Please input the Quiz 1 Score (max 25)")
                quiz2 = input("Please input the Quiz 2 Score (max 35)")
                quiz3 = input("Please input the Quiz 3 Score (max 50)")
                temp = []
                temp.append(nric)
                temp.append(quiz1)
                temp.append(quiz2)
                temp.append(quiz3)
                with open("RESULTS.TXT", "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(temp) 
                results.append(temp)

                query_end = False 
                while True: 
                    more_data = input("Enter more data?")
                    if more_data.upper() == "N":
                        query_end = True 
                    elif more_data.upper() != "Y":
                        print("Invalid input")
                if query_end:
                    break
        
        if user_input == "4":
            break 

        bubble_sort = True 
        if user_input == "3": 
            #Task 1.3
            agg_results = []
            for row in results:
                temp = []
                temp.append(row[0])
                temp.append(0.2*int(row[1])/25+0.3*int(row[2])/35+0.5*int(row[3])/50)
                agg_results.append(temp)
                
            #bubble sort
            if bubble_sort: 
                for i in range(len(agg_results)):
                    swap = False
                    for j in range(len(agg_results)-i-1):
                        if agg_results[j][1] < agg_results[j+1][1]:
                            agg_results[j], agg_results[j+1] = agg_results[j+1], agg_results[j]
                            swap = True
                    if not swap:
                        break
            else: 
                #Task 1.4 (insertion sort)  
                pass

            for i in range(len(agg_results)):
                print("{:
                      6}{}  {:.2%}".format(str(i+1)+":", agg_results[i][0], agg_results[i][1]))
