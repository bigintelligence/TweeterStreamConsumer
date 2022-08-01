from app.utils.logger import Logger


def test__init_logger():
    logger1 = Logger('name1')
    logger2 = Logger('name2')
    assert logger1 != logger2


