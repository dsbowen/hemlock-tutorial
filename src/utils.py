from flask import url_for
from hemlock import User, Page
from hemlock.questions import Input, Label
from hemlock.utils.random import Assigner
from hemlock.utils.statics import make_figure

assigner = Assigner(
    {"image": ("code_quality", "wanna_see_the_code"), "mood": ("happy", "sad")}
)



@User.route("/survey")
def seed():
    assignment = assigner.assign_user()
    if assignment["image"] == "code_quality":
        img_src = url_for("static", filename="code_quality.png")
    else:
        img_src = "https://imgs.xkcd.com/comics/wanna_see_the_code.png"
        
    return [
        Page(
            Label(
                f"""
                Here is a vignette designed to put you in a {assignment['mood']} mood.
                """
            )
        ),
        Page(
            Input(
                f"""
                From 1 (not funny at all) to 5 (very funny), how funny is this image?
                {make_figure(img_src, figure_align="center")}
                """,
                input_tag={"type": "number", "min": 1, "max": 5}
            )
        ),
        Page(
            Label("Goodbye!")
        )
    ]
