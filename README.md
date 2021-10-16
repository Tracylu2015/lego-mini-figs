# lego-mini-figs

# Set DATABASE_URL environment variable
export DATABASE_URL=mysql+pymysql://root:rootroot@localhost:3306/minifigs

# Init database
flask db init
flask db migrate

