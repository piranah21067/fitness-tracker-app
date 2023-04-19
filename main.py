import time
import os
import datetime
print(datetime.date.today())
print("Personalized workout planner: A Python application that creates personalized workout plans based on the user's fitness goals and current fitness level. The tool could also track progress and suggest modifications to the plan. Meal planning : A Python application that generates meal plans and automatically orders groceries for delivery based on the user's dietary preferences and restrictions.")

abs_workout = [ "Figure 8’s",
                "Hands Back Raises",
                "Twisted Pistons",
                "Seated Ab Circles (Clockwise)"
                "Seated Ab Circles (Counter Clockwise)",
                "Scissor V Ups",
                "21” Crunch"]

chest_workout = [ "regular push ups",
                "incline push ups",
                "decline push ups",
                "plyometric push ups"
                "time under tension push ups"]

option=input("enter 1 to get fitness goal enter 2 to track exercise")

if option=="2":
    print("1-lower abs workout")
    print("2-chest workout")
    workout=input("enter your choice here:")
    if workout=="1":
        print("get ready for ")
        for workout in abs_workout:
            print(workout)

        input("Press Enter to Start:")
        for i in range(len(abs_workout)-1):
            for j in range(30):
                print("Keep Doing...")
                print(abs_workout[i])
                print("For" , 30 - j , "seconds")
                time.sleep(1)
                os.system("cls")
                if j==29:
                    print("get ready to switch exercise to")
                    print(abs_workout[i+1])
                    time.sleep(5)
                    os.system("cls")
                    file=open("records.txt","a")
                    record=f"on {datetime.date.today()} completed {abs_workout[i]}\n"
                    file.write(record)
                    file.close()
                    

    elif workout=="2":
            print("get ready for ")
            for workout in chest_workout:
                print(workout)

            input("Press Enter to Start:")
            for i in range(len(chest_workout)-1):
                for j in range(30):
                    print("Keep Doing...")
                    print(chest_workout[i])
                    print("For" , 30 - j , "seconds")
                    time.sleep(1)
                    os.system("cls")
                    if j==29:
                        print("get ready to switch exercise to")
                        print(chest_workout[i+1])
                        time.sleep(5)
                        os.system("cls")
                        file=open("records.txt","a")
                        record=f"on {datetime.date.today()} completed {chest_workout[i]}\n"
                        file.write(record)
                        file.close()
            print("progress saved")

        

print("the fitness goals app is specifically for people ages 18-40")
fitness_goals={
    "build muscle":{
        "exercises":["20 pushups daily","5x10 pullups","4x15 squats","5x12 tricep dips"],
        "diet":[]
    },
    "lose weight":{
        "exercises":["run for 30 mins at pace above 6mph","swimm for 45 mins of breathstroke","5 min intense workout of your choice then 1 min rest interval training", "repeat all steps 3-4 times a week"],
        "diet":["1. Do not skip breakfast, 2. Eat regular meals, 3. Eat plenty of fruit and veg, 5. Drink plenty of water, 6. Eat high fibre foods, 10. Do not stock junk food"]
    }
}
print("which fitness goal would you like to select")


for i in fitness_goals.keys():
    print(i)

choice=input("enter fitness goal here:")



for i,j in fitness_goals.items():
    print(i,j)