"""MCP Prompts - placeholder interfaces.

PLACEHOLDER: Interface only. Do not implement.
"""

from typing import Dict, Any, List
from dataclasses import dataclass


@dataclass
class PromptTemplate:
    """Template for MCP prompt."""
    name: str
    description: str
    template: str
    variables: List[str]


# Placeholder prompt templates
LEGAL_ANALYSIS_PROMPT = PromptTemplate(
    name="legal_analysis",
    description="Analyze a legal document for risks and compliance",
    template="Analyze the following legal document: {document_content}",
    variables=["document_content"],
)

COMPLAINT_DRAFT_PROMPT = PromptTemplate(
    name="complaint_draft",
    description="Draft a legal complaint based on user input",
    template="Draft a formal complaint for: {complaint_details}",
    variables=["complaint_details"],
)

CITATION_GENERATION_PROMPT = PromptTemplate(
    name="citation_generation",
    description="Generate legal citations for a given context",
    template="Generate relevant legal citations for: {context}",
    variables=["context"],
)
