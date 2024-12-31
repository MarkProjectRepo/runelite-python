import argparse
from typing import List
from runelite_python.config.publisher_config import PublisherConfig

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='RuneLite Python Client')
    parser.add_argument(
        '--publishers',
        nargs='+',
        choices=['player', 'client', 'message', 'all'],
        default=['all'],
        help='Specify which publishers to enable'
    )
    parser.add_argument(
        '--tick-sleep',
        type=float,
        default=0.5,
        help='Sleep duration between ticks (default: 0.5)'
    )
    return parser

def get_enabled_publishers(args) -> List[PublisherConfig]:
    if 'all' in args.publishers:
        return PublisherConfig.all_publishers()
    
    all_configs = {config.name: config for config in PublisherConfig.all_publishers()}
    enabled_configs = []
    
    for publisher_name in args.publishers:
        if publisher_name in all_configs:
            config = all_configs[publisher_name]
            config.enabled = True
            enabled_configs.append(config)
    
    return enabled_configs 