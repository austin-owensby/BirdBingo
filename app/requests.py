from sqlalchemy import select
from app.database.database_models import DrawHistory, get_session
from . import app
from app.birds_helper import birds
import random
    
@app.route("/api/draw-bird", methods=["POST"])
def draw_card():
    """Based on drawn birds, randomly draw a new card then add that to the draw history"""

    # Query previously drawn birds from the database
    session = get_session()
    query = select(DrawHistory.name)

    draw_history = session.scalars(query).all()

    # Calculate the remaining birds to draw
    remaining_birds = set([bird['name'] for bird in birds]) - set(draw_history)

    # Check if there are no remaining birds (Shouldn't be possible unless we hit a race condition or someone is hitting the backend directly)
    if len(remaining_birds) == 0:
        return 'No remaining birds are available to draw, please start a new game.', 400

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