import random

user = int(input("Enter 1 for rock 2 for paper and 3 for scissors "))
computer = random.randint(1, 3)


def select(l):
    """

    :type l: object
    """
    if l == 1:
        return "rock"
    elif l == 2:
        return "paper"
    else:
        return "scissors"


def winner(c, u):
    if (u == 1 and c == 3) or (u == 2 and c == 1) or (u == 3 and c == 2):
        print("Player wins!")
    elif u == c:
        print("Tie")
    else:
        print("Computer Wins!")


print("player:", select(user))
print("computer:", select(computer))

winner(computer, user)
