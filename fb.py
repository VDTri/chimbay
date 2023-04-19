

startnum = input("Enter number: ")

endnum = input("enter number: ")

string  = (startnum + endnum).split()


print(string)

if string[-1] < string[0]:
    print("end number must be larger than start number.")
else:
    for i in range(int(startnum), int(endnum) + 1):
        if int(i) %3 == 0 and int(i)%5 == 0:
            print("FizzBuzz")
        elif int(i)%3 == 0:
            print("Fizz")
        elif int(i) % 5 == 0 :
            print("Buzz")
            
        
