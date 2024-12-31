from runelite_python.runelite_data.master_sub import MasterSubscriber
from runelite_python.client.client import ClientGateway
from runelite_python.cli.cli import create_parser, get_enabled_publishers
from typing import Optional, List
import time

def initialize_publishers(client: Optional[ClientGateway] = None, 
                        publisher_configs: Optional[List] = None):
    client = client if client else ClientGateway()
    publisher_configs = publisher_configs or get_enabled_publishers(['all'])
    
    publishers = []
    master_subscriber = MasterSubscriber()
    
    for config in publisher_configs:
        if not config.enabled:
            continue
            
        publisher_class = config.get_publisher_class(config.name)
        if publisher_class:
            if config.name == 'player':
                publisher = publisher_class(client.get_player())
            elif config.name == 'client':
                publisher = publisher_class(client)
            elif config.name == 'message':
                publisher = publisher_class(client.get_client())
            
            publishers.append(publisher)
            publisher.add_subscriber(master_subscriber)
    
    master_subscriber.add_action(print)
    return publishers, master_subscriber

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    client = ClientGateway()
    publishers, master_subscriber = initialize_publishers(
        client, 
        get_enabled_publishers(args)
    )
    
    tick = None
    while True:
        start = time.time()
        game_tick = client.get_game_tick()
        if game_tick == tick:
            continue
        
        for publisher in publishers:
            publisher.publish()
        
        tick = game_tick
        time.sleep(args.tick_sleep)
        print(f"Loop: {time.time() - start}")

if __name__ == "__main__":
    main()
