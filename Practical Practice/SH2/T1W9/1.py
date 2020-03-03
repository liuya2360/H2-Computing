#Task 1.1
def ReadLog():
    with open("WEBLOG.txt") as f:
        lines = f.read()
    lines = lines.strip().split("\n")
    summary = {}
    for row in lines:
        row = row.strip().split("|")
        client_add = row[0]
        date = row[1].strip().split(":")[0]
        if client_add in summary.keys():
            if date not in summary[client_add].keys(): 
                summary[client_add][date] = 1
            else:
                summary[client_add][date] += 1
        else:
            summary[client_add]= {date: 1}  
    return summary 


#Task 1.2 
def ProcessLog(summary):
    with open("SUMMARY.txt", "w") as f:
        for client_add in summary.keys():
            temp = ""
            temp = "{:20}{}\n".format(client_add, ",".join(summary[client_add].keys()))
            f.write(temp)
            
    #Task 1.3
    highest_freq_client_add = []
    highest_freq = -1 
    for client_add in summary.keys():
        for date in summary[client_add].keys():
            if summary[client_add][date] > highest_freq:
                highest_freq = summary[client_add][date]
                highest_freq_client_add = [client_add]
            elif summary[client_add][date] == highest_freq:
                highest_freq.client_add.append(client_add)
    print("Highest frequency (days): "+str(highest_freq))
    print("Accessed by:")
    for client_add in highest_freq_client_add:
        print(client_add) 
    
result = ReadLog()
ProcessLog(result)
