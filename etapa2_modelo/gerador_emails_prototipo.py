import argparse
from transformers import pipeline

# Argumento de entrada
parser = argparse.ArgumentParser()
parser.add_argument('--setor', type=str, required=True)
args = parser.parse_args()

# Inicializar gerador de texto
generator = pipeline("text-generation", model="gpt2")

# Prompt personalizado
prompt = f"Escreva um e-mail persuasivo para um lead do setor de {args.setor} sobre como nossa solução de IA pode melhorar seus resultados."

# Gerar e-mail
email = generator(prompt, max_length=200, num_return_sequences=1)
print("\n📧 E-mail gerado:\n")
print(email[0]['generated_text'])
