from hemlock import User, Page
from hemlock.questions import Label, Select
from sqlalchemy_mutable.utils import partial


@User.route("/survey")
def seed():
    pages = [
        Page(
            favorite_planet := Select(
                "Which planet do you like best?",
                ["Mercury", "Jupiter", "Mars"]
            )
        ),
        Page(
            label := Label()
        )
    ]
    favorite_planet.submit = partial(display_my_favorite_planet, label)
    return pages


def display_my_favorite_planet(favorite_planet, label):
    if favorite_planet.response == "Mars":
        label.label = f"No way! Mars is my favorite planet, too!"
    else:
        label.label = f"{favorite_planet.response} is pretty cool, but I like Mars better."
