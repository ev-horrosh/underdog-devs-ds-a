from random import sample

import pandas as pd

from data_generators.data_options import *


class Mentor:
    """Mentor Schema"""

    def __init__(self):
        self.profile_id = generate_uuid(16)
        self.mentor_intake_id = None
        self.email = "fake@email.com"
        self.location = 'New York, New York'
        self.in_US = True
        self.name = f'{random_first_name()} {choice(last_names)}'
        self.current_comp = choice([
            "Boogle",
            "Amozonian",
            "Poptrist",
            "Macrohard",
            "Pineapple",
        ])
        self.tech_stack = choice(skill_levels)
        self.job_help = self.tech_stack == "Career Development"
        self.industry_knowledge = percent_true(90)
        self.pair_programming = percent_true(90)
        self.can_commit = True
        self.how_commit = 'String'
        self.other_info = "Notes"


class Mentee:
    """Mentee Schema"""

    def __init__(self):
        self.profile_id = generate_uuid(16)
        self.mentee_intake_id = None
        self.name = f'{random_first_name()} {choice(last_names)}'
        self.email = "fake@email.com"
        self.location = 'New York, New York'
        self.in_US = True
        self.formerly_incarcerated = percent_true(80)
        self.underrepresented_group = percent_true(70)
        self.low_income = percent_true(70)
        if self.formerly_incarcerated:
            self.list_convictions = sample(convictions, k=randint(1, 3))
        else:
            self.list_convictions = []
        self.convictions = ", ".join(self.list_convictions)
        self.tech_stack = choice(subjects)
        self.experience_level = choice(skill_levels)
        self.job_help = self.tech_stack == "Career Development"
        self.industry_knowledge = percent_true(15)
        if self.job_help:
            self.pair_programming = False
        else:
            self.pair_programming = percent_true(60)
        self.your_hope = "String"
        self.need = choice(resource_items)
        self.parole_restriction = percent_true(50)
        self.disability = choice(disability)
        self.work_status = choice(work_status)
        self.assistance = choice(receiving_assistance)
        self.other_info = "Notes"


class Resource:
    """ Creates Resource record """

    def __init__(self):
        self.need = choice(resource_items)
        self.item_id = generate_uuid(16)


class MenteeFeedback:
    """Create feedback record from mentee (randomly selected from Mentees Collection) to
    mentor (randomly selected from Mentors Collection), which is stored in Feedbacks Collection.
    1 mentee can give multiple feedbacks to 1 mentor."""
    feedback = pd.read_csv("review.csv", index_col="Id")

    def __init__(self, mentee_id, mentor_id):
        self.ticket_id = generate_uuid(16)
        self.mentee_id = mentee_id
        self.mentor_id = mentor_id
        self.feedback = choice(self.feedback["Review"])

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())


class Meeting:
    """Create dummy meeting record which is stored in
    meeting collection."""

    def __init__(self, mentee_id, mentor_id):
        self.meeting_id = generate_uuid(16)
        self.created_at = "2018-06-12T09:55:22"
        self.updated_at = "2018-06-12T09:55:22"
        self.meeting_topic = choice(topics)
        self.meeting_start_date = "2018-06-12T09:55:22"
        self.meeting_end_date = "2018-06-12T09:55:22"
        self.host_id = mentor_id
        self.attendee_id = mentee_id
        self.meeting_notes = "Meeting notes here!"
        self.meeting_missed = choice(['Missed', 'Attended'])

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())
