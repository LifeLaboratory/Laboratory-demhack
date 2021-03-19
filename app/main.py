from app import app
from app.users import view
from app.person import view
from app.rating import view


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
