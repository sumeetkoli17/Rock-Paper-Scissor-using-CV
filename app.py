import cv2
import random
import cvzone # type: ignore
from cvzone.HandTrackingModule import HandDetector
import time
from collections import deque

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, Player]

# Track player's previous moves
player_history = deque(maxlen=5)  # Stores last 5 moves

def predict_player_move():
    if not player_history:
        return random.randint(1, 3)  # Default to random if no history
    
    most_common = max(set(player_history), key=player_history.count)
    
    # AI chooses the move that beats the most common move
    counter_moves = {1: 2, 2: 3, 3: 1}  # Rock->Paper, Paper->Scissors, Scissors->Rock
    return counter_moves[most_common]

while True:
    imgBG = cv2.imread("assets/BG.png")
    if imgBG is None:
        print("Error: Background image not loaded. Please check the file path.")
        exit()
    
    success, img = cap.read()
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]
    
    hands, img = detector.findHands(imgScaled)
    
    if startGame:
        if not stateResult:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            
            if timer > 3:
                stateResult = True
                timer = 0
                
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1  # Rock
                    elif fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2  # Paper
                    elif fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3  # Scissors
                    
                    if playerMove:
                        player_history.append(playerMove)
                    
                    aiMove = predict_player_move()
                    imgAI = cv2.imread(f'assets/{aiMove}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
                    

                    # Player Wins
                    if (playerMove == 1 and aiMove == 3) or \
                            (playerMove == 2 and aiMove == 1) or \
                            (playerMove == 3 and aiMove == 2):
                        scores[1] += 1
 
                    # AI Wins
                    if (playerMove == 3 and aiMove == 1) or \
                            (playerMove == 1 and aiMove == 2) or \
                            (playerMove == 2 and aiMove == 3):
                        scores[0] += 1

                    # Check if anyone reached max score
                    if scores[0] == 10 or scores[1] == 10:
                        winner = "Player" if scores[1] == 10 else "AI"
                        cv2.putText(imgBG, f"{winner} Wins! Restarting Game...", (300, 300), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 4)
                        cv2.imshow("Game", imgBG)
                        cv2.waitKey(3000)  # Show message for 3 seconds
                        scores = [0, 0]  # Reset Scores
                        startGame = False

    imgBG[234:654, 795:1195] = imgScaled
    
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
    
    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    
    cv2.imshow("Game", imgBG)
    
    key = cv2.waitKey(1)
    if key in [ord('q'), ord('Q')]:
        break
    
    if key in [ord('s'), ord('S')]:
        startGame = True
        initialTime = time.time()
        stateResult = False

cap.release()
cv2.destroyAllWindows()