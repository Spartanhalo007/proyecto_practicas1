from Service.service import BaseService
from Repository.repository_puc import RepositoryPuc

class PucService(BaseService):
    """Lógica de negocio para la tabla t_puc."""
    def __init__(self, conexion):
        super().__init__(RepositoryPuc(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() heredados
