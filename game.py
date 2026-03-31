import streamlit as st
import numpy as np

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3,3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False

def check_winner(b):
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"
    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"
    if not 0 in b:
        return "DRAW"
    return None

def make_move(row, col):
    if st.session_state.board[row, col] == 0 and not st.session_state.game_over:
        st.session_state.board[row, col] = st.session_state.current
        result = check_winner(st.session_state.board)

        if result:
            st.session_state.game_over = True
            st.session_state.result = result
        else:
            st.session_state.current *= -1

def get_symbol(val):
    return "X" if val == 1 else "O" if val == -1 else " "

# UI
st.title("Tic Tac Toe 🎮")

# Display grid
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.button(get_symbol(st.session_state.board[i][j]), key=f"{i}-{j}"):
                make_move(i, j)

# Show result
if st.session_state.game_over:
    if st.session_state.result == "DRAW":
        st.write("🤝 It's a Draw!")
    else:
        st.write(f"🏆 {st.session_state.result} Wins!")

# Restart button
if st.button("Restart Game"):
    st.session_state.board = np.zeros((3,3), dtype=int)
    st.session_state.current = 1
    import numpy as np
    import streamlit as st
    
    st.session_state.game_over = False
    

board = np.zeros((3,3),dtype=int)




def print_board(b):
    symbols = {0:" ",1: "X", -1: "O"}
    for r in range(3):
        row = "  | ".join(symbols[val] for val in b[r])
        print(" " + row)
        if r > 2:
            print("---+---+---")
            print()

def check_winner(b):
    if 3 in np.sum(b,axis = 1) or 3 in np.sum(b,axis = 0):
        return"x"
    if -3 in np.sum(b,axis = 1) or -3 in np.sum(b,axis = 0):
        return"O"
    
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "x"

    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"
    
    if not 0 in b:
        return "DRAW"
        return None
    
    current = 1
    print("Welcome to Tic Tac tow")


    print_board(board)
    while True:
        if current == 1:
            player = "x"
        else:
            player = "O"


        try:
            row = int(input(player + " - Enter row(0,1,2)"))    
            col = int(input(player + " - Enter column(0,1,2)")) 

        except ValueError:
            print("please Enter numbers only \n")
            continue

        if row < 0 or row > 2 or col <0 or col > 2:
            print("row and column must be between o and 2")

        if board[row,col] != 0:
            print("cell is already taken")

        board[row,col] = current
        print_board(board)

        result = check_winner(board)

        if result is None:
            if result == "DRAW":
                print("ohoo its a draw")
            else:
                print(result,"wins")

            break
        if current == 1:
            current = -1
        else:
            current = 1


