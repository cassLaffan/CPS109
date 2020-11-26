

class Board(object):

    def __init__(self,width: int,height: int):
        self.width = width 
        self.height = height
        self.board_space = [[ ' '  for x in range(0,width)] for y in range(0,height)]

    def __str__(self):
        out_string = ""
        out_string += ('-'*(self.width+2)) + '\n'
        for y in range(self.height):
            out_string +='|'
            for x in range(self.width):
                out_string += self.board_space[y][x]
            out_string +='|\n'
        out_string += ('-'*(self.width+2)) + '\n'
        
        return out_string

    def addWord(self,x: int,y: int,word: str):
        spaces = self.width
        if len(word) <= spaces-x:
            index_counter = x
            for char in word:
                self.board_space[y][index_counter] = char
                index_counter += 1
        else:
            print('The word cannot fit')



if __name__ == '__main__':
    my_board = Board(10,10)
    my_board.addWord(0,0,'apple')
    print(my_board)

