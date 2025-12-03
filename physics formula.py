print("Choose a physics formula to calculate:")
print("a → Formula 1 (Speed = Distance / Time)")
print("b → Formula 2 (Force = Mass × Acceleration)")
print("c → Formula 3 (Work Done = Force × Distance)")
print("d → Formula 4 (Pressure = Force / Area)")
print("e → Formula 5 (Density = Mass / Volume)")

choice = input("Enter your choice (a, b, c, d, e): ").lower()

if choice == "a":
    print("Formula 1: Speed = Distance / Time")
    elif choice == "b":
        print("Formula 2: Force = Mass × Acceleration")
        elif choice == "c":
            print("Formula 3: Work Done = Force × Distance")
            elif choice == "d":
                print("Formula 4: Pressure = Force / Area")
                elif choice == "e":
                    print("Formula 5: Density = Mass / Volume")
                    else:
                        print("Invalid choice. Please choose from a–e.")