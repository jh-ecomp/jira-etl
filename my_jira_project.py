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

