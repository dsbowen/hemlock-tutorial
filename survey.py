from hemlock import Branch, Page, Label, route

@route('/survey')
def start():
    return Branch(
        Page(
            Label('<p>Hello, World!</p>'), 
            terminal=True
        )
    )