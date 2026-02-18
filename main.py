from utils.check_env import verificar_ambiente_optimus
from utils.system_health import monitorar_infraestrutura
from core.backup_engine import iniciar_backup

def executar_fluxo_optimus():
    print("--- 🛡️ INICIANDO OPERAÇÃO OPTIMUS: VISÃO CONTÁBIL ---")
    
    # FASE 1: Auditoria
    verificar_ambiente_optimus()
    
    # FASE 2: Saúde do Hardware
    monitorar_infraestrutura()
    
    # FASE 3: Teste de Backup Real
    print("\n[FASE 3] Enviando documento para a Nuvem AWS...")
    
    # Ajuste os nomes abaixo:
    ARQUIVO = "documento_fiscal_teste.txt"
    BUCKET = "optimus-backup-fabio-v1" # Coloque o nome do bucket que você criou na AWS
    
    sucesso = iniciar_backup(ARQUIVO, BUCKET, ARQUIVO)
    
    if sucesso:
        print("\n🏆 MISSÃO CUMPRIDA: O backup está imutável na nuvem!")
    else:
        print("\n⚠️ FALHA NO BACKUP: Verifique as credenciais da AWS.")

if __name__ == "__main__":
    executar_fluxo_optimus()