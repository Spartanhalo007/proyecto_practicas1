class BaseService:
    """Clase base para los servicios de cada entidad, implementa operaciones CRUD y navegación genéricas."""
    def __init__(self, repo):
        self.repo = repo

    def create(self, data):
        """Inserta un nuevo registro y devuelve el ID generado."""
        return self.repo.insert(data)

    def update(self, pk, data):
        """Actualiza un registro identificado por pk."""
        # Construye tupla con pk y datos si es necesario
        if isinstance(data, dict):
            # Suponiendo que repo.update requiere payload tuple
            payload = (pk,) + tuple(data.values())
        else:
            payload = data
        return self.repo.update(payload)

    def delete(self, pk):
        """Elimina un registro identificado por pk."""
        return self.repo.delete(pk, self.repo.get_pk_atribute())

    def first(self):
        """Obtiene el primer registro de la tabla."""
        return self.repo.first()

    def last(self):
        """Obtiene el último registro de la tabla."""
        return self.repo.last()

    def next(self, pk):
        """Obtiene el siguiente registro al dado por pk."""
        return self.repo.next(pk)

    def prev(self, pk):
        """Obtiene el registro anterior al dado por pk."""
        return self.repo.prev(pk)

    def browse(self):
        """Devuelve todos los registros de la tabla para listado/búsqueda."""
        return self.repo.browse()

    def get_attributes(self):
        """Devuelve los nombres de las columnas de la tabla."""
        return [col[0] for col in self.repo.get_atributes()]