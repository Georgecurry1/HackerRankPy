#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks)
   
  #my answer is below
    avgList = student_marks.get(query_name)
    avg = (avgList[0]+avgList[1]+avgList[2])/3
    formattedAns = f"{avg:.2f}"
    print(formattedAns)
