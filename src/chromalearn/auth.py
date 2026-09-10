import grp, os, pwd

TEACHER_GROUP = "chromalearn-teacher"
ADMIN_GROUP = "chromalearn-admin"

ROLE_ORDER = {"student": 0, "teacher": 1, "admin": 2}

def current_username():
    return pwd.getpwuid(os.geteuid()).pw_name

def _group_names(username=None):
    username = username or current_username()
    user = pwd.getpwnam(username)
    names = set()
    try:
        names.add(grp.getgrgid(user.pw_gid).gr_name)
    except KeyError:
        pass
    for g in grp.getgrall():
        if username in g.gr_mem:
            names.add(g.gr_name)
    return names

def detect_role(username=None, groups=None):
    gs = set(groups if groups is not None else _group_names(username))
    if ADMIN_GROUP in gs:
        return "admin"
    if TEACHER_GROUP in gs:
        return "teacher"
    return "student"

def allowed(role, minimum):
    return ROLE_ORDER.get(role, -1) >= ROLE_ORDER.get(minimum, 99)
