

marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input("Enter the number of student: "))):
                name = input("Name: ")
                score = float(input("Score: "))
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1] 

        for a,c in sorted(marksheet):
             if c==b:
                    print("Name of the student having second last grade is: ",a)