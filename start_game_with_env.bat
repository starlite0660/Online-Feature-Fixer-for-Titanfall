@echo off
set OPENSSL_ia32cap=~0x200000200000000
start "" "python" "set_env_var.py"
