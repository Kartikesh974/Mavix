from fastapi import BackgroundTasks
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas, models
from app.database import get_db
from app.email import send_enquiry_email

router = APIRouter(prefix="/api/enquiry", tags=["enquiry"])

@router.post("/", response_model=schemas.EnquiryResponse, status_code=status.HTTP_201_CREATED)
async def create_enquiry(
    enquiry: schemas.EnquiryCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    """Store enquiry in DB and send email notification."""
    # Save to database
    db_enquiry = models.Enquiry(**enquiry.model_dump())
    db.add(db_enquiry)
    await db.commit()
    await db.refresh(db_enquiry)

    # Send email (async to avoid blocking, but here we do sync in background)
    # For production, consider using background tasks.
    background_tasks.add_task(
    send_enquiry_email,
    enquiry.name,
    enquiry.email,
    enquiry.message)

    return db_enquiry