'''
    Defines Player class, and subclasses Human and Minimax Player.
'''
import time
from time import time
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        print(board)
        return col, row


class MinimaxPlayer(Player):
    def __init__(self, symbol):
        self.depth =5
        self.move_time_total = 0
        self.total_moves = 0
        self.start_time = 0
        self.end_time = 0
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
    def average_move_time(self):
        return self.move_time_total / self.total_moves
        

    def MiniMax_Decision(self, board):
        self.start_time = time()
        val, move = self.Max_Value(board) 
        self.end_time = time()
        print("Time taken: ", self.end_time - self.start_time)
        self.move_time_total += self.end_time - self.start_time
        col = move[0]
        row = move[1]   
        self.total_moves += 1
        return col , row

    def Utility(self, board, turn):
        if turn == 0:
          return board.count_score(self.symbol) - board.count_score(self.oppSym)
        if turn == 1:
          return board.count_score(self.oppSym) - board.count_score(self.symbol)

    def Max_Value(self,board):
        if self.depth == 0 or not self.Successors(board, self.symbol):
            return self.Utility(board,0), None
        best_move = None
        val = float("-inf")

        for a in self.Successors(board, self.symbol):
            temp_board = board.clone_of_board()
            temp_board.play_move(a[0],a[1],self.symbol)
            self.depth -= 1
            v2, garbage = self.Min_Value(temp_board)
            self.depth += 1
            if v2 > val:
                val = v2
                best_move = a
        return val, best_move

    def Min_Value(self, board):
        
        if self.depth == 0 or not self.Successors(board, self.oppSym):
            return self.Utility(board,1), None
        val = float("inf")
        best_move = None
        for a in self.Successors(board, self.oppSym):
            temp_board = board.clone_of_board()
            temp_board.play_move(a[0],a[1],self.oppSym)
            self.depth -= 1
            v2, garbage = self.Max_Value(temp_board)
            self.depth += 1
            if v2 < val:
                val = v2
                best_move = a
        return val, best_move
    
    def Successors(self, board, symbol):
        return board.total_legal_moves_remaining(symbol)
        
    

    def get_move(self,board):
        col, row = self.MiniMax_Decision(board)
        return col, row
    


















#         function MINIMAX-SEARCH(game, state) returns an action
# player←game.TO-MOVE(state)
# value, move←MAX-VALUE(game, state)
# return move
# function MAX-VALUE(game, state) returns a (utility, move) pair
# if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
# v←−∞
# for each a in game.ACTIONS(state) do
# v2, a2←MIN-VALUE(game, game.RESULT(state, a))
# if v2 > v then
# v, move←v2, a
# return v, move
# function MIN-VALUE(game, state) returns a (utility, move) pair
# if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
# v←+∞
# for each a in game.ACTIONS(state) do
# v2, a2←MAX-VALUE(game, game.RESULT(state, a))
# if v2 < v then
# v, move←v2, a
# return v, move
      

       
        





