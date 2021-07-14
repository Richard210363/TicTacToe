import unittest
import tictactoe as ttt

class test_tictactoe(unittest.TestCase):

    def setUp(self):

        X = self.X = "X"
        O = self.O = "O"
        EMPTY = self.EMPTY = None

        self.board =    [
                        [X, O, X],
                        [X, O, EMPTY],
                        [EMPTY, EMPTY, EMPTY]
                        ]

    def test_foo(self):
        result = "O"
        assert result == "O"


    def test_Player(self):
       
        #Arrange

        #Act
        result = ttt.player(self.board)

        ##Assert
        assert result == "O"

    def test_Actions(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY

        #Act
        result = ttt.actions(self.board)

        #Assert
        assert result == {(1,2),(2,0),(2,1),(2,2)}

    def test_Result(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        amandedBoard =      [
                            [X, O, X],
                            [X, O, EMPTY],
                            [EMPTY, O, EMPTY]
                            ] 


        #Act
        result = ttt.result(self.board, (2,1))

        #Assert
        assert result == amandedBoard

    def test_Winner_Case01(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [X, X, X],
                        [X, O, EMPTY],
                        [EMPTY, O, EMPTY]
                        ] 

        #Act
        result = ttt.winner(XWinsBoard)

        #Assert
        assert result == X

    def test_Winner_Case02(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [O, O, X],
                        [X, X, X],
                        [O, EMPTY, EMPTY]
                        ] 

        #Act
        result = ttt.winner(XWinsBoard)

        #Assert
        assert result == X

    def test_Winner_Case03(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [O, O, X],
                        [O, O, X],
                        [X, X, X]
                        ] 

        #Act
        result = ttt.winner(XWinsBoard)

        #Assert
        assert result == X

    def test_Winner_Case04(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [X, O, O],
                        [X, O, X],
                        [X, X, X]
                        ] 

        #Act
        result = ttt.winner(XWinsBoard)

        #Assert
        assert result == X

    def test_Winner_Case05(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [O, X, O],
                        [X, X, O],
                        [X, X, X]
                        ] 

        #Act
        result = ttt.winner(XWinsBoard)

        #Assert
        assert result == X

    def test_Winner_Case06(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [O, X, X],
                        [X, O, X],
                        [X, O, X]
                        ] 

        #Act
        result = ttt.winner(XWinsBoard)

        #Assert
        assert result == X

    def test_Winner_Case07(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [X, O, O],
                        [O, X, O],
                        [O, O, X]
                        ] 

        #Act
        result = ttt.winner(XWinsBoard)

        #Assert
        assert result == X

    def test_Winner_Case08(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [O, O, X],
                        [O, X, O],
                        [X, O, O]
                        ] 

        #Act
        result = ttt.winner(XWinsBoard)

        #Assert
        assert result == X


    def test_terminal_Case01(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        GameOverNoWinner =  [
                            [O, X, O],
                            [X, X, O],
                            [X, O, X]
                            ] 

        #Act
        result = ttt.terminal(GameOverNoWinner)

        #Assert
        assert result == True

    def test_terminal_Case02(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        GameOverXWinS = [
                        [O, O, X],
                        [O, X, O],
                        [X, O, O]
                        ] 

        #Act
        result = ttt.terminal(GameOverXWinS)

        #Assert
        assert result == True

    def test_terminal_Case03(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        NotGameOver =   [
                        [O, O, X],
                        [O, X, O],
                        [EMPTY , O, O]
                        ] 

        #Act
        result = ttt.terminal(NotGameOver)

        #Assert
        assert result == False

    def test_utility_Case01(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        XWinsBoard =    [
                        [X, X, X],
                        [X, O, EMPTY],
                        [EMPTY, O, EMPTY]
                        ] 

        #Act
        result = ttt.utility(XWinsBoard)

        #Assert
        assert result == 1

    def test_utility_Case02(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        OWinsBoard =    [
                        [O, X, X],
                        [X, O, EMPTY],
                        [EMPTY, O, O]
                        ] 

        #Act
        result = ttt.utility(OWinsBoard)

        #Assert
        assert result == -1

    def test_utility_Case03(self):

        #Arrange
        X=self.X
        O=self.O 
        EMPTY = self.EMPTY
        GameOverNoWinner =  [
                            [O, X, O],
                            [X, X, O],
                            [X, O, X]
                            ] 

        #Act
        result = ttt.utility(GameOverNoWinner)

        #Assert
        assert result == 0