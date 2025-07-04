from Service.service import BaseService
from Repository.repository_sucur import RepositorySucur

class SucurService(BaseService):
    """Lógica de negocio para la tabla SUCUR."""
    def __init__(self, conexion):
        super().__init__(RepositorySucur(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() vienen de BaseService
