

scores=[]
file_handler=open("RESULTS.txt")                # Notice the File Handler which will represent the file(RESULT.txt) throughout our code.It is our File.
for each_line in file_handler:
    (name,score)=each_line.split()
    scores.append(float(score))                 #use float for a decent sort of numbers not strings
scores.sort()                                   #sorts an float array from LOW to HIGH
scores.reverse()                                #reverses the order of array. Instead of reversing we could have used [scores.sort(reverse=true)]
file_handler.close()
print("RESULTS OF SURFATHON ARE BEING DECLARED:")
print("1st Score: %f "%(scores[0]))
print("2nd Score: %f "%(scores[1]))
print("3rd Score: %f "%(scores[2]))


