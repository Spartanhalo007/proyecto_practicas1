from Service.service import BaseService
from Repository.repository_corr import RepositoryCorr

class CorrService(BaseService):
    """Lógica de negocio para la tabla CORR."""
    def __init__(self, conexion):
        super().__init__(RepositoryCorr(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # first(), prev(), next(), last(), browse() heredados
