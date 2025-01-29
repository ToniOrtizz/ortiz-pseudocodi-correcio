Proceso enunciat_extra_1
	Definir tipusfumigacio como entero;
	definir numhectarias como entero;
	definir preu como real;
	definir nom_granjer como caracter;
	definir tipus1 como entero;
	definir tipus2 como entero;
	definir tipus3 como entero;
	definir tipus4 como entero;
	definir ingres_total como entero;
	definir contador como entero;
		
	
	
	contador <- 0;
	ingres_total <- 0;
	tipus1 <- 0;
	tipus2 <- 0;
	tipus3 <- 0;
	tipus4 <- 0;
	
	
	mientras contador < 10 hacer
		
	
	escribir " introdueix tipus de fumigacio:";
	leer tipusfumigacio;
	
	escribir " introdueix numhectarias:";
	leer numhectarias;
	
	escribir " aquest es el nom del granjer:" ;
	leer nom_granjer;
	

	si tipusfumigacio = 1 entonces
		preu <-numhectarias*50;
		tipus1 <- tipus1 + 1;
	FinSi
	
	si tipusfumigacio = 2 entonces
		preu <-numhectarias*70;
		tipus2 <- tipus2 + 1;
	FinSi
	
	si tipusfumigacio = 3 entonces
		preu <-numhectarias*80;
		tipus3 <- tipus3 + 1;
	finsi	
	
	
	
	si tipusfumigacio = 4 entonces
		preu <-numhectarias*190;
		tipus4 <- tipus4 + 1;
	finsi	
	
	si numhectarias > 100 entonces
		preu <- preu -(preu* 0.05) ;
		
	FinSi
	
	si numhectarias > 10000 entonces
		preu <- preu -(preu* 0.10) ;
	FinSI
	
	escribir sin saltar "aquest es el nom del granjer:",nom_granjer ," aquest es el preu:",preu;
	ingres_total <- ingres_total + preu;
	
	contador<- contador+1;
finMientras
Escribir "Hi han ", tipus1, " fumigacions de tipus 1.";
Escribir "Hi han ", tipus2, " fumigacions de tipus 2.";
Escribir "Hi han ", tipus3, " fumigacions de tipus 3.";
Escribir "Hi han ", tipus4, " fumigacions de tipus 4.";
Escribir "La suma total de totes les fumigacions és de ", ingres_total,".";

	fin Algoritmo
	
	