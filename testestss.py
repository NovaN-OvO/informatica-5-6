elif answer == op:
            streak += 1
            print("Correct!")
            print(f"Streak: {star}")
            if streak == 3:
                break
        else:
            print("Invalid option.")
            break

