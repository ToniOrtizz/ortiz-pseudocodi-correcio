Proceso _18_arrelQuadradaICubica
	//	Anàlisi:
	//		Es demanen número i em de mostra l'arrel quadrada i la cúbica.
	//	Dades d'entrada:
	//		nombre de tipus Entero
	//	Dades de sortida:
	//		arrelQuadrada de tipus Real
	//		arrelCubica de tipus Real
	//	Variables:
	//		nombre de tipus Entero
	//		Es considera que no cal guardar els
	//		valor ni de l'arrel quadrada, ni de
	//		l'arrel cúbica a cap variable.
	//	Disseny:
	//		Llegir el número
	//		Calcular arrel quadrada: es pot fer de dues maneras
	//			funcions (raiz(), RC())
	//		Mostrar les dues arrels.
	
	
	Definir nombre como Entero;
	Definir arrelQuadrada, arrelCubica como Real;
	Escribir sin Saltar "Entra el nombre: ";
	leer nombre;
	arrelQuadrada <- RC(nombre);
	arrelCubica <- nombre^(1/3);
	Escribir "L arrel quadrada de ", nombre , " es ", arrelQuadrada;
	Escribir "L arrel cubica de ", nombre , " es ", arrelCubica;
FinProceso



//diseny
//hem de llegir el numero
// hem de calcular l'arrel cuadrada amb la funcio rc()
//calcular l'arrel cubica utilitezm el ^ i fem 1/3 ens dona la arrel cubica