from datetime import datetime
from sqlalchemy.orm import Session
from app.services.twitter.schemas.report_schema import Record
from app.services.twitter.cruds import record_crud
from app.utils.logger import Logger

logger = Logger(__name__).logger


def create_record(db: Session, record: Record):
    try:
        record_crud.create_record(db, record)
    except Exception as e:
        logger.error(f'Error creating record {record}')
        logger.error(e)


def get_record_by_execution_datetime(db: Session, execution_datetime: datetime):
    try:
        record_crud.get_records_by_execution_datetime(db, execution_datetime)
    except Exception as e:
        logger.error(f'Error reading record from {execution_datetime}')
        logger.error(e)

