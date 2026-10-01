import ipywidgets as widgets
from IPython.display import display


# Game variables
current_player = "X"
count = 0
game_over = False

# Winning combinations
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

# Create 9 buttons
buttons = [
    widgets.Button(
        description=" ",
        layout=widgets.Layout(width="80px", height="80px")
    )
    for _ in range(9)
]

# Output area for messages
message = widgets.HTML(value="<h3>Player X's turn</h3>")


def disable_buttons():
    for button in buttons:
        button.disabled = True


def check_winner():
    global game_over

    for a, b, c in winning_combinations:

        if (
            buttons[a].description != " "
            and buttons[a].description == buttons[b].description
            and buttons[b].description == buttons[c].description
        ):
            winner = buttons[a].description

            buttons[a].style.button_color = "lightgreen"
            buttons[b].style.button_color = "lightgreen"
            buttons[c].style.button_color = "lightgreen"

            message.value = f"<h2>🎉 Player {winner} wins!</h2>"

            game_over = True
            disable_buttons()

            return True

    return False


def check_tie():
    global game_over

    if count == 9:
        game_over = True
        message.value = "<h2>It's a tie! 🤝</h2>"
        disable_buttons()


def button_click(index):
    global current_player, count

    if game_over:
        return

    # Make sure the square is empty
    if buttons[index].description != " ":
        return

    # Put X or O
    buttons[index].description = current_player

    count += 1

    # Check winner
    if check_winner():
        return

    # Check tie
    if count == 9:
        check_tie()
        return

    # Change player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    message.value = f"<h3>Player {current_player}'s turn</h3>"


def restart_game(_=None):
    global current_player, count, game_over

    current_player = "X"
    count = 0
    game_over = False

    for button in buttons:
        button.description = " "
        button.disabled = False
        button.style.button_color = None

    message.value = "<h3>Player X's turn</h3>"


# Connect buttons to the click function
for i, button in enumerate(buttons):
    button.on_click(lambda _, i=i: button_click(i))


# Restart button
restart_button = widgets.Button(
    description="Restart",
    button_style="warning",
    layout=widgets.Layout(width="150px", height="40px")
)

restart_button.on_click(restart_game)


# Arrange the Tic Tac Toe board
board = widgets.VBox([
    widgets.HBox(buttons[0:3]),
    widgets.HBox(buttons[3:6]),
    widgets.HBox(buttons[6:9]),
])


# Display the game
display(message)
display(board)
display(restart_button)