'''
Definimos el corazón del programa; la clase nodo.
Es acá donde se fuardará la información encapsulada

'''

class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

'''
Definida la clase Nodo, se procede con la
clase de la lista doblemente enlazada con cola

'''    
    
class LinkedList:
  _head = None
  _tail = None
  def __init__(self):
    self._head = None
    self._tail = None
    
  def _isEmpty(self):
    return self._head == None

  def _addFront(self, data):
    if self._isEmpty():
      nodo = Node(data)
      self._head = nodo
      self._tail = nodo
    else:
      nodo = Node(data)
      nodo.next = self._head
      self._head.prev = nodo
      self._head = nodo

  def _addRear(self, data):
    if self._isEmpty():
      nodo = Node(data)
      self._head = nodo
      self._tail = nodo
    else:
      nodo = Node(data)
      self._tail.next = nodo
      nodo.prev = self._tail
      self._tail = nodo

  def _getAtFromHead(self, position):
    curr = self._head
    for i in range(position):
      curr = curr.next
    return curr.data
  def _getAtFromTail(self, position):
    curr = self._tail
    for i in range(position):
      curr = curr.prev
    return curr.data
  def _dropTail(self):
    if not self._isEmpty():
      temp = self._tail.prev
      self._tail.prev = None
      if temp != None:
        temp.next = None
      self._tail = temp

  def _dropHead(self):
    if not self._isEmpty():
      temp = self._head.next
      self._head.next = None
      if temp != None:
        temp.prev = None
      self._head = temp
'''
Para los procesos de guardado de información
usaremos Stacks, sólo estacks
'''

class Stack(LinkedList):
  def push(self,data):
    self._addFront(data)
  def pop(self):
    if self._head != None:
        returned = self._head.data
        self._dropHead()
        return returned
  def peek(self):
    return self._head.data
  def isEmpty(self):
    return self._isEmpty()
  def getAt(self, position):
    return self._getAtFromTail(position)

'''
Usaremos una fila para la impresión de los elementos
'''

class Queue(LinkedList):
  def enqueue(self,data):
    self._addRear(data)
  def isEmpty(self):
    return self._isEmpty()
  def peek(self):
    if self.isEmpty():
      print("Esta lista está vacía!!!")
      return
    return self._head.data
  def dequeue(self):
    returned = self.peek()
    self._dropHead()
    return  returned

'''
Implementaremos una clase llamada Editor, que 

hará el trabajo directamente por medio de sus métodos
'''


class Editor:
  def __init__(self):
    self.n_agregados = Stack()
    self.n_retirados = Stack()
    self.retirados = Stack()
    self.ordenes = Stack()
    self.text = Stack()
    self.toPrint = Queue()
  def process(self, order):
    instruccion = order.split(' ')
    current = instruccion[0]
    if current in {'1','2'}:
      self.ordenes.push(current)
      if current == '1':
        numero_agregados = 0
        for i in instruccion[1]:
          numero_agregados += 1
          self.text.push(i)
        self.n_agregados.push(numero_agregados)
      if current == '2':
        difference = int(instruccion[1])
        self.n_retirados.push(difference)
        for i in range(difference):
          self.retirados.push(self.text.pop())
    if current == '3':
      index = int(instruccion[1])
      self.toPrint.enqueue(self.text.getAt(index-1))
    if current == '4':
      deshacer = self.ordenes.pop()
      if deshacer == '1':
        n_deshacer = self.n_agregados.pop()
        for i in range(n_deshacer):
          self.text.pop()
      if deshacer == '2':
        n_deshacer = self.n_retirados.pop()
        for i in range(n_deshacer):
          self.text.push(self.retirados.pop())
        
if __name__ == "__main__":
    n = int(input())
    editor = Editor()
    for i in range(n):
        orden = input()
        editor.process(orden)
    while  not editor.toPrint.isEmpty():
        print(editor.toPrint.dequeue(), end = "")
        if not editor.toPrint.isEmpty():
            print()
