from Service.service import BaseService
from Repository.repository_coraba import RepositoryCoraba

class CorabaService(BaseService):
    """Lógica de negocio para la tabla CORABA."""
    def __init__(self, conexion):
        super().__init__(RepositoryCoraba(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # Métodos first(), prev(), next(), last(), browse() heredados
