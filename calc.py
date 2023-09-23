def calcular_icms_st(valor_base, aliquota_icms, aliquota_mva):
    # Cálculo do ICMS ST
    icms = valor_base * (aliquota_icms / 100)
    mva = (1 + (aliquota_mva / 100))
    icms_st = (valor_base * mva) - valor_base


# Exemplo de uso da função
valor_base = float(input("Informe o valor base para cálculo do ICMS ST: "))
aliquota_icms = float(input("Informe a alíquota do ICMS: "))
aliquota_mva = float(input("Informe a alíquota MVA: "))

resultado = calcular_icms_st(valor_base, aliquota_icms, aliquota_mva)
print(f"O valor do ICMS ST é: R$ {resultado:.2f}")