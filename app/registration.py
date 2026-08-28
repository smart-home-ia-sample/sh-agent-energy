import httpx

from smart_home_common.registration_client import ServiceInfo, register_with_retry

SKILLS = [
    ("inspect_consumption", "Inspect consumption", "Reports total energy consumption and top consumers",
     ["quanto estou gastando de energia?", "como está o consumo?", "energia da casa"]),
    ("identify_critical_devices", "Identify critical devices",
     "Lists currently-on devices that must not be turned off", ["quais aparelhos não posso desligar?"]),
]

CAPABILITIES = [skill_id for skill_id, *_ in SKILLS]
CATALOG = [
    {"id": sid, "name": name, "description": desc, "tags": ["energy"], "examples": examples}
    for sid, name, desc, examples in SKILLS
]


def register_with_bfa(bfa_url: str, port: int, version: str = "0.1.0", max_attempts: int = 10) -> dict:
    service = ServiceInfo(
        name="energy", port=port, capabilities=CAPABILITIES, protocol="http", version=version, catalog=CATALOG
    )
    with httpx.Client(timeout=5.0) as client:
        return register_with_retry(client, bfa_url, service, kind="agents", max_attempts=max_attempts)
