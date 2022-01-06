from hemlock import User, Page
from hemlock.functional import validate
from hemlock.questions import Check, Input, Label
from sqlalchemy_mutable.utils import partial


@User.route("/survey")
def seed():
    return [
        Page(
            id_input := Input(
                "What is your MTurk ID?",
                input_tag={"required": True},
                test_response="test_id"
            ),
            Input(
                "Confirm your MTurk ID",
                test_response="test_id",
                validate=validate.compare_response(
                    id_input, feedback="MTurk IDs do not match."
                )
            )
        ),
        Page(
            resolved_to_lose_weight := Check(
                "Did you make a new year's resolution to lose weight?",
                [(1, "Yes"), (0, "No")]
            ),
            Input(
                "If so, how many pounds do you want to lose?",
                input_tag={"type": "number", "min": 0},
                validate=partial(require_if, resolved_to_lose_weight)
            )
        ),
        Page(
            Label("Goodbye!")
        )
    ]


def require_if(amount_input, resolved_to_lose_weight):
    if resolved_to_lose_weight.response and amount_input.response is None:
        return False, "Please enter how many pounds you want to lose."
