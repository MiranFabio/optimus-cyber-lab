import boto3
import os
from botocore.exceptions import NoCredentialsError

def iniciar_backup(caminho_local, nome_bucket, objeto_aws):
    """
    Faz o upload de um arquivo para o S3 da AWS.
    """
    print(f"🚀 [BACKUP] Iniciando envio: {caminho_local}...")
    
    # Inicializa o cliente S3
    s3 = boto3.client('s3')

    try:
        # Tenta fazer o upload
        s3.upload_file(caminho_local, nome_bucket, objeto_aws)
        print(f"✅ [SUCESSO] Arquivo salvo no cofre: {objeto_aws}")
        return True
    except FileNotFoundError:
        print("❌ [ERRO] O arquivo local não foi encontrado.")
        return False
    except NoCredentialsError:
        print("❌ [ERRO] Chaves da AWS não encontradas! Rode 'aws configure'.")
        return False
    except Exception as e:
        print(f"❌ [ERRO] Falha inesperada: {e}")
        return False

if __name__ == "__main__":
    # Teste rápido individual
    print("Teste isolado do motor de backup...")