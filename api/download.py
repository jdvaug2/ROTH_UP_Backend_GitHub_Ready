
from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from utils.pdf_export import export_projection_to_pdf
import os

router = APIRouter()

class DownloadRequest(BaseModel):
    projection_data: List[Dict]

@router.post("/download")
def download_projection_pdf(data: DownloadRequest):
    try:
        filepath = export_projection_to_pdf(data.projection_data)
        with open(filepath, "rb") as f:
            pdf_bytes = f.read()
        os.remove(filepath)
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=projection_report.pdf"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
