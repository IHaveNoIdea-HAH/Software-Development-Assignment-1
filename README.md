# Software-Development-Assignment-1

# Project Crossword
The game chosen for the Project was Crossword. All members of the team have agreed to do.
Crossword is a puzzle word game where you guess words with the help of clues.

Inside the game consist of black and white grid squares going horizontal and vertical. 
Guessing the correct word will put letters that makes up into a word inside the white squares.

# Team Members

The team is comprised from the following team members:
1. Cedric
2. Shreyas
3. Alex

## Contribution from Cedric

## Contribution from Shreyas

## Contribution from Alex

# Storyboard

The storyboard on how it functions.
This is not what the final product will look like.

Start Screen

<img width="753" height="650" alt="image" src="https://github.com/user-attachments/assets/990d4a10-7e1e-498d-ade4-97eb49ce9500" />

When pressing start. They're met with the game. 6 or more generated words of the crossword in a grid with hints on the Right.
And a input for the word in the bottom.

<img width="1469" height="826" alt="image" src="https://github.com/user-attachments/assets/0b06bfb2-3a53-4056-9de2-96da43157366" />

When they guess correctly it fills the word
And changes the hint on the right from "Incompleted" to "Completed"

<img width="1453" height="832" alt="image" src="https://github.com/user-attachments/assets/c85639c5-3942-49b2-9b47-29c32d1d05d7" />

When the all the words have been found

<img width="1472" height="806" alt="image" src="https://github.com/user-attachments/assets/39253ee9-a178-4f77-ac15-d32e052e46be" />


# Risk 

- Lack of Coding Knowledge
  
Some people in this project may have different coding experience
Causing

- Testing

No amount of testing can make sure the final product will be bug free. Some things might be overlooked.

- Dependencies on libraries

The project requires API for making the game more unique and random
If not, then it will be set values.
Which may cause the user to become bored

- Scope creep

Risk: The project may become too big to handle for the three of us if we keep adding more and more features to the scope.
Mitigation: The scope should be frozen to ensure it can be delievered by the deadline.

# Test Plan

| Test | Input | Expected | Actual | Comment |
| :--- | :---: | :---: | :---: | ---: |
| Inputting the right answer | The actual Word | It fills the grid with the correct letter and words | N/A | N/A |
| Inputting the wrong answer | "ASJF" | Says text saying "Incorrect" | N/A | N/A |
| Inputting random number | 123 | Says text saying "Incorrect | N/A | N/A |

# High level user requirements

1. Game has to have main menu 
2. Game has to have leaderboard with 10 best players and their scores and times
3. Game has to have Game Win screen.
4. Game has to have Game Over screen.
5. Player must be able to play new game
6. The game is going to be focusing on a single topic (to make the delivery manageable).
7. Player must be able to score points when correct letter or word are deduced.
8. Game should have in-built game time which measures how much time a player spent on the game.
9. Player can be asked whether timer should be enabled or not.
10. There has to be a HUD in the game showing current score/time hints remaining.
11. Gameboard should be rendered on screen with words hidden horizontally and vertically also numbered so a player knows what word they are guessing.
12. Player has to be able to select a word on the gameboard and enter a letter or entire word and click ‘Check’ button to see if they guessed correctly.
13. There has to be a clues display which contains all of the clues about words hidden on the crossword gameboard.
14. Player has to be able to uncover a selected letter or an entire word hidden on the gameboard. But this gives a penalty to the score.
15. Player has to be able to click a button to auto-solve the whole crossword but this resets all the scored points to zero.
16. Accessibility features!: high contrast color scheme, fonts, links etc.
17. LOW: More advanced scoring logic like combo-bonuses, power-ups, streak bonuses??? Nice to have, low priority.
18. LOW: Difficulty levels??? Only we manage to deliver this in time. Low priority and nice to have.

# Project's functional requirements

ToDo: add functional requirements here together with acceptance criteria (Alex).

# Software development strategy

We compared three development strategies: Waterfall, Agile and Rapid Application Development (RAD).

## Comparison of the three strategies

ToDo: add a comparison table here with refs (Alex).

## Reasons for choosing RAD for our project

We go with RAD because your project:
1. Time sensitive as the delivery has to happen by 3rd of Nov.
2. Requires speed of delivery and flexibility.
3. Minimise upfront planning so we don’t need waterfall with its rigid planning and significant planning overhead.
4. Process-wise: we aim to hit the ground running by prototyping features, testing them by users, getting feedback and iterating.
5. In the first half of the project minimal documentation while fast prototyping. In the second half when things start to settle, spend time on documenting them.
6. Risks are reduced through the constant user feedback so that pivoting can happen after each prototype. 
7. RAD works great for small teams and our team is small so RAD fits very well.
8. RAD also works well for teams with mixed experience levels as the more experienced members can help the less experienced ones.
9. RAD is good for small projects and our project is small in scope.
10. Outcome focus: deliver working prototype quickly and then iterate fast so that the game crystalises into its final version.
