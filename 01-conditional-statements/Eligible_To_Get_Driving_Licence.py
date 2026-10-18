age=int(input("Enter your age: " ))
learner_licence=input("Do you have a learner licence ? (yes/no): ").lower()

if age < 0:
    print("Invalid age!")

elif age >= 18 and learner_licence == "Yes":
    print("Eligible to apply for a driving licence")  

elif learner_licence not in ("yes", "no"):
    print("Invalid learner licence status !")

else :
    print("Not eligible to apply")          