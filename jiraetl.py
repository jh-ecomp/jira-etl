from base_model import build_db_session
from jira_requests import mount_jira_session, get_jira_issues
from my_jira_project import MyJiraProject
from db_connection import update_issues, search_issue

global jira_config


def get_jira_config():
    config_dict = {'domain': '', 'main_request': '', 'jql': '', 'fields': '', 'expand': '', 'start_at': '', 'max_results': ''}

    with open('jira.config', 'r') as config:
        while True:
            line = config.readline()
            if line == '# end':
                break
            if line == '\n' or line.startswith('#'):
                continue
            config_dict[line.split('#')[0]] = line.split('#')[1][0:-1]
    return config_dict


jira_config = get_jira_config()


def get_issues():
    jira_session = mount_jira_session(jira_config['domain'])
    if jira_session is not None:
        issues = get_jira_issues(jira_config, jira_session.cookies)
        jira_session.close()
    else:
        return None
    return issues


def process_issues(issues):
    processed_issues = list()
    for issue in issues:
        processed_issues.append(MyJiraProject.process_issue(issue))

    return processed_issues


def store_issues(issues):
    issues_to_update = list()
    alchemy_session = build_db_session()
    for issue in issues:
        try:
            issue_imported = search_issue(MyJiraProject().__tablename__, issue['id'])
            issue_parsed = MyJiraProject().parse(issue)
            if issue_imported is False:
                alchemy_session.add(issue_parsed)
            else:
                issues_to_update.append(issue_parsed)
            alchemy_session.commit()

        except Exception as e:
            issue_id = issue['id']
            print(f'Cannot Insert issue: {issue_id} on table {MyJiraProject().__tablename__} cause {e}')

    alchemy_session.close()

    if len(issues_to_update):
        update_issues(MyJiraProject.__tablename__, issues_to_update)
