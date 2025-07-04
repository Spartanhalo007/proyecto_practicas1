from Service.service import BaseService
from Repository.repository_paises import RepositoryPaises

class PaisesService(BaseService):
    """Lógica de negocio para la tabla t_paises."""
    def __init__(self, conexion):
        super().__init__(RepositoryPaises(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() heredados de BaseService
