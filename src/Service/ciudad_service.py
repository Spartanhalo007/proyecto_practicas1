from Service.service import BaseService
from Repository.repository_ciudad import RepositoryCiudad

class CiudadService(BaseService):
    """Lógica de negocio para la tabla CIUDAD."""
    def __init__(self, conexion):
        super().__init__(RepositoryCiudad(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # Métodos first(), prev(), next(), last(), browse() heredados
