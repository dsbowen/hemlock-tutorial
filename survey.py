from hemlock import Branch, Check, Input, Page, Label, Range, Select, route

@route('/survey')
def start():
    return Branch(
        Page(
            Input(
                '<p>Enter your date of birth.</p>',
                placeholder='mm/dd/yyyy'
            ),
            Check(
                '<p>Indicate your gender.</p>',
                ['Male', 'Female', 'Other']
            ),
            Check(
                '<p>Indicate your race or ethnicity. Check as many as apply.</p>',
                [
                    'White',
                    'Black or African-American',
                    'Asian',
                    'Native Hawaiian or other Pacific Islander',
                    'Other',
                ],
                multiple=True
            ),
            Select(
                '<p>Select your current marital status.</p>',
                [
                    'Married',
                    'Widowed',
                    'Divorced',
                    'Separated',
                    'Never married',
                ]
            ),
            Range(
                '''
                <p>At the right end of the scale are the people who are the 
                best off; those who have the most money, the most 
                education, and the best jobs. On the left are the people 
                who are the worst off; those who have the least money, the 
                least education, and the worst jobs (or are unemployed). 
                Please indicate where you think you stand on this scale.</p>
                ''',
                min=0, max=10
            ),
        ),
        Page(
            Label('<p>Thank you for completing this survey.</p>'), 
            terminal=True
        )
    )