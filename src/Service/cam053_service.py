from Service.service import BaseService
from Repository.repository_cam053 import RepositoryCam053

class Cam053Service(BaseService):
    """Lógica de negocio para t_cam053."""
    def __init__(self, conexion):
        super().__init__(RepositoryCam053(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() vienen de BaseService
