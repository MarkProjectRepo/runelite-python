from typing import Dict, Any
from py4j.java_gateway import JavaGateway, GatewayParameters

class EnumManager:
    def __init__(self, gateway: JavaGateway):
        self.gateway = gateway
        self._enums: Dict[str, Any] = {}

    def get_enum(self, enum_name: str) -> Any:
        if enum_name not in self._enums:
            self._load_enum(enum_name)
        return self._enums[enum_name]

    def _load_enum(self, enum_name: str):
        try:
            enum_class = getattr(self.gateway.jvm.net.runelite.api, enum_name)
            self._enums[enum_name] = enum_class
        except AttributeError:
            raise ValueError(f"Enum '{enum_name}' not found in net.runelite.api")

# Example usage:
# enum_manager = EnumManager(gateway)
# prayer_enum = enum_manager.get_enum("Prayer")
