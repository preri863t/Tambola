import random

def generate_ticket():
    ticket = [[0 for _ in range(9)] for _ in range(3)]

    column_ranges = [
        range(1,10), range(10,20), range(20,30),
        range(30,40), range(40,50), range(50,60),
        range(60,70), range(70,80), range(80,91)
    ]

    for row in range(3):
        cols = random.sample(range(9), 5)
        for col in cols:
            ticket[row][col] = random.choice(column_ranges[col])

    return ticket

def print_ticket(ticket, marked):
    for i in range(3):
        for j in range(9):
            if ticket[i][j] == 0:
                print("   ", end=" ")
            elif marked[i][j]:
                print(" X ", end=" ")
            else:
                print(f"{ticket[i][j]:2d} ", end=" ")
        print()
    print()

def count_marked(ticket, marked):
    count = 0
    for i in range(3):
        for j in range(9):
            if ticket[i][j] != 0 and marked[i][j]:
                count += 1
    return count

def play_game():
    print("Tambola - Early 5")

    num_players = int(input("Enter number of players: "))
    players = []

    for p in range(num_players):
        ticket = generate_ticket()
        marked = [[False for _ in range(9)] for _ in range(3)]
        players.append({
            "ticket": ticket,
            "marked": marked
        })

        print(f"\nPlayer {p+1} Ticket:")
        print_ticket(ticket, marked)

    called_numbers = []

    print("\nStart calling numbers (1-90). Type 0 to stop.")

    while True:
        number = int(input("\nCall a number: "))

        if number == 0:
            print("Game Stopped.")
            break

        if number < 1 or number > 90:
            print("Invalid number! Enter between 1 and 90.")
            continue

        if number in called_numbers:
            print("Number already called!")
            continue

        called_numbers.append(number)

        for idx, player in enumerate(players):
            ticket = player["ticket"]
            marked = player["marked"]

            for i in range(3):
                for j in range(9):
                    if ticket[i][j] == number:
                        marked[i][j] = True

            if count_marked(ticket, marked) >= 5:
                print(f"\nPlayer {idx+1} WINS EARLY 5!")
                print("\nWinning Ticket:")
                print_ticket(ticket, marked)
                print("Game Over!")
                return

play_game()
