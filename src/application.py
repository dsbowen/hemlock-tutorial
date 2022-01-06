from hemlock import User, Page
from hemlock.questions import Input, Label


@User.route("/survey")
def seed():
    return [
        Page(
            Input("Where do you most want to go on holiday?")
        ),
        Page(
            Label("Goodbye!")
        )
    ]
