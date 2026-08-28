import asyncio

from app import domain


class FakeMcpClient:
    def __init__(self, responses: dict):
        self.responses = responses
        self.calls: list[tuple] = []

    async def call_tool(self, name, arguments=None):
        self.calls.append(("call_tool", name, arguments))
        return self.responses.get(name, {})

    async def read_resource(self, uri):
        self.calls.append(("read_resource", uri, None))
        return self.responses.get(uri, {})


def test_inspect_consumption_reads_energy_resource():
    fake = FakeMcpClient({"home://energy": {"total_watts": 260, "top_consumers": [], "recommendations": []}})

    result = asyncio.run(domain.inspect_consumption(fake))

    assert fake.calls == [("read_resource", "home://energy", None)]
    assert result["total_watts"] == 260


def test_identify_critical_devices_filters_refrigerator_only():
    fake = FakeMcpClient(
        {
            "home://devices": [
                {"id": "kitchen_refrigerator", "type": "refrigerator", "on": True},
                {"id": "living_room_tv", "type": "tv", "on": True},
                {"id": "bedroom_ac", "type": "ac", "on": False},
            ]
        }
    )

    result = asyncio.run(domain.identify_critical_devices(fake))

    ids = [d["id"] for d in result["critical_devices"]]
    assert ids == ["kitchen_refrigerator"]


def test_identify_critical_devices_ignores_off_refrigerator():
    fake = FakeMcpClient(
        {"home://devices": [{"id": "kitchen_refrigerator", "type": "refrigerator", "on": False}]}
    )

    result = asyncio.run(domain.identify_critical_devices(fake))

    assert result["critical_devices"] == []
