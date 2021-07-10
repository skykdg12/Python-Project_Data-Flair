import random # 필요한 함수 불러오기
import time

print("\nWelcome to Hangman game\n") 
name = input("Enter your name: ") # 이름 입력
print("Hello " + name + "! Best of Luck!") 
time.sleep(2) # 2초 후
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3) # 3초 후

def main(): 
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"] # 임의의 단어 입력
    word = random.choice(words_to_guess) # 랜덤으로 선택
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = [] # 이미 입력한 단어 리스트로 입력
    play_game = ""
    
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    
    while play_game not in ["Y", "N", "y", "n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    
    if play_game == "y" or "Y":
        main()
    elif play_game == "n" or "N":
        print("Thanks For Playing! We expect you back again!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5 # 횟수 제한
    guess = input("This is the Hangman Word: " + display + "Enter your guess: \n")
    guess = guess.strip() # 한 단어씩 나눔
    
    # 게임 조건 생성
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess]) # 시도한 단어들을 추가함
        index = word.find(guess) 
        word = word[:index] + "_" + word[index + 1:] # 유추한 단어와 임의로 선택된 단어 매칭
        display = display[:index] + guess + display[index + 1:] # 남은 단어 칸 표헌
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1 # 틀릴때 마다 횟수 상승
        
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + "guesses remaining\n")
            
        elif count == 2 :
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3 :
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4 :
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     o \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guesses remaining\n")
        elif count == 5 :
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     o\n"
                  "  |    /|\  \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed,word)
            play_loop()
    
    if word == '_' * length: # 정답일 경우
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    
    elif count != limit:
        hangman()

# 게임 실행 
main() 
hangman()