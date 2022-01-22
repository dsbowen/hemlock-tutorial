import os

if (survey_name := os.getenv("SURVEY_NAME", "my_survey")) == "my_survey":
    from . import my_survey
elif survey_name == "application":
    from . import application
elif survey_name == "testing":
    from . import testing
elif survey_name == "data":
    from . import data
elif survey_name == "compile":
    from . import compile
elif survey_name == "validate":
    from . import validate
elif survey_name == "submit":
    from . import submit
elif survey_name == "navigate":
    from . import navigate
elif survey_name == "utils":
    from . import utils
