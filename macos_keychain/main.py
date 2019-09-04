import getpass
import io

import sh

MACOS_KEYCHAIN_PREFIX = "Python macos_keychain"


def add(*, name: str, value: str):
    out = io.StringIO()
    sh.security(
        "add-generic-password",
        a=getpass.getuser(),
        s=f"{MACOS_KEYCHAIN_PREFIX}: {name}",
        w=value,
        _out=out,
    )
    return out.getvalue()


def get(*, name: str):
    out = io.StringIO()
    sh.security(
        "find-generic-password",
        "-w",
        a=getpass.getuser(),
        s=f"{MACOS_KEYCHAIN_PREFIX}: {name}",
        _out=out,
    )
    return out.getvalue()


def ls():
    out = io.StringIO()
    sh.awk(
        sh.grep(sh.security("dump-keychain"), "0x00000007"),
        "-F=",
        "{print $2}",
        _out=out,
    )
    return [
        n.split(f'"{MACOS_KEYCHAIN_PREFIX}: ')[1][:-1]
        for n in out.getvalue().strip().split("\n")
        if n.startswith(f'"{MACOS_KEYCHAIN_PREFIX}: ')
    ]


def rm(name):
    try:
        sh.security(
            "delete-generic-password",
            a=getpass.getuser(),
            s=f"{MACOS_KEYCHAIN_PREFIX}: {name}",
        )
    except sh.ErrorReturnCode_44:
        pass
