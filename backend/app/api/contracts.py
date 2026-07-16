"""Contracts API routes with placeholder implementations."""

from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.get("")
async def list_contracts():
    """List all contracts."""
    return [
        {
            "id": "contract-001",
            "title": "Master Service Agreement - TechCorp",
            "parties": ["TechCorp Solutions", "Apex Global Inc."],
            "contract_type": "service_agreement",
            "status": "active",
            "start_date": "2024-01-01",
            "end_date": "2025-12-31",
            "value": 2500000,
            "risk_score": 72,
            "created_at": "2024-01-15T10:00:00Z",
        },
        {
            "id": "contract-002",
            "title": "NDA - HR Templates",
            "parties": ["Internal HR", "All Employees"],
            "contract_type": "nda",
            "status": "active",
            "start_date": "2024-03-01",
            "end_date": "2026-03-01",
            "value": 0,
            "risk_score": 45,
            "created_at": "2024-03-01T09:00:00Z",
        },
    ]


@router.get("/{contract_id}")
async def get_contract(contract_id: str):
    """Get contract details."""
    return {
        "id": contract_id,
        "title": "Master Service Agreement - TechCorp",
        "parties": ["TechCorp Solutions", "Apex Global Inc."],
        "contract_type": "service_agreement",
        "status": "active",
        "start_date": "2024-01-01",
        "end_date": "2025-12-31",
        "value": 2500000,
        "risk_score": 72,
        "clauses": [
            {"number": "1.1", "title": "Definitions", "risk_level": "low"},
            {"number": "4.1", "title": "Indemnification", "risk_level": "high"},
            {"number": "5.1", "title": "Termination", "risk_level": "medium"},
            {"number": "7.2", "title": "Non-Compete", "risk_level": "high"},
        ],
        "created_at": "2024-01-15T10:00:00Z",
    }
