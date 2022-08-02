def Average(n):
    return sum(n) / len(n)



print("""========Calculator========\n""")

print()
print("\nSelect operation.")
print("\n1.Highest Value")
print("2.Lowest value")
print("3.Average Value")
print("4.Filter Even")
print("5.Exit")

while True:
    
    print()
    choice = input("Enter choice(1/2/3/4/5): ")
    
    if choice in ('1', '2', '3', '4', '5'):
    
        if choice == '5':
                
                    print()
                    print("Thank you")
                    print("Have a nice day!\n")
                    break
    
    digit = eval(input('How many digits do you want to input ? : ')) 
    
    n = [int(input('Enter a positive number: ')) for i in range(digit)]
    
    print()
    print("you added :",n )
    
    if choice == '1':
                
                    n.sort()
                    print("Highest value is:", n[-1])
                    
    elif choice == '2':
                
                    n.sort()
                    print("Lowest value is:", *n[:1])
                    
    elif choice == '3':
                
                    average = Average(n)
                    print("Average of the list =", round(average, 2))
                    
    elif choice == '4':
                
                    for num in n:
 
                        # checking condition
                        if num % 2 == 0:
                            print(num, end=" ""is a even number\n")

     
                            
    next = input("Let's check another list? (yes/no): ")
    if next == "no":
        print()
        print("Thank you")
        print("Have a nice day!\n")
        break
        
    
