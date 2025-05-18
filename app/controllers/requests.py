from flask import redirect, request
from .. import app
from app.services.logic_service import logic_service

logic_service = logic_service()
    
@app.route("/api/draw-bird", methods=["POST"])
def draw_card():
    """Based on drawn birds, randomly draw a new card then add that to the draw history"""
    name = request.form['name']

    logic_service.draw_card(name)
    return redirect("/", code=302)

@app.route("/api/new-game", methods=["POST"])
def new_game():
    """Start a new bingo game"""
    logic_service.new_game()
    return redirect("/", code=302)
    
