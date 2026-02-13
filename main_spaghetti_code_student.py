
# Basic Rock Paper Scissors Game
import random


"""
main_solution.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()

# List of valid choices
choices = ['rock', 'paper', 'scissors']
# Mapping from number input to choice
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

# Welcome message
console.print("[bold cyan]Welcome to Rock, Paper, Scissors![/bold cyan]")
console.print("[green]You can type 'rock', 'paper', 'scissors' or use 1 for rock, 2 for paper, 3 for scissors.[/green]")

# Number of rounds to play
rounds = 3
# Initialize scores
user_score = 0
computer_score = 0

# Main game loop
for round_num in range(1, rounds + 1):
	console.print(f"\n[bold yellow]Round {round_num} of {rounds}[/bold yellow]")

	# Keep prompting until user enters a valid choice
	while True:
		user_input = console.input("[bold]Choose rock (1), paper (2), or scissors (3): [/bold]").strip().lower()
		if user_input in num_to_choice:
			user_choice = num_to_choice[user_input]
		else:
			user_choice = user_input
		if user_choice in choices:
			break
		else:
			console.print("[red]Invalid choice. Please try again.[/red]")

	# Computer randomly selects a choice
	computer_choice = random.choice(choices)
	console.print(f"[magenta]Computer chose: {computer_choice}[/magenta]")

	# Determine round result
	if user_choice == computer_choice:
		console.print("[blue]It's a tie![/blue]")
	elif (
		(user_choice == 'rock' and computer_choice == 'scissors') or
		(user_choice == 'paper' and computer_choice == 'rock') or
		(user_choice == 'scissors' and computer_choice == 'paper')
	):
		console.print("[bold green]You win this round![/bold green]")
		user_score += 1
	else:
		console.print("[bold red]Computer wins this round![/bold red]")
		computer_score += 1

# Game summary
console.print("\n[bold underline]Game Over![/bold underline]")
console.print(f"[cyan]Your score: {user_score}[/cyan]")
console.print(f"[magenta]Computer score: {computer_score}[/magenta]")
# Announce overall winner
if user_score > computer_score:
	console.print("[bold green]Congratulations, you win the game![/bold green]")
elif user_score < computer_score:
	console.print("[bold red]Sorry, the computer wins the game.[/bold red]")
else:
	console.print("[yellow]It's a tie game![/yellow]")
