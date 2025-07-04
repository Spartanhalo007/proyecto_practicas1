from Service.service import BaseService
from Repository.repository_autcom import RepositoryAutcom

class AutcomService(BaseService):
    """Lógica de negocio para operaciones sobre la tabla Autcom."""
    def __init__(self, conexion):
        super().__init__(RepositoryAutcom(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() heredados de BaseService
