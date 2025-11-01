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

Project: Match.
Description: Match is where you are shown a set of items and must relate them into the related Categories
The core requirements are: Displaying items or clues. Drag and Drop system. Tracking score. 

Project: Jigsaw.
Description: Assemble pieces to make an image.
Core requirements: Image silcing into jigsaw. drag and drop system. Snap to place

Project: Crossword (Chosen)
Description: Solve a crossword grid by answering clues
Core requirements: Generating crossword grids. Generating clues. Filling letters and checking if they match

---

## Task 2 – Primary Target Audience

During the brainstorming session we've agreed that our crossword game targets **young adults aged 15–30**, mainly students and young professionals who enjoy short, word-based puzzles during study or work breaks.  
They prefer something quick, clean, and rewarding that helps improve vocabulary while relaxing.

---

## Task 3 - Create an overall specification 

Create an overall specification based on user and system requirements (including HCI, game/application-rules and the 
game/application-mechanics (e.g. what are the rules for the game, how will the game be controlled, how will 
any non-player characters interact, etc.) 

ToDo: add functional requirements here together with acceptance criteria (Alex).

| Functional requirement             | Type | Specification                                                                                       | Acceptance Criteria                                                                                                          |
|------------------------------------|------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Main menu when app starts          | UI   | The main menu is displayed with options to start a new game, view leaderboard, and access settings. | When the app starts, main menu is displayed with all options visible and clickable.                                          |
| Leaderboard shown to a user        | UI   | Leaderboard displays the top 10 players with their scores and times.                                | When user clicks Leaderboard main menu item in the app the Leaderboard is shown and displays top 10 players sorted by score. |
| Game win screen when the user wins | UI   | When a player correctly guesses all words, a Game Win screen is displayed.                          | When all words are guessed correctly, the Game Win screen appears with final score and option to return to main menu.        |
| Game over screen when user loses   | UI   | When a player runs out of guesses, a Game Over screen is displayed.                                 | When the player runs out of guesses, the Game Over screen appears with final score and option to return to main menu.        |
| Start new game                     | UX   | Player can start a new game from the main menu.                                                     | When user clicks "New Game" button in main menu, a new crossword game starts with fresh grid and clues.                      |
| Random words for crossword         | Sys  | The game uses a set of random words from different topics for the crossword.                        | Each new game generates a unique crossword puzzle using randomly selected words from predefined word list.                   |
| Scoring system                     | Sys  | Player scores points when correct word is guessed.                                                  | When player guesses a word correctly, score increases by 10 points.                                                          |
| Game time tracking (optional)      | Sys  | The game tracks how much time a player spends on the game. (If implemented)                         | If timer is enabled, the game displays elapsed time during gameplay.                                                         |
| HUD display                        | UI   | HUD shows current score, guesses made, and hints remaining.                                         | During gameplay, HUD is visible and updates in real-time with score, guesses, and hints.                                     |
| Gameboard rendering                | UI   | Gameboard is rendered on screen with words hidden horizontally and vertically, numbered for clues.  | When game starts, the crossword grid is displayed with numbered cells corresponding to clues.                                |
| Word selection and input           | UX   | Player can select a word on the gameboard and enter an entire word to check.                        | When player selects a word and inputs answer, clicking "Check" validates the answer and updates grid accordingly.            |
| Clue display                       | UI   | Clues for each word are displayed clearly alongside the gameboard.                                  | During gameplay, clues are visible and correspond to numbered words on the grid.                                             |
| Reveal word with penalty           | UX   | Player can uncover an entire word hidden on the gameboard with a score penalty .                    | When player clicks "Reveal Word" button, one word is revealed on the grid and score decreases by 5 points.                   |
| Auto-solve crossword               | UX   | Player can click a button to auto-solve the whole crossword, resetting score to zero.               | When player clicks "Auto-Solve" button, entire crossword is revealed and score resets to zero.                               |
| Accessibility features             | UI   | High contrast color scheme, larger fonts, and keyboard navigation options are available.            | Accessibility options can be toggled in settings and apply immediately to the game interface.                                |
| Responsive design                  | UI   | The game is optimized for various screen sizes and devices.                                         | The game layout adjusts correctly on desktop, tablet, and mobile devices without loss of functionality.                      |
| Real-time feedback                 | UX   | Real-time feedback is provided on answers (correct/incorrect).                                      | When player submits an answer, immediate feedback is shown indicating correctness.                                           |
| Progress saving                    | Sys  | Player’s progress and scores are saved locally to resume unfinished game.                           | When player exits the game, progress is saved and can be resumed from last state upon return                                 |


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
3. Game has to have Game Win screen. (When a player correctly guesses all words)
4. Game has to have Game Over screen. (When a player runs out of guesses)
5. Player must be able to play new game
6. The game is going to use a set of random words from different topics.
7. Player must be able to score points when correct word is guessed. 
8. LOW: Game should have in-built game time which measures how much time a player spent on the game. (For the future perhaps, for now it doesn't need a timer)
9. LOW: Player can be asked whether timer should be enabled or not. (Its too much effort to add a timer currently, and isn't needed maybe future)
10. There has to be a HUD in the game showing current score, guesses made and hints remaining.  
11. Gameboard should be rendered on screen with words hidden horizontally and vertically also numbered so a player knows what word they are guessing.
12. Player has to be able to select a word on the gameboard and enter an entire word and click ‘Check’ button to see if they guessed correctly. (We could just have a box where we input text but maybe)
13. There has to be a clues display which contains all of the clues about words hidden on the crossword gameboard.
14. Player has to be able to uncover an entire word hidden on the gameboard. But this gives a penalty to the score.
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


## Task 6 – Non-Functional Specifications

It is important to consider non-functional specifications as part of the overall specification for the crossword game.
We've identified the following non-functional specifications to be important for our game:

| Category | Specification                                                 |
|-----------|---------------------------------------------------------------|
| **Aesthetic** | Clean grid layout, minimal colours, modern typography.        |
| **Usability** | Simple controls and clear instructions.                       |
| **Responsiveness** | Works perfectly on desktop, tablet, and mobile.               |
| **Accessibility** | High contrast colours, large text option, keyboard navigation. |
| **Feedback** | Real-time indicators: green for correct, red for wrong.       |
| **Performance** | Loads under 3 seconds, no noticeable lag.                     |
| **Reliability** | Auto-saves progress locally.                                  |
| **Maintainability** | Code modular and well-commented for easy updates.             |

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

| Criteria                 | Waterfall                        | Agile                               | Rapid Application Development (RAD)   |
|--------------------------|----------------------------------|-------------------------------------|---------------------------------------|
| Flexibility              | Low - rigid phases               | High - iterative and adaptive       | High - iterative protyping            |
| Speed of Delivery        | Slow - sequential phases         | Fast - frequent releases            | Very Fast - rapid prototyping         |
| User Involvement         | Low - mainly at start and end    | High - continuous feedback          | Very High - constant user feedback    |
| Documentation            | Extensive upfront documentation  | Minimal - just enough               | Minimal - focus on working prototypes |
| Risk Management          | High risk if requirements change | Low risk through constant feedback  | Low risk due to adaptability          |  
| Team Size Suitability    | Large teams                      | Small to medium teams               | Small teams                           |
| Project Size Suitability | Large projects                   | Medium projects                     | Small projects                        |
| Outcome Focus            | Deliver complete product at end  | Deliver working software frequently | Deliver working prototypes quickly    |

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

Unit tests are done on the backend to test the game logic, scoring etc.
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

The pseudocode below outlines the main logic and gameplay flow for the Crossword Game.  
It shows how the player interacts with the game, how answers are checked, and how the score is updated.

```plaintext
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
              DISPLAY "Correct!"
              INCREASE score by 10
              INCREASE wordsSolved by 1
          ELSE
              DISPLAY "Incorrect!"

          IF player clicks "Hint"
              REVEAL one letter in selected word
              DECREASE score by 2

          IF wordsSolved == totalWords
              DISPLAY "You Win!" message
              EXIT LOOP
          END IF
      END WHILE

      SAVE progress locally
      DISPLAY final score
  END IF

END GAME
```



## Task 4 - UML Flowchart
The UML flowchart below represents the overall game logic and user interaction flow for the Crossword game.  
It helps visualize how the game starts, how player input is processed, and how the program determines when the game is complete.

#### Description of Flow

1. The game starts and displays the **Main Menu**.  
2. When the player clicks **Start**, the crossword grid and clues are loaded.  
3. The player types an answer into the input box.  
4. The program checks if the answer matches the correct word.  
   - If correct → the word appears in the grid and the score increases.  
   - If incorrect → an error message appears.  
5. The player can click **Hint** to reveal one letter (with a score penalty).  
6. The program checks whether all words are solved.  
   - If yes → display **"You Win"** message and final score.  
   - If no → continue playing.  
7. The player’s progress is saved locally before the game ends.

#### UML Flow (Text-Based Representation)

```plaintext
          ┌─────────────────────┐
          │     START GAME      │
          └─────────┬───────────┘
                    │
                    ▼
        ┌──────────────────────┐
        │ Display Main Menu    │
        └─────────┬────────────┘
                  │
         ┌────────▼────────┐
         │ User clicks     │
         │ "Start"         │
         └────────┬────────┘
                  │
        ┌─────────▼─────────┐
        │ Load Crossword     │
        │ & Display Clues    │
        └─────────┬─────────┘
                  │
          ┌───────▼────────┐
          │ Player Inputs   │
          │ Answer          │
          └───────┬────────┘
                  │
     ┌────────────▼────────────┐
     │ Is Answer Correct?      │
     ├────────────┬────────────┤
     │ Yes        │ No         │
     ├────────────┼────────────┤
     │ Update Grid│ Display    │
     │ +10 Points │ “Incorrect”│
     └──────┬─────┴────────────┘
            │
  ┌─────────▼──────────┐
  │ Player Clicks Hint?│
  ├─────────┬──────────┤
  │ Yes     │ No       │
  ├─────────┼──────────┤
  │ Reveal  │ Continue │
  │ Letter  │ Game Loop│
  │ -2 Pts  │          │
  └─────────┴──────────┘
            │
    ┌───────▼──────────┐
    │ All Words Solved?│
    ├─────────┬────────┤
    │ Yes     │ No     │
    ├─────────┼────────┤
    │ Display │ Wait for│
    │ “You Win” │ Input │
    └───────┬──────────┘
            │
    ┌───────▼─────────┐
    │ Save Progress   │
    │ Display Score   │
    └───────┬─────────┘
            │
            ▼
     ┌───────────────┐
     │    END GAME    │
     └───────────────┘
```


 ## Task 5 - Game State management

This section defines how the game manages and tracks different states such as **Start**, **Win**, **Lose**, and **Draw**, as well as how these states are detected and updated during gameplay.

#### Game States
1. **Start State** – The game begins when the player clicks the **Start** button on the main menu.  
   - The crossword grid, score, and clue list are loaded.  
   - Score and wordsSolved counters are set to zero.

2. **Active State** – The player is actively entering answers and interacting with the crossword grid.  
   - Input is checked against the correct word list.  
   - Hints can be requested at the cost of points.

3. **Win State** – Triggered when all words are correctly solved.  
   - A **“You Win!”** message is displayed.  
   - The final score is shown and stored locally.

4. **Lose State** – (Optional) Activated if a time limit is implemented in later versions.  
   - The player loses if the time runs out before solving all words.

5. **Draw State** – (For future multiplayer implementation)  
   - Triggered if both players find the same number of words when time expires.

#### Game Logic Overview
- **Check Word Function:**  
  - Compares the player’s input with the stored correct words.  
  - If the word matches → display *“Correct!”*, reveal it in the grid, and award +10 points.  
  - If the word does not match → display *“Incorrect!”* and no points are given.

- **Hint Function:**  
  - Reveals one random unrevealed letter from the selected word.  
  - Deducts 2 points from the player’s score.  
  - Hints limited to showing 3 letters per word.

#### Win / Lose Conditions

**Single Player Mode:**  
- **Win:** All words are correctly solved.  
- **Lose:** (If a timer is added) Time expires before all words are found.

**Multiplayer Mode (Future):**  
- **Win:** Player finds more words than opponent before the time runs out.  
- **Lose:** Opponent finds more words before the timer ends.  
- **Draw:** Both players solve an equal number of words.

---

This design ensures that game states are **clearly defined, easily monitored, and scalable**, allowing smooth future integration of multiplayer and timed challenges.

## Architecture Design

Here goes the architecture design of the project (Alex).

We are using a client-server architecture.
We are going to have a backend server (controller) which will handle the game logic, scoring, leaderboard etc.
The backend will expose a RESTful API which the frontend (view) will call to start new game, get game state, submit guesses, get leaderboard etc.
The frontend will be a web app which will render the gameboard, clues, HUD etc.
The frontend will call the backend API to get game state, submit guesses etc.
Initially the backend will use a set of json files to store the game data (words, clues etc.) but later we might move to a database if time permits.

ToDo: add a block diagram here (Alex).

