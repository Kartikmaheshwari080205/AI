import copy
import random
from game.go import Board

class Agent2:
    
    def __init__(self, color, simulations=100):
        self.color = color.upper()
        self.simulations = simulations

    def random_playout(self, board, color):
        current_color = color
        while board.winner is None:
            actions = board.get_legal_actions()
            if not actions:
                break
            move = random.choice(actions)
            board.put_stone(move)
        return board.winner

    def get_action(self, board: Board):
        legal_actions = board.get_legal_actions()
        if not legal_actions:
            return None
        move_scores = {a: 0 for a in legal_actions}
        for move in legal_actions:
            for _ in range(self.simulations):
                sim_board = copy.deepcopy(board)
                sim_board.put_stone(move)
                winner = self.random_playout(sim_board, 'B' if self.color=='W' else 'W')
                if winner == self.color:
                    move_scores[move] += 1
        best_move = max(move_scores, key=move_scores.get)
        return best_move
