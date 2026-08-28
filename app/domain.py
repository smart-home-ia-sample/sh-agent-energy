from typing import Protocol

CRITICAL_DEVICE_TYPES = {"refrigerator"}


class McpClientLike(Protocol):
    async def call_tool(self, name: str, arguments: dict | None = None): ...
    async def read_resource(self, uri: str): ...


async def inspect_consumption(mcp: McpClientLike) -> dict:
    return await mcp.read_resource("home://energy")


async def identify_critical_devices(mcp: McpClientLike) -> dict:
    devices = await mcp.read_resource("home://devices")
    critical = [d for d in devices if d.get("type") in CRITICAL_DEVICE_TYPES and d.get("on")]
    return {"critical_devices": critical}
