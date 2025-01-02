from runelite_python.java.api.client import Client
from runelite_python.java.api.message_node import MessageNode
from py4j.java_gateway import JavaGateway, GatewayParameters
import argparse, os
from pprint import pprint
from runelite_python.runelite_data.message_pub import MessagePublisher, ChatPublisher
from runelite_python.runelite_data.master_sub import MasterSubscriber


import time
from runelite_python.client.client import ClientGateway


def write_chat(f, x):
    if x:
        f.write(str(x) + '\n')

def main():
    client = ClientGateway()
    message_publisher = ChatPublisher(client.get_client())
    master_subscriber = MasterSubscriber()
    message_publisher.add_subscriber(master_subscriber)
    f = open('chat.txt', 'a')
    master_subscriber.add_action(pprint)
    master_subscriber.add_action(lambda x: write_chat(f, x))
    
    tick = None
    try:
        while True:
            start = time.time()
            game_tick = client.get_game_tick()
            if game_tick == tick:
                continue
            
            message_publisher.publish()
                
            tick = game_tick
            time.sleep(0.6)
            print(f"Loop: {time.time() - start}")
    except KeyboardInterrupt:
        f.close()
if __name__ == "__main__":
    main()