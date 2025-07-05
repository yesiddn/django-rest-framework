from rest_framework import permissions

class IsDoctor(permissions.BasePermission): # clase base para crear permisos personalizados
    """
    Custom permission to only allow doctors to edit their own profile.
    """

    # este método se usa para verificar si el usuario tiene permiso para acceder a un objeto específico
    # en este caso, se usa para verificar si el usuario es el doctor que está editando su perfil
    # def has_object_permission(self, request, view, obj):
    #     # Only allow doctors to edit their own profile
    #     return request.user == obj.user
    
    # este método se usa para verificar si el usuario tiene permiso para acceder a la vista
    def has_permission(self, request, view):
        return request.user.groups.filter(name='doctors').exists()