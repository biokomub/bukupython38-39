from abc import ABCMeta, abstractmethod

class KelasAbstrak(metaclass = ABCMeta): #kelas abstrak
    @abstractmethod #dekorator metode abstrak
    def metAbstrak(self, param1, paramN): #metode abstrak
        pass

objAbstrak = KelasAbstrak()
