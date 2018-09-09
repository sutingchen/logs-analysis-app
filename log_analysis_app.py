#!/usr/bin/python3

import psycopg2
import bleach

DBNAME = "news"


def get_popular_articles(n):
    # Assign an initial value to 'limit'
    limit = 3
    try:
        # Check if n is a valid number
        limit = int(n)
    except ValueError:
        print("Could not convert parameter to an integer."
              "Get the 3 most popular articles.")

    articles = []
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("select articles.title, articles_ranking.view_count "
                  "from articles, articles_ranking "
                  "where articles_ranking.path "
                  "like CONCAT('/article/', articles.slug) limit {0};"
                  .format(bleach.clean(str(limit))))
        articles = c.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            db.close()
    return articles


def get_popular_authors():
    authors = []
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("select articles.author, authors.name, "
                  "sum(articles_ranking.view_count) as author_view_count "
                  "from articles_ranking, articles, authors "
                  "where CONCAT('/article/', articles.slug) = articles_ranking.path "
                  "and articles.author = authors.id "
                  "group by articles.author, authors.name "
                  "order by author_view_count desc;")
        authors = c.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            db.close()
    return authors


def get_date_of_error_gt_1():
    dates = []
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("select date, "
                  "round((error_count*100)::numeric/total_count, 2) as error_rate "
                  "from "
                  "(select date(log.time), count(*) as error_count, "
                  "total_view_by_date.total_view_count as total_count "
                  "from log, total_view_by_date "
                  "where log.status not like '%200%' "
                  "and date(log.time) = total_view_by_date.date "
                  "group by date(log.time), "
                  "total_count) as subq "
                  "where error_count::numeric/total_count > 0.01;")
        dates = c.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            db.close()

    return dates


# Helper functions for displaying log analysis
def display_popular_articles(rows):
    try:
        print('The most popular three articles of all time:')
        count = 1
        for row in rows:
            print('{0}. "{1}" - {2:,} views'.format(count, row[0], row[1]))
            count += 1
    except Exception as error:
        print(error)

    return


def display_popular_authors(rows):
    try:
        print("The most popular article authors of all time:")
        count = 1
        for row in rows:
            print("{0}. {1} - {2:,} views".format(count, row[1], row[2]))
            count += 1
    except Exception as error:
        print(error)

    return


def display_severe_errors_dates(rows):
    try:
        count = 1
        print("Dates having more than 1% of requests lead to errors:")
        for row in rows:
            print("{0}. {1:%B} {1:%d}, {1:%Y} - {2}% errors"
                  .format(count, row[0], row[1]))
    except Exception as error:
        print(error)

    return


if __name__ == "__main__":
    try:
        print("[Log Analysis]\n")
        display_popular_articles(get_popular_articles(3))
        print("\n")
        display_popular_authors(get_popular_authors())
        print("\n")
        display_severe_errors_dates(get_date_of_error_gt_1())
        print("\n")
    except Exception as error:
        print(error)

