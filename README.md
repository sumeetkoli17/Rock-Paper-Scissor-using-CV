# Rock Paper Scissors AI Game

This is a computer vision-based **Rock-Paper-Scissors** game where a player competes against an AI. The AI learns from the player's past moves and predicts the next move to increase its chances of winning. The game utilizes **OpenCV**, **cvzone**, and **MediaPipe** for hand tracking.

## Features
- Hand gesture recognition for Rock (✊), Paper (🖐), and Scissors (✌)
- AI that adapts to the player's moves using a simple prediction model
- Score tracking system (first to 10 wins)
- Smooth UI overlay with a custom background
- Restart functionality when a player reaches 10 points


## How to Run
```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install -r requirements.txt
python game.py
```

## Controls
```plaintext
'S' - Start the game
'Q' - Quit the game
```

## How the Game Works
```plaintext
1. The camera captures the player's hand.
2. The hand tracking module detects the gesture.
3. The AI predicts the player's move based on previous patterns.
4. The AI selects a counter-move to maximize its chances of winning.
5. The game continues until a player reaches 10 points.
6. The winner is displayed, and the game resets automatically.
```

## File Structure
```plaintext
|-- assets/         # Images for AI moves and background
|-- game.py         # Main game script
|-- requirements.txt # Required dependencies
|-- README.md       # Documentation
```

## Possible Enhancements
```plaintext
- Improve AI prediction using machine learning techniques.
- Add a GUI interface instead of OpenCV overlays.
- Include sound effects for a more interactive experience.
```

## Author
```plaintext
Sumeet Koli
```
