import physic
def physic():
    choice = int(input("""
        Please choose which equation:
        1. V = d/t
        2. d = 1/2*(vi + vf)*t
        3. vf = vi + a*t
        4. d = vi*t + 1/2*a*t^2
        5. vf^2 = vi^2 + 2*a*d
        6. d = vf*t - 1/2*a*t^2
        7. Back
    """))

def end():
    check = input("Are you sure (y/n):")
    if check == "y":
        quit()
    else:
        main()

def main():
    choice = int(input("""
        Welcome to the Multi-Calculator!
        Please choose the subject:
        1. Physic
        2. End
    """))

    if choice == 1:
        physic()
    else:
        end()

if __name__ == "__main__":
    main()        