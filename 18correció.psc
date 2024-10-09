Proceso _18_arrelQuadradaICubica
	//	Anàlisi:
	//		Es demanen número i es mostra
	//		l'arrel quadrada i la cúbica.
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
	//		Calcular arrel quadrada: PseInt té dues
	//			funcions (raiz(), RC())
	//		Calcular arrel cúbica: PseInt NO té
	//			cap funció, com ho podem fer??????
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