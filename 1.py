print("============================")
print("       lets go picnic!      ")
print("============================")
print()

print("step 1:pick your snack")
print("1 - kitcat ")
print("2 - oreo ")
print()

choice = int(input("enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2:pick flavor")
    print(" 1 - matcha")
    print(" 2 - original")
    print()

    bike_type = int(input("enter 1 or 2: "))
    print()

    if bike_type==1:
        print("u piked   : matcha flavor")
        print("taste : good for me")
        print("best with  : chocolet milk")
    else:
        print("u piked   : original")
        print("taste : good")
        print("best with  : milk")

elif choice == 2:
    print("step 2: pick the flavor")
    print(" 1 - original")
    print(" 2 - mint")
    print()

    ct=int(input("enter 1 or 2: "))
    print()

    if ct==1:
        print("u picked : original")
        print("tastes : great")
        print("best with: milk")

    else:
         print("u picked mint")
         print("tastes : good")
         print("best with: milk")
else:
        print("that was not a valid choice.")
        print("pls enter 1or 2.")
print()
print("========================")
print(" ok snack set!! lets go ")
print("========================")