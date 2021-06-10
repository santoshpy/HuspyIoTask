def read_sql(filename):
    with open('graph/sql/' + filename) as f:
        return f.read()
