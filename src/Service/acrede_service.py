from Service.service import BaseService
from Repository.repository_acrede import RepositoryAcrede

class AcredeService(BaseService):
    """Lógica de negocio para operaciones sobre la tabla Acrede."""
    def __init__(self, conexion):
        super().__init__(RepositoryAcrede(conexion))

    def create(self, data):
        """Inserta un nuevo registro de acrede."""
        return self.repo.insert(data)

    def update(self, pk, data):
        """Actualiza un registro existente de acrede."""
        return self.repo.update(pk, data)

    def delete(self, pk):
        """Elimina un registro de acrede."""
        return self.repo.delete(pk)

    # Métodos first(), prev(), next(), last(), browse() heredados de BaseService