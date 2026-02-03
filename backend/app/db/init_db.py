# backend/app/db/init_db.py

from app.db.database import init_db


def main() -> None:
    init_db()
    print("✅ Database initialized successfully.")


if __name__ == "__main__":
    main()
