# main.py
from utils.check_env import verificar_ambiente_optimus
from utils.system_health import monitorar_infraestrutura
# from core.backup_engine import iniciar_backup # Descomentaremos quando a AWS estiver pronta

def executar_fluxo_optimus():
    print("==================================================")
    print("       🛡️ ECOSSISTEMA OPTIMUS TECHNOLOGY 🛡️       ")
    print("          CONSULTORIA & RESILIÊNCIA             ")
    print("==================================================\n")

    # 1. ETAPA DE AUDITORIA (O que você mostra no WhatsApp)
    print("[FASE 1] Iniciando Diagnóstico de Ambiente...")
    verificar_ambiente_optimus()
    
    # 2. ETAPA DE SAÚDE (Onde você prova a lentidão/risco)
    print("\n[FASE 2] Analisando Saúde do Hardware...")
    monitorar_infraestrutura()

    print("\n==================================================")
    print("✅ Diagnóstico Concluído com Sucesso!")
    print("PRÓXIMO PASSO: Configurar Backup Imutável AWS S3.")
    print("==================================================")

if __name__ == "__main__":
    executar_fluxo_optimus()