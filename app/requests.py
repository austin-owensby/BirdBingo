import http
import json
from sqlalchemy import select
from app.database.database_models import Board, DrawHistory, get_session
from . import app
from app.birds_helper import birds
import random
    
@app.route("/api/draw-bird", methods=["POST"])
def draw_card():
    """Based on drawn birds, randomly draw a new card then add that to the draw history"""

    # TODO check for win condition before drawing

    # Query previously drawn birds from the database
    session = get_session()
    query = select(DrawHistory.name)

    draw_history = session.scalars(query).all()

    # Calculate the remaining birds to draw
    remaining_birds = set([bird['name'] for bird in birds]) - set(draw_history)

    # Check if there are no remaining birds (Shouldn't be possible unless we hit a race condition or someone is hitting the backend directly)
    if len(remaining_birds) == 0:
        return 'No remaining birds are available to draw, please start a new game.', http.HTTPStatus.BAD_REQUEST

    # Randomly choose a bird from our options
    drawn_bird: str = random.choice(list(remaining_birds))

    # Save the drawn bird to the database
    new_draw_history = DrawHistory(
        name = drawn_bird
    )

    session.add(new_draw_history)
    session.commit()

    # Return the drawn bird to the frontend
    return drawn_bird

@app.route("/api/draw-history", methods=["GET"])
def get_draw_history():
    """Return the list of draw history"""

    # Query all draw history
    session = get_session()
    query = select(DrawHistory.name)

    draw_history = session.scalars(query).all()

    return draw_history

@app.route("/api/boards", methods=["GET"])
def get_boards():
    """Return the list of boards"""

    # Query all boards
    session = get_session()
    query = select(Board)

    boards = session.scalars(query).all()

    return [board.to_dict() for board in boards]

@app.route("/api/new-game", methods=["POST"])
def new_game():
    """Start a new bingo game"""
    # TODO check if game has finished before starting a new one

    # Query all draw history
    session = get_session()
    draw_query = select(DrawHistory)

    draw_history = session.scalars(draw_query).all()

    # Delete all draw history and save
    for draw_history_item in draw_history:
        session.delete(draw_history_item)

    session.commit()

    # Query all boards
    session = get_session()
    board_query = select(Board)

    boards = session.scalars(board_query).all()

    # Delete all boards and save
    for board in boards:
        session.delete(board)

    session.commit()

    # Create new boards
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

    session.add_all(new_boards)

    session.commit()

    return [board.to_dict() for board in new_boards]
