from Service.service import BaseService
from Repository.repository_transa import RepositoryTransa

class TransaService(BaseService):
    """Lógica de negocio para la tabla T_TRANSA."""
    def __init__(self, conexion):
        super().__init__(RepositoryTransa(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() vienen de BaseService
