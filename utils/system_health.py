import psutil
import shutil

def monitorar_infraestrutura():
    print("\n--- 🛡️ MONITOR DE SAÚDE: ECOSSISTEMA OPTIMUS ---")
    
    # Verificação de Disco
    total, usado, livre = shutil.disk_usage("C:/")
    percentual_livre = (livre / total) * 100
    print(f"📊 DISCO C: {percentual_livre:.2f}% Livre ({livre // (2**30)}GB)")

    # Verificação de RAM
    ram = psutil.virtual_memory()
    print(f"🧠 MEMÓRIA RAM: {ram.percent}% em uso")

    # 🔥 O PULO DO GATO: Listar os 3 processos mais pesados
    print("\n🕵️ Caça-Vilões (Top 3 Consumo de RAM):")
    processos = []
    for proc in psutil.process_iter(['name', 'memory_info']):
        try:
            # Pega o nome do programa e quanto ele gasta de memória em MB
            mem = proc.info['memory_info'].rss / (1024 * 1024)
            processos.append((proc.info['name'], mem))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Ordena do maior para o menor e pega os 3 primeiros
    processos.sort(key=lambda x: x[1], reverse=True)
    for i, (nome, mem) in enumerate(processos[:3], 1):
        print(f"  {i}. {nome}: {mem:.2f} MB")

if __name__ == "__main__":
    monitorar_infraestrutura()