import operator
import sys

class Board:

    def __init__(self, board,dimension):
        self.board = board
        self.empty = [dimension-1, dimension-1]

    def __repr__(self):
        string = ''
        for row in self.board:
            for num in row:
                if len(str(num)) == 1:
                    string += '   ' + str(num)
                elif len(str(num)) > 1:
                    string += '  ' + str(num)
            string += '\n'
        return string

    def index_2d(self, v):
        try:
            return [(i,x.index(v)) for i,x in enumerate(self.board) if v in x]

            #for i, x in enumerate(self.board):
            #   if v in x:
            #        return (tuple((i, x.index(v))))
        except IndexError:
            print "please enter valid number from grid"

    def move(self,index_list):
        self.board[index_list[0]][index_list[1]],self.board[self.empty[0]][self.empty[1]] = self.board[self.empty[0]][self.empty[1]],self.board[index_list[0]][index_list[1]]
        self.empty = index_list

    def move_to_decide(self,a_list):
        try:
            a = map(operator.sub,tuple(self.empty),a_list)
            #print a
            mydict = [[1,0],[-1,0],[0,1],[0,-1]]
            if a in mydict:
                self.move(a_list)
            else :
                print "please enter valid nummber from grid "
            # mydict = {(1,0):self.move_up, (-1,0):self.move_down,(0,1):self.move_left,(0,-1):self.move_right }
            # mydict[tuple(a)]()
        except (KeyError,TypeError):
            print "please enter valid number from grid"



if __name__ =="__main__" :

    try:
        board_dimension = int(sys.argv[1]) if len(sys.argv) > 1 else 4
        range1 = board_dimension ** 2 - 1


        b = [range((range1-board_dimension*i),(range1-(board_dimension)*(i+1)),-1) for i in range(board_dimension)]
        b[board_dimension-1][board_dimension-1] = "*"
        if board_dimension % 2 == 0:
            b[board_dimension-1][board_dimension-2],b[board_dimension-1][board_dimension-3] = b[board_dimension-1][board_dimension-3],b[board_dimension-1][board_dimension-2]

        correct_Board = [range((i* board_dimension)+1,((i+1)*board_dimension)+1) for i in range(board_dimension)]
        correct_Board[board_dimension-1][board_dimension-1] = "*"

        board = Board(b,board_dimension)
        print board
        while (board):
            try:
                element_index = board.index_2d(int(raw_input(" enter element to be changed ")))[0]
                #print (element_index)
                board.move_to_decide(element_index)
                print board if board != correct_Board else "Congratulations you win"


            except (ValueError,IndexError):
                print "please enter valid number from grid"

    except (ValueError,NameError):
        print "please enter valid number"
