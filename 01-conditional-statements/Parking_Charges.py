hours = int(input("Enter parking hours: "))

if hours <= 0:
    print("Invalid parking hours")

elif hours <= 2:
    print("Parking charge: ₹30")

elif hours <= 5:
    print("Parking charge: ₹60")
    
else:
    print("Parking charge: ₹100")