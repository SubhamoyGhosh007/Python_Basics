# A program for playing KBC.
questions = [
    ["Who invented FaceBook ?", "Robert Downey JR.", "Lionel Messi", "Ronaldo", "None", "4"],
    ["Who is the Prime Minister of India now ?", "You", "Me", "Modi", "None", "3"],
    ["Who won Shield in 1920?", "Mohun Bagan", "East Bengal", "Mohamedan", "None", "1"],
    ["Who won ISL trophy in 2022?", "Mohun Bagan", "East Bengal", "Mohamedan", "None", "1"],
    ["Who has the record of total highest runs in cricket?", "Virat", "Sachin", "Sehwag", "None", "2"]
]

levels = [100, 200, 300, 400, 500]
currentMoney = 0

givenAnswer = []
masterQuestionIndex = [2 ,4]
masterAnswerInderx = []
print(masterAnswerInderx)
for question in range(0, len(questions)):
    ques = questions[question]
    if question == 2 or question == 4:
        print("It is your master question")
    print(f"Your question for RS {levels[question]} is\n{ques[0]}")
    print(f"1.{ques[1]}\t2.{ques[2]}\t"
          f"3.{ques[3]}\t4.{ques[4]}")
    ch = int(input(f"Enter your choice (1-4) : "))
    givenAnswer.append(ch)
    if ch == int(ques[5]):
        print(f"Congratulations! You have won  RS. {levels[question]}.")
        print("\n")
        currentMoney = currentMoney + levels[question]
        print(f"Current Money is {currentMoney}")
        if question == 2 or question == 4:
            masterAnswerInderx.append(1)
        else:
            masterAnswerInderx.append(0)

    else :
        print(f"OOPS! Wrong Answer.")
        print(f"Correct Answer is options number {ques[5]} : {ques[int(ques[5])]}")

        if question < 2:
            currentMoney = 0
        if 2 < question < 4:
            if masterAnswerInderx[1] == 1:
                currentMoney = levels[2]
            else:
                currentMoney = 0
        print(f"Current Money is {currentMoney}")
        print("\n")
    print(masterAnswerInderx)
print(f"You have won RS {currentMoney}")
print(masterAnswerInderx)
print(masterAnswerInderx[0])
print(masterAnswerInderx)