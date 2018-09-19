# Log-Analysis

This is an Udacity nanodegree full stack web development project

In this project you've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Getting started:

### Prerequisites:

  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Installing:
  1. Install Python3, Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file's name is newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/cmartinezBoada/Log-Analysis-Project)

#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:

  ```
    $ vagrant up
  ```
  2. Then Log into this using command:

  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant.

#### Setting up the database and Creating Views:

  1. Load the data in local database using the command:

  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.

  2. Use `psql -d news` to connect to database.
  * You can use in the command line : 
  
  ```
    \dt — display tables — lists the tables that are available in the database and 
    \d table — (replace table with the name of a table) — shows the database schema for that particular table.
  ```

  3. Create view article_view using:
  ```
    create view article_view as select title,author,count(*) as views from articles,log where
    log.path like concat('%',articles.slug) group by articles.title,articles.author
    order by views desc;
  ```
 
  4. Create author_view using: 
  ```
    create view as author_view as select name, sum(article_view.views) as total from article_view, authors where 
    authors.id=article_view, author group by authors.name order by total desc;
  ```  
  5. Create view error_log_view using:
  ```
    create view error_log_view as select date(time),round(100.0*sum(case log.status when '200 OK'
    then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time)
    order by "Percent Error" desc;
  ```
 * You can see all the views in the command line with this command: \dv

#### Running the queries:
  1. From the vagrant directory inside the virtual machine,run the python file logs_analysis.py using:
  ```
    $ python logs_analysis.py
  ```
  

