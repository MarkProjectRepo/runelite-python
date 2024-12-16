from runelite_python.client.client import ClientGateway

def get_screenshot(client: ClientGateway):
    return client.get_image()