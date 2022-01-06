from random import random

from hemlock import User, Page
from hemlock.questions import Input, Label

EASY_ANSWER = "42"
HARD_ANSWER = "88"
REALLY_HARD_ANSWER = "76"


@User.route("/survey")
def seed():
    return [
        Page(
            Input(
                f"The correct answer to this easy question is '{EASY_ANSWER}'.",
                # 70% of test users will get this correct
                test_response=EASY_ANSWER if random() < .7 else "incorrect_answer"
            ),
            navigate=make_hard_branch
        ),
        Page(
            Label("Goodbye!")
        )
    ]


def make_hard_branch(page):
    # ask the harder questions if and only if the user got the easy question correct
    if page.questions[0].response != EASY_ANSWER:
        return []

    return [
        Page(
            Input(
                f"The correct answer to this hard question is '{HARD_ANSWER}'.",
                # 70% of test users get this correct
                test_response=HARD_ANSWER if random() < .7 else "incorrect_answer"
            ),
            navigate=make_really_hard_branch
        )
    ]


def make_really_hard_branch(page):
    if page.questions[0].response != HARD_ANSWER:
        return []

    return [
        Page(
            Input(f"The answer to this really hard question is '{REALLY_HARD_ANSWER}'.")
        )
    ]
