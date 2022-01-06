from hemlock import User, Page
from hemlock.questions import Check, Label
from hemlock.timer import Timer


@User.route("/survey")
def seed():
    days_ago = ["3 days ago", "2 days ago", "yesterday"]
    return [
        Page(
            *[
                Check(
                    f"How were you feeling {day}?",
                    ["Happy", "Sad", "Optimistic", "Pessimistic"],
                    multiple=True,
                    variable="mood"
                )
                for day in days_ago
            ],
            data=[("days_ago", days_ago)],
            timer=Timer("mood_seconds", fill_rows=True)
        ),
        Page(
            Label("Goodbye!")
        )
    ]
