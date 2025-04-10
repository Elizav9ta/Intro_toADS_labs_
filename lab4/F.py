class TreeNode:
    """Класс узла бинарного дерева поиска."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Класс для построения и работы с бинарным деревом поиска."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставка элемента в BST."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Рекурсивная вставка в дерево."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def count_mini_triangles(self):
        """Подсчёт узлов, имеющих двух потомков."""
        return self._count_mini_triangles_recursive(self.root)

    def _count_mini_triangles_recursive(self, node):
        """Рекурсивный обход для подсчёта узлов с двумя потомками."""
        if node is None:
            return 0

        count = 0
        if node.left is not None and node.right is not None:
            count = 1 

        count += self._count_mini_triangles_recursive(node.left)
        count += self._count_mini_triangles_recursive(node.right)

        return count

n = int(input())  
values = list(map(int, input().split())) 

bst = BST()
for value in values:
    bst.insert(value)

print(bst.count_mini_triangles())
