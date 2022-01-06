from hemlock import User, Page
from hemlock.questions import Check, Input, Label
from sqlalchemy_mutable.utils import partial


@User.route("/survey")
def seed():
    return [
        Page(
            resolved_to_lose_weight := Check(
                "Did you make a new year's resolution to lose weight?",
                [(1, "Yes"), (0, "No")]
            ),
            weight_loss_amount := Input(
                "If so, how many pounds do you want to lose?",
                input_tag={"type": "number", "min": 0}
            )
        ),
        Page(
            Label(
                compile=partial(make_label, resolved_to_lose_weight, weight_loss_amount)
            )
        )
    ]


def make_label(input, resolved_to_lose_weight, weight_loss_amount):
    if resolved_to_lose_weight.response:
        input.label = f"Good luck reaching your goal of losing {weight_loss_amount.response} pounds!"
    else:
        input.label = "Congratulations on being at your target weight!"
