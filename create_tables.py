try:
    from .database import engine
    from .models import Base
except ImportError:
    from database import engine
    from models import Base


def main() -> None:
    Base.metadata.create_all(bind=engine)
    print("Tables created")


if __name__ == "__main__":
    main()
