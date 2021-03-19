from app import app
from app.users import view


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
