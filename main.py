#!/usr/bin/env python
import sys
from match_to_proposal.crew import MatchToProposalCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'path_to_jobs_csv': './data/jobs.csv',
        'path_to_cv': '.data/cv.md'
    }
    MatchToProposalCrew().crew().kickoff(inputs=inputs)

