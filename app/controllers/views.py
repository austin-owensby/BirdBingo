from .. import app
from flask import render_template
from app.services.logic_service import logic_service

logic_service = logic_service()

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/")
def app():
    boards = logic_service.fetch_boards()
    draw_history = logic_service.fetch_draw_history()
    winners = logic_service.check_win_state(boards, draw_history)
    game_won = len(winners) > 0

    board_models = []

    for board in boards:
        board_model = {
            'owner': board.owner,
            'grid': [{'bird': bird, 'selected': any([draw_history_item.name == bird for draw_history_item in draw_history])} for bird in board.grid]
        }

        board_models.append(board_model)

    return render_template("app.html", boards=board_models, draw_history=draw_history, game_won=game_won, winners=winners)
