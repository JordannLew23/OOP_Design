import random

print("--------------Welcome 1v1 Game of Basketball!--------------")

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"Player {self.name} (#{self.position})"

class PlayerWithFavoriteColor(Player):
    def __init__(self, name, position, favorite_color):
        self.name = name
        self.position = position
        self.favorite_color = favorite_color

    def __str__(self):
        return f"Player {self.name} ({self.position}) - Favorite Color: {self.favorite_color}"


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        player_list = ", ".join(player.name for player in self.players)
        return f"Team {self.name}: {player_list}"


class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = 0
        self.team2_score = 0

    def score(self, scoring_team, points):
        if scoring_team == self.team1:
            self.team1_score += points
        elif scoring_team == self.team2:
            self.team2_score += points
        else:
            print("Invalid scoring attempt. Team not in the game.")

    def display_score(self):
        print(f"Score: {self.team1.name} {self.team1_score} - {self.team2_score} {self.team2.name}")

    def end_game(self):
        self.display_score()
        if self.team1_score > self.team2_score:
            print(f"{self.team1.name} win!")
        elif self.team1_score < self.team2_score:
            print(f"{self.team2.name} win!")
        else:
            print("It's a tie!")

# Function to get player names from the user
def get_player_info():
    player_name = input("Enter player name: ")

    positions = ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]

    while True:
        # Prompt user to choose a position
        print("Choose a position:")
        for index, position in enumerate(positions, start=1):
            print(f"{index}. {position}")

        player_position_index = input("Enter the number corresponding to the desired position: ")

        try:
            player_position_index = int(player_position_index)
            if 1 <= player_position_index <= len(positions):
                player_position = positions[player_position_index - 1]
                break
            else:
                print("Invalid position number. Please choose a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    favorite_color = input("Enter Player's Favorite Color: ")

    return PlayerWithFavoriteColor(player_name, player_position, favorite_color)


# Get player names from the user
player1 = get_player_info()
player2 = get_player_info()

print(player1)
print(player2)
# Create teams and add players
team1 = Team("Lakers")
team1.add_player(player1)


team2 = Team("Warriors")
team2.add_player(player2)

# Create a game with two teams
basketball_game = Game(team1, team2)

# Simulate the game by scoring points
basketball_game.score(team1,random.randint(2,40))
basketball_game.score(team2,random.randint(2,40))




# End the game and display the winner or tie


basketball_game.end_game()
while True:
    play_again = input("Do you want to play again?  Yes/No: ").lower()
    if play_again == "yes":
        basketball_game.team1_score = 0
        basketball_game.team1_score = 0

        basketball_game.score(team1,random.randint(2,40))
        basketball_game.score(team2,random.randint(2,40))

        basketball_game.display_score()

    elif play_again == "no":
        print("----------Thank you for playing. Goodybye!----------")
        break

    else:
        print("----------Invalid Input! Enter Yes or No----------")
