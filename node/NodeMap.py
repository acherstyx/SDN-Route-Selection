from node.GetNodeInfo import *
from node.NodeClass import Node


class NodeMap:
    AllNodes = {}

    def __init__(self, json_dict):
        """
        @type json_dict: dict, fetched from odl using get_response function in GetNodeInfo.py
        """
        nodes = load_node_info(json_dict)
        links = load_link_info(json_dict)

        self.__create_nodes__(nodes)
        self.__add_link__(links)
        pass

    def __create_nodes__(self, nodes):
        for node_dict in nodes:
            self.AllNodes.update({node_dict["node-id"]: Node(node_dict["node-id"], [], [])})

    def __add_link__(self, links):
        for a_link in links:
            self.AllNodes[a_link["source"]["source-node"]].addLink(a_link["destination"]["dest-node"])
        pass


if __name__ == '__main__':
    json_dict = get_response()

    map = NodeMap(json_dict)
    print(map)
