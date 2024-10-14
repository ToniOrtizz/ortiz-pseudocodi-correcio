//necesitem saber la velocitat  de cada vehicle i la distancia entre ells
//hem de calcular el temps que trigara el de d'arrere






Proceso _21_vehicleAtrapat
	Definir velocitat1 como real;
	definir velocitat2 como real;
	definir distancia como real;
	definir temps como real;
	
	
	Escribir "introdueix el valor de velocitat1:" ;
	leer velocitat1; 
	
	
	Escribir "introdueix el valor de velocitat2: " ;
	leer velocitat2; 
	
	Escribir "introdueix el valor dedistancia: " ;
	leer distancia; 
	
	temps <- distancia/(velocitat1 + velocitat2) * 60 ;

	

	
	
	Escribir " temps en minuts:",temps;
	
	
	
	
	
	
FinProceso

//hem de llegir les dues velocitats i distancies
//calcular el temps hem d'utlitzar la forumla de v=d/t pero com ens falta la t 
//fem temps = distancia / velocitat
//hem de passar el temps ha minuts h=m--> h/60 s=m--> s*60
//mostrar temps

