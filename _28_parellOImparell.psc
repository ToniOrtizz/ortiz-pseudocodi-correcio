Proceso _28_parellOImparell
	//  Anàlisi:
	//      Hem de demanar un número per teclat,
	//		i comprovar si és parell o imparell.
	//  Dades d'entrada:
	//      nombre (sencer)
	//  Dades de sortida:
	//      Un missatge de text indicant si el
	//		nombre és parell o imparell.
	//  Variables:
	//      num de tipus Entero 
	//  Disseny: Defineix un numero com a  real despres dividirlo entre 2 
	//  i si es igual a 0 es parell si es igual a 1 es senar
	
	
	definir numero1 como real;
	
	Escribir Sin Saltar "Entra el nombre: ";
	Leer numero1;
	
	si (numero1 % 2 = 0) entonces
		Escribir numero1, " es parell";
	sino
		Escribir numero1, " es senar";
	finsi
	
FinProceso
