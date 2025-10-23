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


---

# Activity 1 – Requirements and Creative Session

We've decided to re-arrange the tasks stated in the assignment brief for the Activity 1 in a more logical order to make it easier to work on them and split the work amongst us three.

--- 

## Task 1 – Review all available projects before deciding which to develop

ToDo: add review of available projects here (Cedric).

---

## Task 2 – Primary Target Audience

During the brainstorming session we've agreed that our crossword game targets **young adults aged 15–30**, mainly students and young professionals who enjoy short, word-based puzzles during study or work breaks.  
They prefer something quick, clean, and rewarding that helps improve vocabulary while relaxing.

---

## Task 4 – User Profiles

We've created two user profiles representing our primary target audience:

### 👩‍💼 Sophie (21)
- University student (Business & Marketing)  
- Plays puzzle games to take breaks from studying.  
- **Needs:** Fast-loading crossword, clear design, instant feedback.  
- **Frustrations:** Cluttered interface or slow response.

### 👨‍💻 Aaron (27)
- Software technician; plays games on lunch breaks.  
- **Needs:** Responsive design (desktop & mobile), ability to resume game.  
- **Frustrations:** Laggy inputs or confusing controls.

---

## Task 5 - High level user requirements

### High level user requirements
Based on target audience and user profiles, we've come up with the following preliminary high-level user requirements for our crossword game.
Depending on time available, some of these may be deprioritised to ensure we meet the deadline for our assignment.


NOTE: Delete the things in the bracket in the future. For now do not delete it so we don't confuse ourselves.
If we have time, task to do:
2,4,6 (for now just random generated words), 8, 9, 10, 16, 17, 18
Ignore these task when creating the game, for now create the necessary stuff

1. Game has to have main menu 
2. Game has to have leaderboard with 10 best players and their scores and times (In the future perhaps)
3. Game has to have Game Win screen.
4. Game has to have Game Over screen. (How does one lose) (if we have time, multiplayer currently lose singleplayer)
5. Player must be able to play new game
6. The game is going to use a set of random words from different topics.
7. Player must be able to score points when correct letter or word are deduced. 
8. Game should have in-built game time which measures how much time a player spent on the game. (For the future perhaps, for now it doesn't need a timer)
9. Player can be asked whether timer should be enabled or not. (Its too much effort to add a timer currently, and isn't needed maybe future)
10. There has to be a HUD in the game showing current score/time hints remaining.  (Crossword is an endless game)
11. Gameboard should be rendered on screen with words hidden horizontally and vertically also numbered so a player knows what word they are guessing.
12. Player has to be able to select a word on the gameboard and enter a letter or entire word and click ‘Check’ button to see if they guessed correctly. (We could just have a box where we input text but maybe)
13. There has to be a clues display which contains all of the clues about words hidden on the crossword gameboard.
14. Player has to be able to uncover a selected letter or an entire word hidden on the gameboard. But this gives a penalty to the score.
15. Player has to be able to click a button to auto-solve the whole crossword but this resets all the scored points to zero. 
16. Accessibility features!: high contrast color scheme, fonts, links etc. (ehh maybe in the futyre)
17. LOW: More advanced scoring logic like combo-bonuses, power-ups, streak bonuses??? Nice to have, low priority. (Future)
18. LOW: Difficulty levels??? Only we manage to deliver this in time. Low priority and nice to have. (Future)

### Hardware Requirements

Players of our crossword game will need a device capable of running a web browser, such as a desktop computer, laptop, tablet, or smartphone. 
The device should have a minimum of 2GB RAM and a modern processor to ensure smooth gameplay.

### Operating System Requirements

The crossword game will be web-based and compatible with major operating systems including Windows, macOS, Linux, iOS, and Android.

### Key application functions

Below list of key application functions that the crossword game must support to meet high level user requirements.
This is preliminary list as per our brainstorming session and may be refined further.

| Functionality               | Description                                                                     |
|-----------------------------|---------------------------------------------------------------------------------|
| User Authentication         | Players can create accounts and log in to save progress and access leaderboards |
| Game Interface              | Intuitive UI for navigating menus, starting games, and viewing scores           |
| Crossword Generation        | Dynamic generation of crossword puzzles based on selected difficulty levels     |
| Scoring System              | Points awarded for correct answers, with penalties for hints or auto-solve      |
| Clue Display                | Clear presentation of clues for each word in the crossword                      |
| Accessibility Features     | Options for high contrast mode, larger fonts, and keyboard navigation           |
| Responsive Design          | Optimized for various screen sizes and devices                                  |
| Feedback Mechanism         | Real-time feedback on answers (correct/incorrect)                               |
| Progress Saving            | Saving of game progress and scores in order player can resume unfinished game   |

### AI in the game

In our game we are not planning to use AI features as part of the core gameplay experience.
The only kind of 'AI' feature we are going to use is using a simple algorithm to generate random words for the crossword puzzles our players will be solving.
For this we will use a predefined list of words and clues, and the algorithm would randomly select words from this list to create unique crossword puzzles for each game session played by a user.
So, this is going to be a basic implementation and does not involve advanced AI techniques.

---

## Task 3 - Create an overall specification 

Create an overall specification based on user and system requirements (including HCI, game/application-rules and the 
game/application-mechanics (e.g. what are the rules for the game, how will the game be controlled, how will 
any non-player characters interact, etc.) 

ToDo: add functional requirements here together with acceptance criteria (Alex).

| Functional requirement      | Type | Specification                                                                                       | Acceptance Criteria                                                                                                         |
|-----------------------------|------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Main menu when app starts   | UI   | The main menu is displayed with options to start a new game, view leaderboard, and access settings. | When the app starts, main menu is displayed with all options visible and clickable.                          |
| Leaderboard shown to a user | UI   | Leaderboard displays the top 10 players with their scores and times.                                | When user clicks Leaderboard main menu item in the app the Leaderboard is shown and displays top 10 players sorted by score. |
|                             |      |
|                             |      |
|                             |      |
|                             |      |
|                             |      |
|                             |      |


---


## Task 6 – Non-Functional Specifications

It is important to consider non-functional specifications as part of the overall specification for the crossword game.
We've identified the following non-functional specifications to be important for our game:

| Category | Specification |
|-----------|----------------|
| **Aesthetic** | Clean grid layout, minimal colours, modern typography. |
| **Usability** | Simple controls and clear instructions. |
| **Responsiveness** | Works perfectly on desktop, tablet, and mobile. |
| **Accessibility** | High contrast colours, large text option, keyboard navigation. |
| **Feedback** | Real-time indicators: green for correct, red for wrong. |
| **Performance** | Loads under 3 seconds, no noticeable lag. |
| **Reliability** | Auto-saves progress locally. |
| **Maintainability** | Code modular and well-commented for easy updates. |

---

## Task 7 - Overall mockup

ToDo: add overall mockup here (Cedric).

Main game:
<img width="1343" height="737" alt="image" src="https://github.com/user-attachments/assets/b4ff156f-47d9-4e59-aa3e-4a365e13d771" />



---

## Task 8 - Construct basic storyboards associated with the game-play/app use

The storyboard on how it functions.
This is not what the final product will look like.

### Start Screen

<img width="753" height="650" alt="image" src="https://github.com/user-attachments/assets/990d4a10-7e1e-498d-ade4-97eb49ce9500" />

When pressing start. They're met with the game. 6 or more generated words of the crossword in a grid with hints on the Right.
And a input for the word in the bottom.

<img width="1469" height="826" alt="image" src="https://github.com/user-attachments/assets/0b06bfb2-3a53-4056-9de2-96da43157366" />

When they guess correctly it fills the word
And changes the hint on the right from "Incompleted" to "Completed"

<img width="1453" height="832" alt="image" src="https://github.com/user-attachments/assets/c85639c5-3942-49b2-9b47-29c32d1d05d7" />

When the all the words have been found

<img width="1472" height="806" alt="image" src="https://github.com/user-attachments/assets/39253ee9-a178-4f77-ac15-d32e052e46be" />


---

## Task 9 - Identify and rank potential risks to the project’s success 

During the brainstorming session, we identified the following potential risks to the project's success along with their mitigation strategies:

| Category                                      | Description                                                    | Mitigtion Strategy                                                                       |
|-----------------------------------------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Lack of Coding Knowledge                      | Some people in this project may have different coding experience | Pair programming, online tutorials, team knowledge sharing.                              |
| Dependencies on libraries                     | The project requires API for making the game more unique and random. If not, then it will be set values. Which may cause the user to become bored. | Create backend which will offer wider set of words to be used for crosswords generation. |
| Presence of bugs which affect user experience | No amount of testing can make sure the final product will be bug free. Some things might be overlooked. | Thorough testing, user feedback loops, quick bug fixing cycles.                        |
| Scope creep                             | The project may become too big to handle for the three of us if we keep adding more and more features to the scope. | Mitigation: The scope should be frozen to ensure it can be delievered by the deadline.    |


---

## Task 10 - Software development strategy 

We compared three development strategies: Waterfall, Agile and Rapid Application Development (RAD).

### Comparison of the three strategies

ToDo: add a comparison table here with refs (Alex).

### Reasons for choosing RAD for our project

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

---

## Task 11 - Overall Test Plan

### Overall test strategy

The overall test strategy for the Crossword game involves a combination of manual testing and automated unit tests to ensure the game functions correctly and meets user requirements.
Such combination of manual functional testing and unit tests covering the code allows us to achieve high quality of the software being developed such as our crossword game.

#### Manual Testing

Manual tests are going to be done on the frontend to test the user interface and user experience.
The manual tests will cover the following scenarios:

| Test | Input | Expected | Actual | Comment |
| :--- | :---: | :---: | :---: | ---: |
| Inputting the right answer | The actual Word | It fills the grid with the correct letter and words | N/A | N/A |
| Inputting the wrong answer | "ASJF" | Says text saying "Incorrect" | N/A | N/A |
| Inputting random number | 123 | Says text saying "Incorrect | N/A | N/A |

#### Unit Tests

Unit tests are done on the backend to test the game logic, scoring, timer etc.
pytest framework is used for unit testing of the backend part.
In the backend folder, run the following command to execute the unit tests:
python -m pytest tests/test_app.py 


---

# Activity 2 - Design Analysis Session

---

## Task 1 - Refining and improving 

Task 1 – Refining and Improving

After reviewing our initial specifications from Activity 1, the team met to refine the scope and simplify certain elements to make sure the crossword game could be fully developed within the time limit.

Improvements and Adjustments

| Area | Original Idea | Issue Identified | Improvement Implemented |
|------|----------------|------------------|--------------------------|
| Difficulty Levels | Multiple difficulty levels (easy/medium/hard) | Too time-consuming to design and test within project timeline | Reduced to a single default level for the first release |
| Timer Feature | Optional countdown and stopwatch | Not essential for gameplay; risked extra bugs | Removed timer for version 1.0, may add later |
| Scoring System | Combo/streak bonuses and advanced logic | Over-complicated for MVP | Simplified to +10 points for correct answers and −2 for hints |
| Hint Mechanism | Reveal entire word | Too generous; reduced challenge | Now reveals only one letter per click with a score penalty |
| UI / UX Design | Basic black-and-white layout | Hard to identify selected cells | Added blue highlight for active word and responsive font scaling |
| Backend Logic | Dynamic crossword generator via API | Not achievable in short timeframe | Using pre-defined word sets stored in JSON for reliability |
| Accessibility | Minimal colour contrast only | Needed better readability and accessibility | Added larger-text option and ensured high contrast ratio |
| Testing Plan | Only three manual tests | Limited coverage of key functions | Added more tests for hint button, win screen, and grid reset |

These refinements make the project **more achievable, user-friendly, and stable**, aligning with the RAD (Rapid Application Development) approach that emphasises quick prototyping, continuous testing, and iterative improvement.


## Task 2 - agree project requirements and specifications

After refining our ideas, the team agreed on the final set of requirements that are realistic to deliver within the deadline.  
The focus is on simplicity, functionality, and a smooth user experience.

#### Final Functional Specifications
1. Single-topic crossword with 6–8 words per puzzle.  
2. Player inputs answers manually and clicks **Check** to validate.  
3. **Hint** button reveals one letter and deducts points.  
4. Simple scoring system (+10 for correct, −2 for hint).  
5. Responsive UI with highlighted active word.  
6. **You Win** message appears when all words are completed.  
7. Local storage saves current progress.

#### Final Non-Functional Specifications
- Loads within 3 seconds.  
- Works on desktop, tablet, and mobile.  
- Clear visual feedback (green = correct, red = incorrect).  
- High-contrast colours and readable fonts.  
- Modular code using HTML, CSS, JavaScript, and JSON.  
- Hosted on GitHub Pages for easy access and testing.

These requirements ensure the game remains achievable while maintaining a polished and accessible user experience.

---

## Task 3 - Psuedocode

Below is the pseudocode outlining the main logic and actions for the Crossword game.  
It defines how the player interacts with the game, how answers are checked, and how the score is updated.

START GAME
  DISPLAY main menu
  IF user clicks "Start"
      LOAD crossword grid
      DISPLAY clues and input area
      SET score = 0
      SET wordsSolved = 0

      WHILE game not finished
          WAIT for player input
          IF input matches correct word
              UPDATE grid with correct letters
              DISPLAY “Correct!”
              INCREASE score by 10
              INCREASE wordsSolved by 1
          ELSE
              DISPLAY “Incorrect!”

          IF player clicks “Hint”
              REVEAL one letter in selected word
              DECREASE score by 2

          IF all wordsSolved = totalWords
              DISPLAY “You Win!” message
              END LOOP
      END WHILE
  END IF

SAVE progress locally
DISPLAY final score
END GAME
```


---

## Task 4 - UML Flowchart

Use basic UML flowcharts to help plan, design and test game logic, interaction, mechanics and flow

---

## Task 5 - Game State management

Establish game state management (start, win, lose, draw) – confirm how the state could be monitored, detected or changed?

Check Word:
Words: Sees if the word inputted matches the words set 
Incorrect: If the inputted words doesn't match. Displays "Incorrect"
Correct: If the inputted word matches then display "Correct" and put letters in the box

Hints:
If player presses a hint, it displays one single letter about of a word, only displaying 3 letters of each word.


1 player game
Win Conditions: All words have been found.
Lose Conditiion: If time ran out. You lose. (If time limit has been implemented)

2 player game: (IF time limit has been implemented and Multiplayer Implemented)
Win condition: Get more words than the other opponent when time runs out.
Lose Condition: Get less words than the other opponent when time runs out.
Draw condition: If both players is equal in the amount of words they found.

---

## Architecture Design

Here goes the architecture design of the project (Alex).

We are using a client-server architecture.
We are going to have a backend server (controller) which will handle the game logic, scoring, timer, leaderboard etc.
The backend will expose a RESTful API which the frontend (view) will call to get game state, submit guesses, get leaderboard etc.
The frontend will be a web app which will render the gameboard, clues, HUD etc.
The frontend will call the backend API to get game state, submit guesses etc.
Initially the backend will use a set of json files to store the game data (words, clues etc.) but later we might move to a database if time permits.

ToDo: add a block diagram here (Alex).

