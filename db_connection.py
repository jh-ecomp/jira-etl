import psycopg2


def get_line_attr(line):
    return line[:-1].split('=')[1]


def get_connection():
    user = 'fake_user'
    password = 'not_a_real_password'
    with open('database.config', 'r') as db:
        db.readline()   # skip database_path line
        schema = get_line_attr(db.readline())
        dbname = get_line_attr(db.readline())
        host = get_line_attr(db.readline())
        port = get_line_attr(db.readline())

    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port)
    except Exception as e:
        print(e)
        connection = None

    return connection, schema


def search_issue(table, issue_id):

    conn, schema = get_connection()
    if conn is None:
        return None

    cur = conn.cursor()

    command = f'''SELECT exists (SELECT 1 FROM {schema}.{table} WHERE id={issue_id})'''
    cur.execute(command)
    result = cur.fetchone()

    return result[0]    # the result is a Tuple, so we need to take only first position


def generate_update_sttm(schema, table, issue):
    return f'''UPDATE {schema}.{table}
    SET summary='{issue.summary}',description='{issue.description}',priority='{issue.priority}',
    priority_id={issue.priority_id},issuelinks='{issue.issuelinks}',assignee='{issue.assignee}',
    reporter='{issue.reporter}',status='{issue.status}',status_category='{issue.status_category}',
    resolution='{issue.resolution}',updated='{issue.updated}',resolutiondate='{issue.resolutiondate}',
    duedate='{issue.duedate}',duration={issue.duration}
    WHERE id={issue.id}'''


def update_issues(table, update_issues):
    conn, schema = get_connection()
    if conn is not None:
        cur = conn.cursor()
        for issue in update_issues:
            cur.execute(generate_update_sttm(schema, table, issue))
            # print(generate_update_sttm(schema, table, issue))
        conn.commit()
        cur.close()
        conn.close()

