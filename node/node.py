from time import time
from memory.Memory import Memory
import random
import hashlib

from root import Server


class Node(object):
    # 节点原型
    def __init__(self, parents, gene):
        self.name = hashlib.sha256(f'{"".join(gene)}'.encode()).hexdigest()
        self.address = Node.create_address()
        self.contact_list = {}  # 节点出生的时候有父母作为联系人列表记录
        self._parentsAddress = {'pa': parents['pa'], 'mom': parents['mom']}
        self.memory = Memory(self)
        self._gene = gene
        self._sons = []

    def get_memory(self, key):
        return self.memory.get_info_with_key(key)

    def set_memory(self, key, msg):
        self.memory.set_info_with_key(key, msg)

    def get_info(self):
        return 'name:%s, address:%s' % (self.name, self.address)

    @staticmethod
    def create_address():
        address = 'ce_shi'
        return address

    @property
    def family(self):
        return self._parentsAddress

    def dysjunction(self):
        gene_set = set()
        egg = []
        while len(gene_set) < 23:
            gene_set.add(random.randrange(0, 46))
        for i in gene_set:
            egg.append(self._gene[i])
        return egg

    def siphonogamy(self, egg):
        # 选取不多于3条的基因进行交换
        count = random.randrange(0, 4)
        mgene_set = set()
        her_gene_set = set()
        while len(mgene_set) < count:
            mgene_set.add(random.randrange(0, 23))
        while len(her_gene_set) < count:
            her_gene_set.add(random.randrange(0, 23))
        # 交叉点选取
        cross_point_set = set()
        while len(cross_point_set) < count:
            cross_point_set.add(random.randrange(0, 64))
        return self.cross_with_point(egg, list(mgene_set), list(her_gene_set), list(cross_point_set))

    def cross_with_point(self, her_egg, mgen_set, her_gene_set, cross_point_set):
        megg = self.dysjunction()
        print(megg)
        print(her_egg)
        for i in range(len(mgen_set)):
            mtail = megg[mgen_set[i]][cross_point_set[i]:]
            megg[mgen_set[i]] = megg[mgen_set[i]][0:cross_point_set[i]] + her_egg[her_gene_set[i]][cross_point_set[i]:]
            her_egg[her_gene_set[i]] = her_egg[her_gene_set[i]][0:cross_point_set[i]] + mtail
        print(mgen_set)
        print(her_gene_set)
        print(cross_point_set)
        print(megg)
        print(her_egg)
        son_gene = megg + her_egg
        str = ''.join(son_gene)
        son_gene_name = hashlib.sha256(f'{str}'.encode()).hexdigest()  # 来自父母的基因签名
        self._sons.append(son_gene_name)

        return tuple(son_gene)

    def regsiterNew(self, new_node):
        # TODO 实现联网的寻址
        msg = self._gene[random.randrange(0, 46)]
        random_msg = hashlib.sha256(f'{time()}{msg}'.encode()).hexdigest()
        if new_node.name in self.contact_list:
            return
        self.contact_list[new_node.name] = random_msg+ ":" + new_node.address
        new_node.regsiterNew(self)  # 同样向新生成的节点注册自己

    def publish_son(self, son):
        # 告知朋友后代出生了
        temp = self.contact_list.copy()
        for target_name in temp:
            target = Server.find_node_with_name(target_name)
            if target:
                target.regsiterNew(son)
