class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.es_fin_de_ip = False

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, ip):
        partes = ip.split(".")
        nodo_actual = self.raiz
        
        for parte in partes:
            if parte not in nodo_actual.hijos:
                nodo_actual.hijos[parte] = NodoTrie()
            nodo_actual = nodo_actual.hijos[parte]
            
        nodo_actual.es_fin_de_ip = True

    def buscar(self, ip):
        partes = ip.split(".")
        nodo_actual = self.raiz
        
        for parte in partes:
            if parte not in nodo_actual.hijos:
                return False
            nodo_actual = nodo_actual.hijos[parte]
            
        return nodo_actual.es_fin_de_ip