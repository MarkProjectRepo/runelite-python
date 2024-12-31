from runelite_python.java.api.client import Client
from runelite_python.java.api.message_node import MessageNode
from py4j.java_gateway import JavaGateway, GatewayParameters
import argparse
from pprint import pprint

def main():
    parser = argparse.ArgumentParser(description='Modify chat messages in RuneLite')
    parser.add_argument('--name', type=str, help='New name to set for the message')
    parser.add_argument('--msg', type=str, help='New message to set for the message')
    args = parser.parse_args()
    
    gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_field=True))
    instance = gateway.entry_point
    jclient = instance.getClient()

    client = Client(jclient)
    messages = client.get_messages()
    context = []
    try:
        for message in messages.iterator():
            message = MessageNode(message)
            name = message.get_name()
            value = message.get_value()
            sender = message.get_sender()

            # Handle special formatting
            if '<col' in name:
                name = name.split('>', 1)[1]  # Remove color tags
            if '<img=' in name:
                name = name.split('>', 1)[1]  # Remove image tags
            # Handle special formatting
            if '<col' in value:
                value = value.split('>', 1)[1]  # Remove color tags
            if '<img=' in value:
                value = value.split('>', 1)[1]  # Remove image tags
            
            # Remove non-breaking spaces
            name = name.replace('\xa0', ' ') if name else name
            value = value.replace('\xa0', ' ')
            
            context.append(f"{name}: {value}" if name else "Game message: " + value)
            context[-1] = context[-1].strip()
            if sender == "Endymion":
                context[-1] = "Clan chat: " + context[-1]
    except Exception as e:
        pass
    pprint(context)

    client.refresh_chat()



# def send_message(message):
    # client.send_chat_message(message)

if __name__ == "__main__":
    main()