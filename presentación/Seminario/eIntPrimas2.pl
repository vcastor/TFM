#!/usr/bin/perl -w

#Este script calcula la E_int prima de acuerdo con el artículo de los hexámeros
#del Toche
#asegurarse que en mon1.txt siempre estén las etiquetas del HF
#en los archivos mon.txt hay que colocar las etiquetas de los átomos que forman un grupo de acuerdo a la 
#partición IQA.

$monomeros=6;
$rootPl="/home/vcastor/Documents/m062x/IQA/6_ring_H2O";
$sum="6_ring_H2O.sumviz";
$eH2OAislada=-76.420887;

@energiasAislados=();

#Aqui se asignan las energías de los monómeros aislados al arreglo
#@energiasAislados

for($i = 1; $i <= $monomeros; ++$i){
   @poner=($i,$eH2OAislada);
   push(@energiasAislados,@poner);
}

%energiasAislados=@energiasAislados;

for($h = 1; $h < $monomeros; ++$h){
   for($g = $h + 1; $g <= $monomeros; ++$g){
      $arH = "mon${h}.txt"; #grupo H
      $arG = "mon${g}.txt"; #grupo G
      $arGH = "mon${g}_mon${h}.txt";
      system("cat $arH $arG > $arGH");
      $eIntGH=`$rootPl/interaccionGrupoAIMAll.pl $sum $arGH | tail -1`; chomp($eIntGH); #saca energia de interacción entre grupos GH

      $eClassGH=`$rootPl/interaccionGrupoAIMAllClasXC.pl $sum $arGH | tail -3 | head -1`; chomp($eClassGH); #saca energia de interacción clásica entre grupos GH

      $eXcGH=`$rootPl/interaccionGrupoAIMAllClasXC.pl $sum $arGH | tail -2 | head -1`; chomp($eClassGH); #saca energia de interacción intercambio y correlación entre grupos GH
      
      #cálculo del primer denominador
     $den1=0.0;
      for($i = 1; $i <= $monomeros; ++$i){
         unless ($i == $g){
            $arI = "mon${i}.txt";
            $arIG = "mon${i}_mon${g}.txt";
            system("cat $arI $arG > $arIG");
            $eInt1=`$rootPl/interaccionGrupoAIMAll.pl $sum $arIG | tail -1`; chomp($eInt1);
            $den1 = $den1 + $eInt1;
	    #print "$eInt1\n";
	    #print "$den1\n";
         }
      }

      #cálculo de la primera energía de deformación
      $eMonG=`$rootPl/energiaGrupoAIMAll.pl $sum $arG | tail -1`; chomp($eMonG);
      $eDefG=$eMonG-$energiasAislados{$g}; 
     
     $den2=0.0;
      for($i = 1; $i <= $monomeros; ++$i){
         unless ($i == $h){
            $arI = "mon${i}.txt";
            $arIH = "mon${i}_mon${h}.txt";
            system("cat $arI $arH > $arIH");
            $eInt2=`$rootPl/interaccionGrupoAIMAll.pl $sum $arIH | tail -1`; chomp($eInt2);
            $den2 = $den2 + $eInt2;
	    #print "$eInt2\n";
	    #print "$den2\n";
         }
      }

      #cálculo de la segunda energía de deformación
      $eMonH=`$rootPl/energiaGrupoAIMAll.pl $sum $arH | tail -1`; chomp($eMonH);
      $eDefH=$eMonH-$energiasAislados{$h}; 
      
      #cálculo de Eint prima
      $eIntPrima=$eIntGH*(1.0 + $eDefG/$den1 + $eDefH/$den2)*627.509;
      $eClassPrima=$eClassGH*(1.0 + $eDefG/$den1 + $eDefH/$den2)*627.509;
      $eXcPrima=$eXcGH*(1.0 + $eDefG/$den1 + $eDefH/$den2)*627.509;

      printf("%s   %s   %lf   %lf   %lf\n", $arH, $arG, $eClassPrima, $eXcPrima, $eIntPrima);
   }
}

