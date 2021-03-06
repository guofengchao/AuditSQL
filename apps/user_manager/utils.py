# -*- coding:utf-8 -*-
# edit by fuzongfei

import ldap
from AuditSQL.settings import AUTH_LDAP_SERVER_URI, AUTH_LDAP_BIND_DN, AUTH_LDAP_BIND_PASSWORD, AUTHENTICATION_BACKENDS


def check_ldap_connection():
    """检查ldap服务器连接性和绑定的用户是否有效"""
    if 'django_auth_ldap.backend.LDAPBackend' not in AUTHENTICATION_BACKENDS:
        return True, None
    else:
        try:
            conn = ldap.initialize(AUTH_LDAP_SERVER_URI)
            conn.simple_bind_s(AUTH_LDAP_BIND_DN, AUTH_LDAP_BIND_PASSWORD)
            conn.timeout = 2
            return True, None
        except ldap.INVALID_CREDENTIALS as err:
            msg = '配置文件绑定的LDAP用户名或密码错误'
            return False, msg
        except ldap.SERVER_DOWN as err:
            msg = f"不能连接LDAP服务器：{AUTH_LDAP_SERVER_URI}"
            return False, msg
