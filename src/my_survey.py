from flask_login import current_user
from hemlock import User, Page, utils
from hemlock.functional import compile, validate, test_response
from hemlock.questions import Check, Input, Label, Range, Select, Textarea
from sqlalchemy_mutable.utils import partial


@User.route("/survey")
def seed():
    return [
        Page(
            Label("Hello, world!")
        ),
        Page(
            Label("Goodbye, world!")
        )
    ]
