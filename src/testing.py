from hemlock import User, Page
from hemlock.questions import Input, Label, Select


@User.route("/survey")
def seed():
    return [
        Page(
            Input(
                "What did you want to grow up to be when you were a kid?",
                test_response="Astronaut"
            ),
            Select(
                "Which of these vegan burgers are you most likely to buy?",
                ["Beyond", "Impossible", "Morning star"],
                multiple=True,
                test_response=["Beyond", "Impossible"]
            )
        ),
        Page(
            Label("Goodbye!")
        )
    ]
    