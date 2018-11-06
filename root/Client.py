from node.node import Node


# 应当实现创建节点，并且注册到相邻节点的能力
def get_node():
    return Node([])


class Client(object):

    def __init__(self):
        self.node = get_node()

    def register(self, targets=[]):
        for target in targets:
            target.sign_node(self.node)

    @staticmethod
    def get_local_config():  # 读取本地配置文件获取初始的配置信息
        return []

    def add_to_contact_list(self, address, random_msg):
        addressAndHash = 'address:%s' % (random_msg)
        self.node.contact_list.append(addressAndHash)
        return random_msg