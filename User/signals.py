from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def assign_permissions_to_admin(sender, **kwargs):
    if sender.name == 'User':
        # Get the admin group
        admin_group, created = Group.objects.get_or_create(name='Admin')
        
        # Get all permissions
        permissions = Permission.objects.all()
        
        # Assign all permissions to the admin group
        admin_group.permissions.set(permissions)
        
        if created:
            print(f"Created group: {admin_group.name} and assigned all permissions.")
        else:
            print(f"Updated group: {admin_group.name} with all permissions.")