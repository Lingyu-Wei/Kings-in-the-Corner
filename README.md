# Kings-in-the-Corner

1.	Project Overview
I have decided to make a computer game called Bagels for my final project that the computer program will play both as the Guesser and the Responder. “Bagels is a two-person paper-and-pencil game that is similar to but simpler than Mastermind. One person thinks of a 3-digit number, and the other person tries to guess it. The 3-digit number is not allowed to have repeated digits, but it may begin with a zero (so 012, 987, and 361 are legal, but 112 and 303 are not). The Guesser makes a 3-digit guess. The Responder compares the guess to the actual mystery number, and responds to the guess by some combination of the words “Pico”, “Fermi”, and “Bagels”. The Guesser keeps guessing until the guess is the mystery number.Here are the response rules:

•	If the guess has no digits in common with the mystery number, then the answer is “Bagels.”
•	If the guess has a digit in common with the mystery number, and the common digit is in the same position in both numbers, then the responder says “Fermi” (once per match).
•	If the guess has a digit in common with the mystery number, but that common digit is not in the same position in both numbers, then the responder says “Pico” (once per match).
•	If there are multiple matches, all the Picos should be reported before all Fermis. (So you’d never say “Pico, Fermi, Pico”; if there are two Picos and one Fermi, you’d say “Pico, Pico, Fermi” regardless of which digit was the Fermi.)”
For example, suppose the mystery number is 395. Here are a few guesses and responses:
246 Bagels
037 Pico
105 Fermi
309 Pico, Fermi
395 Fermi, Fermi, Fermi.

2.  Code Outline
In order to implement this program I plan to make the following functionality:
1) Responder — randomly select a 3-digit number (may begin with a zero but the 3-digit number is not allowed to have repeated digits)
2) Guesser — randomly guess a 3-digit number
3) Responder — check whether there’s any number in common. Output “Bagels” if there’s no number in common. If the guess has a digit in common with the mystery number, and the common digit is in the same position in both numbers, then the responder says “Fermi” (once per match).If the guess has a digit in common with the mystery number, but that common digit is not in the same position in both numbers, then the responder says “Pico” (once per match) 
Note: If there are multiple matches, all the Picos should be reported before all Fermis.
4) Guesser — if there’s one “Fermi”, hold the first number ……
Repeat 3) and 4)

3.  Test Plan
Print the guessing number while running the program and check whether it guesses the number as we expected. 

4. Minimal Features and Extras
