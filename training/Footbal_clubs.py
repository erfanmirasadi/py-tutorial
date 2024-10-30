def points_counter():
    # دریافت تعداد بازی‌ها از کاربر
    total_games = int(input("Enter the number of matches: \n"))

    # Variables to accumulate points and count wins, losses, and draws
    total_points = 0
    wins = 0
    losses = 0
    equals = 0

    # Get points for each match
    for game in range(total_games):
        while True:
            points = int(input(f"Enter the points for game number '{game + 1}'\n(0, 1, or 3) or enter '10' for results: \n"))

            # Check if the user entered 10
            if points == 10:
                print(f"Total points: {total_points}")
                print(f"Wins: {wins}")
                print(f"Draws: {equals}")
                print(f"Losses: {losses}")
                return  # Exit the function

            # Check the input and update variables
            if points in [0, 1, 3]:  # Validate input
                total_points += points
                if points == 3:
                    wins = wins + 1
                    
                elif points == 1:
                    equals += 1
                elif points == 0:
                    losses += 1
                break  # Valid input, exit the loop
            else:
                print("Invalid input. Please try again!\n")

    # Print final results
    print(f"Total points: {total_points}")
    print(f"Wins: {wins}")
    print(f"Draws: {equals}")
    print(f"Losses: {losses}")

# Execute the function
points_counter()