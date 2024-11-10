class multiFunctions:

    def EMI():
        bmi=float(input("Enter the BMI Index:"))
        if (bmi < 18.5):
            message = "Underweight"
        elif(bmi < 25):
            message = "Normal"
        elif(bmi < 30):
            message = "Overweight"
        else:
            message = "Very Overweight"
        print(message)
        return message

    def Subfields():
        fields=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in fields:
            print(field)

    def OddEven():
        number=int(input("Enter a number:"))
        if number % 2 == 0:
            print(number, "is Even number")
        else:
            print(number, "is NOT Even number")

    def Eligible():
        gender=input("Your Gender:").lower()
        age=int(input("Your Age:"))
        if gender == "male" and age > 20:
            print("ELIGIBLE")
        elif gender == "female" and age > 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        totalMark=0
        for index in range(1,6):
            mark=int(input(f"Subject{index}="))
            totalMark += mark
        print("Total:", totalMark)
        print("Percentage:", totalMark/5)

    def triangle(self):
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area = self.find_area(height, breadth)
        print("Area of Triangle:", area)
    
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        perimeter = self.find_perimeter(height1, height2, breadth)
        print("Perimeter of Triangle:", perimeter)
        
    def find_area(self, height, breadth):
        print("Area Formula: (Height * Breadth)/2)")
        area = (height * breadth) / 2
        return area
    
    def find_perimeter(self, height1, height2, breadth):
        print("Perimeter Formula: Height1 + Height2 + Breadth")
        perimeter = height1 + height2 + breadth
        return perimeter
