from datetime import datetime
from sqlalchemy.orm import Session
from app.services.twitter.models.record_model import RecordModel
from app.services.twitter.schemas.report_schema import Record


def get_records(db: Session, skip: int = 0, limit: int = 100) -> list[RecordModel]:
    return db.query(RecordModel).offset(skip).limit(limit).all()


def get_records_by_execution_datetime(db: Session, execution_datetime: datetime) -> list[RecordModel]:
    return db.query(RecordModel)\
        .filter(RecordModel.execution_datetime == execution_datetime)\
        .first()


def create_record(db: Session, record: Record) -> RecordModel:
    db_record = RecordModel(**record.dict())
    db.add(db_record)
    return db_record

