#!/usr/bin/env python3
import sys
sys.path.append('..')
from core.scanner import OSINTScanner
from core.utils import save_report

def main():
    print("""
    ╔══════════════════════════════╗
    ║  Framework Tools Mx - CLI    ║
    ║  OSINT mexicano al 100       ║
    ╚══════════════════════════════╝
    """)
    target = input("Ingresa email, usuario o IP: ")
    scanner = OSINTScanner(target)
    results = scanner.run_all()
    for k, v in results.items():
        print(f"\n[ {k.upper()} ]\n{v}")
    save_report(results, target)

if __name__ == "__main__":
    main()
