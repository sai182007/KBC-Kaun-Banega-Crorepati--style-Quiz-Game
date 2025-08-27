# q=["how many days are there in a week?","how many days are there in a year?","what is the capital of India","lucknow is located in which state?","when did jaliya wala bagh kand happened?"]
# ans=[7,365,"new delhi","uttar pradesh",1919]
# amt=0
# user_input=0
# types=[int,int,str,str,int]
# for i in range(0,5):
#     print(q[i])
#     user_input=input("answer the above question: ")
#     a=types[i](user_input)
#     if a == ans[i]:
#         print("correct answer!!!")
#         amt=amt+1000
#         i=i+1
#     else:
#         print("you lose!, you'll win nothing, fuck off!!!")
#         break
# print(f"you won {amt} ruppees")


Questions=[["how many days are there in a week?",1,3,5,7],
           ["what is the capital of india?","new delhi","lucknow","mumbai","none"],
           ["how many days are there in a year?",300,365,100,265],
           ["when was jaliya wala bagh kand happened?",1900,1928,1919,1899],
           ["when is new year celebrated?","1 jan","2 jan","3 jan","4 jan"],
           ["which city is known as city of actors?","lucknow","mumbai","nepal","jaipur"]]
ans=[4,1,2,3,1,2]
level=[1000,3000,5000,10000,20000,40000]
money=0
for i in range(0,len(Questions)):
    question=Questions[i]
    print("----------------------------------------------------------------------")
    print(f"question for ruppees {level[i]} is: ")
    print("----------------------------------------------------------------------")
    print(f"==> {question[0]}")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    reply=int(input("enter your choice between 1-4 here: "))
    if reply == ans[i]:
        print(f"you won {level[i]} ruppees!!!")
        money=money+level[i]
    else:
        print("wrong answer!!!, you lose")
        print(f"you will take {money} ruppees with you, byi byi")
        break