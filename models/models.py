from sqlalchemy import Column, String, JSON, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import UUID
from API_Guardian.db.base import base

class API(Base):
    __tablename__ = "apis"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    base_url = Column(String)

class Endpoint(Base):
    __tablename__ = "endpoints"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    api_id = Column(UUID(as_uuid=True), ForeignKey("apis.id", ondelete="CASCADE"))
    path = Column(String, nullable=False)
    method = Column(String, nullable=False)
    headers = Column(JSON)
    body = Column(JSON)

class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    endpoint_id = Column(UUID(as_uuid=True), ForeignKey("endpoints.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    expected_status = Column(Integer, nullable=False)
    expected_body = Column(JSON)


class TestRun(Base):
    __tablename__ = "test_runs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    test_case_id = Column(UUID(as_uuid=True), ForeignKey("test_cases.id", ondelete="CASCADE"))
    status = Column(String, nullable=False)
    response_status = Column(Integer)
    response_body = Column(JSON)
    execution_time = Column(Float)

