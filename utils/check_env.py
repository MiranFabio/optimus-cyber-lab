import sys
import platform
import ctypes

#Você usa para mostrar que a máquina do cliente pode estar vulnerável se 
# não estiver como Admin, ou se o Python for antigo. É a sua primeira 
# impressão profissional.


def verificar_ambiente_optimus():
    print("\n--- 🛡️ AUDITORIA DE INFRAESTRUTURA: OPTIMUS ---")
    
    # Verifica permissão de Admin (Essencial para LGPD e Backups)
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        is_admin = False
    
    status_admin = "✅ ADMINISTRADOR" if is_admin else "❌ USUÁRIO COMUM (Risco de Bloqueio)"
    print(f"SISTEMA: {platform.system()} {platform.release()}")
    print(f"PYTHON: {sys.version.split()[0]}")
    print(f"STATUS: {status_admin}")

if __name__ == "__main__":
    verificar_ambiente_optimus()