from runelite_python.config.publisher_config import PublisherConfig
from runelite_python.main import initialize_publishers
from runelite_python.client.client import ClientGateway
import time

def custom_action(data):
    # Custom processing of the published data
    print(f"Custom processing: {data}")

def run_custom_setup():
    # Only enable player and message publishers
    configs = [
        PublisherConfig(name="player", enabled=True),
        PublisherConfig(name="message", enabled=True),
        PublisherConfig(name="client", enabled=False)
    ]
    
    client = ClientGateway()
    publishers, master_subscriber = initialize_publishers(client, configs)
    
    # Add custom action instead of default print
    master_subscriber.clear_actions()
    master_subscriber.add_action(custom_action)
    
    tick = None
    while True:
        game_tick = client.get_game_tick()
        if game_tick == tick:
            continue
            
        for publisher in publishers:
            publisher.publish()
            
        tick = game_tick
        time.sleep(0.6)  # Custom tick sleep

if __name__ == "__main__":
    run_custom_setup() 