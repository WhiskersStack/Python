# Ex5 Lab Safety Checklist

print("\nEx5 Lab Safety Checklist\n")

temp = int(input("Enter the temperature : \n"))
pressure = int(input("Enter the pressure : \n"))
voltage = int(input("Enter the voltage : \n"))

if (temp > 20 and temp < 80) and (pressure < 50) and (voltage > 200 and voltage < 250):
    print("\nSafe to work")
else:
    print("\nNot safe to work")

