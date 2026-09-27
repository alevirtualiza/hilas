#!/usr/bin/env python3
"""Hook PreToolUse: só verifica sentinelas quando o Write/Edit alvo está em
fase1-introducao/saidas/ ou fase2-unidades/*/saidas/ -- fora daí (CLAUDE.md,
scripts, este próprio hook), a trava não se aplica.

Lê o payload JSON do hook via stdin (campo tool_input.file_path).
"""
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def alvo_protegido(caminho: str) -> bool:
    p = Path(caminho)
    partes = p.parts
    return "saidas" in partes and ("fase1-introducao" in partes or "fase2-unidades" in partes)


def main():
    try:
        payload = json.load(sys.stdin)
        caminho = payload.get("tool_input", {}).get("file_path", "")
    except (json.JSONDecodeError, AttributeError):
        caminho = ""

    if not caminho or not alvo_protegido(caminho):
        sys.exit(0)  # fora do allowlist de saidas/ -- trava não se aplica

    resultado = subprocess.run(
        [sys.executable, str(RAIZ / "_scripts" / "verificar_sentinelas.py")],
        capture_output=True, text=True,
    )
    print(resultado.stdout.strip(), file=sys.stderr)
    if "[VAZIO]" in resultado.stdout:
        sys.exit(2)  # bloqueia
    sys.exit(0)  # incompleto ou pronto -- passa (com aviso já impresso)


if __name__ == "__main__":
    main()
