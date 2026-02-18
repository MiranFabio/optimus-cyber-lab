import psutil # Biblioteca para ler estatísticas do sistema (disco, CPU, RAM)
import shutil # Biblioteca para operações de arquivos e espaço

def verificar_saude_disco():
    print("--- 🛡️ MONITOR DE SAÚDE: ECOSSISTEMA OPTIMUS ---")
    
    # 1. Captura os dados do disco C:
    # total: total de espaço | used: usado | free: livre
    total, usado, livre = shutil.disk_usage("C:/")

    # 2. Converte de bytes para Gigabytes (GB)
    total_gb = total // (2**30)
    livre_gb = livre // (2**30)
    porcentagem_livre = (livre / total) * 100

    print(f"Disco C: | Total: {total_gb}GB | Livre: {livre_gb}GB")
    print(f"Espaço Disponível: {porcentagem_livre:.2f}%")

    # 3. Lógica de Alerta (O Pulo do Gato para o Cliente)
    if porcentagem_livre < 15:
        print("\n🚨 ALERTA CRÍTICO: Espaço em disco abaixo de 15%!")
        print("Ação recomendada: Mover arquivos pesados para o Disco E: imediatamente.")
    else:
        print("\n✅ Sistema Operacional saudável.")

    # 4. Verifica o uso da Memória RAM (Bônus de Observabilidade)
    ram = psutil.virtual_memory()
    print(f"Memória RAM em uso: {ram.percent}%")

if __name__ == "__main__":
    verificar_saude_disco()