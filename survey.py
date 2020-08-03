from hemlock import Branch, Check, Compile as C, Embedded, Input, Label, Page, Range, Select, Submit as S, Validate as V, route
from hemlock.tools import join

from datetime import datetime

@route('/survey')
def start():
    demographics_page = Page(
        Input(
            '<p>Enter your date of birth.</p>',
            placeholder='mm/dd/yyyy',
            var='DoB', data_rows=-1,
            validate=[V.require(), V.date_format()],
            submit=S.record_age()
        ),
        Check(
            '<p>Indicate your gender.</p>',
            ['Male', 'Female', 'Other'],
            var='Gender', data_rows=-1,
            validate=V.require()
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
            multiple=True, var='Race', data_rows=-1,
            validate=V.require()
        ),
        Select(
            '<p>Select your current marital status.</p>',
            [
                'Married',
                'Widowed',
                'Divorced',
                'Separated',
                'Never married',
            ],
            var='MaritalStatus', data_rows=-1
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
            min=0, max=10,
            var='SubjectiveSES', data_rows=-1
        ),
    )
    return Branch(
        demographics_page,
        Page(
            Label(compile=C.confirm(demographics_page)),
            back=True, terminal=True
        )
    )

@V.register
def date_format(inpt):
    try:
        # try to convert to a datetime object
        datetime.strptime(inpt.response, '%m/%d/%Y')
    except:
        # if this fails, the participant entered an invalid response
        return '<p>Format your date of birth as mm/dd/yyyy.</p>'

@S.register
def record_age(inpt):
    # calculate age in years
    date_of_birth = datetime.strptime(inpt.data, '%m/%d/%Y')
    age = (datetime.utcnow() - date_of_birth).days / 365.25
    # record age as embedded data
    inpt.page.embedded = [Embedded('Age', age, data_rows=-1)]

@C.register
def confirm(confirm_label, demographics_page):
    # get the participant's data from the demographics page
    demographics = [q.data for q in demographics_page.questions]
    # re-format the race demographic data
    race = demographics_page.questions[2]
    race = join('and', *(key for key in race.data if race.data[key]))
    demographics[2] = race
    # set the label based on the participant's demographics data
    confirm_label.label = '''
    <p>Confirm the following information:</p>
    <ul>
        <li>Date of birth: {}</li>
        <li>Gender: {}</li>
        <li>Race/Ethnicity: {}</li>
        <li>Marital status: {}</li>
        <li>Subjective socio-economic status: {}</li>
    </ul>
    <p>To correct this information, click '<<'.</p>
    '''.format(*demographics)