from runelite_python.java.api.client import Client
from py4j.java_gateway import JavaGateway, GatewayParameters
gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_field=True))
instance = gateway.entry_point
jclient = instance.getClient()

client = Client(jclient)

print(f"Total level: {client.get_total_level()}")
