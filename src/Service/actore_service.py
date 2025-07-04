from Service.service import BaseService
from Repository.repository_actore import RepositoryActore

class ActoreService(BaseService):
    """Lógica de negocio para operaciones sobre la tabla Actore."""
    def __init__(self, conexion):
        super().__init__(RepositoryActore(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # Métodos first(), prev(), next(), last(), browse() heredados
