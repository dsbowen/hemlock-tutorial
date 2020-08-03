from hemlock import Branch, Check, Compile as C, Page, Label, Submit as S, route
from hemlock.tools import comprehension_check

@route('/survey')
def start():
    return Branch(
        *comprehension_check(
            instructions=Page(
                Label('<p>Here are some instructions.</p>')
            ),
            checks=Page(
                Check(
                    '<p>Select the correct choice.</p>',
                    ['Correct', 'Incorrect', 'Also incorrect'],
                    compile=[C.clear_response(), C.shuffle()],
                    submit=S.correct_choices('Correct')
                )
            ),
            attempts=3
        ),
        Page(
            Label('<p>You passed the comprehension check!</p>'),
            terminal=True
        )
    )