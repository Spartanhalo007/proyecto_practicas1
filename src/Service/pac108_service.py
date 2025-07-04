from Service.service import BaseService
from Repository.repository_pac108 import RepositoryPac108

class Pac108Service(BaseService):
    """Lógica de negocio para la tabla t_pac108."""
    def __init__(self, conexion):
        super().__init__(RepositoryPac108(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() vienen de BaseService