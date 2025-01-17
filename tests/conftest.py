import pytest
from app import create_app
from app import db
from app.models.board import Board
from app.models.card import Card


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_board(app):
    new_board = Board(
        title = "Test Board", 
        owner = "pinspiration")
    db.session.add(new_board)
    db.session.commit()

@pytest.fixture
def one_card_to_one_board(app):
    card = Card.query.first()
    board = Board.query.first()
    board.cards.append(card)
    db.session.commit()

@pytest.fixture
def one_long_card(app):
    db.session.add_all([
        Board(
            title="Test Board", owner="pinspiration"),
        Card(
            message="aaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd000", board_id=1),
    ])

    db.session.commit()

@pytest.fixture
def one_board_with_cards(app):
    db.session.add_all([
        Board(
            title="Test Board", owner="pinspiration"),
        Card(
            message="Test Message 1", board_id=1),
        Card(
            message="Test Message 2", board_id=1),
    ])

    db.session.commit()