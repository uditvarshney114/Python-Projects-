import random

CHOICES = {1: "Stone", 2: "Paper", 3: "Scissors"}

WINS_AGAINST = {
    "Stone":    "Scissors",
    "Scissors": "Paper",
    "Paper":    "Stone",
}

SCORES = {"player": 0, "computer": 0, "draws": 0}


# ── Game Logic ────────────────────────────────────────────────────────────────

def get_computer_choice() -> str:
    """Return a random choice for the computer."""
    return random.choice(list(CHOICES.values()))


def determine_winner(player: str, computer: str) -> str:
    """
    Compare player and computer choices.
    Returns 'player', 'computer', or 'draw'.
    """
    if player == computer:
        return "draw"
    elif WINS_AGAINST[player] == computer:
        return "player"
    else:
        return "computer"


def display_result(player: str, computer: str, result: str) -> None:
    """Print a formatted round summary and update the scoreboard."""
    print("\n" + "─" * 36)
    print(f"  You chose   : {player}")
    print(f"  Computer    : {computer}")
    print("─" * 36)

    if result == "draw":
        print("  🤝  It's a Draw!")
        SCORES["draws"] += 1
    elif result == "player":
        print("  🎉  You Win this round!")
        SCORES["player"] += 1
    else:
        print("  💻  Computer Wins this round!")
        SCORES["computer"] += 1

    print("─" * 36)


def play_round() -> None:
    """Run a single round of Stone–Paper–Scissors."""
    print("\n  Choose your move:")
    for key, value in CHOICES.items():
        print(f"    {key}. {value}")

    while True:
        try:
            choice = int(input("\n  Enter (1/2/3): "))
            if choice in CHOICES:
                break
            print("  ⚠  Please enter 1, 2, or 3.")
        except ValueError:
            print("  ⚠  Invalid input. Enter a number.")

    player_choice   = CHOICES[choice]
    computer_choice = get_computer_choice()
    result          = determine_winner(player_choice, computer_choice)

    display_result(player_choice, computer_choice, result)


# ── Scoreboard ────────────────────────────────────────────────────────────────

def show_scoreboard() -> None:
    """Display the current score tally."""
    total = sum(SCORES.values())
    print("\n" + "═" * 36)
    print("          S C O R E B O A R D")
    print("═" * 36)
    print(f"  Rounds played : {total}")
    print(f"  Your wins     : {SCORES['player']}")
    print(f"  Computer wins : {SCORES['computer']}")
    print(f"  Draws         : {SCORES['draws']}")
    print("═" * 36)


def reset_scores() -> None:
    """Reset all scores back to zero."""
    for key in SCORES:
        SCORES[key] = 0
    print("\n  ✅  Scores have been reset.")


# ── Menu ──────────────────────────────────────────────────────────────────────

def show_menu() -> None:
    print("\n" + "═" * 36)
    print("    STONE – PAPER – SCISSORS  ✊📄✂️")
    print("═" * 36)
    print("  1. Play a Round")
    print("  2. View Scoreboard")
    print("  3. Reset Scores")
    print("  4. Quit")
    print("═" * 36)


def main() -> None:
    print("\n  Welcome to Stone–Paper–Scissors!")

    while True:
        show_menu()
        choice = input("  Select an option (1-4): ").strip()

        if choice == "1":
            play_round()
        elif choice == "2":
            show_scoreboard()
        elif choice == "3":
            reset_scores()
        elif choice == "4":
            show_scoreboard()
            print("\n  Thanks for playing! Goodbye 👋\n")
            break
        else:
            print("  ⚠  Invalid option. Please choose 1–4.")


# ── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()