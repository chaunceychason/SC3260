#include <stdio.h>
#include <stdlib.h> // srand and rand
#include <time.h>

/*
THIS CODE GENERATES A RANDOM MATRIX OF DIMENSION N with values between 0 and (A-1).
useage:  ./codename {N} {A}    note: the { } are not necessary. Matrix will be N x N. 
*/


int main(int argc, char ** argv)
{
   time_t t;
   /* Intializes random number generator */
   srand((unsigned) time(&t));
   //SETS DEFAULTS AND INITIALIZES ARRAY SIZE AND NUMBER RANGE 
   int i,r,j,n=50;
  
   int amplitude = 50;  //SETS THE MAX NUMBER RANGE
  
  
   if (argc >= 2){
         
      n = atoi(argv[1]);       //SETS THE MATRIX SIZE N, for N x N matrix. 
      if( argc > 2) amplitude = atoi(argv[2]); //SETS THE NUMBER AMPLITUDE
   }
   for ( i=0 ; i<n ; i++ ) {
      for ( j=0; j<n ; j++ ) {
         r = rand() % amplitude;
         printf("%d ",r);
      }
      printf("\n");
   }
 
   return 0;
}
