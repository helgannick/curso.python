contatos = {"helgannickgmail.com": {"nome": "Marcos", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "helgannick@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)