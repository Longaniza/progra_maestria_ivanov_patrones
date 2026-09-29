from __future__ import annotations
from collections.abc import Iterator, Reversible
from abc import ABC, abstractmethod
from collections import deque

class Tree(Reversible, ABC):
    """Interfaz/clase abstracta para cualquier arbol"""
    @abstractmethod
    def add_node(self, item: str) -> None:
        pass


class ITreeFactory(ABC):
    """Interfaz/class abstracta de la fábrica para no instanciar clases concretas directamente."""
    @abstractmethod
    def create_tree(self) -> Tree:
        pass

class TreeFactory(ITreeFactory):
    """Fábrica concreta para crear instancias de árboles."""
    def create_tree(self) -> Tree:
        return BinaryTree()


class _TreeNode:
    """Private node class. Hidden from the user."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BFSIterator(Iterator):
    def __init__(self, root: _TreeNode | None):
        self._queue = deque([root]) if root else deque()

    def __next__(self):
        if not self._queue:
            raise StopIteration
            
        current_node = self._queue.popleft()
        
        # Standard order: Left then Right
        if current_node.left:  self._queue.append(current_node.left)
        if current_node.right: self._queue.append(current_node.right)
            
        return current_node.value

# --- New Iterator: Reverse BFS (Bottom-Up, Right-to-Left) ---
class ReverseBFSIterator(Iterator):
    """
    Traverses the tree in complete reverse order of insertion.
    Yields items from the bottom-right leaves up to the root.
    """
    def __init__(self, root: _TreeNode | None):
        self._stack = []
        if not root:
            return

        # We use a temporary queue to populate our data stack
        queue = deque([root])
        
        while queue:
            current_node = queue.popleft()
            # Push the node's value onto the stack
            self._stack.append(current_node.value)
            
            # Enqueue LEFT first, then RIGHT. 
            # This ensures Right ends up on top of the stack to be popped first.
            if current_node.left:  
                queue.append(current_node.left)
            if current_node.right: 
                queue.append(current_node.right)

    def __next__(self):
        """Pops values off the stack until it is empty."""
        if not self._stack:
            raise StopIteration
        return self._stack.pop()  # O(1) removal from the end of a Python list



class BinaryTree(Tree):
    def __init__(self):
        self._root = None

    def add_node(self, value):
        """Inserts item level-by-level to maintain structural balance."""
        new_node = _TreeNode(value)
        if not self._root:
            self._root = new_node
            return

        queue = deque([self._root])
        while queue:
            current = queue.popleft()
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def __iter__(self) -> Iterator:
        return BFSIterator(self._root)
    
    def __reversed__(self) -> Iterator:
        return ReverseBFSIterator(self._root)
    
    