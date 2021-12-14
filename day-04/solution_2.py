import numpy as np
import re
from pprint import pprint

'''
Results of test should be:
    last Bingo at board: 1 by num: 13
    The summation of the board is: 148, bingoed by num: 13
    Final results: 1924
Results of input should be: 
    last Bingo at board: 34 by num: 99
    The summation of the board is: 170, bingoed by num: 99
    Final results: 16830
    
'''

def get_data(file_path):
    '''
        return:
            numbers: numbers to check the boards on
            data: all the boards values as a single list
    '''

    with open(file_path, 'r') as file:
        # Getting numbers
        numbers = file.readline().strip().split(',')
        data = []
        for line in file.readlines():
            if line != '\n':
                for val in line.split():
                    if val != ' ':
                        data.append(val)

    return numbers, data


def check_num(places, is_checked):
    '''
    Desc:
        Mark a number as checked in boards
    Return:
        - The board index, column or row, idx if it's bingo
        - None if it isn't bingo
    '''

    for place in places:
        #checking number position
        board_idx, row_idx, column_idx = place
        is_checked[board_idx, row_idx, column_idx] = 1

        ## Check if there is a bingo or not
        row = is_checked[board_idx, row_idx, :]
        column = is_checked[board_idx, :, column_idx]

        if 0 not in row:
            marked_list[board_idx] = 1

            if 0 not in marked_list:
                return board_idx

        if 0 not in column:
            marked_list[board_idx] = 1         

            if 0 not in marked_list:
                return board_idx

    return None


def sum_unmarked(board, marked_board):
    summation = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if marked_board[i, j] == 0:
                summation += int(board[i, j])

    return summation


def main():
    #getting the data
    numbers, data = get_data('input.txt') 
    global boards_len 
    boards_len = len(data) // 25

    boards = np.array(data).reshape(boards_len, 5, 5)
    marked_board = np.zeros(boards.shape, dtype='int')
    
    global marked_list
    marked_list = np.zeros(boards_len)

    print(len(boards))

    bingo_num = None
    for num in numbers:
        places = np.argwhere(boards == num)
        bingo = check_num(places, marked_board)

        if bingo != None:
            board_idx = bingo
            bingo_num = num
            
            print(f"last Bingo at board: {board_idx} by num: {num}")
            break

    board_sum = sum_unmarked(boards[board_idx], marked_board[board_idx])

    print(f"The summation of the board is: {board_sum}, bingoed by num: {bingo_num}")
    print(f"Final results: {board_sum * int(bingo_num)}")

if __name__ == '__main__':
    main()