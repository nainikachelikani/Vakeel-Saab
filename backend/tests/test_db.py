"""Tests for database models, relationships, and constraints."""

import uuid
import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from app.database.base import Base
from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.document import UploadedDocument, DocumentChunk
from app.models.report import Report
from app.models.citation import Citation
from app.models.agent_execution import AgentExecution
from app.models.notification import Notification

# In-memory SQLite for testing
TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(name="db_session")
def fixture_db_session():
    """Fixture that initializes a clean in-memory SQLite database for each test."""
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(bind=engine)
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


def test_tables_created(db_session):
    """Verify that all required tables are successfully created in the database."""
    # Query table names from the database
    connection = db_session.connection()
    result = connection.execute(
        Base.metadata.tables[User.__tablename__].select()
    )
    assert result is not None


def test_unique_email_constraint(db_session):
    """Verify that email uniqueness is enforced on the User table."""
    user1 = User(
        email="test@vakeelsaab.com",
        name="User One",
        password_hash="hashed_pw_1",
        role="citizen",
        preferred_language="en"
    )
    db_session.add(user1)
    db_session.commit()

    # Try inserting another user with the same email
    user2 = User(
        email="test@vakeelsaab.com",
        name="User Two",
        password_hash="hashed_pw_2",
        role="professional",
        preferred_language="hi"
    )
    db_session.add(user2)
    
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_nullable_constraints(db_session):
    """Verify that required fields raise IntegrityError if null."""
    # email is not nullable
    user = User(
        name="Test User",
        password_hash="hashed",
        role="citizen"
    )
    db_session.add(user)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_user_conversation_message_relationships(db_session):
    """Verify relationships: User -> Conversations -> Messages."""
    # Create user
    user = User(
        email="lawyer@vakeelsaab.com",
        name="Advocate Verma",
        password_hash="secure_hash",
        role="professional",
        preferred_language="en"
    )
    db_session.add(user)
    db_session.commit()

    # Create conversation
    conversation = Conversation(
        user_id=user.id,
        title="Land Dispute Consultation",
        status="active"
    )
    db_session.add(conversation)
    db_session.commit()

    # Create message
    message1 = Message(
        conversation_id=conversation.id,
        role="user",
        content="I have a dispute regarding property registration.",
        confidence=1.0
    )
    message2 = Message(
        conversation_id=conversation.id,
        role="assistant",
        content="Please provide the registration documents for review.",
        confidence=0.95
    )
    db_session.add_all([message1, message2])
    db_session.commit()

    # Verify relationships & attributes
    db_session.refresh(user)
    db_session.refresh(conversation)

    # Check User -> Conversations
    conversations = user.conversations.all()
    assert len(conversations) == 1
    assert conversations[0].title == "Land Dispute Consultation"
    assert conversations[0].user_id == user.id

    # Check Conversation -> Messages
    messages = conversation.messages.all()
    assert len(messages) == 2
    assert messages[0].content == "I have a dispute regarding property registration."
    assert messages[0].role == "user"
    assert messages[1].confidence == 0.95


def test_uploaded_document_chunks_reports_relationships(db_session):
    """Verify relationships: User -> UploadedDocuments -> DocumentChunks / Reports."""
    # Create user
    user = User(
        email="client@vakeelsaab.com",
        name="Rajesh Patil",
        password_hash="pwdhash",
        role="citizen",
        preferred_language="en"
    )
    db_session.add(user)
    db_session.commit()

    # Create document
    doc = UploadedDocument(
        user_id=user.id,
        filename="lease_agreement.pdf",
        file_type="application/pdf",
        size=102456,
        storage_path="/uploads/lease_agreement.pdf",
        status="processing"
    )
    db_session.add(doc)
    db_session.commit()

    # Create chunk
    chunk = DocumentChunk(
        document_id=doc.id,
        chunk_index=0,
        text="This lease is made on this 15th day of July...",
        page_number=1
    )
    db_session.add(chunk)

    # Create report
    report = Report(
        user_id=user.id,
        document_id=doc.id,
        report_type="contract_summary",
        summary="A lease agreement summary.",
        status="completed"
    )
    db_session.add(report)
    db_session.commit()

    # Verify relationships
    db_session.refresh(user)
    db_session.refresh(doc)

    assert len(user.uploaded_documents.all()) == 1
    assert user.uploaded_documents.first().filename == "lease_agreement.pdf"
    
    assert doc.chunks.count() == 1
    assert doc.chunks.first().text == "This lease is made on this 15th day of July..."
    
    assert doc.reports.count() == 1
    assert doc.reports.first().report_type == "contract_summary"
    assert doc.reports.first().user_id == user.id


def test_citations_agent_execution_notifications(db_session):
    """Verify Citation, AgentExecution, and Notification fields and FKs."""
    user = User(
        email="reporter@vakeelsaab.com",
        name="Reporter",
        password_hash="pwd",
        role="citizen",
        preferred_language="en"
    )
    db_session.add(user)
    db_session.commit()

    # 1. Notification
    notif = Notification(
        user_id=user.id,
        title="Report Ready",
        description="Your legal brief report has been generated.",
        status="unread"
    )
    db_session.add(notif)

    # 2. Citation
    cit = Citation(
        analysis_id=uuid.uuid4(),
        document_name="sc_judgment_2023.pdf",
        page=12,
        clause="Section 5(a)",
        excerpt="The court held that...",
        confidence=0.88
    )
    db_session.add(cit)

    # 3. Agent Execution
    exec_log = AgentExecution(
        analysis_id=uuid.uuid4(),
        agent_name="citation_extractor",
        status="completed",
        execution_time=1.23,
        confidence=0.92
    )
    db_session.add(exec_log)
    db_session.commit()

    # Assert values
    db_session.refresh(user)
    assert len(user.notifications.all()) == 1
    assert user.notifications.first().description == "Your legal brief report has been generated."
    
    db_session.refresh(cit)
    assert cit.document_name == "sc_judgment_2023.pdf"
    assert cit.confidence == 0.88

    db_session.refresh(exec_log)
    assert exec_log.agent_name == "citation_extractor"
    assert exec_log.execution_time == 1.23
    assert exec_log.status == "completed"
