scores={} 
scores['10.0']='deepak'                   #assigning a key-value to a Hash
print(scores.items())
result_f=open("RESULTS.txt")
for each_line in result_f:                #identify the design of data in file for multiple assignment
    (name,score)=each_line.split()        #MULTIPLE ASSIGNMENT
    scores[score]=name                    #Insertin KEY-VALUE pair
print("The Results of Drawing Competition are as follows:-")
                                          #iterate through a HASH with the help of FOR loop
for each_line in sorted(scores.keys(),reverse=True): 
    print("%s got the Score: %s"%(scores[each_line],each_line))
                                          #NOTE: remember to sort keys which are numbers and you can call value by scores[key]
    
    
    



