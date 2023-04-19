SpendHacker - Spend tracker for monthly budgeting

The Brief & App Capability:
- Create and edit merchants, e.g. Tesco, Amazon, ScotRail
- Create and edit tags for their spending, e.g. groceries, entertainment, transport
- Assign categories and merchants to a transaction, as well as an amount spent on each transaction
- Display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions
- Mark Merchants and Categories as deactivated, users will not be able to choose deactivated merchants/tags when creating a transaction
- Transactions have a timestamp, and transactions are sorted by the time they took place
- User can supply a budget, and the app alerts the user somehow when when they have gone over it
- User can filter their view of transactions, for example, to view all transactions by a Merchant or Category

Brief Constraints:
- No use of JavaScript, CSS frameworks (i.e. Bootstrap), Object Relational Mappers (i.e. ActiveRecord), or Authentication (assumes a logged in user)
- Must only be built (as it was) using Python, Flask, PostgreSQL/psycopg and HTML/CSS

To Run:
- Prerequisites = Python 3, SQL/Postgresql, Flask 
1. Open spend_tracker_project/db in the terminal 
2. Run 'psql -d spend_tracker -f spend_tracker.sql' to drop/create the tables and initialise the SQL script
3. Run 'python3 console.py' from the project root
4. Run 'flask run' from the same location
5. Open http://127.0.0.1:4999 in a browser (only fully tested in Chrome v112.0.5615.121)

Known Unresolved Bugs:
1. Transactions - When user filters transactions by category, it takes user back to the top of the transact page rather than anchored link to the view of transactions (hypothesis is that it needs JavaScript to work - out of scope of this project)
2. Account - When user enters a string with spaces i.e. "New York City" for their city, it populates correctly in the database, but the value displaying in the form only returns the first 'part' of that string up to the first space, i.e. "New"

Possible Extensions:
1. Tracking Budget By Time Period - Onus is currently on the user to set their budget for the period they are tracking (i.e. the month), it would be useful to allow the user to set a monthly (or other time interval budget) and then have it reset at that point, along with the 'amount tracked' for that period, without losing historical transactions
2. Open Banking - User has to import their own transactions, it would be far superior to import the user's spending through Open Banking APIs, although data cleansing would be required and may not be compatible with the tech stack this app is built upon