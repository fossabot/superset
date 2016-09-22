SQL Lab
=======

.. image:: _static/img/sqllab.gif
   :scale: 75 %

SQL Lab is a SQL IDE (interactive development environment) for SQL.

It features:

- multiple tabs as individual workspaces
- table and column metadata browsing, providing a reference while authoring
  queries
- viewing query results in a table view
- exposes an easy workflow to create rich visualizations out of arbitrary SQL
  using Caravel's visualization engine
- a per-tab query history, keeping track of previous iterations
- support for long running background sql statements as "CREATE TABLE AS"
- works with most database backends, allowing to query Impala, Presto,
  Hive, MySQL, Postgres, Vertica, Teradata, Oracle and pretty any
  SQL-speaking database you may have laying around
- a query search engine, allowing you to easily find that query you ran a
  few weeks ago, seeing who has been querying a table you created

Caravel's SQL Lab is growing within Airbnb to replace Airpal, a similar tool
focussed on querying Presto. Airpal has served us extremely well, democratizing
access to data internally, and its success built a strong case for SQL Lab.
The rational for integrating the Airpal use case
into Caravel is multifold.  The main reason was to enable a smooth flow from
arbitrary SQL to visualization, dashboarding and sharing. We also wanted to
allow support and centralize the tooling for database engines beyond Presto
which transcends Airpal's original mission.
Another benefit of having all of the data access within one platform is be
able to manage authentication, roles and permissions in a single tool.

Computationally intensive, long running queries are common in this petabyte
scale era, and SQL Lab is designed to provide a nice workflow for this use
case. By setting up an asynchronous backend, you can enable the CTAS
(create table as) feature, which will run your query and store the result
in a newly created table. You can then query and visualize data off of that
summary table. Note that we're planning to add even better support for long running
queries that won't require write access to the source database
in the near future.

SQL Lab makes it easy to expose internal databases to SQL speaking employees.
It a matter of filling in a form to register the database into Caravel, and
granting permissions to users through roles. While a Caravel user either has
full access to a database connection or no access at all,
it's possible for administrator to create different database users
(say one MySQL `all_read_write_access` user and one a `read_only_some_tables`
user) and expose them as different connections into Caravel.

On the Caravel side, individual databases can be set
to allow `CREATE TABLE AS` operation or not, and be instructed to target a
specified database schema when doing so. There's also a flag for defining
whether non-SELECT statements (UPDATE, DELETE, CREATE, ...) are allowed for that
database connection, where Caravel won't even attempt to run these statements.
