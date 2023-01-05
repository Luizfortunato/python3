"""Escreva um programa que converta uma temperatura digitada em °C para °F e K."""

print(' *** Inicio do programa ***\n')

celcius = float(input("Informe a temperatura em °C:"))

fahrenheit = 32 + (celcius * 1.8)

kelvin = celcius + 273.15

print('\n{:.1f}°C equivale a {:.1f}°F e {:.2f}K'.format(celcius, fahrenheit, kelvin))

print('\n *** Fim do programa ***')