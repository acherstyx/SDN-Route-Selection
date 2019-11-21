import requests

# TODO: remove debug output
Debug_ShowJsonText = True
Debug_SaveToFile = True  # for visualization


def get_response(hostname="centos-host"):
    """
    get node info from the controller
    :param hostname: the hostname of the odl controller
    :return: json, represent in python dict
    """
    url = "http://" + hostname + ":8181/restconf/operational/network-topology:network-topology"

    headers = {
        'Authorization': "Basic YWRtaW46YWRtaW4=",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "caa95a0a-cae9-4980-8f61-d70bca8281aa,fd7a0273-6d61-495a-8a6b-ca4377ec2aea",
        'Host': "centos-host:8181",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "rememberMe=deleteMe; JSESSIONID=uq095fhzly1c1u98icrei3nn3",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    if Debug_ShowJsonText:
        print(response.text)
    if Debug_SaveToFile:
        with open("topology.json", "w") as f:
            f.write(response.text)

    return response.json()


def load_node_info(node_json_dict, topology_index=0):
    return node_json_dict["network-topology"]["topology"][topology_index]["node"]


def load_link_info(node_json_dict, topology_index=0):
    return node_json_dict["network-topology"]["topology"][topology_index]["link"]


if __name__ == "__main__":

    print("> Get json data")
    json_dict = get_response()

    print("> get node info")
    nodes = load_node_info(json_dict)
    for a_node in nodes:
        print(a_node)

    print("> get link info")
    links = load_link_info(json_dict)
    for a_link in links:
        print(a_link)
