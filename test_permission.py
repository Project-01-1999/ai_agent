from security.permission_manager import PermissionManager

pm = PermissionManager()

if pm.ask_permission("Delete File", "notes.txt"):
    print("Permission Granted")
else:
    print("Permission Denied")