from open_ai_ex import get_answer

instructiune_pentru_user = "Zi-mi ce ai in frigider pentru gatit: "
print(instructiune_pentru_user)
instructiune_pentru_ai = "Fa-mi o reteta in limba romana cu urmatoarele ingrediente"
textul_instructiunii = input("Da ingredientele tale din frigider cu care vrei sa-ti gatesti ceva")

print(get_answer(instructiune_pentru_ai, textul_instructiunii))