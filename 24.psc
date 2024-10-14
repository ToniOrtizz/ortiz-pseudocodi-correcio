Proceso _24_calculaNotaTest
	//	Anàlisi:
	// 		Calcular la nota d'un test usant les respostes
	// 		correctes i les incorrectes.
	// les corrects son 5 punts les incorrectes -1 i en blanc 0
	// 	Variables:
	// 		valorRespCorrectes, valorRespIncorrectes, valorRespEnBlanc
	// 		respCorrectes, respIncorrectes, respEnBlanc de tipus Entero
	// 		Es considera que no cal guardar el valor
	// 		nota final a cap variable.
	Definir respCorrectes, respIncorrectes, respEnBlanc Como Entero;
	Definir valorRespCorrectes, valorRespIncorrectes, valorRespEnBlanc Como Entero;
	valorRespCorrectes <- 5;
	valorRespIncorrectes <- -1;
	valorRespEnBlanc <- 0;
	
	Escribir Sin Saltar "Entra la quantitat de respostes correctes: ";
	Leer respCorrectes;
	Escribir Sin Saltar "Entra la quantitat de respostes incorrectes: ";
	Leer respIncorrectes;
	Escribir Sin Saltar "Entra la quantitat de respostes en blanc: ";
	Leer respEnBlanc;
	Escribir "La nota final es ", ((respCorrectes * valorRespCorrectes ) + (respIncorrectes * valorRespIncorrectes) + (respEnBlanc * valorRespEnBlanc) );
FinProceso
// 	Disseny:
//	Per poder fer un programa l'exercici 
//	hem de crear tres variables per poder guardar el valor
//	que té cada pregunta.
//	és a dir pel valorRespCorrectes = 5
// 	és a dir pel valorRespIncorrectes = -1
// 	és a dir pel valorRespEnBlanc = 0
// 	Demanar la quantitat de respostes correctes,
// 	d incorrectes i en blanc
// hem de mostrar de tot multiplicat per la seva variable
