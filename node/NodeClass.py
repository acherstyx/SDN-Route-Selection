class Node:
    def __init__(self, node_id, link_list, host_list):
        # node id of this node
        # e.g. "openflow:1"
        self.node_id = node_id
        # String list of dest-node id
        # e.g. ["openflow:2","openflow:3"]
        self.link_list = link_list
        # define if the node has been reached in a DFS, BFS , etc.
        self.reached = False
        self.host_type = node_id[:node_id.find(':', 1)]

    def is_reached(self):
        return self.reached

    def set_reached(self):
        self.reached = True

    def reset_reached(self):
        self.reached = False

    # about the link of switch or host
    def addLink(self, dist_id):
        self.link_list.append(dist_id)


if __name__ == "__main__":
    # test case
    print(">>> __init__ test case")
    node_1 = Node("openflow:1", ["openflow:0", ], ["host:00:00:00:00:00:03", ])
    print(node_1.reached)
    print(node_1.node_id)
    print(node_1.link_list)
    print(node_1.host_list)

    print(">>> add test case")
    node_1.addHost("host:00:00:00:00:00:08")
    node_1.addLink("openflow:996")
    print(node_1.link_list)
    print(node_1.host_list)
