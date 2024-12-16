from runelite_python.runelite_data.player_pub import PlayerPublisher
from runelite_python.runelite_data.client_pub import ClientPublisher
from runelite_python.runelite_data.scene_pub import ScenePublisher
from runelite_python.runelite_data.master_sub import MasterSubscriber
from runelite_python.client.client import ClientGateway
from typing import Optional
import time

def initialize_publishers(client: Optional[ClientGateway] = None):
    client: ClientGateway = client if client else ClientGateway()
    player = client.get_player()
    client_publisher = ClientPublisher(client)
    player_publisher = PlayerPublisher(player)
    # scene_publisher = ScenePublisher(client.get_client().get_scene())

    master_subscriber = MasterSubscriber()
    player_publisher.add_subscriber(master_subscriber)
    client_publisher.add_subscriber(master_subscriber)
    # scene_publisher.add_subscriber(master_subscriber)
    master_subscriber.add_action(print)

    return [client_publisher, player_publisher], master_subscriber

if __name__ == "__main__":
    client = ClientGateway()
    publishers, master_subscriber = initialize_publishers(client)
    tick = None
    while True:
        start = time.time()
        game_tick = client.get_game_tick()
        if game_tick == tick:
            continue
        
        for publisher in publishers:
            publisher.publish()
        
        tick = game_tick
        time.sleep(0.5)
        print(f"Loop: {time.time() - start}")
