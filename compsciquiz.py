import time
score = 0
optionstext = "\nHit 'a', 'b', 'c' or 'd' for your answer: "
nextquestion = "\nNext question..."
ranoutofattempts = "\nIncorrect, you ran out of attempts."
question1 = "\nQuestion 1. What does IP stand for?"
options1 = "\na. Internet Program\nb. Instant Protocol\nc. Internet Policy\nd. Internet Protocol."
correct = "\nWell done, you were correct."
question2 = "\nQuestion 2. Cloud services is an exmaple of ?"
options2 = "\na. Local Hosting\nb. Domain Name Servers\nc. Online Storage\nd. URL"
question3 = "\n"
options3 = "\n"
question4 = "\n"
options4 = "\n"
question5 = "\n"
options5 = "\n"
question6 = "\n"
options6 = "\n"
question7 = "\n"
options7 = "\n"
question8 = "\n"
options8 = "\n"
question9 = "\n"
options9 = "\n"
question10 = "\n"
options10 = "\n"
wait_time = 2

def updatescore():
    global score
    score = score + 1
    print("\nYour current score is", score)

def printscore():
    global score
    print("\nYour current score is", score)

x = True
while x == True: #While x is true run the loop
    print("Welcome to the Internet Technologies Quiz!")
    time.sleep(1)
    start_response = input("\nPlease enter 'yes' to start the quiz: ")
    if start_response == "yes": # If 'yes' is entered the quiz will start
        x = False
        time.sleep(wait_time)
        print("\nStarting the quiz...")
        time.sleep(wait_time)
        print(question1)
        time.sleep(wait_time)
        print(options1)
        time.sleep(wait_time)
        response = input(optionstext)
        time.sleep(wait_time)
        if response == "d":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question1)
            time.sleep(wait_time)
            print(options1)
            time.sleep(wait_time)
            retake_response_1 = input(optionstext)
            time.sleep(wait_time)
            if retake_response_1 == "d":
                print(correct)
                time.sleep(wait_time)
                updatescore
            else:
                print("\nIncorrect, IP stands for Internet Protocol.")
                time.sleep(wait_time)
                printscore()

        #question 2
        time.sleep(wait_time)
        print(question2)
        time.sleep(wait_time)
        print(options2)
        time.sleep(wait_time)
        response1 = input(optionstext)
        time.sleep(wait_time)
        if response1 == "c":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question2)
            time.sleep(wait_time)
            print(options2)
            time.sleep(wait_time)
            retake_response_2 = input(optionstext)
            time.sleep(wait_time)
            if retake_response_2 == "c":
                print(correct)
                time.sleep(wait_time)
                updatescore
            else:
                print("\nIncorrect, Cloud Storage is an example of Cloud Storage.")
                time.sleep(wait_time)
                printscore()

        #question 3
        time.sleep(wait_time)
        print(question3)
        time.sleep(wait_time)
        print(options3)
        time.sleep(wait_time)
        response2 = input(optionstext)
        time.sleep(wait_time)
        if response2 == "":
            print(correct)
            updatescore()
        else:
            print(question3)
            time.sleep(wait_time)
            print(options3)
            time.sleep(wait_time)
            retake_response_3 = input(optionstext)
            time.sleep(wait_time)
            if retake_response_3 == "":
                print(correct)
                time.sleep(wait_time)
                updatescore()
            else:
                print("\nIncorrect,")
                time.sleep(wait_time)
                printscore()
        
        #question 4
        time.sleep(wait_time)
        print(question4)
        time.sleep(wait_time)
        print(options4)
        time.sleep(wait_time)
        response3 = input(optionstext)
        time.sleep(wait_time)
        if response3 == "":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question4)
            time.sleep(wait_time)
            print(options4)
            time.sleep(wait_time)
            retake_response4 = input(optionstext)
            time.sleep(wait_time)
            if retake_response4 == "":
                print(correct)
                time.sleep(wait_time)
                updatescore()
            else:
                print("\nIncorrect,")
                time.sleep(wait_time)
                printscore()
        
        #question 5
        time.sleep(wait_time)
        print(question5)
        time.sleep(wait_time)
        print(options5)
        time.sleep(wait_time)
        response4 = input(optionstext)
        time.sleep(wait_time)
        if response4 == "":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question5)
            time.sleep(wait_time)
            print(options5)
            time.sleep(wait_time)
            retake_response5 = input(optionstext)
            time.sleep(wait_time)
            if retake_response5 == "":
                print(correct)
                time.sleep(wait_time)
                updatescore()
            else:
                print("\nIncorrect,")
                time.sleep(wait_time)
                printscore()

        #question 6
        time.sleep(wait_time)
        print(question6)
        time.sleep(wait_time)
        print(options6)
        time.sleep(wait_time)
        response5 = input(optionstext)
        time.sleep(wait_time)
        if response5 == "":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question6)
            time.sleep(wait_time)
            print(options6)
            time.sleep(wait_time)
            retake_response6 = input(optionstext)
            time.sleep(wait_time)
            if retake_response6 == "":
                print(correct)
                time.sleep(wait_time)
                updatescore()
            else:
                print("\nIncorrect,")
                time.sleep(wait_time)
                printscore()

        #question 7
        time.sleep(wait_time)
        print(question7)
        time.sleep(wait_time)
        print(options7)
        time.sleep(wait_time)
        response6 = input(optionstext)
        time.sleep(wait_time)
        if response6 == "":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question7)
            time.sleep(wait_time)
            print(options7)
            time.sleep(wait_time)
            retake_response7 = input(optionstext)
            time.sleep(wait_time)
            if retake_response7 == "":
                print(correct)
                time.sleep(wait_time)
                updatescore()
            else:
                print("\nIncorrect,")
                time.sleep(wait_time)
                printscore()

        #question 8
        time.sleep(wait_time)
        print(question8)
        time.sleep(wait_time)
        print(options8)
        time.sleep(wait_time)
        response7 = input(optionstext)
        time.sleep(wait_time)
        if response7 == "":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question8)
            time.sleep(wait_time)
            print(options8)
            time.sleep(wait_time)
            retake_response7 = input(optionstext)
            time.sleep(wait_time)
            if retake_response7 == "":
                print(correct)
                time.sleep(wait_time)
                updatescore()
            else:
                print("\nIncorrect,")
                time.sleep(wait_time)
                printscore()

        #question 9
        time.sleep(wait_time)
        print(question9)
        time.sleep(wait_time)
        print(options9)
        time.sleep(wait_time)
        response8 = input(optionstext)
        time.sleep(wait_time)
        if response8 == "":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question9)
            time.sleep(wait_time)
            print(options9)
            time.sleep(wait_time)
            retake_response8 = input(optionstext)
            time.sleep(wait_time)
            if retake_response8 == "":
                print(correct)
                time.sleep(wait_time)
                updatescore()
            else:
                print("\nIncorrect,")
                time.sleep(wait_time)
                printscore()

        #question 10
        time.sleep(wait_time)
        print(question10)
        time.sleep(wait_time)
        print(options10)
        time.sleep(wait_time)
        response10 = input(optionstext)
        time.sleep(wait_time)
        if response10 == "":
            print(correct)
            time.sleep(wait_time)
            updatescore()
        else:
            print(question10)
            time.sleep(wait_time)
            print(options10)
            time.sleep(wait_time)
            retake_response9 = input(optionstext)
            time.sleep(wait_time)
            if retake_response9 == "":
                print(correct)
                time.sleep(wait_time)
                updatescore()
            else:
                print("\nIncorrect,")
                time.sleep(wait_time)
                printscore()

        time.sleep(1)
        printscore()
        time.sleep(1)
        print("\nThank you for playing the Internet Technologies quiz!")
        
    else: # If 'yes' isn't entered
        print(" ")
        x = True