def waitingtime(pr, n, bt, wt):
    wt[0] = 0
    
    for i in range(1,n):
        wt[i] = bt[i-1] + wt[i-1]
        
def tat_time(pr, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
        
def avgtime(pr, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0 
    total_tat = 0
    
    waitingtime(pr, n, bt, wt)
    tat_time(pr, n, bt, wt, tat)
    
    print( "pr Burst time " +
        " Waiting time " +
        " Turn around time")
     
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
                    str(bt[i]) + "\t " +
                    str(wt[i]) + "\t\t " +
                    str(tat[i]))
        
    print("Average Waiting Time = "+ str(total_wt/n))
    print("Average Turn Around Time = "+ str(total_tat/n))
        
if __name__ == "__main__":
    
    print("Enter Process Number: ")
    pr = int(input("Enter Poceess Number:"))
    n = int(pr) 
      
    burst_time = int(input("Enter Burst Time:"))
    arr_time = int(input("Enter Arrival TIme:"))

    avgtime(pr, n, burst_time)  
    
    