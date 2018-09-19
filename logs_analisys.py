import psycopg2
DB_NAME = "news"


def connect():
    return psycopg2.connect("dbname=news")

# 1. What are the most popular three articles of all time?
query1 = "select title, views from article_view limit 3"

# 2. Who are the most popular article authors of all time?
query2 = "select * from author_view"

# 3. On which days did more than 1% of requests lead to errors?
query3 = "select * from error_log_view where \"Percent Error\" > 1"


def popular_articles(query1):
    db = connect()
    c = db.cursor()
    c.execute(query1)
    results = c.fetchall()
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print('\t' + '%s--%d' % (title, views))
    db.close()


def popular_authors(query2):
    db = connect()
    c = db.cursor()
    c.execute(query2)
    results = c.fetchall()
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        print('\t' + '%s--%d' % (name, views))
    db.close()


def percent_error(query3):
    db = connect()
    c = db.cursor()
    c.execute(query3)
    results = c.fetchall()
    for i in range(len(results)):
        date = results[i][0]
        err_prc = results[i][1]
        print ('\t' + str(date) + ' ---> ' + str(err_prc) + ' %')

if __name__ == "__main__":
    print("1. The list of the three most popular articles are:")
    popular_articles(query1)
    print("\n"+"2. The list of the most popular authors are:")
    popular_authors(query2)
    print("\n"+"3. On which days did more than 1% of requests\
    lead to errors?:")
    percent_error(query3)
