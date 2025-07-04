from Service.service import BaseService
from Repository.repository_tipint import RepositoryTipint

class TipintService(BaseService):
    """Lógica de negocio para la tabla T_TIPINT."""
    def __init__(self, conexion):
        super().__init__(RepositoryTipint(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() vienen de BaseService
