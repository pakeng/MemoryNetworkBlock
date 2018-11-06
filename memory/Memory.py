class Memory(object):
    # 记录类
    def __init__(self, node):
        self.type = 0  # 0 private 1 public 2 protected
        self.memory = {'myInfo': node.get_info()}  # initial moemory with self info

    def get_info_with_key(self, key):
        return self.memory[key]

    def set_info_with_key(self, key, msg):
        self.memory[key].append
