import random

# ─────────────────────────────────────────
#  DICE ROLL GAME
# ─────────────────────────────────────────

def roll_dice(sides: int = 6) -> int:
    """Roll a single die and return the result."""
    return random.randint(1, sides)


def roll_multiple_dice(count: int, sides: int = 6) -> list[int]:
    """Roll multiple dice and return a list of results."""
    return [roll_dice(sides) for _ in range(count)]


def determine_winner(player_roll: int, computer_roll: int) -> str:
    """Compare rolls and return the result string."""
    if player_roll > computer_roll:
        return "win"
    elif player_roll < computer_roll:
        return "loss"
    else:
        return "tie"


def display_roll_animation(name: str, roll: int) -> None:
    """Display a formatted roll result."""
    print(f"  🎲  {name:<12} rolled  ──►  [ {roll} ]")


def play_single_round(scoreboard: dict) -> None:
    """Play one Player vs Computer round."""
    print("\n" + "─" * 40)
    print("  🎮  ROUND START")
    print("─" * 40)
    input("  Press ENTER to roll your dice... ")

    player_roll   = roll_dice()
    computer_roll = roll_dice()

    display_roll_animation("You",      player_roll)
    display_roll_animation("Computer", computer_roll)
    print("─" * 40)

    result = determine_winner(player_roll, computer_roll)

    if result == "win":
        scoreboard["player"] += 1
        print("  🏆  YOU WIN this round!")
    elif result == "loss":
        scoreboard["computer"] += 1
        print("  💻  COMPUTER WINS this round!")
    else:
        scoreboard["ties"] += 1
        print("  🤝  IT'S A TIE!")


def play_best_of(rounds: int) -> None:
    """Play a best-of-N series and track the scoreboard."""
    scoreboard = {"player": 0, "computer": 0, "ties": 0}

    print(f"\n  ⚔️   Best of {rounds} — Let's go!\n")

    for rnd in range(1, rounds + 1):
        print(f"\n  [ Round {rnd} of {rounds} ]")
        play_single_round(scoreboard)
        print(f"  Score  →  You {scoreboard['player']}  |  "
              f"Computer {scoreboard['computer']}  |  Ties {scoreboard['ties']}")

    print("\n" + "═" * 40)
    print("  📊  FINAL SCOREBOARD")
    print("═" * 40)
    print(f"  You      : {scoreboard['player']} wins")
    print(f"  Computer : {scoreboard['computer']} wins")
    print(f"  Ties     : {scoreboard['ties']}")
    print("─" * 40)

    if scoreboard["player"] > scoreboard["computer"]:
        print("  🥇  Overall Winner: YOU!")
    elif scoreboard["computer"] > scoreboard["player"]:
        print("  🤖  Overall Winner: COMPUTER!")
    else:
        print("  🤝  It's an overall TIE!")
    print("═" * 40)


def play_multi_dice_round() -> None:
    """Roll multiple dice at once; highest total wins."""
    print("\n" + "─" * 40)

    try:
        count = int(input("  How many dice each? (1–6): ").strip())
        count = max(1, min(count, 6))
    except ValueError:
        count = 2

    print(f"\n  Rolling {count} dice each...\n")
    input("  Press ENTER to roll... ")

    player_rolls   = roll_multiple_dice(count)
    computer_rolls = roll_multiple_dice(count)

    player_total   = sum(player_rolls)
    computer_total = sum(computer_rolls)

    print(f"  🎲  Your dice     : {player_rolls}  →  Total: {player_total}")
    print(f"  🎲  Computer dice : {computer_rolls}  →  Total: {computer_total}")
    print("─" * 40)

    result = determine_winner(player_total, computer_total)
    if result == "win":
        print("  🏆  YOU WIN!")
    elif result == "loss":
        print("  💻  COMPUTER WINS!")
    else:
        print("  🤝  IT'S A TIE!")


def show_rules() -> None:
    """Print game rules."""
    print("""
╔══════════════════════════════════════╗
║            🎲  HOW TO PLAY           ║
╠══════════════════════════════════════╣
║  1. Single Round                     ║
║     Both sides roll one die (1-6).   ║
║     Higher roll wins.                ║
║                                      ║
║  2. Best of N                        ║
║     Play 3 or 5 rounds; most wins    ║
║     takes the series.                ║
║                                      ║
║  3. Multi-Dice                       ║
║     Each side rolls multiple dice.   ║
║     Highest total score wins.        ║
╚══════════════════════════════════════╝
""")


def main_menu() -> None:
    """Main menu loop."""
    print("""
╔══════════════════════════════════════╗
║        🎲  DICE ROLL GAME  🎲        ║
╚══════════════════════════════════════╝""")

    while True:
        print("""
  ┌─────────────────────────────────┐
  │  1 ► Single Round               │
  │  2 ► Best of 3                  │
  │  3 ► Best of 5                  │
  │  4 ► Multi-Dice Round           │
  │  5 ► Rules                      │
  │  6 ► Quit                       │
  └─────────────────────────────────┘""")

        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "1":
            scoreboard = {"player": 0, "computer": 0, "ties": 0}
            play_single_round(scoreboard)
        elif choice == "2":
            play_best_of(3)
        elif choice == "3":
            play_best_of(5)
        elif choice == "4":
            play_multi_dice_round()
        elif choice == "5":
            show_rules()
        elif choice == "6":
            print("\n  👋  Thanks for playing! Goodbye!\n")
            break
        else:
            print("  ⚠️   Invalid choice. Please enter 1–6.")


# ─────────────────────────────────────────
if __name__ == "__main__":
    main_menu()