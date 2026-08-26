from technocore_client import TechnocoreClient

def mcp_send(room, sender, msg):
    return TechnocoreClient().say(room, sender, msg)
