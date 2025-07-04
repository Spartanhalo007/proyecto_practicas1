from Service.service import BaseService
from Repository.repository_aduanas import RepositoryAduanas

class AduanasService(BaseService):
    """Lógica de negocio para operaciones sobre la tabla Aduanas."""
    def __init__(self, conexion):
        super().__init__(RepositoryAduanas(conexion))

    def create(self, data):
        """Inserta un nuevo registro de aduana."""
        # Validaciones específicas pueden añadirse aquí
        return self.repo.insert(data)

    def update(self, pk, data):
        """Actualiza un registro de aduana existente."""
        return self.repo.update(pk, data)

    def delete(self, pk):
        """Elimina un registro de aduana."""
        return self.repo.delete(pk)

    # Métodos first(), prev(), next(), last() heredados de BaseService
