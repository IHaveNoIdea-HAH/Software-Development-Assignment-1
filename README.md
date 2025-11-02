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

We've reviewed all 3 available projects to chose from and during the initial brainstorming session we've decided to go with the crossword game project.
We felt that the crossword game would be a good fit for our team as it combines word puzzles with a simple yet engaging gameplay mechanic.

---

## Task 2 – Primary Target Audience

During the brainstorming session we've agreed that our crossword game targets **young adults aged 15–30**, mainly students and young professionals who enjoy short, word-based puzzles during study or work breaks.  
They prefer something quick, clean, and rewarding that helps improve vocabulary and overall erudition while relaxing.
This choice was made because this demographic is likely to appreciate the cognitive challenge of crosswords while also valuing a polished user experience that fits into their busy lifestyles.

---

## Task 4 – User Profiles

We've created two user profiles representing our primary target audience:

### 👩‍💼 Sophie (21)
- University student (Business & Marketing)
- Plays puzzle games to take breaks from studying.
- **Wants:** quick, engaging puzzles that fit into short breaks.
- **Needs:** fast-loading crossword, clear design, instant feedback.  
- **Frustrations:** Cluttered interface or slow response.

### 👨‍💻 Aaron (27)
- Software technician; plays games on lunch breaks.
- Enjoys word games that challenge vocabulary.
- **Wants:** challenging yet accessible puzzles.
- **Needs:** Responsive design (desktop & mobile), ability to resume game.  
- **Frustrations:** Laggy inputs or confusing controls.

---

## Task 5 - High level user requirements

### High level user requirements
Based on target audience and user profiles, we've come up with the following preliminary high-level user requirements for our crossword game.
Depending on time available, some of these may be deprioritised to ensure we meet the deadline for our assignment.
The strict deadline means we have to focus on the core gameplay features first and polish those before adding any additional features.
Therefore, we identified some of the features to be the core ones and to comprise our minimum viable product (MVP) while the others are nice-to-have features that we may add if time permits and to generally represent Phase 2 features.

NOTE: Delete the things in the bracket in the future. For now do not delete it so we don't confuse ourselves.
If we have time, task to do:
2,4,6 (for now just random generated words), 8, 9, 10, 16, 17, 18
Ignore these task when creating the game, for now create the necessary stuff

MVP features (Must have):
1. Game has to have main menu 
2. Game has to have Game Win screen. (When a player correctly guesses all words)
3. Game has to have Game Over screen. (When a player runs out of guesses)
4. Player must be able to play new game.
5. Each new crossword game is going to use a set of random words from different topics.
6. Player must be able to score points when correct word is guessed. 
7. There has to be a HUD in the game showing current score, words guessed, words remaining to be guessed, guesses made etc.  
8. Gameboard should be rendered on screen with words hidden horizontally and vertically also numbered so a player knows what word they are guessing.
9. Player has to be able to select a word or a clue number corresponding to a word on the gameboard and enter an entire guess word and click ‘Check’ button to see if they guessed correctly.
10. There has to be a numbered list of clues displayed which contains all of the clues about words hidden on the crossword gameboard plus the their directions being across or down.
11. Player has to be able to uncover an entire word hidden on the gameboard. But this gives a penalty to the score.
12. Player has to be able to click a button to auto-solve the whole crossword but this gives penalty points for any unsolved clues.
13. Player has to be able to create an account and log in to the game so that their scores and progress can be saved.
14. Game has to have an intuitive user interface for navigating menus, starting new games, viewing scores etc.
15. Game has to have a simple scoring system where points are awarded for correct answers and penalties for hints or auto-solve.
16. The crossword puzzles should be dynamically generated using some sort of crossword generation algorithm.

Nice to have features (If time permits) so our Phase 2 features:
1. Difficulty levels. User can select from easy, medium, hard difficulty levels.
2. More advanced scoring logic like combo-bonuses, power-ups, streak bonuses??? Nice to have, low priority.
3. Accessibility features!: high contrast color scheme, fonts, links etc.
4. Game has to have leaderboard with 10 best players and their scores and times.
5. Game should have in-built game time which measures how much time a player spent on the game.
6. Player can be asked whether timer should be enabled or not.
7. Game has to be optimized for various screen sizes and devices (responsive design).
8. Progress saving: Player’s progress and scores are saved locally so that they can resume unfinished game later.

### Hardware Requirements

Players of our crossword game will need a device capable of running a web browser, such as a desktop computer, laptop, tablet, or smartphone. 
The device should have a minimum of 2GB RAM and a modern processor to ensure smooth gameplay.
No fancy hardware such as GPU is required as the game is not graphically intensive.

### Operating System Requirements

The crossword game will be web-based and compatible with major operating systems including Windows, macOS, Linux, iOS, and Android.

### Key application functions

Below list of key application functions that the crossword game must support to meet high level MVP version user requirements.
This is preliminary list as per our brainstorming session and may be refined further.

| Functionality           | Description                                                                                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User authentication     | Players can create accounts and log in to save progress and access leaderboards                                                                                              |
| Game interface          | Intuitive UI for navigating menus, starting games, and viewing scores                                                                                                        |
| Crossword generation    | Dynamic generation of crossword puzzles using a vocabulary of clues                                                                                                          |
| Game state management   | Scoring system so that points awarded for correct answers, with penalties for hints or auto-solve. Counting of guesses made, guesses left etc. Game over and game win logic. |
| Clue display            | Clear presentation of clues for each word in the crossword with number and direction                                                                                         |
| Accessibility features  | Options for high contrast mode, larger fonts, and keyboard navigation                                                                                                        |
| Responsive design       | Optimized for various screen sizes and devices                                                                                                                               |
| Feedback mechanism      | Real-time feedback on answers (correct/incorrect)                                                                                                                            |
| Game play HUD           | Display of current score, guesses made, words remaining etc.                                                                                                                 |
| Core game play features | Ability to select clue and guess word, auto solve a clue and auto-solve the entire crossword.                                                                                |


### AI in the game

In our game we are not planning to use AI features as part of the core gameplay experience.
The only kind of 'AI' feature we are going to use is using an algorithm to generate crossword for a new game started by a user using random words from the vocabulary of clues.
For this we will use a predefined list of words and clues, and the algorithm would randomly select words from this list to create unique crossword puzzles for each game session played by a user.
So, this is going to be a basic implementation and does not involve advanced AI techniques.

---

## Task 3 - Create an overall specification 

Create an overall specification based on user and system requirements (including HCI, game/application-rules and the 
game/application-mechanics (e.g. what are the rules for the game, how will the game be controlled, how will 
any non-player characters interact, etc.) 

The following list of functional requirements has been produced to cover the high-level user requirements from task 5 above.
It has to be mentioned the list also has the acceptance criteria for each functional requirement to ensure that the requirement is testable and verifiable.

| Functional requirement             | Type | Specification                                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                                                                                            |
|------------------------------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main menu when app starts          | UI   | The main menu is displayed with options to play a new game or check rules of the game how to play it.                                                                                                  | When the app starts, main menu is displayed with "Play" and "How to play" options visible and clickable.                                                                                                                                                                                                                                       |
| Game win screen when the user wins | UI   | When a player correctly guesses all words, a Game Win screen is displayed.                                                                                                                             | When all words are guessed correctly, the Game Win screen appears with final game state e.g. score, count of guesses made etc. and option to return to main menu.                                                                                                                                                                              |
| Game over screen when user loses   | UI   | When a player runs out of guesses or crossword is auto-solved, a Game Over screen is displayed.                                                                                                        | When the player runs out of guesses or auto-solves the crossword, the Game Over screen appears with final game state and option to return to main menu.                                                                                                                                                                                        |
| Start new game                     | UX   | Player can start a new game from the main menu.                                                                                                                                                        | When user clicks "New Game" button in main menu, a new crossword game starts with fresh grid being rendered on screen and clues being displayed.                                                                                                                                                                                               |
| Random words for crossword         | Sys  | The game uses a set of random words from different topics for the crossword generation.                                                                                                                | Each new game generates a unique crossword puzzle using randomly selected words from predefined word list.                                                                                                                                                                                                                                     |
| Scoring system                     | Sys  | Player scores points when correct word is guessed. The number of points scored equals to the count of letters in a correctly guessed word multiplied by 10.                                            | When player guesses a word correctly, score increases by number of points which equals the count of letters in the guesses word multiplied by 10. Example: guess word is TRAIN so player's score is bumped by 50 points.                                                                                                                       |
| Scoring system                     | Sys  | Player scores penalty points when auto-solves a clue. The number of points subtracted equals to the count of letters in a correctly guessed word multiplied by 10.                                     | When player auto-solves a clue, score is decreased by number of points which equals the count of letters in the word multiplied by 10. Example: guess word is APPLE so player's score is reduced by 50 points.                                                                                                                                 |
| Scoring system                     | Sys  | Player scores penalty points when auto-solves the entire crossword. The number of points subtracted equals to the count of letters in all unsolved words which have been auto-solved multiplied by 10. | When player auto-solves the entire crossword, score is decreased by number of points which equals to the total count of letters in all auto-solved words multiplied by 10. Example: user had two words 'GOLD' and 'IRON' still hidden and clicked 'Auto-solve' button so player's total score for the game is reduced by (4+4)*10 = 80 points. |
| HUD display                        | UI   | HUD shows current game state details like current score, guesses made, guesses remaining, overall guesses limit, words guessed, total words to be guessed.                                             | During gameplay, HUD is visible and is updated with the latest game state with current score, guesses made, guesses remaining, total guesses limit, words guessed and total words to be guessed.                                                                                                                                               |
| Gameboard rendering                | UI   | Gameboard is rendered on screen with words hidden horizontally and vertically, numbered for clues.                                                                                                     | When game starts, the crossword grid is displayed with numbered cells corresponding to clues.                                                                                                                                                                                                                                                  |
| Clue selection and word guessing   | UX   | Player can select a clue number and enter a word guess and then submit this word guess and get response whether the word was guessed correctly or not.                                                 | When player selects a clue number and inputs word guess, clicking "Check" validates the answer and provides response whether guess was correct or not. If a user guess a word correctly it is rendered onto the gameboard and player's score is updated as per the scroing logic.                                                              |
| Clue display                       | UI   | Clues for each word are displayed clearly alongside the gameboard.                                                                                                                                     | During gameplay, clues are visible and correspond to numbered words on the grid.                                                                                                                                                                                                                                                               |
| Auto-solve a clue with penalty     | UX   | Player can uncover an entire word hidden on the gameboard with a score penalty.                                                                                                                        | When player selects a clue number and clicks "Reveal Word" button, one word is revealed on the grid and score decreases according to the scroting logic.                                                                                                                                                                                       |
| Auto-solve crossword               | UX   | Player can click a button to auto-solve the whole crossword and getting penalty points for each word remaining hidden on the gameboard. This trigger Game Over state.                                  | When player clicks "Auto-Solve" button, entire crossword is revealed and score is decreased as per the scoring logic and Game Over screen is rendered.                                                                                                                                                                                         |
| Responsive design                  | UI   | The game is optimized for various screen sizes and devices.                                                                                                                                            | The game layout adjusts correctly on desktop, tablet, and mobile devices without loss of functionality.                                                                                                                                                                                                                                        |
| User management                   | Sys  | Player can create an account so that their scores and progress can be saved.                                                                                                   | Players can register with a username and password and optional email address.                                                                                                                                                                                                                                                                  |
| User management                   | Sys  | Player can log in to the game so that their scores and progress can be saved.                                                                                                   | Players log in with their previously registered username and password.                                                                                                                                                                                                         |

---


## Task 6 – Non-Functional Specifications

It is important to consider non-functional specifications as part of the overall specification for the crossword game.
We've identified the following non-functional specifications to be important for our game:

| Category | Specification                                           |
|-----------|---------------------------------------------------------|
| **Aesthetic** | Clean grid layout, minimal colours, modern typography.  |
| **Usability** | Simple controls and clear instructions.                 |
| **Responsiveness** | Works perfectly on desktop, tablet, and mobile.         |
| **Feedback** | Real-time indicators: green for correct, red for wrong. |
| **Performance** | Loads under 3 seconds, no noticeable lag.               |
| **Reliability** | Auto-saves progress locally in memory.                  |
| **Maintainability** | Code modular and well-commented for easy updates.       |

---

## Task 7 - Overall mockup

The following image represents the overall mockup of the crossword game application.

Main game:
<img width="1343" height="737" alt="image" src="https://github.com/user-attachments/assets/b4ff156f-47d9-4e59-aa3e-4a365e13d771" />

---

## Task 8 - Construct basic storyboards associated with the game-play/app use

The storyboard on how the application is going to function.
These are the preliminary storyboards and may be refined further as we progress with the project.

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

| Category                                      | Description                                                    | Mitigtion Strategy                                                                                                                                            |
|-----------------------------------------------|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lack of Coding Knowledge                      | Some people in this project may have different coding experience | Pair programming, online tutorials, team knowledge sharing.                                                                                                   |
| Dependencies on libraries                     | The project requires API for making the game more unique and random. If not, then it will be set values. Which may cause the user to become bored. | Create backend which will offer REST API and perform the overall heavy lifting of the game maintining game states, handling users, generating crosswords etc. |
| Presence of bugs which affect user experience | No amount of testing can make sure the final product will be bug free. Some things might be overlooked. | Thorough testing, user feedback loops, quick bug fixing cycles.                                                                                               |
| Scope creep                             | The project may become too big to handle for the three of us if we keep adding more and more features to the scope. | Mitigation: The scope should be frozen to MVP features only to ensure it can be delievered by the deadline.                                                   |


---

## Task 10 - Software development strategy 

We compared three software development strategies Waterfall, Agile and Rapid Application Development (RAD) as the main three candidates to select from a software development strategy for our project.

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

After careful consideration we've decided to go with RAD software development strategy for our project because of the following reasons:
1. Time sensitivity as the delivery has to happen by 3rd of Nov so the turnaround should be really fast to deliver the project.
2. Requires speed of delivery and flexibility which RAD perfectly provides.
3. Minimise upfront planning so we don’t need waterfall with its rigid planning and significant planning overhead.
4. Process-wise: we aim to hit the ground running by prototyping features, testing them by users, getting feedback and iterating fast.
5. In the first half of the project minimal documentation while fast prototyping. In the second half when things start to settle, spend time on documenting them to have everything documented by the submission deadline.
6. Risks are reduced through the constant user feedback so that pivoting can happen after each prototype. 
7. RAD works great for small teams and our team is small so RAD fits very well.
8. RAD also works well for teams with mixed experience levels as the more experienced members can help the less experienced ones.
9. RAD is good for small projects and our project is small in scope and also has to happen within a short span of time.
10. Outcome focus: deliver working prototype quickly and then iterate fast to implement all MVP features so that the game crystalises into its final version to be submitted.

---

## Task 11 - Overall Test Plan

### Overall test strategy

The overall test strategy for the Crossword game involves a combination of manual testing and automated unit tests to ensure the game functions correctly and meets user requirements.
Such combination of manual functional testing and unit tests covering the code allows us to achieve high quality of the software being developed such as our crossword game.

#### Manual Testing

Manual tests are going to be done on the frontend to test the user interface and user experience.
For the manual testing a range of test cases will be created to cover all the main user flows and edge cases.
The manual tests will cover the following areas:
1. Game start and main menu navigation.
2. Crossword grid rendering and clue display.
3. Word guessing and answer validation.
4. Scoring system and HUD updates.
5. Hint and auto-solve functionality.
6. Game win and game over screens.
7. User account creation and login.

The detailed manual test cases will be documented as part of the Activity 4 below.

#### Unit Tests

Unit tests are done on the backend to test the REST API endpoints, game logic, scoring etc.
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

# Activity 4 - Testing

## Home page, Register and Login Page Testing section
| What's being tested | Testing type | What it should do | What it actually done | Comments | Proof |
|-----------|-----------|-----------|-----------|-----------|-----------|
| Login/Register | Manual | Store data in crossword_session | Stores user id, username and security token | Data has been stored after login | <img width="1375" height="58" alt="image" src="https://github.com/user-attachments/assets/b632e42a-d65f-49ee-a09a-e30a85f53aa1" /> <img width="1384" height="59" alt="image" src="https://github.com/user-attachments/assets/58744c38-466b-4e1e-9eb5-3e56efb15095" /> |
| Play button | Manual | Takes user to the login page | Successfully took user to login page  | Button does take to login page | <img width="756" height="422" alt="image" src="https://github.com/user-attachments/assets/b010440b-76ee-403e-aea9-8690a313b2d3" /> | 
| Register storing data and encrypting password | Manual | When registering. It should store in the json file | Stored without issue | Stored in json file |  <img width="824" height="664" alt="image" src="https://github.com/user-attachments/assets/6c78fd84-7259-4c6f-8747-54935cb8baa7" /> <img width="832" height="181" alt="image" src="https://github.com/user-attachments/assets/c4f189d8-746a-4274-95dd-13b4091ba799" /> |
| How to play button | Manual | Show pop up of how to play | Showed pop up  | Showed pop up without issue | <img width="997" height="1008" alt="image" src="https://github.com/user-attachments/assets/f194bb09-a658-4649-882f-b83a2bafea27"/> |
| Register Invalidation | Manual | Error shows up saying fields must be filled out. email must have @ and end with .com | Inputting email without @ or .com invalidated the attempt. | Worked as intended | <img width="786" height="661" alt="image" src="https://github.com/user-attachments/assets/e48fac73-1982-47bd-bbcd-cbb1b4fb7a6d" /> |
| Register Invalidation 2 | Manual | Password must be longer than 6 letters and user name must be longer than 3 letters | Registering with password that less than 5 letters and not longer than 3 letters invalidated attempt to register | Worked as intended | <img width="731" height="579" alt="image" src="https://github.com/user-attachments/assets/59c244f6-f494-434e-bfe9-11aaafc662a6" /><img width="769" height="690" alt="image" src="https://github.com/user-attachments/assets/ae254987-3e75-4c73-8983-47aa9a5b9bf3" /> |
| Login takes you to play page | Manual | Takes you to play page | Took to play page when pressing play and login | Bug: When running the program for the first time. it takes you to the play page instantly. When starting new game bug occurs. |  <img width="1083" height="768" alt="image" src="https://github.com/user-attachments/assets/a61ce486-26bf-4fe5-958a-aecee2e1561b" /> |

## Play page Testing section
| What's being tested | Testing type | What it should do | What it actually done | Comments | Proof |
|-----------|-----------|-----------|-----------|-----------|-----------|
| Logining out | Manual | Logs you out | takes you to the login page and logs you out. | N/A | <img width="1083" height="768" alt="image" src="https://github.com/user-attachments/assets/a61ce486-26bf-4fe5-958a-aecee2e1561b" /> |
| New game | Manual | Pressing new game | error when pressing new game, takes you to login page then play page. Cannot start game due to not logging in | When pressing new game and not going to /register to go to /login. This error occurs. To fix this temporarily. Going to /register then login fixes it. Logging out works as well to fix it.| <img width="993" height="773" alt="image" src="https://github.com/user-attachments/assets/8cf838f2-ea7b-41b8-88d3-0da16f8c6b8f" /> |
| New game generation | Manual | Generates the words and grid when choosing difficulty | Generated words without issue.| Generated words just fine based on difficulties | <img width="364" height="474" alt="image" src="https://github.com/user-attachments/assets/7cd78e30-8c1b-4bfc-a7e8-5e55db62959d" /> <img width="887" height="559" alt="image" src="https://github.com/user-attachments/assets/32ff05fa-59ba-4072-a8b2-7f50c14ce477" /> <img width="818" height="321" alt="image" src="https://github.com/user-attachments/assets/d8ac01dd-9dd2-4a91-8ccd-809d00cafae1" /> |
| Grid generation when pressing new game | Manual | Generates grid when pressing new game based of difficulty | Chosen Difficulty: Medium. Generates 10 words | N/A | <img width="705" height="853" alt="image" src="https://github.com/user-attachments/assets/219a4b71-c006-414b-9a2c-22364b83dac8" /> |
| Auto solver deducting points when pressing button | Manual | Deducting the points when pressing "auto solve" | Deducted points when pressed "auto solve" | N/A | <img width="765" height="486" alt="image" src="https://github.com/user-attachments/assets/3c2e672f-fca2-443a-812c-15c2b4d1054a" /> |
| Submitting incorrect guess | Manual | Says incorrect and add  | Any incorrect answer increased the counter guesses made | N/A |  <img width="873" height="734" alt="image" src="https://github.com/user-attachments/assets/419c19ae-f0ab-44c0-b087-b7ea63120aab" /> |
| guessing the correct guess | Manual | inputting the correct guess and number. Fills the grid as well. | added points when guessing correctly. | No comments | <img width="883" height="489" alt="image" src="https://github.com/user-attachments/assets/697389a3-73e3-4024-9706-3d34460e697b" /> |
| Guessing the correct guess but inputting the wrong guess number | Manual | say incorrect | Said incorrect. | Worked as intended. | <img width="916" height="744" alt="image" src="https://github.com/user-attachments/assets/ab339171-d13d-4bb5-9a12-22bf19bb7d02" /> <img width="831" height="392" alt="image" src="https://github.com/user-attachments/assets/e221379c-1c1c-495e-be11-fcf0705acaee" />. The correct number <img width="831" height="392" alt="image" src="https://github.com/user-attachments/assets/6557151b-a465-401e-80c4-d3588c63a0a7" /> |
| Inputting nothing  | Manual | Shouldn't allow any guesses | didn't allow any guess| if the box is empty no guesses are made | <img width="840" height="412" alt="image" src="https://github.com/user-attachments/assets/85fbc9bf-7933-4fbe-8c31-7c95d3fd0016" /> |
| Placeholder | Manual | placeholder | placeholder | N/A | Add Picture here |
| Placeholder | Manual | placeholder | placeholder | N/A | Add Picture here |
| Placeholder | Manual | placeholder | placeholder | N/A | Add Picture here |




