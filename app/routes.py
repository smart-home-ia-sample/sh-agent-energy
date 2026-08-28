import os

from fastapi import APIRouter, FastAPI

from app import domain
from app.registration import SKILLS
from smart_home_common import HomeMcpClient, IntentAgentExecutor, build_agent_card, mount_a2a

router = APIRouter()
mcp_client = HomeMcpClient(os.environ["BFA_URL"])

HANDLERS = {
    "inspect_consumption": lambda input: domain.inspect_consumption(mcp_client),
    "identify_critical_devices": lambda input: domain.identify_critical_devices(mcp_client),
}


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.get("/ready")
def ready():
    return {"status": "ready"}


def mount(app: FastAPI) -> None:
    app.include_router(router)
    executor = IntentAgentExecutor(HANDLERS)
    card = build_agent_card("energy", skills=SKILLS)
    mount_a2a(app, card, executor)
