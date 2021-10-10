from datetime import datetime
from dateutil.parser import parse
from sqlalchemy import Column, String, Integer, TIMESTAMP, Date

from base_model import Base


class MyJiraProject(Base):
    __tablename__ = 'my_jira_project'

    id = Column(Integer, primary_key=True)
    jira_key = Column(String)
    project = Column(String)
    issuetype = Column(String)
    summary = Column(String)
    description = Column(String)
    priority = Column(String)
    priority_id = Column(Integer)
    issuelinks = Column(String)
    creator = Column(String)
    assignee = Column(String)
    reporter = Column(String)
    status = Column(String)
    status_category = Column(String)
    resolution = Column(String)
    created = Column(TIMESTAMP)
    updated = Column(TIMESTAMP)
    resolutiondate = Column(TIMESTAMP)
    duedate = Column(Date)
    duration = Column(Integer)

    def __str__(self):
        return "%r" % self.__dict__

    @classmethod
    def days_diference(cls, out_date, in_date):
        if out_date is None or in_date is None:
            return 0
        return round(abs((out_date - in_date).total_seconds()) / 86400, 4)

    @classmethod
    def parse(cls, issue_dict):
        issue = MyJiraProject()
        issue.id = issue_dict['id']
        issue.jira_key = issue_dict['jira_key']
        issue.project = issue_dict['project']
        issue.issuetype = issue_dict['issuetype']
        issue.summary = issue_dict['summary']
        issue.description = issue_dict['description']
        issue.priority = issue_dict['priority']
        issue.priority_id = issue_dict['priority_id']
        issue.issuelinks = issue_dict['issuelinks']
        issue.creator = issue_dict['creator']
        issue.assignee = issue_dict['assignee']
        issue.reporter = issue_dict['reporter']
        issue.status = issue_dict['status']
        issue.status_category = issue_dict['status_category']
        issue.resolution = issue_dict['resolution']
        issue.created = issue_dict['created']
        issue.updated = issue_dict['updated']
        issue.resolutiondate = issue_dict['resolutiondate']
        issue.duedate = issue_dict['duedate']
        issue.duration = issue_dict['duration']

        return issue

    @classmethod
    def process_issue(cls, issue):
        issue_dict = dict()
        issue_fields = issue['fields']

        issue_dict['id'] = issue['id']
        issue_dict['jira_key'] = issue['key']

        issue_dict['project'] = issue_fields['project']['key']
        issue_dict['issuetype'] = issue_fields['issuetype']['name']
        issue_dict['summary'] = issue_fields['summary']
        issue_dict['description'] = issue_fields['description']
        issue_dict['priority'] = issue_fields['priority']['name']
        issue_dict['priority_id'] = issue_fields['priority']['id']

        links = issue_fields['issuelinks']
        outward_issues = list()
        for link in links:
            try:
                outward_issues.append(link['outwardIssue']['key'])
            except:
                pass
        issue_dict['issuelinks'] = str(outward_issues).replace('\'', '')

        issue_dict['creator'] = issue_fields['creator']['displayName']

        issue_dict['assignee'] = None if issue_fields['assignee'] is None else issue_fields['assignee']['displayName']
        issue_dict['reporter'] = None if issue_fields['reporter'] is None else issue_fields['reporter']['displayName']
        issue_dict['status'] = issue_fields['status']['name']
        issue_dict['status_category'] = issue_fields['status']['statusCategory']['name']
        issue_dict['resolution'] = None if issue_fields['resolution'] is None else issue_fields['resolution']['name']

        issue_dict['created'] = parse(issue_fields['created'].split('+')[0])
        issue_dict['updated'] = parse(issue_fields['updated'].split('+')[0])
        resolutiondate = issue_fields['resolutiondate']
        if resolutiondate is not None:
            resolutiondate = resolutiondate.split('+')[0]
            issue_dict['resolutiondate'] = parse(resolutiondate)
            issue_dict['duration'] = cls.days_diference(issue_dict['created'], issue_dict['resolutiondate'])
        else:
            now = datetime.now().replace(microsecond=0)
            issue_dict['resolutiondate'] = None
            issue_dict['duration'] = cls.days_diference(issue_dict['created'], now)

        issue_dict['duedate'] = None if issue_fields['duedate'] is None else parse(issue_fields['duedate']).date()

        return issue_dict

