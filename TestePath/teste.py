from pathlib import Path

print("Arquivo atual:")
print(__file__)

print("\nPasta do arquivo:")
print(Path(__file__).resolve().parent)
