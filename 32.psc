Proceso _32_potencia
	//	An�lisi:
	//	Hem de comprovar l'exponent: si �s 0 la pot�ncia �s 1,
	//	si �s menor que 0, la pot�ncia �s 1/pot�ncia (amb l'exponent
	//	positiu) i si �s m�s gran que 0 es calcula la pot�ncia.
	//	Dades d'entrada:
	//	base, exponent (sencer)
	//	Dades de sortida:
	//	Valor de la pot�ncia
	//	Variables:
	//	base de tipus Entero
	//	exponent de tipus Entero
	//	
	
	Definir base, exponent Como Entero;
	Escribir  "Entra la base: ";
	Leer base;
	Escribir  "Entra l exponent: ";
	Leer exponent;
	Si (exponent > 0) Entonces
		Escribir base, " ^ ", exponent, " = ", (base^exponent);
	SiNo
		Si (exponent = 0) Entonces
			Escribir "En ser l exponente 0 el resultat de la potencia sempre sera 1";
		SiNo
			Escribir base, " ^ ", exponent, " = ", (1/(base^(exponent * (-1))));
		FinSi
	FinSi
FinProceso
Definir base, exponent Como Entero;
//	Disseny:
//Hem de Llegir la base i l'exponent
//Comprovar si l'exponent es mes gran que 0 i mostrar el resultat de la potencia
//Comprovar si l'exponent es igual a 0 i mostrar que el resultat es 1
//Comprovar si l'exponent es menor que 0 i mostrar el resultat de 1/(base^(exponent * (-1))