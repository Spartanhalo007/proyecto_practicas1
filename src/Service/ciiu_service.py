from Service.service import BaseService
from Repository.repository_ciiu import RepositoryCiiu

class CiiuService(BaseService):
    """Lógica de negocio para la tabla CIIU."""
    def __init__(self, conexion):
        super().__init__(RepositoryCiiu(conexion))

    def create(self, data):
        return self.repo.insert(data)

    def update(self, pk, data):
        return self.repo.update(pk, data)

    def delete(self, pk):
        return self.repo.delete(pk)
    # Métodos first(), prev(), next(), last(), browse() heredados
