def feet_into_inches(feet):
    return feet * 12
def inches_into_cm(inches):
    return inches * 2.54

feet = float(input("Enter height in feet: "))
inches = float(input("Enter height in inches: "))
Total_Inches = feet_into_inches(feet) + inches
Total_Cm = inches_into_cm(Total_Inches)
print(f"Total height in centimeters: {Total_Cm} cm")