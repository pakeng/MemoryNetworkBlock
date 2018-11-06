import hashlib
import random
from time import time

# 辅助生成初始节点的工具
from node import Node
from root.manger import Manager


class God(object):

    def __init__(self):
        self._name = "GOD"

    def __str__(self):
        return 'Name %s' % self._name

    @property
    def name(self):
        return self._name

    @staticmethod
    def generate_hash(previous_hash, timestamp):
        nonce = random.randrange(0, 99999)
        guess = f'{previous_hash}{nonce}{timestamp}'.encode()
        hash = hashlib.sha256(guess).hexdigest()
        return hash

    @staticmethod
    def generate_gene():
        gene = []
        nonce = random.randrange(0, 99999)
        guess = f'{time()}{nonce}{time()}'.encode()
        gene.append(hashlib.sha256(guess).hexdigest())
        for i in range(1, 46):
            gene.append(God.generate_hash(gene[i-1], time()))
        return tuple(gene)


def test():
    god = God()
    print(god.generate_gene())


def make_world():
    parents = {'pa': "", 'mom': ""}
    gene = God.generate_gene()
    Adam = Node(parents, gene)
    gene = God.generate_gene()
    Eve = Node(parents, gene)
    parents = {'pa': Adam, 'mom': Eve}

    for i in range(0, 10):
        son_gene = Eve.siphonogamy(Adam.dysjunction())
        Manager.sons.append(Node(parents, son_gene))
        Adam.publish_son(Manager.sons[i])
        Eve.publish_son(Manager.sons[i])
    print(Manager.sons)
    #  注册前10个节点
    for i in range(0, 9):
        for j in range(i, 10):
            Manager.sons[i].regsiterNew(Manager.sons[j])

    for i in range(0, 9):
        for j in range(i, 10):
            parents = {'pa': Manager.sons[i], 'mom': Manager.sons[j]}
            son_gene = Manager.sons[j].siphonogamy(Manager.sons[i].dysjunction())
            Manager.sons.append(Node(parents, son_gene))
            Manager.sons[i].publish_son(Manager.sons[-1])
            Manager.sons[j].publish_son(Manager.sons[-1])
    print(Manager.sons)


if __name__ == '__main__':
    test()
    make_world()

