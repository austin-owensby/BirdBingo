import random
from sqlalchemy import Sequence, select
from app.database.database_models import Board, DrawHistory, get_engine
from app.services.birds_helper import birds
from sqlalchemy.orm import Session

class logic_service:
    def __init__(self):
        return
    
    def fetch_boards(self):
        """Returns all boards from the database"""
        engine = get_engine()
        with Session(engine) as session:
            query = select(Board)

            boards = session.scalars(query).all()

        return boards

    def fetch_draw_history(self):
        """Return the list of draw history"""

        # Query all draw history
        engine = get_engine()
        with Session(engine) as session:
            query = select(DrawHistory)

            draw_history = session.scalars(query).all()

        return draw_history

    def create_draw_history(self, name: str):
        """Add a Draw History to the database"""
        new_draw_history = DrawHistory(
            name = name
        )

        engine = get_engine()
        with Session(engine) as session:
            session.add(new_draw_history)
            session.commit()

    def clear_data(self, draw_history: Sequence[DrawHistory], boards: Sequence[Board]):
        # Check if there's anything to clear
        if (len(draw_history) + len(boards)) == 0:
            return
        
        # Delete all draw history
        engine = get_engine()
        with Session(engine) as session:
            for draw_history_item in draw_history:
                session.delete(draw_history_item)

            # Delete all boards
            for board in boards:
                session.delete(board)

            session.commit()

    def draw_card(self):
        """Based on drawn birds, randomly draw a new card then add that to the draw history"""
        
        # Query previously drawn birds from the database
        draw_history = self.fetch_draw_history()

        boards = self.fetch_boards()

        # Check for win condition before drawing
        winners = self.check_win_state(boards, draw_history)
        game_won = len(winners) > 0

        if game_won:
            raise Exception('The game has finished, please start a new game.')

        # Calculate the remaining birds to draw
        remaining_birds = set([bird['name'] for bird in birds]) - set([history.name for history in draw_history])

        # Check if there are no remaining birds (Shouldn't be possible unless we hit a race condition or someone is hitting the backend directly)
        if len(remaining_birds) == 0:
            raise Exception('No remaining birds are available to draw, please start a new game.')

        # Randomly choose a bird from our options
        drawn_bird: str = random.choice(list(remaining_birds))

        self.create_draw_history(drawn_bird)

    def check_win_state(self, boards: list[Board], draw_history: list[DrawHistory]):
        """Check if the game has been won"""

        # Check if there's enough data for a win
        if len(boards) == 0 or len(draw_history) < 5:
            return []
        
        # 5 horizontal wins, 5 vertical wins, 2 diagonal wins
        winningIndexes = [
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],
            [0, 5, 10, 15, 20],
            [1, 6, 11, 16, 21],
            [2, 7, 12, 17, 22],
            [3, 8, 13, 18, 23],
            [4, 9, 14, 19, 24],
            [0, 6, 12, 18, 24],
            [4, 8, 12, 16, 20],
        ]

        winners = []

        # Check each board
        for board in boards:
            # Get the indexes of the matches for the board
            indexes = []
            for i in range(25):
                if board.grid[i] in [draw_history_item.name for draw_history_item in draw_history]:
                    indexes.append(i)

            # Don't bother checking if we don't have enough matches on this board for a win
            if len(indexes) > 4:
                # Check each potential win
                for potentialWin in winningIndexes:
                    # Check if the board has a win in this way
                    if all(potentialWinIndex in indexes for potentialWinIndex in potentialWin):
                        # Update the list of winners and move on to the next board in case there are multiple winners at once
                        winners.append(board.owner)
                        break
    
        return winners

    def create_boards(self):
        """Generate a new list of boards"""
        # For now, we're assuming there is only ever these 4 teams.
        teams = [
            "Chaos and Affection",
            "Fire for Justice",
            "In the Box, Truth",
            "Learn Forever"
        ]

        new_boards = []

        for team in teams:
            random.shuffle(birds)
            selected_birds = birds[:25]

            new_board = Board(
                owner = team,
                grid = [bird['name'] for bird in selected_birds]
            )
            new_boards.append(new_board)

        engine = get_engine()
        with Session(engine) as session:
            session.add_all(new_boards)
            session.commit()

    def new_game(self):
        """Starts a new game of bingo"""
        draw_history = self.fetch_draw_history()

        boards = self.fetch_boards()

        winners = self.check_win_state(boards, draw_history)
        game_won = len(winners) > 0

        if not (game_won or len(boards) == 0):
            raise Exception('Finish the existing game before starting a new one')
        
        self.clear_data(draw_history, boards)
        self.create_boards()
