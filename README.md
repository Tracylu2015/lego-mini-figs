# lego-mini-figs

# Set DATABASE_URL environment variable

export DATABASE_URL=mysql+pymysql://root:rootroot@localhost:3306/minifigs

# Init database

flask db init
flask db migrate
python import_db.py

# Update the project

pip freeze > requirements.txt
pip3 install -r requirements.txt # team members need to install this document
